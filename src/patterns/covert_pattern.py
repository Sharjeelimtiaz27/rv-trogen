#!/usr/bin/env python3
"""
Covert Channel Pattern
Based on timing side-channel literature: Kocher (1996), Lipp et al. (2021), Lin et al. (2009)

Creates hidden communication channels through timing
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class CovertPattern:
    """
    Covert Channel Trojan Pattern
    
    Trust-Hub Status: Related to "Leak Information" (power channels only)
    Literature Sources: Kocher 1996, Lipp et al. 2021, Lin et al. 2009
    Severity: High
    
    Description:
        Creates hidden communication channel through timing variations,
        power consumption, or other side channels. Trust-Hub focuses on
        power/current side channels; timing channels require processor-
        specific implementation.
    
    Trust-Hub Note:
        Trust-Hub's "Leak Information" category covers power and current
        side channels. Timing-based covert channels are not explicitly
        present in the taxonomy. Our implementation extends the side-channel
        concept to timing domains for RISC-V processors.
    
    Timing Side-Channel Background:
        Timing attacks are foundational (Kocher 1996) and have been
        demonstrated in modern processors (Meltdown, Spectre). We adapt
        these concepts for automated trojan generation.
    
    Trigger Mechanism:
        - Secret data to transmit
        - External synchronization signal
        - Specific operational phase
        - Data bit encoding
    
    Payload:
        Encodes secret data in timing delays, power signatures,
        or other observable side channels. Modulates execution
        time based on secret bits.
    
    Target Signals:
        - Trigger: data, input, secret signals
        - Payload: debug, test, unused, timing-sensitive signals
    
    Real-World Impact:
        - Secret data exfiltration
        - Covert communication (1-10 bits/sec)
        - Side-channel attacks
        - Information leakage (subtle and stealthy)
        - Difficult to detect without statistical analysis
    
    Example in RISC-V:
        - Target: Any module with observable timing
        - Signal: Response delays
        - Effect: Leaks data through timing channel
        - Encoding: Long delay = '1', short delay = '0'
    
    References:
        [1] P. C. Kocher, "Timing Attacks on Implementations of
            Diffie-Hellman, RSA, DSS, and Other Systems," CRYPTO, 1996
            (foundational work)
        [2] M. Lipp et al., "Tapeout of a RISC-V Crypto Chip with
            Hardware Trojans," ACM CF, 2021
        [3] L. Lin et al., "Trojan Side-Channels: Lightweight Hardware
            Trojans through Side-Channel Engineering," CHES, 2009
        [4] F. Liu et al., "Last-Level Cache Side-Channel Attacks are
            Practical," IEEE S&P, 2015
        [5] O. Weisse et al., "Prevention of Microarchitectural Covert
            Channels on an Open-Source 64-bit RISC-V Core," IEEE CSF, 2021
    """
    
    name: str = "Covert"
    category: str = "Covert Channel"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Related to Leak Information (power only, not timing)"
    trust_hub_category: str = "Leak Information (power/current)"
    trust_hub_benchmarks: str = "N/A (timing channels not explicit)"
    trust_hub_source: str = "N/A"
    
    # Literature citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Kocher, CRYPTO 1996 (foundational)",
        "Lipp et al., ACM CF 2021",
        "Lin et al., CHES 2009",
        "Liu et al., IEEE S&P 2015",
        "Weisse et al., IEEE CSF 2021"
    ])
    
    # Pattern metadata
    severity: str = "High"
    description: str = "Creates hidden communication channel through timing"
    adaptation_note: str = "Extends Trust-Hub power channels to timing domain for RISC-V"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'data', 'input', 'secret', 'key', 'priv',
        'load', 'fetch', 'access', 'cache', 'memory'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'debug', 'test', 'unused', 'spare', 'reserved',
        'delay', 'timing', 'wait', 'busy', 'ready', 'valid'
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
            'trigger_type': 'data_encoding',
            'payload_action': 'timing_channel',
            'encoding': 'bit_to_delay',
            'comment_header': f"// Timing Side-Channel (extends Trust-Hub Leak Information)\n// Sources: {', '.join(self.rtl_citations[:3])}"
        }


covert_pattern = CovertPattern()


def get_pattern() -> CovertPattern:
    """Get Covert pattern instance"""
    return covert_pattern