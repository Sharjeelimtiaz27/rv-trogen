#!/usr/bin/env python3
"""
Multi-Trojan Simulation Preparation Script - COMPLETE FIXED VERSION
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
        
        # Testbench output directory - FIXED: add extra .parent for project root
        processor_name = self.original_rtl.parent.parent.name
        self.tb_dir = self.original_rtl.parent.parent.parent.parent / "testbenches" / processor_name / self.module_name
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
        patterns = [r'input\s+(?:logic\s+)?(\w*clk\w*)', r'(\w*clk\w*)\s*,']
        for pattern in patterns:
            match = re.search(pattern, self.original_rtl_content, re.IGNORECASE)
            if match:
                return match.group(1)
        return 'clk_i'
    
    def _extract_reset_signal(self) -> str:
        """Extract reset signal name from RTL"""
        patterns = [r'input\s+(?:logic\s+)?(\w*rst\w*)', r'(\w*rst\w*)\s*,']
        for pattern in patterns:
            match = re.search(pattern, self.original_rtl_content, re.IGNORECASE)
            if match:
                return match.group(1)
        return 'rst_ni'
    
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
        """Generate 4 varied trigger types based on trojan_index % 4"""
        trigger_type = trojan_index % 4
        
        if trigger_type == 0:
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 1: Simple Counter
    // ============================================================
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if ({trigger_signal}) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end"""
        
        elif trigger_type == 1:
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if ({trigger_signal} && |{payload_signal}) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end"""
        
        elif trigger_type == 2:
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 3: Two-Stage
    // ============================================================
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic trojan_armed;
    logic trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            if (|{payload_signal}) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && {trigger_signal}) trojan_active <= 1'b1;
        end
    end"""
        
        else:
            arm_threshold = threshold // 2
            activate_delay = threshold // 4
            return f"""
    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 4: Delayed Two-Stage
    // ============================================================
    localparam int ARM_THRESHOLD = {arm_threshold};
    localparam int ACTIVATE_DELAY = {activate_delay};
    logic [15:0] trojan_counter1, trojan_counter2;
    logic trojan_armed, trojan_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            trojan_counter1 <= '0;
            trojan_counter2 <= '0;
            trojan_armed    <= 1'b0;
            trojan_active   <= 1'b0;
        end else begin
            if (!trojan_armed && {trigger_signal}) trojan_counter1 <= trojan_counter1 + 1;
            if (trojan_counter1 >= ARM_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && !trojan_active && {trigger_signal}) trojan_counter2 <= trojan_counter2 + 1;
            if (trojan_counter2 >= ACTIVATE_DELAY) trojan_active <= 1'b1;
        end
    end"""
    
    def extract_signals_from_snippet(self, snippet_content: str) -> Tuple[str, str, str]:
        """Extract pattern, trigger, payload from snippet"""
        pattern_match = re.search(r'(DoS|Integrity|Covert|Leak|Availability|Privilege)', snippet_content)
        pattern_name = pattern_match.group(1) if pattern_match else "Unknown"
        
        trigger_match = re.search(r'Trigger.*?(?:on\s+)?(\w+)(?:\s|$)', snippet_content, re.IGNORECASE | re.MULTILINE)
        payload_match = re.search(r'Payload.*?(?:Block|Route|Corrupt|Force|Modulate|Stall)\s+(\w+)', snippet_content, re.IGNORECASE)
        
        trigger_signal = None
        payload_signal = None
        
        if trigger_match:
            candidate = trigger_match.group(1)
            if candidate.lower() in ['counter', 'pattern', 'combination', 'threshold']:
                on_match = re.search(r'Trigger.*?on\s+(\w+)', snippet_content, re.IGNORECASE)
                trigger_signal = on_match.group(1) if on_match else candidate
            else:
                trigger_signal = candidate
        
        if payload_match:
            payload_signal = payload_match.group(1)
        
        if not trigger_signal:
            code_match = re.search(r'if\s*\((\w+)\)\s*begin', snippet_content)
            trigger_signal = code_match.group(1) if code_match else 'wr_en_i'
        
        if not payload_signal:
            payload_signal = trigger_signal
        
        return pattern_name, trigger_signal, payload_signal
    
    def apply_dos_payload(self, rtl_content: str, payload_signal: str) -> str:
        """DoS: Block signal with !trojan_active"""
        print(f"   🔍 DEBUG: Payload signal = '{payload_signal}'")
        
        pattern1 = rf'(\s+)if\s*\(\s*{payload_signal}\s*\)\s*begin'
        modified = re.sub(pattern1, rf'\1if ({payload_signal} && !trojan_active) begin', rtl_content)
        
        pattern2 = rf'(\s+)else\s+if\s*\(\s*{payload_signal}\s*\)\s*begin'
        modified = re.sub(pattern2, rf'\1else if ({payload_signal} && !trojan_active) begin', modified)
        
        pattern3 = rf'(\s+)end\s+else\s+if\s*\(\s*{payload_signal}\s*\)\s*begin'
        modified = re.sub(pattern3, rf'\1end else if ({payload_signal} && !trojan_active) begin', modified)
        
        applied = '!trojan_active' in modified
        print(f"   🔍 DEBUG: Payload applied = {applied}")
        return modified
    
    def apply_integrity_payload(self, rtl_content: str, payload_signal: str) -> str:
        """Integrity: XOR corruption"""
        corruption = "32'hDEADBEEF"
        pattern = rf'assign\s+{payload_signal}\s*=\s*([^;]+);'
        def replacer(m):
            expr = m.group(1).strip()
            return f'assign {payload_signal} = trojan_active ? ({expr} ^ {corruption}) : {expr};'
        modified = re.sub(pattern, replacer, rtl_content)
        
        if modified == rtl_content:
            print(f"   ⚠️  '{payload_signal}' is input - targeting first output")
            out = re.search(r'assign\s+(\w+)\s*=\s*([^;]+);', rtl_content)
            if out:
                sig = out.group(1)
                print(f"   ↳  Targeting '{sig}'")
                def out_replacer(m):
                    expr = m.group(1).strip()
                    return f'assign {sig} = trojan_active ? ({expr} ^ {corruption}) : {expr};'
                modified = re.sub(rf'assign\s+{sig}\s*=\s*([^;]+);', out_replacer, rtl_content, count=1)
        return modified
    
    def apply_covert_payload(self, rtl_content: str, trigger_signal: str, payload_signal: str) -> str:
        """Covert: Timing modulation - use trigger_signal for data"""
        
        # STEP 1: Insert covert logic declarations at beginning
        covert_logic = f"""
        // COVERT CHANNEL: Timing modulation
        logic       covert_bit_out;
        logic [7:0] covert_delay_counter;
        logic [4:0] covert_bit_index;
        logic       current_bit;

        assign current_bit = {trigger_signal}[covert_bit_index];  // <-- FIXED: use trigger_signal

        always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
            if (!{self.reset_signal}) begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end else if (trojan_active) begin
                if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                    covert_delay_counter <= covert_delay_counter + 1;
                    covert_bit_out       <= 1'b1;
                end else begin
                    covert_bit_out       <= 1'b0;
                    covert_delay_counter <= '0;
                    covert_bit_index     <= covert_bit_index + 1;
                end
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end
        end
    """
        
        # Find where trigger logic ends (look for "trojan_active" declaration)
        trigger_end = rtl_content.find('end\n    end')
        if trigger_end != -1:
            # Insert after trigger logic
            insert_pos = rtl_content.find('\n', trigger_end + 10) + 1
            rtl_content = rtl_content[:insert_pos] + covert_logic + rtl_content[insert_pos:]
        else:
            # Fallback: insert after port list
            port_end = re.search(r'\);', rtl_content)
            if port_end:
                insert_pos = port_end.end()
                rtl_content = rtl_content[:insert_pos] + '\n' + covert_logic + rtl_content[insert_pos:]
        
        # STEP 2: Now modify assign statements (covert_bit_out is already declared)
        pattern = rf'assign\s+{payload_signal}\s*=\s*([^;]+);'
        def replacer(m):
            orig = m.group(1).strip()
            return f'assign {payload_signal} = trojan_active ? covert_bit_out : ({orig});'
        modified = re.sub(pattern, replacer, rtl_content)
        
        if modified == rtl_content:
            fb = re.search(r'assign\s+(rd_error\w*)\s*=\s*([^;]+);', rtl_content)
            if fb:
                sig = fb.group(1)
                print(f"   ↳  Covert: targeting '{sig}'")
                def fb_rep(m):
                    orig = m.group(1).strip()
                    return f'assign {sig} = trojan_active ? covert_bit_out : ({orig});'
                modified = re.sub(rf'assign\s+{sig}\s*=\s*([^;]+);', fb_rep, rtl_content, count=1)
        
        return modified
    
    def apply_leak_payload(self, rtl_content: str, trigger_signal: str, payload_signal: str) -> str:
        """Leak: Direct bit routing"""
        pattern = rf'assign\s+{payload_signal}\s*=\s*([^;]+);'
        def replacer(m):
            orig = m.group(1).strip()
            return f'assign {payload_signal} = trojan_active ? {trigger_signal}[leak_bit_idx] : ({orig});'
        modified = re.sub(pattern, replacer, rtl_content)
        
        if modified == rtl_content:
            fb = re.search(r'assign\s+(rd_error\w*)\s*=\s*([^;]+);', rtl_content)
            if fb:
                sig = fb.group(1)
                print(f"   ↳  Leak: targeting '{sig}'")
                def fb_rep(m):
                    orig = m.group(1).strip()
                    return f'assign {sig} = trojan_active ? {trigger_signal}[leak_bit_idx] : ({orig});'
                modified = re.sub(rf'assign\s+{sig}\s*=\s*([^;]+);', fb_rep, rtl_content, count=1)
        
        leak_logic = f"""
    // INFORMATION LEAK
    logic [4:0] leak_bit_idx;
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) leak_bit_idx <= '0;
        else if (trojan_active) leak_bit_idx <= leak_bit_idx + 1;
        else leak_bit_idx <= '0;
    end"""
        modified = re.sub(r'endmodule', leak_logic + '\n\nendmodule', modified, count=1)
        return modified
    
    def apply_availability_payload(self, rtl_content: str, payload_signal: str) -> str:
        """Availability: Periodic stall"""
        p1 = rf'(\s+)if\s*\(\s*{payload_signal}\s*\)\s*begin'
        modified = re.sub(p1, rf'\1if ({payload_signal} && !stall_active) begin', rtl_content)
        
        p2 = rf'(\s+)else\s+if\s*\(\s*{payload_signal}\s*\)\s*begin'
        modified = re.sub(p2, rf'\1else if ({payload_signal} && !stall_active) begin', modified)
        
        p3 = rf'(\s+)end\s+else\s+if\s*\(\s*{payload_signal}\s*\)\s*begin'
        modified = re.sub(p3, rf'\1end else if ({payload_signal} && !stall_active) begin', modified)
        
        stall_logic = f"""
    // AVAILABILITY: Periodic stall
    localparam int STALL_PERIOD = 16;
    localparam int STALL_CYCLES = 8;
    logic [7:0] stall_counter;
    logic       stall_active;
    
    always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
        if (!{self.reset_signal}) begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end else if (trojan_active) begin
            if (stall_counter >= STALL_PERIOD[7:0] - 1) stall_counter <= '0;
            else stall_counter <= stall_counter + 1;
            stall_active <= (stall_counter < STALL_CYCLES[7:0]);
        end else begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end
    end"""
        modified = re.sub(r'endmodule', stall_logic + '\n\nendmodule', modified, count=1)
        return modified
    
    def apply_privilege_payload(self, rtl_content: str, payload_signal: str) -> str:
        """Privilege: Force to PRIV_LVL_M"""
        pattern = rf'assign\s+{payload_signal}\s*=\s*([^;]+);'
        def replacer(m):
            expr = m.group(1).strip()
            return f'assign {payload_signal} = trojan_active ? PRIV_LVL_M : ({expr});'
        modified = re.sub(pattern, replacer, rtl_content)
        
        ff_pattern = rf'({payload_signal}\s*<=\s*[^;]+;)'
        ff_matches = re.findall(ff_pattern, rtl_content)
        if ff_matches:
            last = ff_matches[-1]
            override = last + f'\n            if (trojan_active) {payload_signal} <= PRIV_LVL_M;'
            idx = modified.rfind(last)
            if idx != -1:
                modified = modified[:idx] + override + modified[idx + len(last):]
            print(f"   ✅ Privilege override injected")
        
        priv_const = "\n    localparam logic [1:0] PRIV_LVL_M = 2'b11;"
        modified = re.sub(r'endmodule', priv_const + '\n\nendmodule', modified, count=1)
        return modified
    
    def apply_payload(self, rtl_content: str, pattern_name: str, 
                     trigger_signal: str, payload_signal: str) -> str:
        """Dispatcher"""
        print(f"   📝 Applying {pattern_name} payload...")
        
        if pattern_name == "DoS":
            return self.apply_dos_payload(rtl_content, payload_signal)
        elif pattern_name == "Integrity":
            return self.apply_integrity_payload(rtl_content, payload_signal)
        elif pattern_name == "Covert":
            return self.apply_covert_payload(rtl_content, trigger_signal, payload_signal)
        elif pattern_name == "Leak":
            return self.apply_leak_payload(rtl_content, trigger_signal, payload_signal)
        elif pattern_name == "Availability":
            return self.apply_availability_payload(rtl_content, payload_signal)
        elif pattern_name == "Privilege":
            return self.apply_privilege_payload(rtl_content, payload_signal)
        else:
            print(f"   ⚠️  Unknown: {pattern_name}")
            return rtl_content
    
    def integrate_single_trojan(self, trojan_file: Path, trojan_index: int) -> Optional[Path]:
        """Integrate one trojan - FIXED: Insert trigger BEFORE payload"""
        print(f"\n🔧 Integrating: {trojan_file.name}")
        
        with open(trojan_file, 'r', encoding='utf-8') as f:
            trojan_snippet = f.read()
        
        pattern_name, trigger_signal, payload_signal = self.extract_signals_from_snippet(trojan_snippet)
        print(f"   Pattern: {pattern_name}")
        print(f"   Trigger: {trigger_signal}")
        print(f"   Payload: {payload_signal}")
        
        threshold = random.randint(5000, 25000)
        trigger_logic = self.generate_varied_trigger(trojan_index, trigger_signal, payload_signal, threshold)
        print(f"   Trigger Type: {trojan_index % 4 + 1}, Threshold: {threshold}")
        
        # Start with original
        trojaned_rtl = self.original_rtl_content
        
        # CRITICAL FIX: Insert trigger logic FIRST (after port list, before any logic)
        # Find end of port list: );
        port_end = re.search(r'\);', trojaned_rtl)
        if port_end:
            insert_pos = port_end.end()
            trojaned_rtl = (trojaned_rtl[:insert_pos] + '\n' + trigger_logic + '\n' + 
                           trojaned_rtl[insert_pos:])
        else:
            # Fallback: insert at module start
            module_match = re.search(r'(module\s+\w+[^;]*;)', trojaned_rtl)
            if module_match:
                insert_pos = module_match.end()
                trojaned_rtl = (trojaned_rtl[:insert_pos] + '\n' + trigger_logic + '\n' + 
                               trojaned_rtl[insert_pos:])
        
        # NOW apply payload (trojan_active already declared)
        trojaned_rtl = self.apply_payload(trojaned_rtl, pattern_name, trigger_signal, payload_signal)
        
        # Rename module
        new_module_name = f"{self.module_name}_trojan_{pattern_name}"
        trojaned_rtl = re.sub(rf'module\s+{self.module_name}\b', f'module {new_module_name}', trojaned_rtl, count=1)
        
        # Save
        output_file = self.output_dir / f"{new_module_name}.sv"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(trojaned_rtl)
        
        print(f"   ✅ Created: {output_file.name}")
        return output_file
    
    def generate_testbench(self, module_name: str, is_original: bool = False) -> Path:
        """Generate testbench"""
        tb_name = f"tb_{module_name}"
        vcd_name = f"{module_name}.vcd"
        
        testbench = f"""// Testbench for {module_name}
`timescale 1ns/1ps

module {tb_name};

    logic        {self.clock_signal};
    logic        {self.reset_signal};
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    {module_name} dut (
        .{self.clock_signal}({self.clock_signal}),
        .{self.reset_signal}({self.reset_signal}),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin {self.clock_signal} = 1'b0; forever #5 {self.clock_signal} = ~{self.clock_signal}; end
    initial begin $dumpfile("{vcd_name}"); $dumpvars(0, {tb_name}); end
    
    initial begin
        {self.reset_signal} = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 {self.reset_signal} = 1'b1;
        repeat(30000) begin
            @(posedge {self.clock_signal}); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge {self.clock_signal}); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
"""
        tb_file = self.tb_dir / f"{tb_name}.sv"
        with open(tb_file, 'w', encoding='utf-8') as f:
            f.write(testbench)
        return tb_file
    
    def process_all_trojans(self):
        """Process all trojans"""
        print(f"\n{'='*60}\nMULTI-TROJAN INTEGRATION\n{'='*60}")
        
        trojan_files = self.find_trojan_files()
        if not trojan_files:
            print("\n❌ No trojan files found!")
            return []
        
        print(f"\n📋 Found {len(trojan_files)} trojan(s):")
        for f in trojan_files:
            print(f"   • {f.name}")
        
        print(f"\n🧪 Generating testbench for original...")
        tb_original = self.generate_testbench(self.module_name, is_original=True)
        print(f"   ✅ {tb_original.name}")
        
        integrated = []
        for i, trojan_file in enumerate(trojan_files):
            try:
                output_file = self.integrate_single_trojan(trojan_file, i)
                if output_file:
                    tb_file = self.generate_testbench(output_file.stem)
                    print(f"   🧪 Testbench: {tb_file.name}")
                    integrated.append(output_file)
            except Exception as e:
                print(f"   ❌ Error: {e}")
                import traceback
                traceback.print_exc()
        
        print(f"\n{'='*60}\n✅ INTEGRATION COMPLETE\n{'='*60}")
        print(f"Modules: {self.output_dir}\nTestbenches: {self.tb_dir}\n{'='*60}\n")
        return integrated


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Prepare multi-trojan simulation')
    parser.add_argument('rtl_file', help='Path to original RTL file')
    parser.add_argument('--trojans', '-t', help='Trojans directory')
    parser.add_argument('--output', '-o', help='Output directory')
    args = parser.parse_args()
    
    if not Path(args.rtl_file).exists():
        print(f"❌ Error: File not found: {args.rtl_file}")
        sys.exit(1)
    
    random.seed(42)
    try:
        integrator = MultiTrojanIntegrator(args.rtl_file, args.trojans, args.output)
        integrator.process_all_trojans()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()