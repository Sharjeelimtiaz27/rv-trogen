#!/usr/bin/env python3
"""
Information Leakage Pattern
Based on Trust-Hub RSA-T600

Leaks sensitive data to attacker-accessible locations
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class LeakPattern:
    """
    Information Leakage Trojan Pattern
    
    Trust-Hub Source: RSA-T600
    Category: Information Leakage
    Severity: Critical
    
    Description:
        Leaks sensitive data (keys, secrets, addresses) to attacker-accessible
        locations such as unused ports, debug interfaces, or observable channels.
    
    Trigger Mechanism:
        - Debug mode activation
        - External pin signal
        - Specific operational mode
        - Test mode enabled
    
    Payload:
        Routes secret data to unused output ports, debug interfaces, or
        creates observable side channels.
    
    Target Signals:
        - Trigger: debug, test, mode, external control signals
        - Payload: key, secret, data, addr, address, priv signals
    
    Real-World Impact:
        - Cryptographic key exposure
        - Privileged information leak
        - Address space disclosure
        - Security bypass
    
    Example in RISC-V:
        - Target: ibex_cs_registers module
        - Signal: csr_rdata_o
        - Effect: Leaks CSR contents to unused debug port
    """
    
    name: str = "Leak"
    category: str = "Information Leakage"
    trust_hub_source: str = "RSA-T600"
    severity: str = "Critical"
    description: str = "Leaks sensitive data to attacker-accessible location"
    
    trigger_keywords: List[str] = None
    payload_keywords: List[str] = None
    preferred_module_type: str = "both"
    
    def __post_init__(self):
        """Initialize keyword lists"""
        if self.trigger_keywords is None:
            self.trigger_keywords = [
                'debug', 'test', 'mode', 'scan', 'jtag', 'tap',
                'external', 'ext', 'ctrl', 'control'
            ]
        
        if self.payload_keywords is None:
            self.payload_keywords = [
                'key', 'secret', 'priv', 'privilege', 'data', 'addr',
                'address', 'csr', 'reg', 'secure', 'confidential'
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
            'trigger_type': 'signal',
            'payload_action': 'leak',
            'leak_destination': 'debug_port',
            'comment_header': f"// Trust-Hub {self.trust_hub_source}: {self.category}"
        }


leak_pattern = LeakPattern()


def get_pattern() -> LeakPattern:
    """Get Leak pattern instance"""
    return leak_pattern