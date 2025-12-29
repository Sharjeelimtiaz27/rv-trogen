#!/usr/bin/env python3
"""
Integrity Violation Pattern
Based on Trust-Hub AES-T800

Corrupts computation results or data
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class IntegrityPattern:
    """
    Integrity Violation Trojan Pattern
    
    Trust-Hub Source: AES-T800
    Category: Integrity Violation
    Severity: High
    
    Description:
        Corrupts computation results, data, or memory contents by XORing
        with corruption patterns or flipping specific bits.
    
    Trigger Mechanism:
        - Specific input patterns
        - Address-based trigger
        - Data value trigger
        - Operation type
    
    Payload:
        Corrupts output data by XORing with corruption pattern,
        bit flipping, or other data manipulation.
    
    Target Signals:
        - Trigger: data, input, addr, address, operation signals
        - Payload: data, result, output, computation signals
    
    Real-World Impact:
        - Incorrect computation results
        - Data corruption
        - Memory corruption
        - Control flow hijacking
    
    Example in RISC-V:
        - Target: ibex_alu module
        - Signal: result_o
        - Effect: Corrupts ALU output for specific operations
    """
    
    name: str = "Integrity"
    category: str = "Integrity Violation"
    trust_hub_source: str = "AES-T800"
    severity: str = "High"
    description: str = "Corrupts computation results or data"
    
    trigger_keywords: List[str] = None
    payload_keywords: List[str] = None
    preferred_module_type: str = "both"
    
    def __post_init__(self):
        """Initialize keyword lists"""
        if self.trigger_keywords is None:
            self.trigger_keywords = [
                'data', 'input', 'addr', 'address', 'op', 'operation',
                'cmd', 'command', 'sel', 'select'
            ]
        
        if self.payload_keywords is None:
            self.payload_keywords = [
                'data', 'result', 'output', 'out', 'computation',
                'calc', 'value', 'write', 'store'
            ]
    
    def get_info(self) -> Dict:
        """Get pattern information"""
        return {
            'name': self.name,
            'category': self.category,
            'trust_hub_source': self.trust_hub_source,
            'severity': self.severity,
            'description': self.description,
            'trigger_keywords': self.trigger_keywords,
            'payload_keywords': self.payload_keywords,
            'preferred_module_type': self.preferred_module_type
        }
    
    def get_template_params(self) -> Dict:
        """Get parameters for template generation"""
        return {
            'pattern_name': self.name,
            'description': self.description,
            'trigger_type': 'pattern',
            'payload_action': 'corrupt',
            'corruption_pattern': '32\'hDEADBEEF',
            'corruption_method': 'xor',
            'comment_header': f"// Trust-Hub {self.trust_hub_source}: {self.category}"
        }


integrity_pattern = IntegrityPattern()


def get_pattern() -> IntegrityPattern:
    """Get Integrity pattern instance"""
    return integrity_pattern