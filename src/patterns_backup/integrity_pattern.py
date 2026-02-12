#!/usr/bin/env python3
"""
Data Integrity Pattern
Based on Trust-Hub Benchmarks: AES-T2300, AES-T2400, AES-T2500, AES-T2600

Corrupts data through XOR or bit flipping
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class IntegrityPattern:
    """
    Data Integrity Violation Trojan Pattern
    
    Trust-Hub Category: Change Functionality ✓ (Verified)
    Trust-Hub Benchmarks: AES-T2300, AES-T2400, AES-T2500, AES-T2600, AES-T2700, AES-T2800
    Severity: High
    
    Description:
        Corrupts data by XORing with patterns or flipping bits when
        triggered. Based on verified Trust-Hub RTL benchmarks that
        corrupt AES encryption output.
    
    Trust-Hub Mechanism:
        Trust-Hub integrity trojans flip bits in AES ciphertext when
        rare signal combinations occur (e.g., s2[89] and s5[121] both high).
    
    RISC-V Adaptation:
        Adapted to corrupt processor data paths (CSR reads, LSU data)
        using XOR masks or bit flipping, triggered by rare conditions.
    
    Trigger Mechanism:
        - Rare signal combinations
        - Specific data patterns
        - Counter threshold
        - Address-based trigger
    
    Payload:
        Corrupts output data by:
        - XOR with corruption pattern (0xDEADBEEF)
        - Bit flipping (LSB or specific bits)
        - Data value manipulation
    
    Target Signals:
        - Trigger: data, input, addr, address, op signals
        - Payload: data, result, output, rdata, wdata signals
    
    Real-World Impact:
        - Incorrect computation results
        - Data corruption in memory
        - Control flow hijacking
        - Security bypass through corrupted checks
    
    Example in RISC-V:
        - Target: ibex_cs_registers
        - Signal: csr_rdata_o
        - Effect: Corrupts CSR read data randomly
    
    References:
        [1] Trust-Hub, "AES-T2300: Change Functionality Trojan"
        [2] Trust-Hub, "AES-T2400: Change Functionality Trojan"
        [3] Trust-Hub, "AES-T2500-T2800: Data Integrity Trojans"
    """
    
    name: str = "Integrity"
    category: str = "Data Integrity"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Verified RTL Benchmarks"
    trust_hub_category: str = "Change Functionality"
    trust_hub_benchmarks: str = "AES-T2300, AES-T2400, AES-T2500, AES-T2600, AES-T2700, AES-T2800"
    trust_hub_source: str = "AES-T2300"  # Primary benchmark
    
    # Citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Trust-Hub AES-T2300",
        "Trust-Hub AES-T2400",
        "Trust-Hub AES-T2500",
        "Trust-Hub AES-T2600"
    ])
    
    # Pattern metadata
    severity: str = "High"
    description: str = "Corrupts computation results or data"
    adaptation_note: str = "Adapted from AES state corruption to RISC-V data path"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'data', 'input', 'addr', 'address', 'op', 'operation',
        'cmd', 'command', 'sel', 'select'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'data', 'result', 'output', 'out', 'rdata', 'wdata',
        'calc', 'value', 'write', 'store', 'computation'
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
            'trigger_type': 'pattern',
            'payload_action': 'corrupt',
            'corruption_pattern': '32\'hDEADBEEF',
            'corruption_method': 'xor',
            'comment_header': f"// Trust-Hub {self.trust_hub_benchmarks}: {self.category}"
        }


integrity_pattern = IntegrityPattern()


def get_pattern() -> IntegrityPattern:
    """Get Integrity pattern instance"""
    return integrity_pattern