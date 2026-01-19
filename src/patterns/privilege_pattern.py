#!/usr/bin/env python3
"""
Privilege Escalation Pattern
RISC-V specific pattern based on: Bailey (2017), Dessouky et al. (2017), Clercq & Verbauwhede (2017)

Escalates privilege level to machine mode
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class PrivilegePattern:
    """
    Privilege Escalation Trojan Pattern
    
    Trust-Hub Status: Not applicable (processor-specific attack)
    Literature Sources: Bailey 2017, Dessouky et al. 2017, Clercq & Verbauwhede 2017
    Severity: Critical
    
    Description:
        Escalates privilege level from user/supervisor mode to machine mode,
        bypassing RISC-V privilege separation mechanisms. This attack is
        processor-specific and not present in Trust-Hub (which focuses on
        cryptographic circuits without privilege levels).
    
    Trust-Hub Note:
        Trust-Hub does not include privilege escalation attacks because
        its benchmarks focus on cryptographic circuits (AES, RSA) which
        do not have privilege modes. This is a RISC-V processor-specific
        attack pattern.
    
    RISC-V Adaptation:
        Novel automated implementation for RISC-V processors. Previous
        work (Bailey 2017) demonstrated manual exploitation; we provide
        the first automated generation framework.
    
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
        - Payload: priv, privilege, mode, level, lvl, mstatus, mepc, mtvec
    
    Real-World Impact:
        - Complete security bypass
        - Unauthorized system access
        - Malware can gain kernel privileges
        - TEE/enclave compromise
        - Memory protection (PMP) bypass
    
    Example in RISC-V:
        - Target: ibex_cs_registers module
        - Signal: priv_lvl_q
        - Effect: User mode code gains machine privileges
    
    References:
        [1] D. A. Bailey, "The RISC-V Files: Supervisor → Machine
            Privilege Escalation Exploit," Security Mouse Blog, 2017
        [2] G. Dessouky et al., "LO-PHI: Low-Observable Physical Host
            Instrumentation for Malware Analysis," NDSS, 2017
        [3] R. De Clercq and I. Verbauwhede, "A Survey on Hardware-based
            Control Flow Integrity (CFI)," ACM Computing Surveys, 2017
        [4] S. Nashimoto et al., "Bypassing Isolated Execution on RISC-V
            with Fault Injection," IACR ePrint 2020/1193, 2020
    """
    
    name: str = "Privilege"
    category: str = "Privilege Escalation"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Not applicable (processor-specific)"
    trust_hub_category: str = "N/A"
    trust_hub_benchmarks: str = "N/A"
    trust_hub_source: str = "N/A"
    
    # Literature citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Bailey, Security Mouse Blog 2017",
        "Dessouky et al., NDSS 2017",
        "De Clercq & Verbauwhede, ACM Computing Surveys 2017",
        "Nashimoto et al., IACR ePrint 2020/1193"
    ])
    
    # Pattern metadata
    severity: str = "Critical"
    description: str = "Escalates privilege level to machine mode"
    adaptation_note: str = "Novel automated generation for RISC-V (first of its kind)"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'csr', 'write', 'we', 'wen', 'mode', 'ctrl', 'control',
        'cmd', 'command', 'addr', 'address', 'mstatus', 'priv'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'priv', 'privilege', 'mode', 'level', 'lvl',
        'state', 'status', 'mstatus', 'permission', 'mepc', 'mtvec'
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
            'trigger_type': 'csr_write',
            'payload_action': 'escalate',
            'target_privilege': 'PRIV_LVL_M',
            'magic_value': '8\'hBA',
            'comment_header': f"// RISC-V Specific Pattern (not in Trust-Hub)\n// Sources: {', '.join(self.rtl_citations[:2])}"
        }


privilege_pattern = PrivilegePattern()


def get_pattern() -> PrivilegePattern:
    """Get Privilege pattern instance"""
    return privilege_pattern