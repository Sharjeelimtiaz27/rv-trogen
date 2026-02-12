#!/usr/bin/env python3
"""
DoS (Denial of Service) Pattern
Based on Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200

Disables functionality by forcing control signals to 0
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class DoSPattern:
    """
    Denial of Service Trojan Pattern
    
    Trust-Hub Category: Denial of Service ✓ (Verified)
    Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
    Severity: High
    
    Description:
        Disables functionality by forcing critical control signals to 0
        after a specific trigger condition is met. Based on verified
        Trust-Hub RTL benchmarks.
    
    Trust-Hub Mechanism:
        Trust-Hub DoS trojans target cryptographic circuits, causing
        battery drain and resource exhaustion.
    
    RISC-V Adaptation:
        Adapted for processor control signals (enable, valid, ready).
        Targets functional disruption rather than battery drain.
    
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
    
    References:
        [1] Trust-Hub, "AES-T1800: Denial of Service Trojan"
        [2] Trust-Hub, "AES-T1900: Denial of Service Trojan"
        [3] Trust-Hub, "AES-T500: Denial of Service Trojan"
        [4] Trust-Hub, "BasicRSA-T200: Denial of Service Trojan"
    """
    
    name: str = "DoS"
    category: str = "Denial of Service"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Verified RTL Benchmarks"
    trust_hub_category: str = "Denial of Service"
    trust_hub_benchmarks: str = "AES-T1800, AES-T1900, AES-T500, BasicRSA-T200"
    trust_hub_source: str = "AES-T1800"  # Primary benchmark
    
    # Citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Trust-Hub AES-T1800",
        "Trust-Hub AES-T1900",
        "Trust-Hub AES-T500",
        "Trust-Hub BasicRSA-T200"
    ])
    
    # Pattern metadata
    severity: str = "High"
    description: str = "Disables functionality by forcing control signals to 0"
    adaptation_note: str = "Adapted from crypto circuits to RISC-V control signals"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'enable', 'en', 'valid', 'ready', 'start', 'req', 'request',
        'active', 'go', 'trigger'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'enable', 'en', 'valid', 'ready', 'start', 'req',
        'active', 'done', 'complete'
    ])
    
    # Module type preference
    preferred_module_type: str = "sequential"  # Can work with both
    
    def get_info(self) -> Dict:
        """Get pattern information as dictionary"""
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
            'trigger_type': 'counter',  # or 'condition'
            'payload_action': 'disable',
            'default_counter_value': '32\'hFFFF',
            'comment_header': f"// Trust-Hub {self.trust_hub_benchmarks}: {self.category}"
        }


# Create default instance
dos_pattern = DoSPattern()


def get_pattern() -> DoSPattern:
    """Get DoS pattern instance"""
    return dos_pattern