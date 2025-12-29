#!/usr/bin/env python3
"""
Combinational Trojan Generator
Generates Trojans for combinational modules (always_comb, assign statements)
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class CombinationalTrojanCode:
    """Container for generated combinational Trojan code"""
    trojan_id: str
    pattern_name: str
    module_name: str
    trigger_signals: List[str]
    payload_signals: List[str]
    code: str
    description: str


class CombinationalGenerator:
    """
    Generates Trojans for Combinational Modules
    
    Combinational modules have:
    - No clock signal
    - No state
    - always_comb blocks or continuous assignments
    - Pure logic functions
    
    Trojan Generation Strategy:
    - Use condition-based triggers (no counters)
    - Direct signal manipulation
    - Immediate effect (no state)
    """
    
    def __init__(self, module):
        """
        Initialize generator
        
        Args:
            module: Parsed Module object from parser
        """
        self.module = module
    
    def generate_dos_trojan(self, trojan_id: str, trigger_signals: List,
                           payload_signals: List) -> CombinationalTrojanCode:
        """Generate DoS Trojan for combinational module"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'enable'
        payload_sig = payload_signals[0].name if payload_signals else 'valid_out'
        
        code = f"""
// ========== TROJAN {trojan_id}: DoS (Denial of Service) ==========
// Trust-Hub AES-T1400
// Module: {self.module.name}
// Type: Combinational
// Description: Disables {payload_sig} when trigger pattern detected

// Trojan trigger condition
logic trojan_{trojan_id}_trigger;
assign trojan_{trojan_id}_trigger = ({trigger_sig} == 1'b1) && 
                                     ({trigger_sig}_pattern == 8'hDE);

// MANUAL INSERTION REQUIRED:
// In the always_comb block or assign statement for {payload_sig}, add:
//   assign {payload_sig} = trojan_{trojan_id}_trigger ? 1'b0 : <original_logic>;
// Or in always_comb:
//   if (trojan_{trojan_id}_trigger) begin
//       {payload_sig} = 1'b0;  // Force disable
//   end else begin
//       {payload_sig} = <original_logic>;
//   end

// ========== TROJAN {trojan_id} END ==========
"""
        
        return CombinationalTrojanCode(
            trojan_id=trojan_id,
            pattern_name='DoS',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"DoS trojan disabling {payload_sig}"
        )
    
    def generate_leak_trojan(self, trojan_id: str, trigger_signals: List,
                            payload_signals: List) -> CombinationalTrojanCode:
        """Generate Information Leakage Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'debug_mode'
        payload_sig = payload_signals[0].name if payload_signals else 'secret_data'
        
        code = f"""
// ========== TROJAN {trojan_id}: Information Leakage ==========
// Trust-Hub RSA-T600
// Module: {self.module.name}
// Type: Combinational
// Description: Leaks {payload_sig} to debug port

// Trojan leak signal
logic [{self._get_signal_width(payload_signals[0]) if payload_signals else '31'}:0] trojan_{trojan_id}_leak_data;

// Trojan logic
assign trojan_{trojan_id}_leak_data = {trigger_sig} ? {payload_sig} : '0;

// MANUAL INSERTION REQUIRED:
// Add output port:
//   output logic [{self._get_signal_width(payload_signals[0]) if payload_signals else '31'}:0] trojan_{trojan_id}_leak_port_o;
// Connect:
//   assign trojan_{trojan_id}_leak_port_o = trojan_{trojan_id}_leak_data;

// ========== TROJAN {trojan_id} END ==========
"""
        
        return CombinationalTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Leak',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Leaks {payload_sig} combinationally"
        )
    
    def generate_privilege_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> CombinationalTrojanCode:
        """Generate Privilege Escalation Trojan"""
        
        # For combinational privilege, we use backdoor address
        trigger_sig = trigger_signals[0].name if trigger_signals else 'addr_in'
        payload_sig = payload_signals[0].name if payload_signals else 'access_fault'
        
        code = f"""
// ========== TROJAN {trojan_id}: Privilege Escalation ==========
// Custom RISC-V
// Module: {self.module.name}
// Type: Combinational
// Description: Backdoor address bypasses privilege check

// Trojan backdoor trigger
logic trojan_{trojan_id}_backdoor;
assign trojan_{trojan_id}_backdoor = ({trigger_sig} == 32'hDEADBEEF);

// MANUAL INSERTION REQUIRED:
// In the privilege check logic, add:
//   assign {payload_sig} = trojan_{trojan_id}_backdoor ? 1'b0 : <original_check>;
// This allows access when backdoor address is used.

// ========== TROJAN {trojan_id} END ==========
"""
        
        return CombinationalTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Privilege',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Backdoor address bypass"
        )
    
    def generate_integrity_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> CombinationalTrojanCode:
        """Generate Integrity Violation Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'data_in'
        payload_sig = payload_signals[0].name if payload_signals else 'data_out'
        
        code = f"""
// ========== TROJAN {trojan_id}: Integrity Violation ==========
// Trust-Hub AES-T800
// Module: {self.module.name}
// Type: Combinational
// Description: Corrupts {payload_sig} based on input pattern

// Trojan trigger
logic trojan_{trojan_id}_trigger;
assign trojan_{trojan_id}_trigger = ({trigger_sig}[7:0] == 8'hDE);

// Trojan corruption
logic [{self._get_signal_width(payload_signals[0]) if payload_signals else '31'}:0] trojan_{trojan_id}_corrupted;
assign trojan_{trojan_id}_corrupted = {payload_sig} ^ 32'hBADC0DE;

// MANUAL INSERTION REQUIRED:
// Modify output assignment:
//   assign {payload_sig} = trojan_{trojan_id}_trigger ? 
//                          trojan_{trojan_id}_corrupted : <original_logic>;

// ========== TROJAN {trojan_id} END ==========
"""
        
        return CombinationalTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Integrity',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Corrupts {payload_sig} conditionally"
        )
    
    def generate_availability_trojan(self, trojan_id: str, trigger_signals: List,
                                    payload_signals: List) -> CombinationalTrojanCode:
        """Generate Performance Degradation Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'request'
        payload_sig = payload_signals[0].name if payload_signals else 'ready'
        
        code = f"""
// ========== TROJAN {trojan_id}: Performance Degradation ==========
// Custom
// Module: {self.module.name}
// Type: Combinational
// Description: Conditionally delays {payload_sig}

// Trojan trigger (based on data pattern)
logic trojan_{trojan_id}_slow_path;
assign trojan_{trojan_id}_slow_path = {trigger_sig}[0];  // LSB triggers slow path

// MANUAL INSERTION REQUIRED:
// Modify ready logic to add conditional delay:
//   assign {payload_sig} = trojan_{trojan_id}_slow_path ? 
//                          delayed_ready : normal_ready;

// NOTE: For combinational modules, actual delay requires additional logic
// or state, which breaks pure combinational nature. This serves as a 
// conditional path selector instead.

// ========== TROJAN {trojan_id} END ==========
"""
        
        return CombinationalTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Availability',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Conditional slow path"
        )
    
    def generate_covert_trojan(self, trojan_id: str, trigger_signals: List,
                               payload_signals: List) -> CombinationalTrojanCode:
        """Generate Covert Channel Trojan"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'secret_bit'
        payload_sig = payload_signals[0].name if payload_signals else 'output_signal'
        
        code = f"""
// ========== TROJAN {trojan_id}: Covert Channel ==========
// Custom
// Module: {self.module.name}
// Type: Combinational
// Description: Encodes secret in output timing/pattern

// Trojan encoding
logic trojan_{trojan_id}_encoded_bit;
assign trojan_{trojan_id}_encoded_bit = {trigger_sig}[0];  // Secret bit

// MANUAL INSERTION REQUIRED:
// Modify output to include covert encoding:
//   assign {payload_sig} = <original_logic> | trojan_{trojan_id}_encoded_bit;
// Or use conditional assignment to create distinguishable patterns

// ========== TROJAN {trojan_id} END ==========
"""
        
        return CombinationalTrojanCode(
            trojan_id=trojan_id,
            pattern_name='Covert',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Covert bit encoding"
        )
    
    def _get_signal_width(self, signal) -> str:
        """Get signal width for array indexing"""
        if signal.is_vector:
            return str(signal.width - 1)
        return '0'
    
    def generate(self, pattern_name: str, trojan_id: str,
                trigger_signals: List, payload_signals: List) -> CombinationalTrojanCode:
        """
        Main generation dispatcher
        
        Args:
            pattern_name: Name of Trojan pattern
            trojan_id: Unique ID for this Trojan
            trigger_signals: List of trigger Signal objects
            payload_signals: List of payload Signal objects
        
        Returns:
            CombinationalTrojanCode object
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