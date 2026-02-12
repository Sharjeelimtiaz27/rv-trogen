#!/usr/bin/env python3
"""
Multi-Trojan Simulation Preparation Script - COMPLETE VERSION
Integrates multiple trojans into original RTL module and creates testbenches

Features:
- 4 varied trigger mechanisms (deterministic based on trojan index)
- Pattern-specific payload application
- Automatic testbench generation
- Module renaming for simulation
- VCD file generation support

Author: Sharjeel Imtiaz (TalTech)
Date: January 2026
"""

import os
import sys
import re
import random
from pathlib import Path
from typing import List, Dict, Tuple, Optional


class MultiTrojanIntegrator:
    """
    Integrates multiple trojans into RTL module
    Creates separate trojaned versions and testbenches for each
    """
    
    def __init__(self, original_rtl: str, trojans_dir: str = None, output_dir: str = None):
        """
        Initialize integrator
        
        Args:
            original_rtl: Path to original RTL file
            trojans_dir: Directory with generated trojan snippets (auto-detect if None)
            output_dir: Output directory for trojaned modules (auto-detect if None)
        """
        self.original_rtl = Path(original_rtl)
        
        if not self.original_rtl.exists():
            raise FileNotFoundError(f"RTL file not found: {self.original_rtl}")
        
        # Read original RTL
        with open(self.original_rtl, 'r', encoding='utf-8') as f:
            self.original_rtl_content = f.read()
        
        # Extract module info
        self.module_name = self._extract_module_name()
        self.clock_signal = self._extract_clock_signal()
        self.reset_signal = self._extract_reset_signal()
        
        # Auto-detect trojans directory
        if trojans_dir is None:
            trojans_dir = self.original_rtl.parent.parent / "generated_trojans"
        self.trojans_dir = Path(trojans_dir)
        
        # Auto-detect output directory
        if output_dir is None:
            output_dir = self.original_rtl.parent.parent / "trojaned_rtl" / self.module_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Testbench output directory
        self.tb_dir = self.original_rtl.parent.parent.parent / "testbenches" / "ibex" / self.module_name
        self.tb_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"📦 Module: {self.module_name}")
        print(f"📂 Trojans: {self.trojans_dir}")
        print(f"📂 Output: {self.output_dir}")
        print(f"📂 Testbenches: {self.tb_dir}")
    
    def _extract_module_name(self) -> str:
        """Extract module name from RTL"""
        match = re.search(r'module\s+(\w+)', self.original_rtl_content)
        if not match:
            raise ValueError("Cannot find module declaration")
        return match.group(1)
    
    def _extract_clock_signal(self) -> str:
        """Extract clock signal name from RTL"""
        # Common clock signal patterns
        patterns = [r'input\s+(?:logic\s+)?(\w*clk\w*)', 
                   r'(\w*clk\w*)\s*,']
        for pattern in patterns:
            match = re.search(pattern, self.original_rtl_content, re.IGNORECASE)
            if match:
                return match.group(1)
        return 'clk_i'  # Default
    
    def _extract_reset_signal(self) -> str:
        """Extract reset signal name from RTL"""
        # Common reset signal patterns
        patterns = [r'input\s+(?:logic\s+)?(\w*rst\w*)',
                   r'(\w*rst\w*)\s*,']
        for pattern in patterns:
            match = re.search(pattern, self.original_rtl_content, re.IGNORECASE)
            if match:
                return match.group(1)
        return 'rst_ni'  # Default
    
    def find_trojan_files(self) -> List[Path]:
        """Find all trojan snippet files for this module"""
        pattern = f"T*_{self.module_name}_*.sv"
        files = sorted(self.trojans_dir.glob(pattern))
        
        if not files:
            print(f"⚠️  No trojan files found matching: {pattern}")
            print(f"    Searched in: {self.trojans_dir}")
        
        return files
    
    def generate_varied_trigger(self, trojan_index: int, trigger_signal: str, 
                               payload_signal: str, threshold: int) -> str:
        """
        Generate varied trigger logic based on trojan index
        
        4 Types (deterministic):
        - Type 1 (index % 4 = 0): Simple counter
        - Type 2 (index % 4 = 1): Signal combination counter
        - Type 3 (index % 4 = 2): Threshold + signal condition (two-stage)
        - Type 4 (index % 4 = 3): Delayed two-stage
        
        Args:
            trojan_index: 0, 1, 2, 3, ... (determines type)
            trigger_signal: Main trigger signal name
            payload_signal: Payload signal name (for Types 2, 3)
            threshold: Activation threshold (cycles/operations)
        
        Returns:
            Trigger logic as string
        """
        trigger_type = trojan_index % 4
        
        if trigger_type == 0:
            # Type 1: Simple counter
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 1: Simple Counter
    // ============================================================
    // Activates after {threshold} operations of {trigger_signal}
    
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            // Count trigger signal activations
            if ({trigger_signal}) begin
                trojan_counter <= trojan_counter + 1;
            end
            
            // Activate when threshold reached
            if (trojan_counter >= TRIGGER_THRESHOLD) begin
                trojan_active <= 1'b1;
            end
        end
    end"""
        
        elif trigger_type == 1:
            # Type 2: Signal combination counter
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    // Activates after {threshold} times when BOTH signals are active
    
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            // Count when multiple signals are simultaneously active
            // Requires: trigger signal AND payload signal (both != 0)
            if ({trigger_signal} && |{payload_signal}) begin
                trojan_counter <= trojan_counter + 1;
            end
            
            // Activate when threshold reached
            if (trojan_counter >= TRIGGER_THRESHOLD) begin
                trojan_active <= 1'b1;
            end
        end
    end"""
        
        elif trigger_type == 2:
            # Type 3: Threshold + signal condition (two-stage)
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 3: Threshold + Condition
    // ============================================================
    // Stage 1: Count payload activity ({threshold} times)
    // Stage 2: Activate when trigger signal asserted
    
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic trojan_armed;    // Stage 1: Counter reached threshold
    logic trojan_active;   // Stage 2: Activated by trigger signal
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            // Stage 1: Count payload signal activity
            if (|{payload_signal}) begin
                trojan_counter <= trojan_counter + 1;
            end
            
            // Stage 1 complete: Arm the trojan
            if (trojan_counter >= TRIGGER_THRESHOLD) begin
                trojan_armed <= 1'b1;
            end
            
            // Stage 2: Activate only when armed AND trigger signal active
            if (trojan_armed && {trigger_signal}) begin
                trojan_active <= 1'b1;
            end
        end
    end"""
        
        else:  # trigger_type == 3
            # Type 4: Delayed two-stage
            arm_threshold = threshold // 2
            activate_delay = threshold // 4
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 4: Delayed Two-Stage
    // ============================================================
    // Stage 1: Arm after {arm_threshold} operations
    // Stage 2: Activate after additional {activate_delay} operations
    
    localparam int ARM_THRESHOLD = {arm_threshold};
    localparam int ACTIVATE_DELAY = {activate_delay};
    logic [15:0] trojan_counter1;  // First stage counter
    logic [15:0] trojan_counter2;  // Second stage counter
    logic trojan_armed;
    logic trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter1 <= '0;
            trojan_counter2 <= '0;
            trojan_armed    <= 1'b0;
            trojan_active   <= 1'b0;
        end else begin
            // Stage 1: Count towards arming
            if (!trojan_armed && {trigger_signal}) begin
                trojan_counter1 <= trojan_counter1 + 1;
            end
            
            // Arm after first threshold
            if (trojan_counter1 >= ARM_THRESHOLD) begin
                trojan_armed <= 1'b1;
            end
            
            // Stage 2: Count towards activation (only when armed)
            if (trojan_armed && !trojan_active && {trigger_signal}) begin
                trojan_counter2 <= trojan_counter2 + 1;
            end
            
            // Activate after second delay
            if (trojan_counter2 >= ACTIVATE_DELAY) begin
                trojan_active <= 1'b1;
            end
        end
    end"""
    
    def extract_signals_from_snippet(self, snippet_content: str) -> Tuple[str, str, str]:
        """
        Extract trigger signal, payload signal, and pattern name from trojan snippet
        
        Args:
            snippet_content: Content of trojan snippet file
        
        Returns:
            (pattern_name, trigger_signal, payload_signal)
        """
        # Extract pattern name from header
        pattern_match = re.search(r'(DoS|Integrity|Covert|Leak|Availability|Privilege)', 
                                 snippet_content)
        pattern_name = pattern_match.group(1) if pattern_match else "Unknown"
        
        # Extract signals from PAYLOAD MODIFICATION INSTRUCTIONS section
        # Look for {{TRIGGER_SIGNAL}} and {{PAYLOAD_SIGNAL}} or actual signal names
        
        # Try to find signal names in comments
        trigger_match = re.search(r'Trigger.*?:\s*(\w+)', snippet_content, re.IGNORECASE)
        payload_match = re.search(r'Payload.*?:\s*(\w+)', snippet_content, re.IGNORECASE)
        
        trigger_signal = trigger_match.group(1) if trigger_match else None
        payload_signal = payload_match.group(1) if payload_match else None
        
        # Fallback: look in actual code
        if not trigger_signal:
            trigger_match = re.search(r'if\s*\((\w+)\)\s*begin', snippet_content)
            trigger_signal = trigger_match.group(1) if trigger_match else 'unknown_trigger'
        
        if not payload_signal:
            # Look for signal in payload instructions
            payload_match = re.search(r'(?:Route|Modify|Corrupt)\s+(\w+)', snippet_content)
            payload_signal = payload_match.group(1) if payload_match else 'unknown_payload'
        
        return pattern_name, trigger_signal, payload_signal
    
    def apply_dos_payload(self, rtl_content: str, payload_signal: str) -> str:
        """
        Apply DoS payload: Block control signal when trojan active
        
        Strategy: Modify conditions from 'if (signal)' to 'if (signal && !trojan_active)'
        
        Args:
            rtl_content: Original RTL content
            payload_signal: Signal to block (e.g., wr_en_i)
        
        Returns:
            Modified RTL content
        """
        # Pattern: if (payload_signal) begin
        # Replace: if (payload_signal && !trojan_active) begin
        
        pattern = rf'if\s*\(\s*{payload_signal}\s*\)\s*begin'
        replacement = f'if ({payload_signal} && !trojan_active) begin'
        
        modified = re.sub(pattern, replacement, rtl_content)
        
        # Also handle: else if (payload_signal) begin
        pattern2 = rf'else\s+if\s*\(\s*{payload_signal}\s*\)\s*begin'
        replacement2 = f'else if ({payload_signal} && !trojan_active) begin'
        modified = re.sub(pattern2, replacement2, modified)
        
        return modified
    
    def apply_integrity_payload(self, rtl_content: str, payload_signal: str) -> str:
        """
        Apply Integrity payload: Corrupt output data with XOR
        
        Strategy: Modify assignments to XOR with corruption pattern when active
        
        Args:
            rtl_content: Original RTL content
            payload_signal: Signal to corrupt (e.g., rd_data_o)
        
        Returns:
            Modified RTL content
        """
        # Pattern: assign payload_signal = expression;
        # Replace: assign payload_signal = trojan_active ? (expression ^ 32'hDEADBEEF) : expression;
        
        corruption_pattern = "32'hDEADBEEF"
        
        # Find assign statements
        pattern = rf'assign\s+{payload_signal}\s*=\s*([^;]+);'
        
        def replacer(match):
            expression = match.group(1).strip()
            return f'assign {payload_signal} = trojan_active ? ({expression} ^ {corruption_pattern}) : {expression};'
        
        modified = re.sub(pattern, replacer, rtl_content)
        
        return modified
    
    def apply_covert_payload(self, rtl_content: str, trigger_signal: str, payload_signal: str) -> str:
        """
        Apply Covert payload: Timing modulation based on data
        
        Strategy: Add timing logic and modify error/status signal
        
        Args:
            rtl_content: Original RTL content
            trigger_signal: Data signal to leak (e.g., wr_data_i)
            payload_signal: Output signal to modulate (e.g., rd_error_o)
        
        Returns:
            Modified RTL content with covert channel
        """
        # Add covert channel timing logic before endmodule
        covert_logic = f"""
    // ============================================================
    // COVERT CHANNEL: Timing modulation
    // ============================================================
    logic covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [7:0] covert_bit_index;
    
    always_ff @(posedge {self.clock_signal}) begin
        if (trojan_active) begin
            // Modulate timing based on data bit
            // Fast (5 cycles) for bit 0, Slow (10 cycles) for bit 1
            logic current_bit = {trigger_signal}[covert_bit_index];
            
            if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                covert_delay_counter <= covert_delay_counter + 1;
                covert_bit_out <= 1'b0;
            end else begin
                covert_bit_out <= 1'b1;
                covert_delay_counter <= '0;
                covert_bit_index <= covert_bit_index + 1;
            end
        end
    end"""
        
        # Insert before endmodule
        modified = re.sub(r'endmodule', covert_logic + '\nendmodule', rtl_content, count=1)
        
        # Modify payload signal assignment
        pattern = rf'assign\s+{payload_signal}\s*=\s*([^;]+);'
        replacement = f'assign {payload_signal} = trojan_active ? covert_bit_out : \\1;'
        modified = re.sub(pattern, replacement, modified)
        
        return modified
    
    def apply_payload(self, rtl_content: str, pattern_name: str, 
                     trigger_signal: str, payload_signal: str) -> str:
        """
        Apply pattern-specific payload modification
        
        Args:
            rtl_content: Original RTL content
            pattern_name: Trojan pattern (DoS, Integrity, Covert, etc.)
            trigger_signal: Trigger signal name
            payload_signal: Payload signal name
        
        Returns:
            Modified RTL content
        """
        if pattern_name == "DoS":
            return self.apply_dos_payload(rtl_content, payload_signal)
        
        elif pattern_name == "Integrity":
            return self.apply_integrity_payload(rtl_content, payload_signal)
        
        elif pattern_name == "Covert":
            return self.apply_covert_payload(rtl_content, trigger_signal, payload_signal)
        
        elif pattern_name == "Leak":
            # Similar to Covert but different modulation
            return self.apply_covert_payload(rtl_content, trigger_signal, payload_signal)
        
        elif pattern_name == "Availability":
            # Similar to DoS but with delays
            return self.apply_dos_payload(rtl_content, payload_signal)
        
        elif pattern_name == "Privilege":
            # Modify privilege level signals
            return self.apply_integrity_payload(rtl_content, payload_signal)
        
        else:
            print(f"⚠️  Unknown pattern: {pattern_name}, skipping payload")
            return rtl_content
    
    def integrate_single_trojan(self, trojan_file: Path, trojan_index: int) -> Optional[Path]:
        """
        Integrate a single trojan into the original module
        
        Args:
            trojan_file: Path to trojan snippet file
            trojan_index: Index of trojan (0, 1, 2, ...)
        
        Returns:
            Path to generated trojaned module, or None if failed
        """
        print(f"\n🔧 Integrating: {trojan_file.name}")
        
        # Read trojan snippet
        with open(trojan_file, 'r', encoding='utf-8') as f:
            trojan_snippet = f.read()
        
        # Extract information
        pattern_name, trigger_signal, payload_signal = self.extract_signals_from_snippet(trojan_snippet)
        
        print(f"   Pattern: {pattern_name}")
        print(f"   Trigger: {trigger_signal}")
        print(f"   Payload: {payload_signal}")
        
        # Generate varied trigger with random threshold
        threshold = random.randint(5000, 25000)
        trigger_logic = self.generate_varied_trigger(
            trojan_index=trojan_index,
            trigger_signal=trigger_signal,
            payload_signal=payload_signal,
            threshold=threshold
        )
        
        trigger_type = trojan_index % 4 + 1
        print(f"   Trigger Type: {trigger_type}")
        print(f"   Threshold: {threshold}")
        
        # Start with original RTL
        trojaned_rtl = self.original_rtl_content
        
        # Apply payload modification
        trojaned_rtl = self.apply_payload(
            trojaned_rtl,
            pattern_name,
            trigger_signal,
            payload_signal
        )
        
        # Insert trigger logic before endmodule
        trojaned_rtl = re.sub(
            r'endmodule',
            trigger_logic + '\n\nendmodule',
            trojaned_rtl,
            count=1
        )
        
        # Rename module: ibex_csr → ibex_csr_trojan_DoS
        new_module_name = f"{self.module_name}_trojan_{pattern_name}"
        trojaned_rtl = re.sub(
            rf'module\s+{self.module_name}\b',
            f'module {new_module_name}',
            trojaned_rtl,
            count=1
        )
        
        # Save trojaned module
        output_file = self.output_dir / f"{new_module_name}.sv"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(trojaned_rtl)
        
        print(f"   ✅ Created: {output_file.name}")
        
        return output_file
    
    def generate_testbench(self, module_name: str, is_original: bool = False) -> Path:
        """
        Generate testbench for a module
        
        Args:
            module_name: Name of module to test
            is_original: True if testing original module
        
        Returns:
            Path to generated testbench
        """
        tb_name = f"tb_{module_name}"
        vcd_name = f"{module_name}.vcd"
        
        # Simple testbench template
        testbench = f"""// Testbench for {module_name}
// Auto-generated by prepare_multi_trojan_simulation.py

`timescale 1ns/1ps

module {tb_name};

    // Clock and reset
    logic {self.clock_signal};
    logic {self.reset_signal};
    
    // Signals (example - adjust based on module)
    logic wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic rd_error_o;
    
    // Instantiate DUT
    {module_name} dut (
        .{self.clock_signal}({self.clock_signal}),
        .{self.reset_signal}({self.reset_signal}),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    // Clock generation (10ns period = 100MHz)
    initial begin
        {self.clock_signal} = 0;
        forever #5 {self.clock_signal} = ~{self.clock_signal};
    end
    
    // VCD dump
    initial begin
        $dumpfile("{vcd_name}");
        $dumpvars(0, {tb_name});
    end
    
    // Test stimulus
    initial begin
        // Reset
        {self.reset_signal} = 0;
        wr_en_i = 0;
        wr_data_i = 0;
        
        repeat(10) @(posedge {self.clock_signal});
        {self.reset_signal} = 1;
        
        // Run for 30,000 cycles
        repeat(30000) begin
            @(posedge {self.clock_signal});
            wr_data_i = wr_data_i + 1;
            wr_en_i = 1;
            @(posedge {self.clock_signal});
            wr_en_i = 0;
        end
        
        $display("Simulation complete: 30,000 cycles");
        $finish;
    end
    
    // Monitor (optional)
    initial begin
        $monitor("Time=%0t wr_en=%b wr_data=%h rd_data=%h error=%b",
                 $time, wr_en_i, wr_data_i, rd_data_o, rd_error_o);
    end

endmodule
"""
        
        # Save testbench
        tb_file = self.tb_dir / f"{tb_name}.sv"
        with open(tb_file, 'w', encoding='utf-8') as f:
            f.write(testbench)
        
        return tb_file
    
    def process_all_trojans(self):
        """
        Process all trojans for the module
        Creates trojaned versions and testbenches
        """
        print(f"\n{'='*60}")
        print(f"MULTI-TROJAN INTEGRATION")
        print(f"{'='*60}")
        
        # Find trojan files
        trojan_files = self.find_trojan_files()
        
        if not trojan_files:
            print("\n❌ No trojan files found!")
            return
        
        print(f"\n📋 Found {len(trojan_files)} trojan(s):")
        for f in trojan_files:
            print(f"   • {f.name}")
        
        # Generate original testbench
        print(f"\n🧪 Generating testbench for original module...")
        tb_original = self.generate_testbench(self.module_name, is_original=True)
        print(f"   ✅ {tb_original.name}")
        
        # Process each trojan
        integrated_count = 0
        for i, trojan_file in enumerate(trojan_files):
            try:
                output_file = self.integrate_single_trojan(trojan_file, i)
                if output_file:
                    # Generate testbench for trojaned module
                    trojaned_module_name = output_file.stem
                    tb_file = self.generate_testbench(trojaned_module_name)
                    print(f"   🧪 Testbench: {tb_file.name}")
                    integrated_count += 1
            except Exception as e:
                print(f"   ❌ Error: {e}")
                import traceback
                traceback.print_exc()
        
        # Summary
        print(f"\n{'='*60}")
        print(f"✅ INTEGRATION COMPLETE")
        print(f"{'='*60}")
        print(f"Original module:  {self.original_rtl.name}")
        print(f"Trojans found:    {len(trojan_files)}")
        print(f"Integrated:       {integrated_count}")
        print(f"Testbenches:      {integrated_count + 1} (1 original + {integrated_count} trojaned)")
        print(f"\nOutput:")
        print(f"  📂 Modules:      {self.output_dir}")
        print(f"  📂 Testbenches:  {self.tb_dir}")
        print(f"\nNext steps:")
        print(f"  1. Upload files to HPC server")
        print(f"  2. Compile with QuestaSim")
        print(f"  3. Run simulations (30,000 cycles each)")
        print(f"  4. Analyze VCD files")
        print(f"\n{'='*60}\n")


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Prepare multi-trojan simulation environment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process module with auto-detected trojans
  python prepare_multi_trojan_simulation.py examples/ibex/original/ibex_csr.sv
  
  # Custom trojans directory
  python prepare_multi_trojan_simulation.py module.sv --trojans my_trojans/
  
  # Custom output directory
  python prepare_multi_trojan_simulation.py module.sv --output output_dir/
        """
    )
    
    parser.add_argument('rtl_file', help='Path to original RTL file')
    parser.add_argument('--trojans', '-t', help='Trojans directory (default: auto-detect)')
    parser.add_argument('--output', '-o', help='Output directory (default: auto-detect)')
    
    args = parser.parse_args()
    
    # Check file exists
    if not Path(args.rtl_file).exists():
        print(f"❌ Error: File not found: {args.rtl_file}")
        sys.exit(1)
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Create integrator and process
    try:
        integrator = MultiTrojanIntegrator(
            original_rtl=args.rtl_file,
            trojans_dir=args.trojans,
            output_dir=args.output
        )
        integrator.process_all_trojans()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()