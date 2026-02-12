#!/usr/bin/env python3
"""
Integrity Violation Pattern
Based on Trust-Hub Benchmarks: AES-T2500, AES-T2600, AES-T2700, AES-T2800

Corrupts computation results or data
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class IntegrityPattern:
    """
    Integrity Violation Trojan Pattern
    
    Trust-Hub Category: Change Functionality ✓ (Verified)
    Trust-Hub Benchmarks: AES-T2500, AES-T2600, AES-T2700, AES-T2800
    Severity: High
    
    Description:
        Corrupts computation results, data, or memory contents by XORing
        with corruption patterns or flipping specific bits. Based on
        verified Trust-Hub RTL benchmarks.
    
    Trust-Hub Mechanism:
        Trust-Hub integrity trojans corrupt AES encryption output through
        bit flips and XOR operations on data paths.
    
    RISC-V Adaptation:
        Adapted for RISC-V ALU and data path corruption. Targets
        computation results and data integrity.
    
    Trigger Mechanism:
        - Specific input patterns
        - Address-based trigger
        - Data value trigger
        - Operation type
    
    Payload:
        Corrupts output data by XORing with corruption pattern,
        bit flipping, or other data manipulation.
    
    Target Signals:
        - Trigger: data, input, addr, address, operation signals
        - Payload: data, result, output, computation signals
    
    Real-World Impact:
        - Incorrect computation results
        - Data corruption
        - Memory corruption
        - Control flow hijacking
    
    Example in RISC-V:
        - Target: ibex_alu module
        - Signal: result_o
        - Effect: Corrupts ALU output for specific operations
    
    References:
        [1] Trust-Hub, "AES-T2500: Data Integrity Trojan"
        [2] Trust-Hub, "AES-T2600: Data Integrity Trojan"
        [3] Trust-Hub, "AES-T2700: Data Integrity Trojan"
        [4] Trust-Hub, "AES-T2800: Data Integrity Trojan"
    """
    
    name: str = "Integrity"
    category: str = "Integrity Violation"
    
    # Trust-Hub verification status
    trust_hub_status: str = "Verified RTL Benchmarks"
    trust_hub_category: str = "Change Functionality"
    trust_hub_benchmarks: str = "AES-T2500, AES-T2600, AES-T2700, AES-T2800"
    trust_hub_source: str = "AES-T2500"  # Primary benchmark
    
    # Citations
    rtl_citations: List[str] = field(default_factory=lambda: [
        "Trust-Hub AES-T2500",
        "Trust-Hub AES-T2600",
        "Trust-Hub AES-T2700",
        "Trust-Hub AES-T2800"
    ])
    
    # Pattern metadata
    severity: str = "High"
    description: str = "Corrupts computation results or data"
    adaptation_note: str = "Adapted from AES data corruption to RISC-V ALU targeting"
    
    # Keywords for signal matching
    trigger_keywords: List[str] = field(default_factory=lambda: [
        'OpInfo',
        'OpOperandType',
        'SRC_OP_NUM',
        'SRC_OP_NUM-1:0',
        '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0',
        'addr',
        'addr_i',
        'addr_incr_req_o',
        'addr_last_o',
        'addr_o',
        'address_i',
        'alu_op_a_mux_sel_o',
        'alu_op_b_mux_sel_o',
        'alu_operator_ex_o',
        'alu_operator_i',
        'alu_operator_o',
        'amo_op',
        'amo_op_i',
        'axi_data_i',
        'axi_data_o',
        'boot_addr_i',
        'bt_a_mux_sel_o',
        'bt_b_mux_sel_o',
        'bypass_data_i',
        'bypass_data_o',
        'conf_addr_i',
        'conf_addr_mode_i',
        'conf_addr_prev_i',
        'csr_addr_i',
        'csr_addr_o',
        'csr_op_en_i',
        'csr_op_en_o',
        'csr_op_i',
        'csr_op_o',
        'csr_pmp_addr_i',
        'csr_pmp_addr_o',
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
        'div_sel_ex_o',
        'div_sel_i',
        'div_sel_o',
        'dummy_instr_data_o',
        'exc_pc_sel_e',
        'exception_addr_i',
        'fu_data_cpop_i',
        'fu_data_i',
        'fu_data_o',
        'fu_data_t',
        'fu_op',
        'ibex_pkg::alu_op_e',
        'ibex_pkg::csr_op_e',
        'ibex_pkg::exc_pc_sel_e',
        'ibex_pkg::imm_a_sel_e',
        'ibex_pkg::imm_b_sel_e',
        'ibex_pkg::md_op_e',
        'ibex_pkg::op_a_sel_e',
        'ibex_pkg::op_b_sel_e',
        'ibex_pkg::pc_sel_e',
        'ibex_pkg::rf_wd_sel_e',
        'ic_data_addr_i',
        'ic_data_addr_o',
        'ic_data_rdata_i',
        'ic_data_req_i',
        'ic_data_req_o',
        'ic_data_wdata_i',
        'ic_data_wdata_o',
        'ic_data_write_i',
        'ic_data_write_o',
        'ic_tag_addr_i',
        'ic_tag_addr_o',
        'icache_data_ack_o',
        'icache_data_i',
        'icache_data_req_i',
        'imm_a_mux_sel_o',
        'imm_b_mux_sel_o',
        'in_addr_i',
        'instr_addr_i',
        'instr_addr_o',
        'inval_addr_i',
        'inval_addr_o',
        'jump_address_i',
        'jump_address_o',
        'l_data_t',
        'lsu_addr_incr_req_i',
        'lsu_addr_last_i',
        'mem_data_ack_i',
        'mem_data_o',
        'mem_data_req_o',
        'memory_addr',
        'memory_data',
        'mshr_addr_i',
        'mshr_addr_matches_i',
        'mshr_addr_matches_o',
        'mshr_addr_o',
        'mult_sel_ex_o',
        'mult_sel_i',
        'mult_sel_o',
        'multdiv_operator_ex_o',
        'multdiv_operator_i',
        'multdiv_operator_o',
        'multdiv_sel_i',
        'nt_branch_addr_i',
        'nt_branch_addr_o',
        'op',
        'opInfo',
        'op_a_i',
        'op_a_sign)',
        'op_b_i',
        'op_b_sign)',
        'operator_i',
        'out_addr_o',
        'pc_sel_e',
        'perf_addr_o',
        'perf_data_i',
        'perf_data_o',
        'pmp_req_addr_i',
        'predict_address_i',
        'ram_cfg_icache_data_i',
        'ram_cfg_rsp_icache_data_o',
        'rd_addr_i',
        'rd_data_i',
        'rd_data_o',
        'replay_addr_o',
        'req_port_i.data_rvalid',
        'rf_wdata_sel_o',
        'riscv::pmp_addr_mode_t',
        'rvfi_mem_addr',
        'rvfi_rd_addr',
        'rvfi_rs1_addr',
        'rvfi_rs2_addr',
        'rvfi_rs3_addr',
        'sel',
        'wbuffer_data_i',
        'wbuffer_data_o',
        'wr_addr_i',
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
        'STORE_ISSUE_WIDTH',
        'WRITE_NUM',
        '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0',
        'acc_result_o',
        'adder_result_ex_i',
        'adder_result_ext_o',
        'adder_result_o',
        'alu_adder_result_ex_o',
        'amo_result_o',
        'axi_data_i',
        'axi_data_o',
        'branch_result_o',
        'bypass_data_i',
        'bypass_data_o',
        'comparison_result_o',
        'csr_rdata_i',
        'csr_rdata_o',
        'csr_result_o',
        'csr_wdata_i',
        'csr_wdata_o',
        'csr_write_fflags_i',
        'csr_write_fflags_o',
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
        'dummy_instr_data_o',
        'expecting_store_resp_o',
        'fetch_rdata_i',
        'flu_result_o',
        'fma_result',
        'fpu_result_o',
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
        'ic_tag_rdata_i',
        'ic_tag_wdata_i',
        'ic_tag_wdata_o',
        'ic_tag_write_i',
        'ic_tag_write_o',
        'icache_data_ack_o',
        'icache_data_i',
        'icache_data_req_i',
        'in_rdata_i',
        'instr_rdata_alu_i',
        'instr_rdata_alu_id_o',
        'instr_rdata_c_i',
        'instr_rdata_c_id_o',
        'instr_rdata_i',
        'instr_rdata_id_o',
        'instr_rdata_intg_i',
        'is_equal_result_o',
        'l_data_t',
        'load_result_o',
        'lsu_is_store_i',
        'lsu_rdata_o',
        'lsu_rdata_valid_o',
        'lsu_store_err_i',
        'lsu_store_resp_intg_err_i',
        'lsu_wdata_i',
        'lsu_wdata_o',
        'mem_data_ack_i',
        'mem_data_o',
        'mem_data_req_o',
        'mem_store_i',
        'memory_data',
        'miss_wdata_i',
        'miss_wdata_o',
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
        'outstanding_store_wb_i',
        'outstanding_store_wb_o',
        'perf_data_i',
        'perf_data_o',
        'perf_store_o',
        'ram_cfg_icache_data_i',
        'ram_cfg_rsp_icache_data_o',
        'rd_data_i',
        'rd_data_o',
        'rdata_a_o',
        'rdata_b_o',
        'rdata_i',
        'rdata_o',
        'req_port_i.data_rvalid',
        'result',
        'result_ex_i',
        'result_ex_o',
        'result_i',
        'result_o',
        'result_ready_o',
        'result_valid_i',
        'rf_rdata_a_ecc_i',
        'rf_rdata_a_i',
        'rf_rdata_b_ecc_i',
        'rf_rdata_b_i',
        'rf_wdata_fwd_wb_i',
        'rf_wdata_fwd_wb_o',
        'rf_wdata_id_i',
        'rf_wdata_id_o',
        'rf_wdata_lsu_i',
        'rf_wdata_sel_o',
        'rf_wdata_wb_ecc_i',
        'rf_wdata_wb_o',
        'rf_write_wb_i',
        'rf_write_wb_o',
        'rvfi_mem_rdata',
        'rvfi_mem_wdata',
        'rvfi_pc_rdata',
        'rvfi_pc_wdata',
        'rvfi_rd_wdata',
        'rvfi_rs1_rdata',
        'rvfi_rs2_rdata',
        'rvfi_rs3_rdata',
        'storeIssueReq',
        'storeQueueEmpty',
        'storeQueueHeadPtr',
        'storeQueueRecoveryTailPtr',
        'store_buffer_empty_i',
        'store_buffer_empty_o',
        'store_err_i',
        'store_err_o',
        'store_exception_o',
        'store_resp_intg_err_o',
        'store_result_i',
        'store_result_o',
        'store_trans_id_o',
        'store_valid_o',
        'wbuffer_data_i',
        'wbuffer_data_o',
        'wdata_a_i',
        'wdata_i',
        'wdata_o',
        'wr_cl_data_be_i',
        'wr_cl_data_be_o',
        'wr_cl_data_i',
        'wr_cl_data_o',
        'wr_data_be_i',
        'wr_data_be_o',
        'wr_data_i',
        'wr_data_o',
        'write',
        'writeIndex',
        'x_result_i',
        'x_result_o',
        'x_result_ready_o',
        'x_result_t',
        'x_result_valid_i'
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
