#!/usr/bin/env python3
"""
Availability (Performance Degradation) Pattern
Based on: Boraten & Kodi (2016), Jin & Makris (2008)

Degrades performance through artificial delays
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class AvailabilityPattern:
    """
    Availability/Performance Degradation Trojan Pattern
    
    Trust-Hub Category: Performance Degradation ✓ (exists, but gate-level only)
    Trust-Hub Benchmarks: N/A (only gate-level implementations available)
    Literature Sources: Boraten & Kodi 2016, Jin & Makris 2008
    Severity: Medium
    
    Description:
        Degrades system performance by adding artificial delays,
        stalls, or wait cycles to critical operations. Trust-Hub
        has a Performance Degradation category, but benchmarks are
        gate-level (delay chains). We adapted the concept to RTL
        for RISC-V processor control flow.
    
    Trust-Hub Concept:
        Performance degradation through gate-level delay insertion
        and timing path manipulation.
    
    RTL Adaptation:
        Implemented at RTL level for RISC-V Load/Store Unit (LSU),
        targeting ready/valid control signals to introduce pipeline
        stalls and memory access delays.
    
    Trigger Mechanism:
        - Secret data bit patterns
        - Probabilistic activation
        - Time-based activation
        - Specific operation types (memory access)
    
    Payload:
        Adds artificial delay cycles to ready signals, introduces
        stalls, or slows down critical paths.
    
    Target Signals:
        - Trigger: data, valid, request, operation signals
        - Payload: ready, stall, busy, delay, wait signals
    
    Real-World Impact:
        - System slowdown (5-30%)
        - Reduced throughput
        - Increased latency
        - Performance anomalies
        - Missed real-time deadlines
    
    Example in RISC-V:
        - Target: ibex_load_store_unit
        - Signal: lsu_resp_valid_o
        - Effect: Slows memory operations randomly
    
    References:
        [1] T. Boraten and A. K. Kodi, "Mitigation of Denial of Service
            Attack with Hardware Trojans in NoC Architectures,"
            IEEE IPDPS, 2016
        [2] Y. Jin and Y. Makris, "Hardware Trojan Detection Using
            Path Delay Fingerprint," IEEE HOST, 2008
        [3] T. Hoque et al., "Hardware Trojan Attacks in Embedded Memory,"
            ACM JETC, vol. 16, no. 4, 2020
    """
    
    name: str = "Availability"
    category: str = "Performance Degradation"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Category exists (gate-level only)"
    trust_hub_category: str = "Performance Degradation"
    trust_hub_benchmarks: str = "N/A (gate-level only)"
    trust_hub_source: str = "N/A"
    
    # Literature citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Boraten & Kodi, IEEE IPDPS 2016",
        "Jin & Makris, IEEE HOST 2008",
        "Hoque et al., ACM JETC 2020"
    ])
    
    # Pattern metadata
    severity: str = "Medium"
    description: str = "Degrades performance through artificial delays"
    adaptation_note: str = "RTL adaptation of gate-level concept for RISC-V LSU"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'data', 'valid', 'req', 'request', 'op', 'operation',
        'cmd', 'start', 'trigger', 'lsu', 'load', 'store'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'ready', 'stall', 'busy', 'wait', 'delay',
        'valid', 'done', 'complete', 'ack', 'gnt', 'grant'
    ])
    
    # Module type preference
    preferred_module_type: str = "sequential"
    
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
            'trigger_type': 'data_bit',
            'payload_action': 'delay',
            'delay_cycles': '8',
            'comment_header': f"// Trust-Hub Category: {self.trust_hub_category} (RTL adaptation)\n// Sources: {', '.join(self.rtl_citations[:2])}"
        }


availability_pattern = AvailabilityPattern()


def get_pattern() -> AvailabilityPattern:
    """Get Availability pattern instance"""
    return availability_pattern