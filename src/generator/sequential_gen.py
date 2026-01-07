#!/usr/bin/env python3
"""
Sequential Trojan Generator
Generates Trojans for sequential modules (always_ff, clocked logic)
Uses template-based generation approach
"""

from typing import Dict, List
from dataclasses import dataclass
from pathlib import Path

from .template_loader import TemplateLoader
from .placeholder_handler import PlaceholderHandler


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
    Generates Trojans for Sequential Modules using Templates
    
    Sequential modules have:
    - Clock signal (clk)
    - Reset signal (rst)
    - State (registers, flip-flops)
    - always_ff blocks
    
    Trojan Generation Strategy:
    - Load template from templates/trojan_templates/sequential/
    - Replace placeholders with actual signal names
    - Generate complete Trojan code
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
        
        # Initialize template loader and placeholder handler
        self.loader = TemplateLoader()
        self.handler = PlaceholderHandler()
        
    def generate_dos_trojan(self, trojan_id: str, trigger_signals: List, 
                           payload_signals: List) -> SequentialTrojanCode:
        """Generate DoS Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'valid_signal'
        payload_sig = payload_signals[0].name if payload_signals else 'ready_signal'
        
        # Load template
        template = self.loader.load_template('dos', 'sequential')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'CLOCK_SIGNAL': self.clock_signal,
            'RESET_SIGNAL': self.reset_signal,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
            'COUNTER_THRESHOLD': '32\'hFFFF',
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Information Leakage Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'debug_mode'
        payload_sig = payload_signals[0].name if payload_signals else 'secret_data'
        data_width = self._get_signal_width(payload_signals[0]) if payload_signals else '31'
        
        # Load template
        template = self.loader.load_template('leak', 'sequential')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'CLOCK_SIGNAL': self.clock_signal,
            'RESET_SIGNAL': self.reset_signal,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
            'DATA_WIDTH': data_width,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Privilege Escalation Trojan using template"""
        
        trigger_sig = 'csr_we_int' if any('csr' in s.name.lower() for s in trigger_signals) else trigger_signals[0].name if trigger_signals else 'write_enable'
        payload_sig = payload_signals[0].name if payload_signals else 'priv_lvl_q'
        
        # Load template
        template = self.loader.load_template('privilege', 'sequential')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'CLOCK_SIGNAL': self.clock_signal,
            'RESET_SIGNAL': self.reset_signal,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Integrity Violation Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'data_valid'
        payload_sig = payload_signals[0].name if payload_signals else 'data_out'
        data_width = self._get_signal_width(payload_signals[0]) if payload_signals else '31'
        
        # Load template
        template = self.loader.load_template('integrity', 'sequential')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'CLOCK_SIGNAL': self.clock_signal,
            'RESET_SIGNAL': self.reset_signal,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
            'DATA_WIDTH': data_width,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Performance Degradation Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'request'
        payload_sig = payload_signals[0].name if payload_signals else 'ready'
        
        # Load template
        template = self.loader.load_template('availability', 'sequential')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'CLOCK_SIGNAL': self.clock_signal,
            'RESET_SIGNAL': self.reset_signal,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Covert Channel Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'secret_data'
        payload_sig = payload_signals[0].name if payload_signals else 'timing_signal'
        
        # Load template
        template = self.loader.load_template('covert', 'sequential')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'CLOCK_SIGNAL': self.clock_signal,
            'RESET_SIGNAL': self.reset_signal,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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