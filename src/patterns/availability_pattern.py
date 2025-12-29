#!/usr/bin/env python3
"""
Availability (Performance Degradation) Pattern
Custom pattern

Degrades performance through artificial delays
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class AvailabilityPattern:
    """
    Availability/Performance Degradation Trojan Pattern
    
    Trust-Hub Source: Custom
    Category: Availability
    Severity: Medium
    
    Description:
        Degrades system performance by adding artificial delays,
        stalls, or wait cycles to critical operations.
    
    Trigger Mechanism:
        - Secret data bit patterns
        - Probabilistic activation
        - Time-based activation
        - Specific operation types
    
    Payload:
        Adds artificial delay cycles to ready signals, introduces
        stalls, or slows down critical paths.
    
    Target Signals:
        - Trigger: data, valid, request, operation signals
        - Payload: ready, stall, busy, delay, wait signals
    
    Real-World Impact:
        - System slowdown
        - Reduced throughput
        - Increased latency
        - Performance anomalies
    
    Example in RISC-V:
        - Target: ibex_load_store_unit
        - Signal: lsu_resp_valid_o
        - Effect: Slows memory operations randomly
    """
    
    name: str = "Availability"
    category: str = "Performance Degradation"
    trust_hub_source: str = "Custom"
    severity: str = "Medium"
    description: str = "Degrades performance through artificial delays"
    
    trigger_keywords: List[str] = None
    payload_keywords: List[str] = None
    preferred_module_type: str = "sequential"
    
    def __post_init__(self):
        """Initialize keyword lists"""
        if self.trigger_keywords is None:
            self.trigger_keywords = [
                'data', 'valid', 'req', 'request', 'op', 'operation',
                'cmd', 'start', 'trigger'
            ]
        
        if self.payload_keywords is None:
            self.payload_keywords = [
                'ready', 'stall', 'busy', 'wait', 'delay',
                'valid', 'done', 'complete', 'ack'
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
            'trigger_type': 'data_bit',
            'payload_action': 'delay',
            'delay_cycles': '8',
            'comment_header': f"// Trust-Hub {self.trust_hub_source}: {self.category}"
        }


availability_pattern = AvailabilityPattern()


def get_pattern() -> AvailabilityPattern:
    """Get Availability pattern instance"""
    return availability_pattern