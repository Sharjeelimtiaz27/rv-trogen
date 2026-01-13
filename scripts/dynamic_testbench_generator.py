#!/usr/bin/env python3
"""
Dynamic Testbench Generator - ROBUST VERSION
Handles parser quirks and filters invalid signals properly
"""

import sys
import re
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the simple regex-based parser (more reliable than RTLParser)
from simple_parser import SimpleModuleParser


class DynamicTestbenchGenerator:
    """Generates testbenches by parsing the actual module"""
    
    def __init__(self, module_file: str):
        self.module_file = Path(module_file)
        self.module = None
        
    def parse_module(self):
        """Parse the module to get all signals"""
        print(f"📄 Parsing module: {self.module_file.name}")
        
        parser = SimpleModuleParser(str(self.module_file))
        self.module = parser.parse()
        
        if not self.module:
            raise ValueError("Failed to parse module")
        
        print(f"   Module: {self.module.name}")
        print(f"   Type: {'Sequential' if self.module.is_sequential else 'Combinational'}")
        print(f"   Clock: {self.module.clock_signal or 'None'}")
        print(f"   Reset: {self.module.reset_signal or 'None'}")
        print(f"   Inputs: {[f'{s.name}[{s.width-1}:0]' if s.is_vector else s.name for s in self.module.inputs]}")
        print(f"   Outputs: {[f'{s.name}[{s.width-1}:0]' if s.is_vector else s.name for s in self.module.outputs]}")
        
        return self.module
    
    def generate_testbench(self, is_trojan=False):
        """Generate testbench code for the module"""
        
        if not self.module:
            self.parse_module()
        
        module_name = self.module.name
        
        # Determine testbench and VCD file names
        if is_trojan:
            tb_name = f"tb_{module_name}_trojan"
            vcd_file = f"{module_name}_trojan.vcd"
            dut_name = f"{module_name}_trojan"
        else:
            tb_name = f"tb_{module_name}"
            vcd_file = f"{module_name}_original.vcd"
            dut_name = module_name
        
        tb_code = []
        
        # Module declaration
        tb_code.append(f"module {tb_name};")
        tb_code.append("")
        
        # Signal declarations - INPUTS ONLY (driven by testbench)
        tb_code.append("  // Input signals (driven by testbench)")
        for sig in self.module.inputs:
            if sig.width > 1:
                tb_code.append(f"  logic [{sig.width-1}:0] {sig.name} = {sig.width}'b0;")
            else:
                tb_code.append(f"  logic {sig.name} = 1'b0;")
        tb_code.append("")
        
        # Signal declarations - OUTPUTS ONLY (from DUT - NO initial values!)
        tb_code.append("  // Output signals (from DUT)")
        for sig in self.module.outputs:
            if sig.width > 1:
                tb_code.append(f"  logic [{sig.width-1}:0] {sig.name};")
            else:
                tb_code.append(f"  logic {sig.name};")
        tb_code.append("")
        
        # Clock generation
        if self.module.clock_signal:
            clk = self.module.clock_signal
            tb_code.append(f"  // Clock generation (10ns period = 100MHz)")
            tb_code.append(f"  always #5 {clk} = ~{clk};")
            tb_code.append("")
        
        # DUT instantiation
        tb_code.append(f"  // Device Under Test")
        tb_code.append(f"  {dut_name} dut (")
        
        # Port connections
        port_list = []
        for sig in self.module.inputs:
            port_list.append(f"    .{sig.name}({sig.name})")
        for sig in self.module.outputs:
            port_list.append(f"    .{sig.name}({sig.name})")
        
        tb_code.append(",\n".join(port_list))
        tb_code.append("  );")
        tb_code.append("")
        
        # Test sequence
        tb_code.append("  initial begin")
        tb_code.append(f"    // VCD dump for waveform analysis")
        tb_code.append(f'    $dumpfile("{vcd_file}");')
        tb_code.append(f"    $dumpvars(0, {tb_name});")
        tb_code.append("")
        
        # Reset sequence
        if self.module.reset_signal:
            rst = self.module.reset_signal
            # Check if active low (has 'n' in name)
            active_low = 'n' in rst.lower()
            
            tb_code.append(f"    // Reset sequence")
            if active_low:
                tb_code.append(f"    {rst} = 0;  // Assert reset (active low)")
            else:
                tb_code.append(f"    {rst} = 1;  // Assert reset (active high)")
            
            if self.module.clock_signal:
                tb_code.append(f"    repeat(10) @(posedge {self.module.clock_signal});")
            else:
                tb_code.append(f"    #100;")
            
            if active_low:
                tb_code.append(f"    {rst} = 1;  // Deassert reset")
            else:
                tb_code.append(f"    {rst} = 0;  // Deassert reset")
            
            if self.module.clock_signal:
                tb_code.append(f"    @(posedge {self.module.clock_signal});")
            else:
                tb_code.append(f"    #10;")
            tb_code.append("")
        
        # Test stimulus - find control/data signals
        write_enables = [s for s in self.module.inputs if 'we' in s.name.lower() or 'wr_en' in s.name.lower() or 'write' in s.name.lower() or 'en' in s.name.lower()]
        data_signals = [s for s in self.module.inputs if 'data' in s.name.lower() or 'wdata' in s.name.lower()]
        
        if write_enables and data_signals and self.module.clock_signal:
            we_sig = write_enables[0]
            data_sig = data_signals[0]
            clk = self.module.clock_signal
            
            tb_code.append(f"    // Test stimulus - Write operations to trigger trojan")
            tb_code.append(f"    // Trojan threshold = 1000, so we do 2000+ operations")
            tb_code.append(f"    repeat(2000) begin")
            tb_code.append(f"      @(posedge {clk});")
            tb_code.append(f"      {data_sig.name} = $random;")
            tb_code.append(f"      {we_sig.name} = 1;")
            tb_code.append(f"      @(posedge {clk});")
            tb_code.append(f"      {we_sig.name} = 0;")
            tb_code.append(f"      @(posedge {clk});")
            tb_code.append(f"    end")
            tb_code.append("")
            tb_code.append(f"    // Additional cycles for observation")
            tb_code.append(f"    repeat(100) @(posedge {clk});")
        elif self.module.clock_signal:
            # Generic sequential test
            tb_code.append(f"    // Generic test stimulus")
            tb_code.append(f"    repeat(2000) @(posedge {self.module.clock_signal});")
        else:
            # Combinational test
            tb_code.append(f"    // Combinational test")
            tb_code.append(f"    #20000;")
        
        tb_code.append("")
        tb_code.append(f'    $display("{"Trojan" if is_trojan else "Original"} simulation done");')
        tb_code.append(f"    $finish;")
        tb_code.append("  end")
        tb_code.append("")
        
        # Timeout watchdog
        tb_code.append("  // Timeout watchdog (prevents infinite simulation)")
        tb_code.append("  initial begin")
        tb_code.append("    #200000000;  // 200ms timeout")
        tb_code.append('    $display("ERROR: Simulation timeout!");')
        tb_code.append("    $finish;")
        tb_code.append("  end")
        tb_code.append("")
        
        tb_code.append("endmodule")
        
        return "\n".join(tb_code)
    
    def generate_testbenches(self, output_dir=None):
        """Generate both original and trojan testbenches"""
        
        if not self.module:
            self.parse_module()
        
        if output_dir is None:
            output_dir = Path("testbenches/ibex")
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        module_name = self.module.name
        
        # Generate original testbench
        print(f"\n📝 Generating original testbench...")
        orig_tb = self.generate_testbench(is_trojan=False)
        orig_file = output_dir / f"tb_{module_name}.sv"
        orig_file.write_text(orig_tb)
        print(f"   ✅ Created: {orig_file.name}")
        
        # Generate trojan testbench
        print(f"\n📝 Generating trojan testbench...")
        trojan_tb = self.generate_testbench(is_trojan=True)
        trojan_file = output_dir / f"tb_{module_name}_trojan.sv"
        trojan_file.write_text(trojan_tb)
        print(f"   ✅ Created: {trojan_file.name}")
        
        return orig_file, trojan_file


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate dynamic testbenches for any RTL module',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate testbenches for a module
  python dynamic_testbench_generator.py examples/ibex/original/ibex_csr.sv
  
  # Custom output directory
  python dynamic_testbench_generator.py module.sv --output my_testbenches/
        """
    )
    
    parser.add_argument('module_file', help='Path to SystemVerilog module')
    parser.add_argument('--output', '-o', help='Output directory (default: testbenches/ibex/)')
    
    args = parser.parse_args()
    
    # Check file exists
    if not Path(args.module_file).exists():
        print(f"❌ Error: File not found: {args.module_file}")
        sys.exit(1)
    
    print("="*60)
    print("DYNAMIC TESTBENCH GENERATOR")
    print("="*60)
    print()
    
    # Generate testbenches
    try:
        gen = DynamicTestbenchGenerator(args.module_file)
        orig_tb, trojan_tb = gen.generate_testbenches(args.output)
        
        print("\n" + "="*60)
        print("✅ SUCCESS!")
        print("="*60)
        print(f"Original TB:  {orig_tb}")
        print(f"Trojan TB:    {trojan_tb}")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()