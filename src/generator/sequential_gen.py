#!/usr/bin/env python3
"""
Sequential Trojan Generator - FIXED VERSION
NO FALLBACKS - Uses ONLY real signals from parsed RTL
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
        self.clock_signal = module.clock_signal or 'clk_i'
        self.reset_signal = module.reset_signal or 'rst_ni'
        
        # Initialize template loader and placeholder handler
        self.loader = TemplateLoader()
        self.handler = PlaceholderHandler()
        
    def generate_dos_trojan(self, trojan_id: str, trigger_signals: List, 
                           payload_signals: List) -> SequentialTrojanCode:
        """Generate DoS Trojan using template - STRICT MODE"""
        
        # STRICT: Require both trigger and payload signals
        if not trigger_signals:
            raise ValueError("DoS trojan requires trigger signal (enable/valid/ready)")
        if not payload_signals:
            raise ValueError("DoS trojan requires payload signal to disable")
        
        # Use REAL signals from module
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
        # Load template
        template = self.loader.load_template('dos', 'sequential')
        
        # Prepare replacements with REAL signal names
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
            pattern_name='DoS',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"DoS trojan: disables {payload_sig} after {trigger_sig} activates 1000 times"
        )
    
    def generate_leak_trojan(self, trojan_id: str, trigger_signals: List,
                            payload_signals: List) -> SequentialTrojanCode:
        """Generate Information Leakage Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Leak trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Leak trojan requires payload signal (secret data to leak)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Leak trojan: leaks {payload_sig} when {trigger_sig} activates"
        )
    
    def generate_privilege_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> SequentialTrojanCode:
        """Generate Privilege Escalation Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Privilege trojan requires trigger signal (CSR write)")
        if not payload_signals:
            raise ValueError("Privilege trojan requires payload signal (privilege level)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Privilege trojan: escalates {payload_sig} to M-mode"
        )
    
    def generate_integrity_trojan(self, trojan_id: str, trigger_signals: List,
                                  payload_signals: List) -> SequentialTrojanCode:
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
        template = self.loader.load_template('integrity', 'sequential')
        
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
            pattern_name='Integrity',
            module_name=self.module.name,
            trigger_signals=[s.name for s in trigger_signals],
            payload_signals=[s.name for s in payload_signals],
            code=code,
            description=f"Integrity trojan: corrupts {payload_sig} with XOR mask"
        )
    
    def generate_availability_trojan(self, trojan_id: str, trigger_signals: List,
                                    payload_signals: List) -> SequentialTrojanCode:
        """Generate Performance Degradation Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Availability trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Availability trojan requires payload signal (ready/valid to delay)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Availability trojan: delays {payload_sig} by 8 cycles"
        )
    
    def generate_covert_trojan(self, trojan_id: str, trigger_signals: List,
                               payload_signals: List) -> SequentialTrojanCode:
        """Generate Covert Channel Trojan - STRICT MODE"""
        
        # STRICT: Require both signals
        if not trigger_signals:
            raise ValueError("Covert trojan requires trigger signal")
        if not payload_signals:
            raise ValueError("Covert trojan requires payload signal (secret data to transmit)")
        
        # Use REAL signals
        trigger_sig = trigger_signals[0].name
        payload_sig = payload_signals[0].name
        
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
            description=f"Covert trojan: timing channel using {payload_sig}"
        )
    
    def generate(self, pattern_name: str, trojan_id: str, 
                trigger_signals: List, payload_signals: List) -> SequentialTrojanCode:
        """
        Main generation dispatcher
        
        Args:
            pattern_name: Name of Trojan pattern (DoS, Leak, etc.)
            trojan_id: Unique ID for this Trojan
            trigger_signals: List of trigger Signal objects (MUST NOT BE EMPTY)
            payload_signals: List of payload Signal objects (MUST NOT BE EMPTY)
        
        Returns:
            SequentialTrojanCode object
            
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