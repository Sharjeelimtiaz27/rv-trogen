#!/usr/bin/env python3
"""
Prepare Simulation Script - FIXED VERSION
Properly integrates generated trojan code into original RTL
Reads trojan snippet and inserts it correctly
"""

import sys
import re
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import simple parser for reliable parsing
sys.path.insert(0, str(Path(__file__).parent))
from simple_parser import SimpleModuleParser


def extract_trojan_type(trojan_filename: str) -> str:
    """
    Extract trojan type from filename
    
    Example: T1_ibex_csr_DoS.sv → DoS
    """
    parts = trojan_filename.split('_')
    if len(parts) >= 3:
        return parts[-1].replace('.sv', '')
    return 'Unknown'


def read_trojan_code(trojan_file: Path) -> dict:
    """
    Read generated trojan code and extract components
    
    Returns:
        dict with:
            - trigger_code: The trigger logic
            - payload_instructions: How to modify signals
            - trojan_type: DoS, Leak, etc.
    """
    content = trojan_file.read_text(encoding='utf-8')
    
    result = {
        'trigger_code': '',
        'payload_instructions': '',
        'trojan_type': extract_trojan_type(trojan_file.name),
        'full_content': content
    }
    
    # Extract trigger logic section
    trigger_match = re.search(
        r'// ={10,}.*?TROJAN TRIGGER.*?// ={10,}(.*?)(?=// ={10,}|$)',
        content,
        re.DOTALL
    )
    
    if trigger_match:
        result['trigger_code'] = trigger_match.group(1).strip()
    
    # Extract payload instructions
    payload_match = re.search(
        r'// ={10,}.*?PAYLOAD.*?// ={10,}(.*?)(?=$)',
        content,
        re.DOTALL
    )
    
    if payload_match:
        result['payload_instructions'] = payload_match.group(1).strip()
    
    return result


def extract_signal_names_from_trojan(trojan_code: str) -> dict:
    """
    Extract actual signal names used in trojan code
    
    Returns:
        dict with:
            - trigger_signal: Name of trigger signal
            - payload_signal: Name of payload signal
    """
    signals = {
        'trigger_signal': None,
        'payload_signal': None
    }
    
    # Look for signal usage in trigger code
    # Pattern: if (signal_name) begin
    trigger_pattern = r'if\s+\(([a-zA-Z_][a-zA-Z0-9_]*)\)\s+begin'
    matches = re.findall(trigger_pattern, trojan_code)
    if matches:
        # Skip 'trojan_active' and get actual signal
        for match in matches:
            if match != 'trojan_active':
                signals['trigger_signal'] = match
                break
    
    # Look for payload signal in comments
    payload_pattern = r'(?:Payload|payload|PAYLOAD).*?:\s*([a-zA-Z_][a-zA-Z0-9_]*)'
    matches = re.findall(payload_pattern, trojan_code)
    if matches:
        signals['payload_signal'] = matches[0]
    
    return signals


def inject_trojan_payload_dos(content: str, payload_signal: str, module) -> str:
    """
    Inject DoS payload - disable signal when trojan_active
    
    Strategy:
    1. Add forward declaration of trojan_active
    2. Find where payload_signal is assigned/used
    3. Modify to: trojan_active ? 1'b0 : original_value
    """
    
    # STEP 1: Add forward declaration
    module_decl_pattern = rf'module\s+{module.name}[^;]*;\s*'
    match = re.search(module_decl_pattern, content, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        forward_decl = "\n  // Trojan signal (forward declaration)\n  logic trojan_active;\n\n"
        content = content[:insert_pos] + forward_decl + content[insert_pos:]
        print(f"   ✅ Added trojan_active declaration")
    
    # STEP 2: Find and modify signal assignment
    # Try different patterns
    modified = False
    
    # Pattern 1: assign signal = value;
    pattern1 = rf'(assign\s+{payload_signal}\s*=\s*)([^;]+)(;)'
    match1 = re.search(pattern1, content)
    if match1:
        original_value = match1.group(2).strip()
        new_assignment = f"{match1.group(1)}trojan_active ? 1'b0 : {original_value}{match1.group(3)}"
        content = content.replace(match1.group(0), new_assignment)
        print(f"   ✅ Modified assign {payload_signal} (DoS payload)")
        modified = True
    
    # Pattern 2: In always_ff block
    if not modified:
        pattern2 = rf'({payload_signal}\s*<=\s*)([^;]+)(;)'
        match2 = re.search(pattern2, content)
        if match2:
            original_value = match2.group(2).strip()
            new_assignment = f"{match2.group(1)}trojan_active ? 1'b0 : {original_value}{match2.group(3)}"
            content = content.replace(match2.group(0), new_assignment)
            print(f"   ✅ Modified {payload_signal} <= (DoS payload)")
            modified = True
    
    if not modified:
        print(f"   ⚠️  Warning: Could not find assignment for {payload_signal}")
        print(f"   ⚠️  Trojan trigger will be added but payload may not work")
    
    return content


def inject_trojan_payload_integrity(content: str, payload_signal: str, module) -> str:
    """
    Inject Integrity payload - corrupt signal with XOR
    
    Strategy:
    1. Add forward declaration
    2. Find signal assignment
    3. Modify to: trojan_active ? (value ^ CORRUPTION_MASK) : value
    """
    
    # STEP 1: Add forward declaration
    module_decl_pattern = rf'module\s+{module.name}[^;]*;\s*'
    match = re.search(module_decl_pattern, content, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        forward_decl = "\n  // Trojan signal (forward declaration)\n  logic trojan_active;\n\n"
        content = content[:insert_pos] + forward_decl + content[insert_pos:]
        print(f"   ✅ Added trojan_active declaration")
    
    # STEP 2: Find and modify signal assignment
    modified = False
    
    # Pattern 1: assign signal = value;
    pattern1 = rf'(assign\s+{payload_signal}\s*=\s*)([^;]+)(;)'
    match1 = re.search(pattern1, content)
    if match1:
        original_value = match1.group(2).strip()
        new_assignment = f"{match1.group(1)}trojan_active ? ({original_value} ^ 32'hDEADBEEF) : {original_value}{match1.group(3)}"
        content = content.replace(match1.group(0), new_assignment)
        print(f"   ✅ Modified assign {payload_signal} (Integrity payload)")
        modified = True
    
    if not modified:
        print(f"   ⚠️  Warning: Could not find assignment for {payload_signal}")
    
    return content


def inject_trojan_payload_generic(content: str, trojan_type: str, payload_signal: str, module) -> str:
    """
    Generic payload injection - adds trojan_active declaration
    More complex payloads handled by trojan code itself
    """
    
    # Add forward declaration
    module_decl_pattern = rf'module\s+{module.name}[^;]*;\s*'
    match = re.search(module_decl_pattern, content, re.DOTALL)
    
    if match:
        insert_pos = match.end()
        forward_decl = "\n  // Trojan signal (forward declaration)\n  logic trojan_active;\n\n"
        content = content[:insert_pos] + forward_decl + content[insert_pos:]
        print(f"   ✅ Added trojan_active declaration")
    
    print(f"   ℹ️  {trojan_type} payload requires manual signal modification")
    print(f"   ℹ️  See payload instructions in generated trojan file")
    
    return content


def insert_trojan_properly(original_module_path: str):
    """
    Complete trojan insertion workflow:
    1. Parse original module
    2. Read generated trojan code snippet
    3. Extract trojan trigger logic
    4. Add trojan trigger before endmodule
    5. Modify signal assignments for payload
    6. Generate testbenches
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
    print("\n[1/6] Parsing original module...")
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
    print("\n[2/6] Finding generated trojan code...")
    trojan_files = sorted(trojan_src_dir.glob('T*_*.sv'))
    
    if not trojan_files:
        print(f"   ❌ No trojan files found in {trojan_src_dir}")
        return False
    
    trojan_file = trojan_files[0]
    print(f"   ✅ Found: {trojan_file.name}")
    
    # STEP 3: Read trojan code
    print("\n[3/6] Reading trojan code snippet...")
    trojan_data = read_trojan_code(trojan_file)
    
    print(f"   ✅ Trojan type: {trojan_data['trojan_type']}")
    print(f"   ✅ Trigger code: {len(trojan_data['trigger_code'])} chars")
    
    # Extract signal names
    signals = extract_signal_names_from_trojan(trojan_data['trigger_code'])
    print(f"   ✅ Trigger signal: {signals['trigger_signal']}")
    print(f"   ✅ Payload signal: {signals['payload_signal']}")
    
    # STEP 4: Inject payload modification
    print("\n[4/6] Injecting trojan payload...")
    
    trojaned_content = original_content
    
    # Choose payload injection strategy based on trojan type
    if trojan_data['trojan_type'] == 'DoS':
        if signals['payload_signal']:
            trojaned_content = inject_trojan_payload_dos(
                trojaned_content,
                signals['payload_signal'],
                module
            )
    elif trojan_data['trojan_type'] == 'Integrity':
        if signals['payload_signal']:
            trojaned_content = inject_trojan_payload_integrity(
                trojaned_content,
                signals['payload_signal'],
                module
            )
    else:
        # Generic - just add declaration
        trojaned_content = inject_trojan_payload_generic(
            trojaned_content,
            trojan_data['trojan_type'],
            signals['payload_signal'],
            module
        )
    
    # STEP 5: Insert trojan trigger before endmodule
    print("\n[5/6] Inserting trojan trigger logic...")
    
    last_endmodule = trojaned_content.rfind('endmodule')
    if last_endmodule == -1:
        print("   ❌ Could not find endmodule!")
        return False
    
    trojaned_content = (
        trojaned_content[:last_endmodule] +
        "\n" +
        trojan_data['trigger_code'] +
        "\n\n" +
        trojaned_content[last_endmodule:]
    )
    
    print(f"   ✅ Inserted trigger logic before endmodule")
    
    # Rename module to {module_name}_trojan
    trojaned_content = re.sub(
        rf'module\s+{module.name}\s*#?\(',
        f'module {module.name}_trojan #(',
        trojaned_content,
        count=1
    )
    
    # STEP 6: Save trojaned module
    print("\n[6/6] Saving files...")
    
    output_file = trojaned_rtl_dir / f"{module_name}_trojan.sv"
    output_file.write_text(trojaned_content)
    print(f"   ✅ Trojaned RTL: {output_file}")
    
    # Generate testbenches
    print("\n[Bonus] Generating testbenches...")
    try:
        from dynamic_testbench_generator import DynamicTestbenchGenerator
        
        # Generate for original
        gen_orig = DynamicTestbenchGenerator(str(original_path))
        orig_tb_file, _ = gen_orig.generate_testbenches(str(testbench_dir))
        print(f"   ✅ Original TB: {orig_tb_file.name}")
        
        # Generate for trojan
        gen_trojan = DynamicTestbenchGenerator(str(output_file))
        trojan_tb_file, _ = gen_trojan.generate_testbenches(str(testbench_dir))
        print(f"   ✅ Trojan TB: {trojan_tb_file.name}")
        
    except Exception as e:
        print(f"   ⚠️  Testbench generation failed: {e}")
        print(f"   ℹ️  You can generate them manually later")
    
    print("\n" + "="*70)
    print("✅ TROJAN INTEGRATION COMPLETE!")
    print("="*70)
    print(f"📁 Trojaned RTL: {output_file}")
    print(f"📁 Testbenches: {testbench_dir}/")
    print("="*70)
    
    return True


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Prepare simulation by integrating trojan into original RTL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Integrate trojan for ibex_csr
  python prepare_simulation.py examples/ibex/original/ibex_csr.sv
  
  # After running trojan_generator.py, this script:
  #   1. Reads generated trojan code
  #   2. Inserts it into original module
  #   3. Creates module_trojan.sv
  #   4. Generates testbenches for both versions
        """
    )
    
    parser.add_argument('module_file', help='Path to original RTL module (.sv)')
    
    args = parser.parse_args()
    
    # Check file exists
    if not Path(args.module_file).exists():
        print(f"❌ Error: File not found: {args.module_file}")
        sys.exit(1)
    
    print("\n" + "="*70)
    print("PREPARE SIMULATION")
    print("="*70)
    print()
    
    # Run integration
    try:
        success = insert_trojan_properly(args.module_file)
        
        if success:
            print("\n✅ SUCCESS! Ready for simulation.")
            print("\nNext steps:")
            print("  1. Copy files to HPC server")
            print("  2. Run simulation with QuestaSim")
            print("  3. Analyze VCD files")
        else:
            print("\n❌ Integration failed!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()