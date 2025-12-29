#!/usr/bin/env python3
"""
DoS (Denial of Service) Pattern
Based on Trust-Hub AES-T1400

Disables functionality by forcing control signals to 0
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class DoSPattern:
    """
    Denial of Service Trojan Pattern
    
    Trust-Hub Source: AES-T1400
    Category: Denial of Service
    Severity: High
    
    Description:
        Disables functionality by forcing critical control signals to 0
        after a specific trigger condition is met.
    
    Trigger Mechanism:
        - Counter-based: Activates after N operations
        - Condition-based: Specific input pattern
        - Time-based: After certain clock cycles
    
    Payload:
        Forces control signals (enable, valid, ready) to 0, effectively
        disabling the functionality of the module.
    
    Target Signals:
        - Trigger: enable, valid, start, request signals
        - Payload: enable, valid, ready, start signals (force to 0)
    
    Real-World Impact:
        - System becomes unresponsive
        - Critical operations fail
        - Service denial to legitimate users
    
    Example in RISC-V:
        - Target: ibex_decoder module
        - Signal: instr_valid_o
        - Effect: Prevents instruction execution
    """
    
    name: str = "DoS"
    category: str = "Denial of Service"
    trust_hub_source: str = "AES-T1400"
    severity: str = "High"
    description: str = "Disables functionality by forcing control signals to 0"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = None
    payload_keywords: List[str] = None
    
    # Module type preference
    preferred_module_type: str = "sequential"  # Can work with both
    
    def __post_init__(self):
        """Initialize keyword lists"""
        if self.trigger_keywords is None:
            self.trigger_keywords = [
                'enable', 'en', 'valid', 'ready', 'start', 'req', 'request',
                'active', 'go', 'trigger'
            ]
        
        if self.payload_keywords is None:
            self.payload_keywords = [
                'enable', 'en', 'valid', 'ready', 'start', 'req',
                'active', 'done', 'complete'
            ]
    
    def get_info(self) -> Dict:
        """Get pattern information as dictionary"""
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
            'trigger_type': 'counter',  # or 'condition'
            'payload_action': 'disable',
            'default_counter_value': '32\'hFFFF',
            'comment_header': f"// Trust-Hub {self.trust_hub_source}: {self.category}"
        }


# Create default instance
dos_pattern = DoSPattern()


def get_pattern() -> DoSPattern:
    """Get DoS pattern instance"""
    return dos_pattern