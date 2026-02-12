#!/usr/bin/env python3
"""
Information Leakage Pattern
Based on Trust-Hub Benchmarks: AES-T600, AES-T1400, AES-T800

Leaks sensitive data to attacker-accessible locations
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class LeakPattern:
    """
    Information Leakage Trojan Pattern
    
    Trust-Hub Category: Leak Information ✓ (Verified)
    Trust-Hub Benchmarks: AES-T600, AES-T1400, AES-T800
    Severity: Critical
    
    Description:
        Leaks sensitive data (keys, secrets, addresses) to attacker-accessible
        locations such as unused ports, debug interfaces, or observable channels.
        Based on verified Trust-Hub RTL benchmarks.
    
    Trust-Hub Mechanism:
        Trust-Hub leak trojans use side-channel methods (power, current)
        to exfiltrate cryptographic keys from AES circuits.
    
    RISC-V Adaptation:
        Adapted to route processor secrets (CSR contents, privilege data)
        to debug outputs or unused ports for direct leakage.
    
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
    
    References:
        [1] Trust-Hub, "AES-T600: Information Leakage Trojan"
        [2] Trust-Hub, "AES-T1400: Information Leakage Trojan"
        [3] Trust-Hub, "AES-T800: Information Leakage Trojan"
    """
    
    name: str = "Leak"
    category: str = "Information Leakage"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Verified RTL Benchmarks"
    trust_hub_category: str = "Leak Information"
    trust_hub_benchmarks: str = "AES-T600, AES-T1400, AES-T800"
    trust_hub_source: str = "AES-T600"  # Primary benchmark
    
    # Citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Trust-Hub AES-T600",
        "Trust-Hub AES-T1400",
        "Trust-Hub AES-T800"
    ])
    
    # Pattern metadata
    severity: str = "Critical"
    description: str = "Leaks sensitive data to attacker-accessible location"
    adaptation_note: str = "Adapted from power side-channels to direct CSR leakage"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'debug', 'test', 'mode', 'scan', 'jtag', 'tap',
        'external', 'ext', 'ctrl', 'control'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'key', 'secret', 'priv', 'privilege', 'data', 'addr',
        'address', 'csr', 'reg', 'secure', 'confidential'
    ])
    
    # Module type preference
    preferred_module_type: str = "both"
    
    def get_info(self) -> Dict:
        """Get pattern information"""
        return {
            'name': self.name,
            'category': self.category,
            'trust_hub_status': self.trust_hub_status,
            'trust_hub_category': self.trust_hub_category,
            'trust_hub_benchmarks': self.trust_hub_benchmarks,
            'trust_hub_source': self.trust_hub_source,
            'rtl_citations': self.rtl_citations,
            'severity': self.severity,
            'description': self.description,
            'adaptation_note': self.adaptation_note,
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
            'comment_header': f"// Trust-Hub {self.trust_hub_benchmarks}: {self.category}"
        }


leak_pattern = LeakPattern()


def get_pattern() -> LeakPattern:
    """Get Leak pattern instance"""
    return leak_pattern