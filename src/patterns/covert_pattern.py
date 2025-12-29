#!/usr/bin/env python3
"""
Covert Channel Pattern
Custom pattern

Creates hidden communication channels through timing
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class CovertPattern:
    """
    Covert Channel Trojan Pattern
    
    Trust-Hub Source: Custom
    Category: Covert Channel
    Severity: Medium
    
    Description:
        Creates hidden communication channel through timing variations,
        power consumption, or other side channels.
    
    Trigger Mechanism:
        - Secret data to transmit
        - External synchronization signal
        - Specific operational phase
    
    Payload:
        Encodes secret data in timing delays, power signatures,
        or other observable side channels.
    
    Target Signals:
        - Trigger: data, input, secret signals
        - Payload: debug, test, unused, timing-sensitive signals
    
    Real-World Impact:
        - Secret data exfiltration
        - Covert communication
        - Side-channel attacks
        - Information leakage (subtle)
    
    Example in RISC-V:
        - Target: Any module with observable timing
        - Signal: Response delays
        - Effect: Leaks data through timing channel
    """
    
    name: str = "Covert"
    category: str = "Covert Channel"
    trust_hub_source: str = "Custom"
    severity: str = "Medium"
    description: str = "Creates hidden communication channel through timing"
    
    trigger_keywords: List[str] = None
    payload_keywords: List[str] = None
    preferred_module_type: str = "both"
    
    def __post_init__(self):
        """Initialize keyword lists"""
        if self.trigger_keywords is None:
            self.trigger_keywords = [
                'data', 'input', 'secret', 'key', 'priv',
                'load', 'fetch', 'access'
            ]
        
        if self.payload_keywords is None:
            self.payload_keywords = [
                'debug', 'test', 'unused', 'spare', 'reserved',
                'delay', 'timing', 'wait', 'busy'
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
            'trigger_type': 'data_encoding',
            'payload_action': 'timing_channel',
            'encoding': 'bit_to_delay',
            'comment_header': f"// Trust-Hub {self.trust_hub_source}: {self.category}"
        }


covert_pattern = CovertPattern()


def get_pattern() -> CovertPattern:
    """Get Covert pattern instance"""
    return covert_pattern