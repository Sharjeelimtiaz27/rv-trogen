#!/usr/bin/env python3
"""
Combinational Trojan Generator
Generates Trojans for combinational modules (always_comb, assign statements)
Uses template-based generation approach
"""

from typing import Dict, List
from dataclasses import dataclass

from .template_loader import TemplateLoader
from .placeholder_handler import PlaceholderHandler


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
    Generates Trojans for Combinational Modules using Templates
    
    Combinational modules have:
    - No clock signal
    - No state
    - always_comb blocks or continuous assignments
    - Pure logic functions
    
    Trojan Generation Strategy:
    - Load template from templates/trojan_templates/combinational/
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
        
        # Initialize template loader and placeholder handler
        self.loader = TemplateLoader()
        self.handler = PlaceholderHandler()
    
    def generate_dos_trojan(self, trojan_id: str, trigger_signals: List,
                           payload_signals: List) -> CombinationalTrojanCode:
        """Generate DoS Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'enable'
        payload_sig = payload_signals[0].name if payload_signals else 'valid_out'
        
        # Load template
        template = self.loader.load_template('dos', 'combinational')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Information Leakage Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'debug_mode'
        payload_sig = payload_signals[0].name if payload_signals else 'secret_data'
        data_width = self._get_signal_width(payload_signals[0]) if payload_signals else '31'
        
        # Load template
        template = self.loader.load_template('leak', 'combinational')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
            'DATA_WIDTH': data_width,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Privilege Escalation Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'addr_in'
        payload_sig = payload_signals[0].name if payload_signals else 'access_fault'
        
        # Load template
        template = self.loader.load_template('privilege', 'combinational')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Integrity Violation Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'data_in'
        payload_sig = payload_signals[0].name if payload_signals else 'data_out'
        data_width = self._get_signal_width(payload_signals[0]) if payload_signals else '31'
        
        # Load template
        template = self.loader.load_template('integrity', 'combinational')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
            'DATA_WIDTH': data_width,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Performance Degradation Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'request'
        payload_sig = payload_signals[0].name if payload_signals else 'ready'
        
        # Load template
        template = self.loader.load_template('availability', 'combinational')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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
        """Generate Covert Channel Trojan using template"""
        
        trigger_sig = trigger_signals[0].name if trigger_signals else 'secret_bit'
        payload_sig = payload_signals[0].name if payload_signals else 'output_signal'
        
        # Load template
        template = self.loader.load_template('covert', 'combinational')
        
        # Prepare replacements
        replacements = {
            'TROJAN_ID': trojan_id,
            'MODULE_NAME': self.module.name,
            'TRIGGER_SIGNAL': trigger_sig,
            'PAYLOAD_SIGNAL': payload_sig,
        }
        
        # Replace placeholders
        code = self.handler.replace_placeholders(template, replacements)
        
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