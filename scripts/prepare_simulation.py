#!/usr/bin/env python3
"""
prepare_simulation_v3.py - COMPLETE TROJAN INTEGRATION
Properly inserts trojan logic into original module and generates dynamic testbenches
"""

import sys
import re
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import simple parser for reliable parsing
sys.path.insert(0, str(Path(__file__).parent))
from simple_parser import SimpleModuleParser


def insert_trojan_properly(original_module_path: str):
    """
    Complete trojan insertion workflow:
    1. Parse original module
    2. Read generated trojan
    3. Add trojan counter/trigger logic
    4. MODIFY original signal assignments to inject payload
    5. Generate dynamic testbenches
    """
    
    original_path = Path(original_module_path)
    module_name = original_path.stem
    
    # Setup paths
    repo_root = Path.cwd()
    trojan_src_dir = repo_root / 'examples/ibex/generated_trojans' / module_name
    trojaned_rtl_dir = repo_root / 'examples/ibex/trojaned_rtl'
    testbench_dir = repo_root / 'testbenches/ibex'
    
    trojaned_rtl_dir.mkdir(parents=True, exist_ok=True)
    testbench_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*70)
    print(f"TROJAN INTEGRATION: {module_name}")
    print("="*70)
    
    # STEP 1: Parse original module
    print("\n[1/5] Parsing original module...")
    parser = SimpleModuleParser(str(original_path))
    module = parser.parse()
    
    if not module:
        print("❌ Failed to parse module!")
        return False
    
    print(f"   ✅ Module: {module.name}")
    print(f"   Clock: {module.clock_signal}")
    print(f"   Reset: {module.reset_signal}")
    print(f"   Signals: {len(module.get_all_signals())}")
    
    # Read original content
    original_content = original_path.read_text()
    
    # STEP 2: Find generated trojan
    print("\n[2/5] Finding generated trojan...")
    trojan_files = sorted(trojan_src_dir.glob('T*_*.sv'))
    
    if not trojan_files:
        print(f"   ❌ No trojan files found in {trojan_src_dir}")
        return False
    
    trojan_file = trojan_files[0]
    print(f"   ✅ Found: {trojan_file.name}")
    
    # STEP 3: Add trojan trigger logic
    print("\n[3/5] Creating trojan trigger logic...")
    
    trojan_trigger = create_trojan_trigger(module)
    print(f"   ✅ Trigger logic created")
    
    # STEP 4: MODIFY original assignments to add payload
    print("\n[4/5] Injecting trojan payload...")
    
    trojaned_content = inject_trojan_payload(original_content, module)
    print(f"   ✅ Payload injected")
    
    # Insert trojan trigger before endmodule
    last_endmodule = trojaned_content.rfind('endmodule')
    if last_endmodule == -1:
        print("   ❌ Could not find endmodule!")
        return False
    
    trojaned_content = (
        trojaned_content[:last_endmodule] +
        "\n// ============================================================\n" +
        "// HARDWARE TROJAN TRIGGER LOGIC\n" +
        "// ============================================================\n\n" +
        trojan_trigger + "\n\n" +
        trojaned_content[last_endmodule:]
    )
    
    # Rename module to {module_name}_trojan
    trojaned_content = re.sub(
        rf'\bmodule\s+{module_name}\b',
        f'module {module_name}_trojan',
        trojaned_content,
        count=1
    )
    
    # Save trojaned module
    trojaned_file = trojaned_rtl_dir / f"{module_name}_trojan.sv"
    trojaned_file.write_text(trojaned_content)
    print(f"   ✅ Created: {trojaned_file.name}")
    
    # STEP 5: Generate dynamic testbenches
    print("\n[5/5] Generating testbenches...")
    
    # Import dynamic testbench generator
    sys.path.insert(0, str(repo_root / 'scripts'))
    from dynamic_testbench_generator import DynamicTestbenchGenerator
    
    # Generate testbenches for original
    gen_orig = DynamicTestbenchGenerator(str(original_path))
    orig_tb = gen_orig.generate_testbench(is_trojan=False)
    orig_tb_file = testbench_dir / f"tb_{module_name}.sv"
    orig_tb_file.write_text(orig_tb)
    print(f"   ✅ Original TB: {orig_tb_file.name}")
    
    # Generate testbench for trojan
    # Simple approach: generate for original, then replace module name
    gen_trojan = DynamicTestbenchGenerator(str(original_path))
    gen_trojan.parse_module()  # Explicitly parse it
    
    # Generate as if it's original, then replace module name
    trojan_tb = gen_trojan.generate_testbench(is_trojan=False)
    
    # Replace all occurrences of original module name with trojan version
    trojan_tb = trojan_tb.replace(f"tb_{module_name}", f"tb_{module_name}_trojan")
    trojan_tb = trojan_tb.replace(f"{module_name} dut", f"{module_name}_trojan dut")
    trojan_tb = trojan_tb.replace(f'"{module_name}_original.vcd"', f'"{module_name}_trojan.vcd"')
    trojan_tb = trojan_tb.replace('"Original simulation done"', '"Trojan simulation done"')
    
    trojan_tb_file = testbench_dir / f"tb_{module_name}_trojan.sv"
    trojan_tb_file.write_text(trojan_tb)
    print(f"   ✅ Trojan TB: {trojan_tb_file.name}")
    
    # Summary
    print("\n" + "="*70)
    print("✅ INTEGRATION COMPLETE!")
    print("="*70)
    print(f"Original Module:  {original_path}")
    print(f"Trojaned Module:  {trojaned_file}")
    print(f"Original TB:      {orig_tb_file}")
    print(f"Trojan TB:        {trojan_tb_file}")
    print("="*70)
    
    return True


def create_trojan_trigger(module):
    """Create trojan trigger logic (counter-based)"""
    
    clock = module.clock_signal or 'clk_i'
    reset = module.reset_signal or 'rst_ni'
    
    # Find write enable
    write_enable = None
    for sig in module.inputs:
        if 'we' in sig.name.lower() or 'wr_en' in sig.name.lower() or 'write' in sig.name.lower():
            write_enable = sig.name
            break
    
    if not write_enable:
        write_enable = 'wr_en_i'
    
    trigger_logic = f"""// Trojan Trigger: Counter-based activation
localparam int TRIGGER_THRESHOLD = 1000;
logic [31:0] trojan_counter;
// Note: trojan_active is declared at module top

always_ff @(posedge {clock} or negedge {reset}) begin
    if (!{reset}) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        if ({write_enable}) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end"""
    
    return trigger_logic


def inject_trojan_payload(content: str, module):
    """
    Inject trojan payload by modifying original assignments
    
    Steps:
    1. Add forward declaration of trojan_active at module start
    2. Find: assign rd_data_o = rdata_q;
    3. Replace: assign rd_data_o = trojan_active ? (rdata_q ^ 32'hDEAD) : rdata_q;
    """
    
    # Find data output assignment
    data_output = None
    for sig in module.outputs:
        if 'data' in sig.name.lower() and 'rd' in sig.name.lower():
            data_output = sig.name
            break
    
    if not data_output:
        print("   ⚠️  No rd_data output found, trojan will be trigger-only")
        return content
    
    # STEP 1: Add forward declaration of trojan_active after module ports
    # Find the closing parenthesis of module declaration
    module_decl_pattern = rf'module\s+{module.name}[^;]*;\s*'
    match = re.search(module_decl_pattern, content, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        forward_decl = "\n  // Trojan signal (forward declaration)\n  logic trojan_active;\n\n"
        content = content[:insert_pos] + forward_decl + content[insert_pos:]
        print(f"   ✅ Added forward declaration of trojan_active")
    
    # STEP 2: Find and modify assignment
    # Find assignment pattern: assign rd_data_o = ...;
    pattern = rf'(assign\s+{data_output}\s*=\s*)([^;]+)(;)'
    
    match = re.search(pattern, content)
    if not match:
        print(f"   ⚠️  Could not find assignment for {data_output}")
        return content
    
    original_value = match.group(2).strip()
    
    # Create trojaned assignment
    trojaned_assignment = f"{match.group(1)}trojan_active ? ({original_value} ^ 32'hDEADBEEF) : {original_value}{match.group(3)}"
    
    # Replace in content
    modified_content = content.replace(match.group(0), trojaned_assignment)
    
    print(f"   ✅ Modified: {data_output} = trojan_active ? CORRUPTED : normal")
    
    return modified_content
    """
    Complete trojan insertion workflow:
    1. Parse original module
    2. Read generated trojan
    3. Create internal trojan logic (NOT standalone module)
    4. Insert before endmodule
    5. Generate dynamic testbenches
    """
    
    original_path = Path(original_module_path)
    module_name = original_path.stem
    
    # Setup paths
    repo_root = Path.cwd()
    trojan_src_dir = repo_root / 'examples/ibex/generated_trojans' / module_name
    trojaned_rtl_dir = repo_root / 'examples/ibex/trojaned_rtl'
    testbench_dir = repo_root / 'testbenches/ibex'
    
    trojaned_rtl_dir.mkdir(parents=True, exist_ok=True)
    testbench_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*70)
    print(f"TROJAN INTEGRATION: {module_name}")
    print("="*70)
    
    # STEP 1: Parse original module to get its interface
    print("\n[1/5] Parsing original module...")
    parser = SimpleModuleParser(str(original_path))
    module = parser.parse()
    
    if not module:
        print("❌ Failed to parse module!")
        return False
    
    print(f"   ✅ Module: {module.name}")
    print(f"   Clock: {module.clock_signal}")
    print(f"   Reset: {module.reset_signal}")
    print(f"   Signals: {len(module.get_all_signals())}")
    
    # Read original content
    original_content = original_path.read_text()
    
    # STEP 2: Find generated trojan
    print("\n[2/5] Finding generated trojan...")
    trojan_files = sorted(trojan_src_dir.glob('T*_*.sv'))
    
    if not trojan_files:
        print(f"   ❌ No trojan files found in {trojan_src_dir}")
        return False
    
    trojan_file = trojan_files[0]
    trojan_content = trojan_file.read_text()
    print(f"   ✅ Found: {trojan_file.name}")
    
    # STEP 3: Create internal trojan logic
    print("\n[3/5] Creating internal trojan logic...")
    
    # The generated trojan is a standalone module - we need to convert it to internal logic
    # Extract just the logic between module declaration and endmodule
    
    # Strategy: Since templates create standalone modules with their own ports,
    # we'll create INTERNAL trojan logic that intercepts signals
    
    internal_trojan = create_internal_trojan_logic(module, trojan_content)
    
    print(f"   ✅ Converted to internal logic ({len(internal_trojan)} chars)")
    
    # STEP 4: Insert trojan before endmodule
    print("\n[4/5] Inserting trojan into module...")
    
    # Find last endmodule
    last_endmodule = original_content.rfind('endmodule')
    if last_endmodule == -1:
        print("   ❌ Could not find endmodule!")
        return False
    
    # Insert trojan logic before endmodule
    trojaned_content = (
        original_content[:last_endmodule] +
        "\n// ============================================================\n" +
        "// HARDWARE TROJAN INSERTED\n" +
        "// ============================================================\n\n" +
        internal_trojan + "\n\n" +
        "// ============================================================\n" +
        "// END OF TROJAN\n" +
        "// ============================================================\n\n" +
        original_content[last_endmodule:]
    )
    
    # Rename module to {module_name}_trojan
    trojaned_content = re.sub(
        rf'\bmodule\s+{module_name}\b',
        f'module {module_name}_trojan',
        trojaned_content,
        count=1
    )
    
    # Save trojaned module
    trojaned_file = trojaned_rtl_dir / f"{module_name}_trojan.sv"
    trojaned_file.write_text(trojaned_content)
    print(f"   ✅ Created: {trojaned_file.name}")
    
    # STEP 5: Generate dynamic testbenches
    print("\n[5/5] Generating testbenches...")
    
    # Import dynamic testbench generator
    sys.path.insert(0, str(repo_root / 'scripts'))
    from dynamic_testbench_generator import DynamicTestbenchGenerator
    
    # Generate testbenches for original
    gen_orig = DynamicTestbenchGenerator(str(original_path))
    orig_tb = gen_orig.generate_testbench(is_trojan=False)
    orig_tb_file = testbench_dir / f"tb_{module_name}.sv"
    orig_tb_file.write_text(orig_tb)
    print(f"   ✅ Original TB: {orig_tb_file.name}")
    
    # Generate testbench for trojan
    # Simple approach: generate for original, then replace module name
    gen_trojan = DynamicTestbenchGenerator(str(original_path))
    gen_trojan.parse_module()  # Explicitly parse it
    
    # Generate as if it's original, then replace module name
    trojan_tb = gen_trojan.generate_testbench(is_trojan=False)
    
    # Replace all occurrences of original module name with trojan version
    trojan_tb = trojan_tb.replace(f"tb_{module_name}", f"tb_{module_name}_trojan")
    trojan_tb = trojan_tb.replace(f"{module_name} dut", f"{module_name}_trojan dut")
    trojan_tb = trojan_tb.replace(f'"{module_name}_original.vcd"', f'"{module_name}_trojan.vcd"')
    trojan_tb = trojan_tb.replace('"Original simulation done"', '"Trojan simulation done"')
    
    trojan_tb_file = testbench_dir / f"tb_{module_name}_trojan.sv"
    trojan_tb_file.write_text(trojan_tb)
    print(f"   ✅ Trojan TB: {trojan_tb_file.name}")
    
    # Summary
    print("\n" + "="*70)
    print("✅ INTEGRATION COMPLETE!")
    print("="*70)
    print(f"Original Module:  {original_path}")
    print(f"Trojaned Module:  {trojaned_file}")
    print(f"Original TB:      {orig_tb_file}")
    print(f"Trojan TB:        {trojan_tb_file}")
    print("="*70)
    
    return True




def main():
    """Command-line interface"""
    if len(sys.argv) != 2:
        print("="*70)
        print("TROJAN INTEGRATION SCRIPT")
        print("="*70)
        print("\nUsage: python prepare_simulation.py <module.sv>")
        print("\nExample:")
        print("  python prepare_simulation.py examples/ibex/original/ibex_csr.sv")
        print("\nThis will:")
        print("  1. Parse the original module")
        print("  2. Find generated trojan in generated_trojans/")
        print("  3. Insert trojan logic into module")
        print("  4. Generate dynamic testbenches")
        print("  5. Output to trojaned_rtl/ and testbenches/")
        print("="*70)
        sys.exit(1)
    
    success = insert_trojan_properly(sys.argv[1])
    
    if success:
        print("\n✅ Ready for simulation!")
        print("\nNext steps:")
        print("  1. Upload files to server (or use local QuestaSim if available)")
        print("  2. Run simulations")
        print("  3. Download VCD files")
        print("  4. Analyze with: python scripts/analyze_vcd.py")
    else:
        print("\n❌ Failed!")
        sys.exit(1)


if __name__ == '__main__':
    main()