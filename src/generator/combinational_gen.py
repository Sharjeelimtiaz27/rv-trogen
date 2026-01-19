#!/usr/bin/env python3
"""
Combinational Trojan Generator - FIXED VERSION
NO FALLBACKS - Uses ONLY real signals from parsed RTL
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
    
    STRICT MODE: Only generates if REAL signals exist
    NO FALLBACKS to hardcoded signal names
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
        """Generate DoS Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("DoS trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("DoS trojan requires payload signal to disable")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"DoS trojan: disables {payload_sig} on pattern match"
        )
    
    def generate_leak_trojan(self, trojan_id: str, trigger_signals: List,
                            payload_signals: List) -> CombinationalTrojanCode:
        """Generate Information Leakage Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Leak trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Leak trojan requires payload signal (secret data)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
        # Load template
        template = self.loader.load_template('leak', 'combinational')
        
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
            pattern_name='Leak',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Leak trojan: leaks {payload_sig} on trigger"
        )
    
    def generate_privilege_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> CombinationalTrojanCode:
        """Generate Privilege Escalation Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Privilege trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Privilege trojan requires payload signal (privilege level)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Privilege trojan: escalates {payload_sig} to M-mode"
        )
    
    def generate_integrity_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> CombinationalTrojanCode:
        """Generate Integrity Violation Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Integrity trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Integrity trojan requires payload signal (data to corrupt)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
        # Load template
        template = self.loader.load_template('integrity', 'combinational')
        
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
            pattern_name='Integrity',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Integrity trojan: corrupts {payload_sig} conditionally"
        )
    
    def generate_availability_trojan(self, trojan_id: str, trigger_signals: List,
                                    payload_signals: List) -> CombinationalTrojanCode:
        """Generate Performance Degradation Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Availability trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Availability trojan requires payload signal (ready/valid)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Availability trojan: conditionally delays {payload_sig}"
        )
    
    def generate_covert_trojan(self, trojan_id: str, trigger_signals: List,
                               payload_signals: List) -> CombinationalTrojanCode:
        """Generate Covert Channel Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Covert trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Covert trojan requires payload signal (secret data)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Covert trojan: encodes {payload_sig} into output"
        )
    
    def generate(self, pattern_name: str, trojan_id: str,
                trigger_signals: List, payload_signals: List) -> CombinationalTrojanCode:
        """
        Main generation dispatcher
        
        Args:
            pattern_name: Name of Trojan pattern
            trojan_id: Unique ID for this Trojan
            trigger_signals: List of trigger Signal objects (MUST NOT BE EMPTY)
            payload_signals: List of payload Signal objects (MUST NOT BE EMPTY)
        
        Returns:
            CombinationalTrojanCode object
            
        Raises:
            ValueError: If no matching signals found
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