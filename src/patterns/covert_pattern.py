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
        'FETCH_WIDTH',
        'FETCH_WIDTH-1:0',
        'LOAD_ISSUE_WIDTH',
        '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0',
        'access',
        'access_type_i',
        'alu_operand_a_ex_o',
        'alu_operand_a_i',
        'alu_operand_a_o',
        'alu_operand_b_ex_o',
        'alu_operand_b_i',
        'alu_operand_b_o',
        'amo_operand_a_i',
        'amo_operand_b_i',
        'axi_data_i',
        'axi_data_o',
        'bt_a_operand_i',
        'bt_a_operand_o',
        'bt_b_operand_i',
        'bt_b_operand_o',
        'bypass_data_i',
        'bypass_data_o',
        'csr_access_i',
        'csr_access_o',
        'data',
        'dataIn',
        'dataOut',
        'data_addr_i',
        'data_addr_o',
        'data_be_i',
        'data_be_o',
        'data_bus_err_i',
        'data_err_i',
        'data_gnt_i',
        'data_i',
        'data_ind_timing_i',
        'data_ind_timing_o',
        'data_o',
        'data_pmp_err_i',
        'data_rdata_i',
        'data_rdata_intg_i',
        'data_req_i',
        'data_req_o',
        'data_rvalid_i',
        'data_sign_extension_o',
        'data_size_i',
        'data_type_o',
        'data_wdata_i',
        'data_wdata_intg_o',
        'data_wdata_o',
        'data_we_i',
        'data_we_o',
        'dcache_data_ack_o',
        'dcache_data_i',
        'dcache_data_req_i',
        'dcache_mem_req_write_data_o',
        'dcache_mem_req_write_data_ready_i',
        'dcache_mem_req_write_data_valid_o',
        'dcache_write_data_i',
        'dcache_write_data_ready_o',
        'dcache_write_data_valid_i',
        'dummy_instr_data_o',
        'expecting_load_resp_o',
        'fetch_enable_i',
        'fetch_entry_i',
        'fetch_entry_o',
        'fetch_entry_ready_i',
        'fetch_entry_ready_o',
        'fetch_entry_t',
        'fetch_entry_valid_i',
        'fetch_entry_valid_o',
        'fetch_pc_i',
        'fetch_rdata_i',
        'fetch_stall_o',
        'fetch_valid_i',
        'fu_data_cpop_i',
        'fu_data_i',
        'fu_data_o',
        'fu_data_t',
        'ic_data_addr_i',
        'ic_data_addr_o',
        'ic_data_rdata_i',
        'ic_data_req_i',
        'ic_data_req_o',
        'ic_data_wdata_i',
        'ic_data_wdata_o',
        'ic_data_write_i',
        'ic_data_write_o',
        'ic_scr_key_req_i',
        'ic_scr_key_req_o',
        'ic_scr_key_valid_i',
        'icache_data_ack_o',
        'icache_data_i',
        'icache_data_req_i',
        'icache_fetch_vaddr_i',
        'instr_fetch_err_i',
        'instr_fetch_err_o',
        'instr_fetch_err_plus2_i',
        'instr_fetch_err_plus2_o',
        'l1_dcache_access_i',
        'l1_icache_access_i',
        'l_data_t',
        'loadIssueReq',
        'loadQueueHeadPtr',
        'loadQueueRecoveryTailPtr',
        'load_err_i',
        'load_err_o',
        'load_exception_o',
        'load_resp_intg_err_o',
        'load_result_o',
        'load_trans_id_o',
        'load_valid_o',
        'lsu_load_err_i',
        'lsu_load_resp_intg_err_i',
        'lu_access_i',
        'mem_data_ack_i',
        'mem_data_o',
        'mem_data_req_o',
        'mem_load_i',
        'memory_data',
        'multdiv_operand_a_ex_o',
        'multdiv_operand_a_i',
        'multdiv_operand_b_ex_o',
        'multdiv_operand_b_i',
        'operand_a_i',
        'operand_b_i',
        'outstanding_load_wb_i',
        'outstanding_load_wb_o',
        'perf_data_i',
        'perf_data_o',
        'perf_load_o',
        'ram_cfg_icache_data_i',
        'ram_cfg_rsp_icache_data_o',
        'rd_data_i',
        'rd_data_o',
        'req_port_i.data_rvalid',
        'riscv::pmp_access_t',
        'scramble_key_i',
        'scramble_key_valid_i',
        'wbuffer_data_i',
        'wbuffer_data_o',
        'wr_cl_data_be_i',
        'wr_cl_data_be_o',
        'wr_cl_data_i',
        'wr_cl_data_o',
        'wr_data_be_i',
        'wr_data_be_o',
        'wr_data_i',
        'wr_data_o'
    ])
    
    payload_keywords: List[str] = field(default_factory=lambda: [
        '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0',
        'acc_fflags_ex_valid_i',
        'acc_fflags_valid_o',
        'acc_result_o',
        'acc_valid_ex_o',
        'acc_valid_i',
        'acc_valid_o',
        'adder_result_ex_i',
        'adder_result_ext_o',
        'adder_result_o',
        'aes_valid_i',
        'aes_valid_o',
        'alu2_valid_i',
        'alu2_valid_o',
        'alu_adder_result_ex_o',
        'alu_valid_i',
        'alu_valid_o',
        'amo_result_o',
        'amo_valid_commit_i',
        'amo_valid_commit_o',
        'axi_data_i',
        'axi_data_o',
        'branch_result_o',
        'branch_valid_i',
        'branch_valid_o',
        'busy_i',
        'busy_o',
        'bypass_data_i',
        'bypass_data_o',
        'bypass_valid_i',
        'bypass_valid_o',
        'commit_lsu_ready_i',
        'commit_ready_o',
        'commit_valid_o',
        'comparison_result_o',
        'compressed_ready_i',
        'compressed_ready_o',
        'compressed_valid_i',
        'compressed_valid_o',
        'core_busy_i',
        'critical_word_valid_i',
        'critical_word_valid_o',
        'csr_ready_o',
        'csr_result_o',
        'csr_valid_i',
        'csr_valid_o',
        'ctrl_busy_o',
        'cvxif_ready_i',
        'cvxif_valid_o',
        'data',
        'dataIn',
        'dataOut',
        'data_addr_i',
        'data_addr_o',
        'data_be_i',
        'data_be_o',
        'data_bus_err_i',
        'data_err_i',
        'data_gnt_i',
        'data_i',
        'data_ind_timing_i',
        'data_ind_timing_o',
        'data_o',
        'data_pmp_err_i',
        'data_rdata_i',
        'data_rdata_intg_i',
        'data_req_i',
        'data_req_o',
        'data_rvalid_i',
        'data_sign_extension_o',
        'data_size_i',
        'data_type_o',
        'data_wdata_i',
        'data_wdata_intg_o',
        'data_wdata_o',
        'data_we_i',
        'data_we_o',
        'dcache_data_ack_o',
        'dcache_data_i',
        'dcache_data_req_i',
        'dcache_mem_req_read_ready_i',
        'dcache_mem_req_read_valid_o',
        'dcache_mem_req_write_data_o',
        'dcache_mem_req_write_data_ready_i',
        'dcache_mem_req_write_data_valid_o',
        'dcache_mem_req_write_ready_i',
        'dcache_mem_req_write_valid_o',
        'dcache_mem_resp_read_ready_o',
        'dcache_mem_resp_read_valid_i',
        'dcache_mem_resp_write_ready_o',
        'dcache_mem_resp_write_valid_i',
        'dcache_read_ready_o',
        'dcache_read_resp_ready_i',
        'dcache_read_resp_valid_o',
        'dcache_read_valid_i',
        'dcache_write_data_i',
        'dcache_write_data_ready_o',
        'dcache_write_data_valid_i',
        'dcache_write_ready_o',
        'dcache_write_resp_ready_i',
        'dcache_write_resp_valid_o',
        'dcache_write_valid_i',
        'decoded_instr_valid_i',
        'div_wait_i',
        'dside_wait_i',
        'dummy_instr_data_o',
        'ex_valid_i',
        'ex_valid_o',
        'fetch_entry_ready_i',
        'fetch_entry_ready_o',
        'fetch_entry_valid_i',
        'fetch_entry_valid_o',
        'fetch_valid_i',
        'flu_ready_i',
        'flu_ready_o',
        'flu_result_o',
        'flu_valid_o',
        'fma_result',
        'fpu_early_valid_i',
        'fpu_early_valid_o',
        'fpu_ready_i',
        'fpu_ready_o',
        'fpu_result_o',
        'fpu_valid_i',
        'fpu_valid_o',
        'fu_data_cpop_i',
        'fu_data_i',
        'fu_data_o',
        'fu_data_t',
        'hpdcache_req_ready_i',
        'hpdcache_req_valid_o',
        'hpdcache_rsp_valid_i',
        'ic_data_addr_i',
        'ic_data_addr_o',
        'ic_data_rdata_i',
        'ic_data_req_i',
        'ic_data_req_o',
        'ic_data_wdata_i',
        'ic_data_wdata_o',
        'ic_data_write_i',
        'ic_data_write_o',
        'ic_scr_key_valid_i',
        'icache_data_ack_o',
        'icache_data_i',
        'icache_data_req_i',
        'icache_miss_ready_o',
        'icache_miss_resp_valid_o',
        'icache_miss_valid_i',
        'id_in_ready_i',
        'id_in_ready_o',
        'if_busy_o',
        'in_valid_i',
        'instr_valid_clear_i',
        'instr_valid_clear_o',
        'instr_valid_i',
        'instr_valid_id_o',
        'inval_ready_i',
        'inval_ready_o',
        'inval_valid_i',
        'inval_valid_o',
        'is_equal_result_o',
        'iside_wait_i',
        'issue_entry_valid_o',
        'issue_instr_valid_i',
        'issue_instr_valid_o',
        'issue_ready_i',
        'issue_ready_o',
        'issue_valid_i',
        'issue_valid_o',
        'l_data_t',
        'load_result_o',
        'load_valid_o',
        'lsu_commit_ready_o',
        'lsu_rdata_valid_o',
        'lsu_ready_i',
        'lsu_ready_o',
        'lsu_req_valid_i',
        'lsu_resp_valid_i',
        'lsu_resp_valid_o',
        'lsu_valid_i',
        'lsu_valid_o',
        'mem_data_ack_i',
        'mem_data_o',
        'mem_data_req_o',
        'memory_data',
        'mul_wait_i',
        'mult_ready_o',
        'mult_valid_i',
        'mult_valid_o',
        'multdiv_ready_id_i',
        'multdiv_ready_id_o',
        'multdiv_result_o',
        'out',
        'out_addr_o',
        'out_err_o',
        'out_err_plus2_o',
        'out_rdata_o',
        'out_rdy_i',
        'out_ready_i',
        'out_valid_o',
        'out_vld_o',
        'perf_data_i',
        'perf_data_o',
        'perf_div_wait_o',
        'perf_dside_wait_o',
        'perf_mul_wait_o',
        'ram_cfg_icache_data_i',
        'ram_cfg_rsp_icache_data_o',
        'rd_data_i',
        'rd_data_o',
        'rd_valid_o',
        'ready_i',
        'ready_o',
        'ready_wb_i',
        'ready_wb_o',
        'req_port_i.data_rvalid',
        'result',
        'result_ex_i',
        'result_ex_o',
        'result_i',
        'result_o',
        'result_ready_o',
        'result_valid_i',
        'rs_valid_i',
        'rvfi_ext_expanded_insn_valid',
        'rvfi_valid',
        'scramble_key_valid_i',
        'store_result_i',
        'store_result_o',
        'store_valid_o',
        'valid',
        'valid_dirty)',
        'valid_i',
        'valid_o',
        'valid_without_flush_i',
        'wbuffer_data_i',
        'wbuffer_data_o',
        'wr_cl_data_be_i',
        'wr_cl_data_be_o',
        'wr_cl_data_i',
        'wr_cl_data_o',
        'wr_data_be_i',
        'wr_data_be_o',
        'wr_data_i',
        'wr_data_o',
        'wr_valid_o',
        'wt_valid_i',
        'x_commit_valid_o',
        'x_issue_ready_i',
        'x_issue_valid_o',
        'x_ready_o',
        'x_result_i',
        'x_result_o',
        'x_result_ready_o',
        'x_result_t',
        'x_result_valid_i',
        'x_valid_i',
        'x_valid_o',
        'xfu_ready_i',
        'xfu_valid_o'
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
            'trigger_type': 'counter',
            'payload_action': 'timing_modulation_sequential_or_xor_combinational',
            'encoding': 'bit_to_delay',
            'comment_header': f"// Timing Side-Channel (extends Trust-Hub Leak Information)\n// Sources: {', '.join(self.rtl_citations[:3])}"
        }


covert_pattern = CovertPattern()


def get_pattern() -> CovertPattern:
    """Get Covert pattern instance"""
    return covert_pattern