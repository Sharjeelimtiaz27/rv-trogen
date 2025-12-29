#!/usr/bin/env python3
"""
Privilege Escalation Pattern
Custom RISC-V specific pattern

Escalates privilege level to machine mode
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class PrivilegePattern:
    """
    Privilege Escalation Trojan Pattern
    
    Trust-Hub Source: Custom RISC-V
    Category: Privilege Escalation
    Severity: Critical
    
    Description:
        Escalates privilege level from user/supervisor mode to machine mode,
        bypassing RISC-V privilege separation mechanisms.
    
    Trigger Mechanism:
        - Specific CSR write pattern
        - Magic value in instruction
        - Specific memory access pattern
        - Special opcode sequence
    
    Payload:
        Forces privilege level (priv_lvl_q) to machine mode (PRIV_LVL_M),
        granting full system access to unprivileged code.
    
    Target Signals:
        - Trigger: csr_addr, csr_we, csr_wdata, mode signals
        - Payload: priv, privilege, mode, level, lvl signals
    
    Real-World Impact:
        - Complete security bypass
        - Unauthorized system access
        - Malware can gain kernel privileges
        - TEE/enclave compromise
    
    Example in RISC-V:
        - Target: ibex_cs_registers module
        - Signal: priv_lvl_q
        - Effect: User mode code gains machine privileges
    """
    
    name: str = "Privilege"
    category: str = "Privilege Escalation"
    trust_hub_source: str = "Custom RISC-V"
    severity: str = "Critical"
    description: str = "Escalates privilege level to machine mode"
    
    trigger_keywords: List[str] = None
    payload_keywords: List[str] = None
    preferred_module_type: str = "sequential"
    
    def __post_init__(self):
        """Initialize keyword lists"""
        if self.trigger_keywords is None:
            self.trigger_keywords = [
                'csr', 'write', 'we', 'wen', 'mode', 'ctrl', 'control',
                'cmd', 'command', 'addr', 'address'
            ]
        
        if self.payload_keywords is None:
            self.payload_keywords = [
                'priv', 'privilege', 'mode', 'level', 'lvl',
                'state', 'status', 'mstatus', 'permission'
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
            'trigger_type': 'csr_write',
            'payload_action': 'escalate',
            'target_privilege': 'PRIV_LVL_M',
            'magic_value': '8\'hBA',
            'comment_header': f"// Trust-Hub {self.trust_hub_source}: {self.category}"
        }


privilege_pattern = PrivilegePattern()


def get_pattern() -> PrivilegePattern:
    """Get Privilege pattern instance"""
    return privilege_pattern