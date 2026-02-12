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
        'Rounding_Mode',
        'WRITE_NUM',
        'addr',
        'addr_i',
        'addr_incr_req_o',
        'addr_last_o',
        'addr_o',
        'address_i',
        'boot_addr_i',
        'commit_csr_o',
        'conf_addr_i',
        'conf_addr_mode_i',
        'conf_addr_prev_i',
        'counter_we_i',
        'counterh_we_i',
        'csr_access_i',
        'csr_access_o',
        'csr_addr)',
        'csr_addr_i',
        'csr_addr_o',
        'csr_commit_i',
        'csr_depc_i',
        'csr_depc_o',
        'csr_exception_i',
        'csr_exception_o',
        'csr_hs_ld_st_inst_i',
        'csr_hs_ld_st_inst_o',
        'csr_i',
        'csr_mcause_i',
        'csr_mepc_i',
        'csr_mepc_o',
        'csr_mstatus_mie_i',
        'csr_mstatus_mie_o',
        'csr_mstatus_tw_i',
        'csr_mstatus_tw_o',
        'csr_mtval_i',
        'csr_mtval_o',
        'csr_mtvec_i',
        'csr_mtvec_init_i',
        'csr_mtvec_init_o',
        'csr_mtvec_o',
        'csr_op_en_i',
        'csr_op_en_o',
        'csr_op_i',
        'csr_op_o',
        'csr_pipe_flush_i',
        'csr_pmp_addr_i',
        'csr_pmp_addr_o',
        'csr_pmp_cfg_i',
        'csr_pmp_cfg_o',
        'csr_pmp_mseccfg_i',
        'csr_pmp_mseccfg_o',
        'csr_rdata_i',
        'csr_rdata_o',
        'csr_ready_o',
        'csr_restore_dret_i',
        'csr_restore_dret_id_o',
        'csr_restore_mret_i',
        'csr_restore_mret_id_o',
        'csr_result_o',
        'csr_save_cause_i',
        'csr_save_cause_o',
        'csr_save_id_i',
        'csr_save_id_o',
        'csr_save_if_i',
        'csr_save_if_o',
        'csr_save_wb_i',
        'csr_save_wb_o',
        'csr_shadow_err_o',
        'csr_valid_i',
        'csr_valid_o',
        'csr_wdata_i',
        'csr_wdata_o',
        'csr_write_fflags_i',
        'csr_write_fflags_o',
        'data_addr_i',
        'data_addr_o',
        'data_we_i',
        'data_we_o',
        'dcache_mem_req_write_data_o',
        'dcache_mem_req_write_data_ready_i',
        'dcache_mem_req_write_data_valid_o',
        'dcache_mem_req_write_o',
        'dcache_mem_req_write_ready_i',
        'dcache_mem_req_write_valid_o',
        'dcache_mem_resp_write_i',
        'dcache_mem_resp_write_ready_o',
        'dcache_mem_resp_write_valid_i',
        'dcache_write_data_i',
        'dcache_write_data_ready_o',
        'dcache_write_data_valid_i',
        'dcache_write_i',
        'dcache_write_ready_o',
        'dcache_write_resp_o',
        'dcache_write_resp_ready_i',
        'dcache_write_resp_valid_o',
        'dcache_write_valid_i',
        'debug_csr_save_i',
        'debug_csr_save_o',
        'debug_mode_entering_i',
        'debug_mode_entering_o',
        'debug_mode_i',
        'debug_mode_o',
        'exception_addr_i',
        'flush_csr_i',
        'halt_csr_i',
        'halt_csr_o',
        'ic_data_addr_i',
        'ic_data_addr_o',
        'ic_data_write_i',
        'ic_data_write_o',
        'ic_tag_addr_i',
        'ic_tag_addr_o',
        'ic_tag_write_i',
        'ic_tag_write_o',
        'illegal_csr_insn_i',
        'illegal_csr_insn_o',
        'imd_val_we_ex_i',
        'imd_val_we_o',
        'in_addr_i',
        'instr_addr_i',
        'instr_addr_o',
        'inval_addr_i',
        'inval_addr_o',
        'jump_address_i',
        'jump_address_o',
        'lsu_addr_incr_req_i',
        'lsu_addr_last_i',
        'lsu_we_i',
        'lsu_we_o',
        'memory_addr',
        'memory_we',
        'miss_we_i',
        'miss_we_o',
        'mode',
        'mshr_addr_i',
        'mshr_addr_matches_i',
        'mshr_addr_matches_o',
        'mshr_addr_o',
        'multdiv_signed_mode_ex_o',
        'multdiv_signed_mode_i',
        'multdiv_signed_mode_o',
        'nmi_mode_i',
        'nmi_mode_o',
        'nt_branch_addr_i',
        'nt_branch_addr_o',
        'out_addr_o',
        'perf_addr_o',
        'perf_we_o',
        'pmp_req_addr_i',
        'predict_address_i',
        'priv_mode_i',
        'priv_mode_id_o',
        'priv_mode_lsu_o',
        'rd_addr_i',
        'replay_addr_o',
        'rf_we_id_i',
        'rf_we_id_o',
        'rf_we_lsu_i',
        'rf_we_o',
        'rf_we_wb_i',
        'rf_we_wb_o',
        'rf_write_wb_i',
        'rf_write_wb_o',
        'riscv::pmp_addr_mode_t',
        'rvfi_csr_o',
        'rvfi_csr_t',
        'rvfi_mem_addr',
        'rvfi_mode',
        'rvfi_probes_csr_t',
        'rvfi_rd_addr',
        'rvfi_rs1_addr',
        'rvfi_rs2_addr',
        'rvfi_rs3_addr',
        'signed_mode_i',
        'tdata1_we',
        'tdata2_we',
        'tdata3_we',
        'tselect_we',
        'we',
        'we_a_i',
        'we_fpr_i',
        'we_fpr_o',
        'we_gpr_i',
        'we_gpr_o',
        'we_i',
        'we_o',
        'wr_addr_i',
        'wr_cl_we_i',
        'wr_cl_we_o',
        'write',
        'writeIndex',
        'x_we_i',
        'x_we_o'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        'Rounding_Mode',
        'conf_addr_mode_i',
        'csr_mepc_i',
        'csr_mepc_o',
        'csr_mstatus_mie_i',
        'csr_mstatus_mie_o',
        'csr_mstatus_tw_i',
        'csr_mstatus_tw_o',
        'csr_mtvec_i',
        'csr_mtvec_init_i',
        'csr_mtvec_init_o',
        'csr_mtvec_o',
        'debug_mode_entering_i',
        'debug_mode_entering_o',
        'debug_mode_i',
        'debug_mode_o',
        'hwpf_status_o',
        'ibex_pkg::priv_lvl_e',
        'ld_st_priv_lvl_i',
        'ld_st_priv_lvl_o',
        'mode',
        'multdiv_signed_mode_ex_o',
        'multdiv_signed_mode_i',
        'multdiv_signed_mode_o',
        'nmi_mode_i',
        'nmi_mode_o',
        'priv_lvl_i',
        'priv_lvl_o',
        'priv_lvl_t',
        'priv_mode_i',
        'priv_mode_id_o',
        'priv_mode_lsu_o',
        'riscv::pmp_addr_mode_t',
        'riscv::priv_lvl_t',
        'rvfi_mode',
        'signed_mode_i'
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
