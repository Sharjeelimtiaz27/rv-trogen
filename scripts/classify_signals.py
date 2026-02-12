#!/usr/bin/env python3
"""
Signal Classifier for Hardware Trojan Generation
Classifies signals from RISC-V modules by trojan pattern type

Usage:
1. Edit the PROCESSOR_SIGNALS dict below (paste your signals)
2. Run: python classify_signals.py
3. Get CSV files: ibex_signals.csv, cva6_signals.csv, rsd_signals.csv
"""

import csv
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict


# ============================================================================
# CLASSIFICATION RULES
# ============================================================================

PATTERN_RULES = {
    'DoS': {
        'trigger_keywords': [
            'enable', 'en', 'valid', 'ready', 'start', 'req', 'request',
            'active', 'go', 'trigger', 'we', 'wen'
        ],
        'payload_keywords': [
            'enable', 'en', 'valid', 'ready', 'start', 'req',
            'active', 'done', 'complete', 'we', 'wen'
        ]
    },
    
    'Leak': {
        'trigger_keywords': [
            'debug', 'test', 'mode', 'csr', 'write', 'we', 'wen'
        ],
        'payload_keywords': [
            'data', 'rdata', 'wdata', 'result', 'operand', 'csr',
            'addr', 'address', 'output', 'out', 'value', 'reg'
        ]
    },
    
    'Privilege': {
        'trigger_keywords': [
            'csr', 'write', 'we', 'wen', 'addr', 'address', 'mode'
        ],
        'payload_keywords': [
            'priv', 'privilege', 'mode', 'level', 'lvl',
            'mstatus', 'mepc', 'mtvec', 'status', 'permission'
        ]
    },
    
    'Integrity': {
        'trigger_keywords': [
            'operator', 'op', 'cmd', 'command', 'addr', 'address',
            'data', 'input', 'sel', 'select'
        ],
        'payload_keywords': [
            'result', 'data', 'output', 'out', 'rdata', 'wdata',
            'calc', 'value', 'write', 'store'
        ]
    },
    
    'Availability': {
        'trigger_keywords': [
            'req', 'request', 'valid', 'start', 'op', 'operation',
            'cmd', 'trigger', 'lsu', 'load', 'store'
        ],
        'payload_keywords': [
            'ready', 'valid', 'done', 'complete', 'ack',
            'grant', 'gnt', 'stall', 'busy', 'wait', 'delay'
        ]
    },
    
    'Covert': {
        'trigger_keywords': [
            'data', 'operand', 'input', 'secret', 'key',
            'load', 'fetch', 'access', 'value'
        ],
        'payload_keywords': [
            'output', 'result', 'ready', 'valid', 'delay',
            'timing', 'wait', 'busy', 'data', 'out'
        ]
    }
}


# ============================================================================
# PASTE YOUR SIGNALS HERE
# ============================================================================

PROCESSOR_SIGNALS = {
    # Example format - REPLACE WITH YOUR ACTUAL SIGNALS
    'ibex': {
        'ibex_alu': {
            'inputs': ['ibex_pkg::alu_op_e', 'operator_i', 'operand_a_i', 'operand_b_i', 'instr_first_cycle_i', 'multdiv_operand_a_i', 'multdiv_operand_b_i', 'multdiv_sel_i', 'imd_val_we_o', 'adder_result_o', 'adder_result_ext_o', 'result_o', 'comparison_result_o', 'is_equal_result_o', ')'],
            'outputs': ['imd_val_we_o', 'adder_result_o', 'adder_result_ext_o', 'result_o', 'comparison_result_o', 'is_equal_result_o', ')'],
            'internals': []
        },
        'ibex_branch_predict': {
            'inputs': ['clk_i', 'rst_ni', 'fetch_rdata_i', 'fetch_pc_i', 'fetch_valid_i', 'predict_branch_taken_o', 'predict_branch_pc_o', ')'],
            'outputs': ['predict_branch_taken_o', 'predict_branch_pc_o', ')'],
            'internals': []
        },
        'ibex_controller': {
            'inputs': ['clk_i', 'rst_ni', 'ctrl_busy_o', 'illegal_insn_i', 'ecall_insn_i', 'mret_insn_i', 'dret_insn_i', 'wfi_insn_i', 'ebrk_insn_i', 'csr_pipe_flush_i', 'instr_valid_i', 'instr_i', 'instr_compressed_i', 'instr_is_compressed_i', 'instr_bp_taken_i', 'instr_fetch_err_i', 'instr_fetch_err_plus2_i', 'pc_id_i', 'instr_valid_clear_o', 'id_in_ready_o', 'controller_run_o', 'instr_exec_i', 'instr_req_o', 'pc_set_o', 'ibex_pkg::pc_sel_e', 'pc_mux_o', 'nt_branch_mispredict_o', 'ibex_pkg::exc_pc_sel_e', 'exc_pc_mux_o', 'ibex_pkg::exc_cause_t', 'exc_cause_o', 'lsu_addr_last_i', 'load_err_i', 'store_err_i', 'mem_resp_intg_err_i', 'wb_exception_o', 'id_exception_o', 'branch_set_i', 'branch_not_set_i', 'jump_set_i', 'csr_mstatus_mie_i', 'irq_pending_i', 'ibex_pkg::irqs_t', 'irqs_i', 'irq_nm_ext_i', 'nmi_mode_o', 'debug_req_i', 'ibex_pkg::dbg_cause_e', 'debug_cause_o', 'debug_csr_save_o', 'debug_mode_o', 'debug_mode_entering_o', 'debug_single_step_i', 'debug_ebreakm_i', 'debug_ebreaku_i', 'trigger_match_i', 'csr_save_if_o', 'csr_save_id_o', 'csr_save_wb_o', 'csr_restore_mret_id_o', 'csr_restore_dret_id_o', 'csr_save_cause_o', 'csr_mtval_o', 'ibex_pkg::priv_lvl_e', 'priv_mode_i', 'stall_id_i', 'stall_wb_i', 'flush_id_o', 'ready_wb_i', 'perf_jump_o', 'perf_tbranch_o', ')'],
            'outputs': ['ctrl_busy_o', 'illegal_insn_i', 'ecall_insn_i', 'mret_insn_i', 'dret_insn_i', 'wfi_insn_i', 'ebrk_insn_i', 'csr_pipe_flush_i', 'instr_valid_i', 'instr_i', 'instr_compressed_i', 'instr_is_compressed_i', 'instr_bp_taken_i', 'instr_fetch_err_i', 'instr_fetch_err_plus2_i', 'pc_id_i', 'instr_valid_clear_o', 'id_in_ready_o', 'controller_run_o', 'instr_exec_i', 'instr_req_o', 'pc_set_o', 'ibex_pkg::pc_sel_e', 'pc_mux_o', 'nt_branch_mispredict_o', 'ibex_pkg::exc_pc_sel_e', 'exc_pc_mux_o', 'ibex_pkg::exc_cause_t', 'exc_cause_o', 'lsu_addr_last_i', 'load_err_i', 'store_err_i', 'mem_resp_intg_err_i', 'wb_exception_o', 'id_exception_o', 'branch_set_i', 'branch_not_set_i', 'jump_set_i', 'csr_mstatus_mie_i', 'irq_pending_i', 'ibex_pkg::irqs_t', 'irqs_i', 'irq_nm_ext_i', 'nmi_mode_o', 'debug_req_i', 'ibex_pkg::dbg_cause_e', 'debug_cause_o', 'debug_csr_save_o', 'debug_mode_o', 'debug_mode_entering_o', 'debug_single_step_i', 'debug_ebreakm_i', 'debug_ebreaku_i', 'trigger_match_i', 'csr_save_if_o', 'csr_save_id_o', 'csr_save_wb_o', 'csr_restore_mret_id_o', 'csr_restore_dret_id_o', 'csr_save_cause_o', 'csr_mtval_o', 'ibex_pkg::priv_lvl_e', 'priv_mode_i', 'stall_id_i', 'stall_wb_i', 'flush_id_o', 'ready_wb_i', 'perf_jump_o', 'perf_tbranch_o', ')'],
            'internals': []
        },
        'ibex_counter': {
            'inputs': ['clk_i', 'rst_ni', 'counter_inc_i', 'counterh_we_i', 'counter_we_i', 'counter_val_i', 'counter_val_o', 'counter_val_upd_o', ')'],
            'outputs': ['counter_val_o', 'counter_val_upd_o', ')'],
            'internals': []
        },
        'ibex_cs_registers': {
            'inputs': ['clk_i', 'rst_ni', 'hart_id_i', 'ibex_pkg::priv_lvl_e', 'priv_mode_id_o', 'ibex_pkg::priv_lvl_e', 'priv_mode_lsu_o', 'csr_mstatus_tw_o', 'csr_mtvec_o', 'csr_mtvec_init_i', 'boot_addr_i', 'csr_access_i', 'ibex_pkg::csr_num_e', 'csr_addr_i', 'csr_wdata_i', 'ibex_pkg::csr_op_e', 'csr_op_i', 'csr_op_en_i', 'csr_rdata_o', 'irq_software_i', 'irq_timer_i', 'irq_external_i', 'irq_fast_i', 'nmi_mode_i', 'irq_pending_o', 'ibex_pkg::irqs_t', 'irqs_o', 'csr_mstatus_mie_o', 'csr_mepc_o', 'csr_mtval_o', 'ibex_pkg::pmp_cfg_t', 'csr_pmp_cfg_o', 'csr_pmp_addr_o', 'ibex_pkg::pmp_mseccfg_t', 'csr_pmp_mseccfg_o', 'debug_mode_i', 'debug_mode_entering_i', 'ibex_pkg::dbg_cause_e', 'debug_cause_i', 'debug_csr_save_i', 'csr_depc_o', 'debug_single_step_o', 'debug_ebreakm_o', 'debug_ebreaku_o', 'trigger_match_o', 'pc_if_i', 'pc_id_i', 'pc_wb_i', 'data_ind_timing_o', 'dummy_instr_en_o', 'dummy_instr_mask_o', 'dummy_instr_seed_en_o', 'dummy_instr_seed_o', 'icache_enable_o', 'csr_shadow_err_o', 'ic_scr_key_valid_i', 'csr_save_if_i', 'csr_save_id_i', 'csr_save_wb_i', 'csr_restore_mret_i', 'csr_restore_dret_i', 'csr_save_cause_i', 'ibex_pkg::exc_cause_t', 'csr_mcause_i', 'csr_mtval_i', 'illegal_csr_insn_o', 'double_fault_seen_o', 'instr_ret_i', 'instr_ret_compressed_i', 'instr_ret_spec_i', 'instr_ret_compressed_spec_i', 'iside_wait_i', 'jump_i', 'branch_i', 'branch_taken_i', 'mem_load_i', 'mem_store_i', 'dside_wait_i', 'mul_wait_i', 'div_wait_i', ')'],
            'outputs': ['ibex_pkg::priv_lvl_e', 'priv_mode_id_o', 'ibex_pkg::priv_lvl_e', 'priv_mode_lsu_o', 'csr_mstatus_tw_o', 'csr_mtvec_o', 'csr_mtvec_init_i', 'boot_addr_i', 'csr_access_i', 'ibex_pkg::csr_num_e', 'csr_addr_i', 'csr_wdata_i', 'ibex_pkg::csr_op_e', 'csr_op_i', 'csr_op_en_i', 'csr_rdata_o', 'irq_software_i', 'irq_timer_i', 'irq_external_i', 'irq_fast_i', 'nmi_mode_i', 'irq_pending_o', 'ibex_pkg::irqs_t', 'irqs_o', 'csr_mstatus_mie_o', 'csr_mepc_o', 'csr_mtval_o', 'ibex_pkg::pmp_cfg_t', 'csr_pmp_cfg_o', 'csr_pmp_addr_o', 'ibex_pkg::pmp_mseccfg_t', 'csr_pmp_mseccfg_o', 'debug_mode_i', 'debug_mode_entering_i', 'ibex_pkg::dbg_cause_e', 'debug_cause_i', 'debug_csr_save_i', 'csr_depc_o', 'debug_single_step_o', 'debug_ebreakm_o', 'debug_ebreaku_o', 'trigger_match_o', 'pc_if_i', 'pc_id_i', 'pc_wb_i', 'data_ind_timing_o', 'dummy_instr_en_o', 'dummy_instr_mask_o', 'dummy_instr_seed_en_o', 'dummy_instr_seed_o', 'icache_enable_o', 'csr_shadow_err_o', 'ic_scr_key_valid_i', 'csr_save_if_i', 'csr_save_id_i', 'csr_save_wb_i', 'csr_restore_mret_i', 'csr_restore_dret_i', 'csr_save_cause_i', 'ibex_pkg::exc_cause_t', 'csr_mcause_i', 'csr_mtval_i', 'illegal_csr_insn_o', 'double_fault_seen_o', 'instr_ret_i', 'instr_ret_compressed_i', 'instr_ret_spec_i', 'instr_ret_compressed_spec_i', 'iside_wait_i', 'jump_i', 'branch_i', 'branch_taken_i', 'mem_load_i', 'mem_store_i', 'dside_wait_i', 'mul_wait_i', 'div_wait_i', ')'],
            'internals': []
        },
        'ibex_csr': {
            'inputs': ['clk_i', 'rst_ni', 'wr_data_i', 'wr_en_i', 'rd_data_o', 'rd_error_o', ')'],
            'outputs': ['rd_data_o', 'rd_error_o', ')'],
            'internals': []
        },
        'ibex_dummy_instr': {
            'inputs': ['clk_i', 'rst_ni', 'dummy_instr_en_i', 'dummy_instr_mask_i', 'dummy_instr_seed_en_i', 'dummy_instr_seed_i', 'fetch_valid_i', 'id_in_ready_i', 'insert_dummy_instr_o', 'dummy_instr_data_o', ')'],
            'outputs': ['insert_dummy_instr_o', 'dummy_instr_data_o', ')'],
            'internals': []
        },
        'ibex_ex_block': {
            'inputs': ['clk_i', 'rst_ni', 'ibex_pkg::alu_op_e', 'alu_operator_i', 'alu_operand_a_i', 'alu_operand_b_i', 'alu_instr_first_cycle_i', 'bt_a_operand_i', 'bt_b_operand_i', 'ibex_pkg::md_op_e', 'multdiv_operator_i', 'mult_en_i', 'div_en_i', 'mult_sel_i', 'div_sel_i', 'multdiv_signed_mode_i', 'multdiv_operand_a_i', 'multdiv_operand_b_i', 'multdiv_ready_id_i', 'data_ind_timing_i', 'imd_val_we_o', 'alu_adder_result_ex_o', 'result_ex_o', 'branch_target_o', 'branch_decision_o', 'ex_valid_o', ')'],
            'outputs': ['imd_val_we_o', 'alu_adder_result_ex_o', 'result_ex_o', 'branch_target_o', 'branch_decision_o', 'ex_valid_o', ')'],
            'internals': []
        },
        'ibex_fetch_fifo': {
            'inputs': ['clk_i', 'rst_ni', 'clear_i', 'busy_o', 'in_valid_i', 'in_addr_i', 'in_rdata_i', 'in_err_i', 'out_valid_o', 'out_ready_i', 'out_addr_o', 'out_rdata_o', 'out_err_o', 'out_err_plus2_o', ')'],
            'outputs': ['busy_o', 'in_valid_i', 'in_addr_i', 'in_rdata_i', 'in_err_i', 'out_valid_o', 'out_ready_i', 'out_addr_o', 'out_rdata_o', 'out_err_o', 'out_err_plus2_o', ')'],
            'internals': []
        },
        'ibex_icache': {
            'inputs': ['clk_i', 'rst_ni', 'req_i', 'branch_i', 'addr_i', 'ready_i', 'valid_o', 'rdata_o', 'addr_o', 'err_o', 'err_plus2_o', 'instr_req_o', 'instr_gnt_i', 'instr_addr_o', 'instr_rdata_i', 'instr_err_i', 'instr_rvalid_i', 'ic_tag_req_o', 'ic_tag_write_o', 'ic_tag_addr_o', 'ic_tag_wdata_o', 'ic_tag_rdata_i', 'ic_data_req_o', 'ic_data_write_o', 'ic_data_addr_o', 'ic_data_wdata_o', 'ic_data_rdata_i', 'ic_scr_key_valid_i', 'ic_scr_key_req_o', 'icache_enable_i', 'icache_inval_i', 'busy_o', 'ecc_error_o', ')'],
            'outputs': ['valid_o', 'rdata_o', 'addr_o', 'err_o', 'err_plus2_o', 'instr_req_o', 'instr_gnt_i', 'instr_addr_o', 'instr_rdata_i', 'instr_err_i', 'instr_rvalid_i', 'ic_tag_req_o', 'ic_tag_write_o', 'ic_tag_addr_o', 'ic_tag_wdata_o', 'ic_tag_rdata_i', 'ic_data_req_o', 'ic_data_write_o', 'ic_data_addr_o', 'ic_data_wdata_o', 'ic_data_rdata_i', 'ic_scr_key_valid_i', 'ic_scr_key_req_o', 'icache_enable_i', 'icache_inval_i', 'busy_o', 'ecc_error_o', ')', '='],
            'internals': []
        },
        'ibex_id_stage': {
            'inputs': ['clk_i', 'rst_ni', 'ctrl_busy_o', 'illegal_insn_o', 'instr_valid_i', 'instr_rdata_i', 'instr_rdata_alu_i', 'instr_rdata_c_i', 'instr_is_compressed_i', 'instr_bp_taken_i', 'instr_req_o', 'instr_first_cycle_id_o', 'instr_valid_clear_o', 'id_in_ready_o', 'instr_exec_i', 'icache_inval_o', 'branch_decision_i', 'pc_set_o', 'ibex_pkg::pc_sel_e', 'pc_mux_o', 'nt_branch_mispredict_o', 'nt_branch_addr_o', 'ibex_pkg::exc_pc_sel_e', 'exc_pc_mux_o', 'ibex_pkg::exc_cause_t', 'exc_cause_o', 'illegal_c_insn_i', 'instr_fetch_err_i', 'instr_fetch_err_plus2_i', 'pc_id_i', 'ex_valid_i', 'lsu_resp_valid_i', 'ibex_pkg::alu_op_e', 'alu_operator_ex_o', 'alu_operand_a_ex_o', 'alu_operand_b_ex_o', 'imd_val_we_ex_i', 'bt_a_operand_o', 'bt_b_operand_o', 'mult_en_ex_o', 'div_en_ex_o', 'mult_sel_ex_o', 'div_sel_ex_o', 'ibex_pkg::md_op_e', 'multdiv_operator_ex_o', 'multdiv_signed_mode_ex_o', 'multdiv_operand_a_ex_o', 'multdiv_operand_b_ex_o', 'multdiv_ready_id_o', 'csr_access_o', 'ibex_pkg::csr_op_e', 'csr_op_o', 'ibex_pkg::csr_num_e', 'csr_addr_o', 'csr_op_en_o', 'csr_save_if_o', 'csr_save_id_o', 'csr_save_wb_o', 'csr_restore_mret_id_o', 'csr_restore_dret_id_o', 'csr_save_cause_o', 'csr_mtval_o', 'ibex_pkg::priv_lvl_e', 'priv_mode_i', 'csr_mstatus_tw_i', 'illegal_csr_insn_i', 'data_ind_timing_i', 'lsu_req_o', 'lsu_we_o', 'lsu_type_o', 'lsu_sign_ext_o', 'lsu_wdata_o', 'lsu_req_done_i', 'lsu_addr_incr_req_i', 'lsu_addr_last_i', 'csr_mstatus_mie_i', 'irq_pending_i', 'ibex_pkg::irqs_t', 'irqs_i', 'irq_nm_i', 'nmi_mode_o', 'lsu_load_err_i', 'lsu_load_resp_intg_err_i', 'lsu_store_err_i', 'lsu_store_resp_intg_err_i', 'expecting_load_resp_o', 'expecting_store_resp_o', 'debug_mode_o', 'debug_mode_entering_o', 'ibex_pkg::dbg_cause_e', 'debug_cause_o', 'debug_csr_save_o', 'debug_req_i', 'debug_single_step_i', 'debug_ebreakm_i', 'debug_ebreaku_i', 'trigger_match_i', 'result_ex_i', 'csr_rdata_i', 'rf_raddr_a_o', 'rf_rdata_a_i', 'rf_raddr_b_o', 'rf_rdata_b_i', 'rf_ren_a_o', 'rf_ren_b_o', 'rf_waddr_id_o', 'rf_wdata_id_o', 'rf_we_id_o', 'rf_rd_a_wb_match_o', 'rf_rd_b_wb_match_o', 'rf_waddr_wb_i', 'rf_wdata_fwd_wb_i', 'rf_write_wb_i', 'en_wb_o', 'ibex_pkg::wb_instr_type_e', 'instr_type_wb_o', 'instr_perf_count_id_o', 'ready_wb_i', 'outstanding_load_wb_i', 'outstanding_store_wb_i', 'perf_jump_o', 'perf_branch_o', 'perf_tbranch_o', 'perf_dside_wait_o', 'perf_mul_wait_o', 'perf_div_wait_o', 'instr_id_done_o', ')'],
            'outputs': ['ctrl_busy_o', 'illegal_insn_o', 'instr_valid_i', 'instr_rdata_i', 'instr_rdata_alu_i', 'instr_rdata_c_i', 'instr_is_compressed_i', 'instr_bp_taken_i', 'instr_req_o', 'instr_first_cycle_id_o', 'instr_valid_clear_o', 'id_in_ready_o', 'instr_exec_i', 'icache_inval_o', 'branch_decision_i', 'pc_set_o', 'ibex_pkg::pc_sel_e', 'pc_mux_o', 'nt_branch_mispredict_o', 'nt_branch_addr_o', 'ibex_pkg::exc_pc_sel_e', 'exc_pc_mux_o', 'ibex_pkg::exc_cause_t', 'exc_cause_o', 'illegal_c_insn_i', 'instr_fetch_err_i', 'instr_fetch_err_plus2_i', 'pc_id_i', 'ex_valid_i', 'lsu_resp_valid_i', 'ibex_pkg::alu_op_e', 'alu_operator_ex_o', 'alu_operand_a_ex_o', 'alu_operand_b_ex_o', 'imd_val_we_ex_i', 'bt_a_operand_o', 'bt_b_operand_o', 'mult_en_ex_o', 'div_en_ex_o', 'mult_sel_ex_o', 'div_sel_ex_o', 'ibex_pkg::md_op_e', 'multdiv_operator_ex_o', 'multdiv_signed_mode_ex_o', 'multdiv_operand_a_ex_o', 'multdiv_operand_b_ex_o', 'multdiv_ready_id_o', 'csr_access_o', 'ibex_pkg::csr_op_e', 'csr_op_o', 'ibex_pkg::csr_num_e', 'csr_addr_o', 'csr_op_en_o', 'csr_save_if_o', 'csr_save_id_o', 'csr_save_wb_o', 'csr_restore_mret_id_o', 'csr_restore_dret_id_o', 'csr_save_cause_o', 'csr_mtval_o', 'ibex_pkg::priv_lvl_e', 'priv_mode_i', 'csr_mstatus_tw_i', 'illegal_csr_insn_i', 'data_ind_timing_i', 'lsu_req_o', 'lsu_we_o', 'lsu_type_o', 'lsu_sign_ext_o', 'lsu_wdata_o', 'lsu_req_done_i', 'lsu_addr_incr_req_i', 'lsu_addr_last_i', 'csr_mstatus_mie_i', 'irq_pending_i', 'ibex_pkg::irqs_t', 'irqs_i', 'irq_nm_i', 'nmi_mode_o', 'lsu_load_err_i', 'lsu_load_resp_intg_err_i', 'lsu_store_err_i', 'lsu_store_resp_intg_err_i', 'expecting_load_resp_o', 'expecting_store_resp_o', 'debug_mode_o', 'debug_mode_entering_o', 'ibex_pkg::dbg_cause_e', 'debug_cause_o', 'debug_csr_save_o', 'debug_req_i', 'debug_single_step_i', 'debug_ebreakm_i', 'debug_ebreaku_i', 'trigger_match_i', 'result_ex_i', 'csr_rdata_i', 'rf_raddr_a_o', 'rf_rdata_a_i', 'rf_raddr_b_o', 'rf_rdata_b_i', 'rf_ren_a_o', 'rf_ren_b_o', 'rf_waddr_id_o', 'rf_wdata_id_o', 'rf_we_id_o', 'rf_rd_a_wb_match_o', 'rf_rd_b_wb_match_o', 'rf_waddr_wb_i', 'rf_wdata_fwd_wb_i', 'rf_write_wb_i', 'en_wb_o', 'ibex_pkg::wb_instr_type_e', 'instr_type_wb_o', 'instr_perf_count_id_o', 'ready_wb_i', 'outstanding_load_wb_i', 'outstanding_store_wb_i', 'perf_jump_o', 'perf_branch_o', 'perf_tbranch_o', 'perf_dside_wait_o', 'perf_mul_wait_o', 'perf_div_wait_o', 'instr_id_done_o', ')'],
            'internals': []
        },
        'ibex_if_stage': {
            'inputs': ['clk_i', 'rst_ni', 'boot_addr_i', 'req_i', 'instr_req_o', 'instr_addr_o', 'instr_gnt_i', 'instr_rvalid_i', 'instr_rdata_i', 'instr_bus_err_i', 'instr_intg_err_o', 'ic_tag_req_o', 'ic_tag_write_o', 'ic_tag_addr_o', 'ic_tag_wdata_o', 'ic_tag_rdata_i', 'ic_data_req_o', 'ic_data_write_o', 'ic_data_addr_o', 'ic_data_wdata_o', 'ic_data_rdata_i', 'ic_scr_key_valid_i', 'ic_scr_key_req_o', 'instr_valid_id_o', 'instr_new_id_o', 'instr_rdata_id_o', 'instr_rdata_alu_id_o', 'instr_rdata_c_id_o', 'instr_is_compressed_id_o', 'instr_exp_e', 'instr_gets_expanded_id_o', 'instr_expanded_id_o', 'instr_bp_taken_o', 'instr_fetch_err_o', 'instr_fetch_err_plus2_o', 'illegal_c_insn_id_o', 'dummy_instr_id_o', 'pc_if_o', 'pc_id_o', 'pmp_err_if_i', 'pmp_err_if_plus2_i', 'instr_valid_clear_i', 'pc_set_i', 'pc_sel_e', 'pc_mux_i', 'nt_branch_mispredict_i', 'nt_branch_addr_i', 'exc_pc_sel_e', 'exc_pc_mux_i', 'exc_cause_t', 'exc_cause', 'dummy_instr_en_i', 'dummy_instr_mask_i', 'dummy_instr_seed_en_i', 'dummy_instr_seed_i', 'icache_enable_i', 'icache_inval_i', 'icache_ecc_error_o', 'branch_target_ex_i', 'csr_mepc_i', 'csr_depc_i', 'csr_mtvec_i', 'csr_mtvec_init_o', 'id_in_ready_i', 'pc_mismatch_alert_o', 'if_busy_o', ')', '=', 'ic_tag_rdata_i', '=', 'ic_data_rdata_i'],
            'outputs': ['instr_req_o', 'instr_addr_o', 'instr_gnt_i', 'instr_rvalid_i', 'instr_rdata_i', 'instr_bus_err_i', 'instr_intg_err_o', 'ic_tag_req_o', 'ic_tag_write_o', 'ic_tag_addr_o', 'ic_tag_wdata_o', 'ic_tag_rdata_i', 'ic_data_req_o', 'ic_data_write_o', 'ic_data_addr_o', 'ic_data_wdata_o', 'ic_data_rdata_i', 'ic_scr_key_valid_i', 'ic_scr_key_req_o', 'instr_valid_id_o', 'instr_new_id_o', 'instr_rdata_id_o', 'instr_rdata_alu_id_o', 'instr_rdata_c_id_o', 'instr_is_compressed_id_o', 'instr_exp_e', 'instr_gets_expanded_id_o', 'instr_expanded_id_o', 'instr_bp_taken_o', 'instr_fetch_err_o', 'instr_fetch_err_plus2_o', 'illegal_c_insn_id_o', 'dummy_instr_id_o', 'pc_if_o', 'pc_id_o', 'pmp_err_if_i', 'pmp_err_if_plus2_i', 'instr_valid_clear_i', 'pc_set_i', 'pc_sel_e', 'pc_mux_i', 'nt_branch_mispredict_i', 'nt_branch_addr_i', 'exc_pc_sel_e', 'exc_pc_mux_i', 'exc_cause_t', 'exc_cause', 'dummy_instr_en_i', 'dummy_instr_mask_i', 'dummy_instr_seed_en_i', 'dummy_instr_seed_i', 'icache_enable_i', 'icache_inval_i', 'icache_ecc_error_o', 'branch_target_ex_i', 'csr_mepc_i', 'csr_depc_i', 'csr_mtvec_i', 'csr_mtvec_init_o', 'id_in_ready_i', 'pc_mismatch_alert_o', 'if_busy_o', ')', 'val)', 'nonce)'],
            'internals': []
        },
        'ibex_load_store_unit': {
            'inputs': ['clk_i', 'rst_ni', 'data_req_o', 'data_gnt_i', 'data_rvalid_i', 'data_bus_err_i', 'data_pmp_err_i', 'data_addr_o', 'data_we_o', 'data_be_o', 'data_wdata_o', 'data_rdata_i', 'lsu_we_i', 'lsu_type_i', 'lsu_wdata_i', 'lsu_sign_ext_i', 'lsu_rdata_o', 'lsu_rdata_valid_o', 'lsu_req_i', 'adder_result_ex_i', 'addr_incr_req_o', 'addr_last_o', 'lsu_req_done_o', 'lsu_resp_valid_o', 'load_err_o', 'load_resp_intg_err_o', 'store_err_o', 'store_resp_intg_err_o', 'busy_o', 'perf_load_o', 'perf_store_o', ')'],
            'outputs': ['data_req_o', 'data_gnt_i', 'data_rvalid_i', 'data_bus_err_i', 'data_pmp_err_i', 'data_addr_o', 'data_we_o', 'data_be_o', 'data_wdata_o', 'data_rdata_i', 'lsu_we_i', 'lsu_type_i', 'lsu_wdata_i', 'lsu_sign_ext_i', 'lsu_rdata_o', 'lsu_rdata_valid_o', 'lsu_req_i', 'adder_result_ex_i', 'addr_incr_req_o', 'addr_last_o', 'lsu_req_done_o', 'lsu_resp_valid_o', 'load_err_o', 'load_resp_intg_err_o', 'store_err_o', 'store_resp_intg_err_o', 'busy_o', 'perf_load_o', 'perf_store_o', ')'],
            'internals': []
        },
        'ibex_multdiv_fast': {
            'inputs': ['clk_i', 'rst_ni', 'mult_en_i', 'div_en_i', 'mult_sel_i', 'div_sel_i', 'ibex_pkg::md_op_e', 'operator_i', 'signed_mode_i', 'op_a_i', 'op_b_i', 'alu_adder_ext_i', 'alu_adder_i', 'equal_to_zero_i', 'data_ind_timing_i', 'alu_operand_a_o', 'alu_operand_b_o', 'imd_val_we_o', 'multdiv_ready_id_i', 'multdiv_result_o', 'valid_o', ')'],
            'outputs': ['alu_operand_a_o', 'alu_operand_b_o', 'imd_val_we_o', 'multdiv_ready_id_i', 'multdiv_result_o', 'valid_o', ')'],
            'internals': []
        },
        'ibex_multdiv_slow': {
            'inputs': ['clk_i', 'rst_ni', 'mult_en_i', 'div_en_i', 'mult_sel_i', 'div_sel_i', 'ibex_pkg::md_op_e', 'operator_i', 'signed_mode_i', 'op_a_i', 'op_b_i', 'alu_adder_ext_i', 'alu_adder_i', 'equal_to_zero_i', 'data_ind_timing_i', 'alu_operand_a_o', 'alu_operand_b_o', 'imd_val_we_o', 'multdiv_ready_id_i', 'multdiv_result_o', 'valid_o', ')'],
            'outputs': ['alu_operand_a_o', 'alu_operand_b_o', 'imd_val_we_o', 'multdiv_ready_id_i', 'multdiv_result_o', 'valid_o', ')'],
            'internals': []
        },
        'ibex_pmp': {
            'inputs': ['ibex_pkg::pmp_cfg_t', 'csr_pmp_cfg_i', 'csr_pmp_addr_i', 'ibex_pkg::pmp_mseccfg_t', 'csr_pmp_mseccfg_i', 'debug_mode_i', 'ibex_pkg::priv_lvl_e', 'priv_mode_i', 'pmp_req_addr_i', 'ibex_pkg::pmp_req_e', 'pmp_req_type_i', 'pmp_req_err_o', ')'],
            'outputs': ['pmp_req_err_o', ')'],
            'internals': []
        },
        'ibex_prefetch_buffer': {
            'inputs': ['clk_i', 'rst_ni', 'req_i', 'branch_i', 'addr_i', 'ready_i', 'valid_o', 'rdata_o', 'addr_o', 'err_o', 'err_plus2_o', 'instr_req_o', 'instr_gnt_i', 'instr_addr_o', 'instr_rdata_i', 'instr_err_i', 'instr_rvalid_i', 'busy_o', ')'],
            'outputs': ['valid_o', 'rdata_o', 'addr_o', 'err_o', 'err_plus2_o', 'instr_req_o', 'instr_gnt_i', 'instr_addr_o', 'instr_rdata_i', 'instr_err_i', 'instr_rvalid_i', 'busy_o', ')'],
            'internals': []
        },
        'ibex_register_file_ff': {
            'inputs': ['clk_i', 'rst_ni', 'test_en_i', 'dummy_instr_id_i', 'dummy_instr_wb_i', 'raddr_a_i', 'rdata_a_o', 'raddr_b_i', 'rdata_b_o', 'waddr_a_i', 'wdata_a_i', 'we_a_i', 'err_o', ')'],
            'outputs': ['rdata_a_o', 'raddr_b_i', 'rdata_b_o', 'waddr_a_i', 'wdata_a_i', 'we_a_i', 'err_o', ')'],
            'internals': []
        },
        'ibex_register_file_fpga': {
            'inputs': ['clk_i', 'rst_ni', 'test_en_i', 'dummy_instr_id_i', 'dummy_instr_wb_i', 'raddr_a_i', 'rdata_a_o', 'raddr_b_i', 'rdata_b_o', 'waddr_a_i', 'wdata_a_i', 'we_a_i', 'err_o', ')'],
            'outputs': ['rdata_a_o', 'raddr_b_i', 'rdata_b_o', 'waddr_a_i', 'wdata_a_i', 'we_a_i', 'err_o', ')'],
            'internals': []
        },
        'ibex_register_file_latch': {
            'inputs': ['clk_i', 'rst_ni', 'test_en_i', 'dummy_instr_id_i', 'dummy_instr_wb_i', 'raddr_a_i', 'rdata_a_o', 'raddr_b_i', 'rdata_b_o', 'waddr_a_i', 'wdata_a_i', 'we_a_i', 'err_o', ')'],
            'outputs': ['rdata_a_o', 'raddr_b_i', 'rdata_b_o', 'waddr_a_i', 'wdata_a_i', 'we_a_i', 'err_o', ')'],
            'internals': []
        },
        'ibex_tracer': {
            'inputs': ['clk_i', 'rst_ni', 'hart_id_i', 'rvfi_valid', 'rvfi_order', 'rvfi_insn', 'rvfi_trap', 'rvfi_halt', 'rvfi_intr', 'rvfi_mode', 'rvfi_ixl', 'rvfi_rs1_addr', 'rvfi_rs2_addr', 'rvfi_rs3_addr', 'rvfi_rs1_rdata', 'rvfi_rs2_rdata', 'rvfi_rs3_rdata', 'rvfi_rd_addr', 'rvfi_rd_wdata', 'rvfi_pc_rdata', 'rvfi_pc_wdata', 'rvfi_mem_addr', 'rvfi_mem_rmask', 'rvfi_mem_wmask', 'rvfi_mem_rdata', 'rvfi_mem_wdata', 'rvfi_ext_expanded_insn_valid', 'rvfi_ext_expanded_insn', ')', 'addr)', 'addr)', 'csr_addr)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'string', 'mnemonic)', 'addr)', 'string', 'mnemonic)', 'string', 'mnemonic)'],
            'outputs': [],
            'internals': []
        },
        'ibex_wb_stage': {
            'inputs': ['clk_i', 'rst_ni', 'en_wb_i', 'ibex_pkg::wb_instr_type_e', 'instr_type_wb_i', 'pc_id_i', 'instr_is_compressed_id_i', 'instr_perf_count_id_i', 'ready_wb_o', 'rf_write_wb_o', 'outstanding_load_wb_o', 'outstanding_store_wb_o', 'pc_wb_o', 'perf_instr_ret_wb_o', 'perf_instr_ret_compressed_wb_o', 'perf_instr_ret_wb_spec_o', 'perf_instr_ret_compressed_wb_spec_o', 'rf_waddr_id_i', 'rf_wdata_id_i', 'rf_we_id_i', 'dummy_instr_id_i', 'rf_wdata_lsu_i', 'rf_we_lsu_i', 'rf_wdata_fwd_wb_o', 'rf_waddr_wb_o', 'rf_wdata_wb_o', 'rf_we_wb_o', 'dummy_instr_wb_o', 'lsu_resp_valid_i', 'lsu_resp_err_i', 'instr_done_wb_o', ')'],
            'outputs': ['ready_wb_o', 'rf_write_wb_o', 'outstanding_load_wb_o', 'outstanding_store_wb_o', 'pc_wb_o', 'perf_instr_ret_wb_o', 'perf_instr_ret_compressed_wb_o', 'perf_instr_ret_wb_spec_o', 'perf_instr_ret_compressed_wb_spec_o', 'rf_waddr_id_i', 'rf_wdata_id_i', 'rf_we_id_i', 'dummy_instr_id_i', 'rf_wdata_lsu_i', 'rf_we_lsu_i', 'rf_wdata_fwd_wb_o', 'rf_waddr_wb_o', 'rf_wdata_wb_o', 'rf_we_wb_o', 'dummy_instr_wb_o', 'lsu_resp_valid_i', 'lsu_resp_err_i', 'instr_done_wb_o', ')'],
            'internals': []
        },
        'instantiates': {
            'inputs': ['clk_i', 'rst_ni', 'hart_id_i', 'boot_addr_i', 'instr_req_i', 'instr_gnt_i', 'instr_rvalid_i', 'instr_addr_i', 'instr_rdata_i', 'instr_err_i', 'data_req_i', 'data_gnt_i', 'data_rvalid_i', 'data_we_i', 'data_be_i', 'data_addr_i', 'data_wdata_i', 'data_rdata_i', 'data_err_i', 'dummy_instr_id_i', 'dummy_instr_wb_i', 'rf_raddr_a_i', 'rf_raddr_b_i', 'rf_waddr_wb_i', 'rf_we_wb_i', 'rf_wdata_wb_ecc_i', 'rf_rdata_a_ecc_i', 'rf_rdata_b_ecc_i', 'ic_tag_req_i', 'ic_tag_write_i', 'ic_tag_addr_i', 'ic_tag_wdata_i', 'ic_tag_rdata_i', 'ic_data_req_i', 'ic_data_write_i', 'ic_data_addr_i', 'ic_data_wdata_i', 'ic_data_rdata_i', 'ic_scr_key_valid_i', 'ic_scr_key_req_i', 'irq_software_i', 'irq_timer_i', 'irq_external_i', 'irq_fast_i', 'irq_nm_i', 'irq_pending_i', 'debug_req_i', 'crash_dump_t', 'crash_dump_i', 'double_fault_seen_i', 'ibex_mubi_t', 'fetch_enable_i', 'alert_minor_o', 'alert_major_internal_o', 'alert_major_bus_o', 'ibex_mubi_t', 'core_busy_i', 'test_en_i', 'scan_rst_ni', ')'],
            'outputs': ['alert_minor_o', 'alert_major_internal_o', 'alert_major_bus_o', 'ibex_mubi_t', 'core_busy_i', 'test_en_i', 'scan_rst_ni', ')'],
            'internals': []
        },
        'is': {
            'inputs': ['clk_i', 'rst_ni', 'illegal_insn_o', 'ebrk_insn_o', 'mret_insn_o', 'dret_insn_o', 'ecall_insn_o', 'wfi_insn_o', 'jump_set_o', 'branch_taken_i', 'icache_inval_o', 'instr_first_cycle_i', 'instr_rdata_i', 'instr_rdata_alu_i', 'illegal_c_insn_i', 'ibex_pkg::imm_a_sel_e', 'imm_a_mux_sel_o', 'ibex_pkg::imm_b_sel_e', 'imm_b_mux_sel_o', 'ibex_pkg::op_a_sel_e', 'bt_a_mux_sel_o', 'ibex_pkg::imm_b_sel_e', 'bt_b_mux_sel_o', 'imm_i_type_o', 'imm_s_type_o', 'imm_b_type_o', 'imm_u_type_o', 'imm_j_type_o', 'zimm_rs1_type_o', 'ibex_pkg::rf_wd_sel_e', 'rf_wdata_sel_o', 'rf_we_o', 'rf_raddr_a_o', 'rf_raddr_b_o', 'rf_waddr_o', 'rf_ren_a_o', 'rf_ren_b_o', 'ibex_pkg::alu_op_e', 'alu_operator_o', 'ibex_pkg::op_a_sel_e', 'alu_op_a_mux_sel_o', 'ibex_pkg::op_b_sel_e', 'alu_op_b_mux_sel_o', 'alu_multicycle_o', 'mult_en_o', 'div_en_o', 'mult_sel_o', 'div_sel_o', 'ibex_pkg::md_op_e', 'multdiv_operator_o', 'multdiv_signed_mode_o', 'csr_access_o', 'ibex_pkg::csr_op_e', 'csr_op_o', 'ibex_pkg::csr_num_e', 'csr_addr_o', 'data_req_o', 'data_we_o', 'data_type_o', 'data_sign_extension_o', 'jump_in_dec_o', 'branch_in_dec_o', ')'],
            'outputs': ['illegal_insn_o', 'ebrk_insn_o', 'mret_insn_o', 'dret_insn_o', 'ecall_insn_o', 'wfi_insn_o', 'jump_set_o', 'branch_taken_i', 'icache_inval_o', 'instr_first_cycle_i', 'instr_rdata_i', 'instr_rdata_alu_i', 'illegal_c_insn_i', 'ibex_pkg::imm_a_sel_e', 'imm_a_mux_sel_o', 'ibex_pkg::imm_b_sel_e', 'imm_b_mux_sel_o', 'ibex_pkg::op_a_sel_e', 'bt_a_mux_sel_o', 'ibex_pkg::imm_b_sel_e', 'bt_b_mux_sel_o', 'imm_i_type_o', 'imm_s_type_o', 'imm_b_type_o', 'imm_u_type_o', 'imm_j_type_o', 'zimm_rs1_type_o', 'ibex_pkg::rf_wd_sel_e', 'rf_wdata_sel_o', 'rf_we_o', 'rf_raddr_a_o', 'rf_raddr_b_o', 'rf_waddr_o', 'rf_ren_a_o', 'rf_ren_b_o', 'ibex_pkg::alu_op_e', 'alu_operator_o', 'ibex_pkg::op_a_sel_e', 'alu_op_a_mux_sel_o', 'ibex_pkg::op_b_sel_e', 'alu_op_b_mux_sel_o', 'alu_multicycle_o', 'mult_en_o', 'div_en_o', 'mult_sel_o', 'div_sel_o', 'ibex_pkg::md_op_e', 'multdiv_operator_o', 'multdiv_signed_mode_o', 'csr_access_o', 'ibex_pkg::csr_op_e', 'csr_op_o', 'ibex_pkg::csr_num_e', 'csr_addr_o', 'data_req_o', 'data_we_o', 'data_type_o', 'data_sign_extension_o', 'jump_in_dec_o', 'branch_in_dec_o', ')'],
            'internals': []
        },
        'of': {
            'inputs': ['clk_i', 'rst_ni', 'test_en_i', 'scan_rst_ni', 'prim_ram_1p_pkg::ram_1p_cfg_t', 'ram_cfg_icache_tag_i', 'prim_ram_1p_pkg::ram_1p_cfg_rsp_t', 'ram_cfg_rsp_icache_tag_o', 'prim_ram_1p_pkg::ram_1p_cfg_t', 'ram_cfg_icache_data_i', 'prim_ram_1p_pkg::ram_1p_cfg_rsp_t', 'ram_cfg_rsp_icache_data_o', 'hart_id_i', 'boot_addr_i', 'instr_req_o', 'instr_gnt_i', 'instr_rvalid_i', 'instr_addr_o', 'instr_rdata_i', 'instr_rdata_intg_i', 'instr_err_i', 'data_req_o', 'data_gnt_i', 'data_rvalid_i', 'data_we_o', 'data_be_o', 'data_addr_o', 'data_wdata_o', 'data_wdata_intg_o', 'data_rdata_i', 'data_rdata_intg_i', 'data_err_i', 'irq_software_i', 'irq_timer_i', 'irq_external_i', 'irq_fast_i', 'irq_nm_i', 'scramble_key_valid_i', 'scramble_key_i', 'scramble_nonce_i', 'scramble_req_o', 'debug_req_i', 'crash_dump_t', 'crash_dump_o', 'double_fault_seen_o', 'ibex_mubi_t', 'fetch_enable_i', 'alert_minor_o', 'alert_major_internal_o', 'alert_major_bus_o', 'core_sleep_o', ')'],
            'outputs': ['prim_ram_1p_pkg::ram_1p_cfg_rsp_t', 'ram_cfg_rsp_icache_tag_o', 'prim_ram_1p_pkg::ram_1p_cfg_t', 'ram_cfg_icache_data_i', 'prim_ram_1p_pkg::ram_1p_cfg_rsp_t', 'ram_cfg_rsp_icache_data_o', 'hart_id_i', 'boot_addr_i', 'instr_req_o', 'instr_gnt_i', 'instr_rvalid_i', 'instr_addr_o', 'instr_rdata_i', 'instr_rdata_intg_i', 'instr_err_i', 'data_req_o', 'data_gnt_i', 'data_rvalid_i', 'data_we_o', 'data_be_o', 'data_addr_o', 'data_wdata_o', 'data_wdata_intg_o', 'data_rdata_i', 'data_rdata_intg_i', 'data_err_i', 'irq_software_i', 'irq_timer_i', 'irq_external_i', 'irq_fast_i', 'irq_nm_i', 'scramble_key_valid_i', 'scramble_key_i', 'scramble_nonce_i', 'scramble_req_o', 'debug_req_i', 'crash_dump_t', 'crash_dump_o', 'double_fault_seen_o', 'ibex_mubi_t', 'fetch_enable_i', 'alert_minor_o', 'alert_major_internal_o', 'alert_major_bus_o', 'core_sleep_o', ')'],
            'internals': []
        },
    },
    
# Copy this into classify_signals.py PROCESSOR_SIGNALS dict

    'CVA6': {
        'acc_dispatcher': {
            'inputs': ['clk_i', 'rst_ni', 'acc_cons_en_i', 'acc_fflags_valid_o', 'acc_fflags_o', 'priv_lvl_t', 'ld_st_priv_lvl_i', 'sum_i', 'pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', 'fcsr_frm_i', 'dirty_v_state_o', 'acc_mmu_en_i', 'scoreboard_entry_t', 'issue_instr_i', 'issue_instr_hs_i', 'issue_stall_o', 'fu_data_t', 'fu_data_i', 'scoreboard_entry_t', 'commit_instr_i', 'acc_trans_id_o', 'acc_result_o', 'acc_valid_o', 'exception_t', 'acc_exception_o', 'acc_valid_ex_o', 'commit_ack_i', 'commit_st_barrier_i', 'acc_stall_st_pending_o', 'acc_no_st_pending_i', 'dcache_req_i_t', 'dcache_req_ports_i', 'acc_mmu_req_t', 'acc_mmu_req_o', 'acc_mmu_resp_t', 'acc_mmu_resp_i', 'ctrl_halt_o', 'csr_addr_i', 'flush_unissued_instr_i', 'flush_ex_i', 'flush_pipeline_o', 'single_step_o', 'dcache_req_i_t', 'acc_dcache_req_ports_o', 'dcache_req_o_t', 'acc_dcache_req_ports_i', 'inval_ready_i', 'inval_valid_o', 'inval_addr_o', 'acc_req_t', 'acc_req_o', 'acc_resp_t', 'acc_resp_i', ')'],
            'outputs': ['acc_fflags_valid_o', 'acc_fflags_o', 'priv_lvl_t', 'ld_st_priv_lvl_i', 'sum_i', 'pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', 'fcsr_frm_i', 'dirty_v_state_o', 'acc_mmu_en_i', 'scoreboard_entry_t', 'issue_instr_i', 'issue_instr_hs_i', 'issue_stall_o', 'fu_data_t', 'fu_data_i', 'scoreboard_entry_t', 'commit_instr_i', 'acc_trans_id_o', 'acc_result_o', 'acc_valid_o', 'exception_t', 'acc_exception_o', 'acc_valid_ex_o', 'commit_ack_i', 'commit_st_barrier_i', 'acc_stall_st_pending_o', 'acc_no_st_pending_i', 'dcache_req_i_t', 'dcache_req_ports_i', 'acc_mmu_req_t', 'acc_mmu_req_o', 'acc_mmu_resp_t', 'acc_mmu_resp_i', 'ctrl_halt_o', 'csr_addr_i', 'flush_unissued_instr_i', 'flush_ex_i', 'flush_pipeline_o', 'single_step_o', 'dcache_req_i_t', 'acc_dcache_req_ports_o', 'dcache_req_o_t', 'acc_dcache_req_ports_i', 'inval_ready_i', 'inval_valid_o', 'inval_addr_o', 'acc_req_t', 'acc_req_o', 'acc_resp_t', 'acc_resp_i', ')'],
            'internals': []
        },
        'aes': {
            'inputs': ['clk_i', 'rst_ni', 'fu_data_t', 'fu_data_i', 'orig_instr_aes', 'result_o', ')'],
            'outputs': ['result_o', ')'],
            'internals': []
        },
        'alu': {
            'inputs': ['clk_i', 'rst_ni', 'fu_data_t', 'fu_data_i', 'fu_data_t', 'fu_data_cpop_i', 'result_o', 'alu_branch_res_o', ')'],
            'outputs': ['result_o', 'alu_branch_res_o', ')'],
            'internals': []
        },
        'alu_wrapper': {
            'inputs': ['clk_i', 'rst_ni', 'alu_bypass_t', 'alu_bypass_i', 'fu_data_t', 'fu_data_i', 'result_o', 'alu_branch_res_o', ')'],
            'outputs': ['result_o', 'alu_branch_res_o', ')'],
            'internals': []
        },
        'amo_alu': {
            'inputs': ['ariane_pkg::amo_t', 'amo_op_i', 'amo_operand_a_i', 'amo_operand_b_i', 'amo_result_o', ')'],
            'outputs': ['amo_result_o', ')'],
            'internals': []
        },
        'amo_buffer': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'valid_i', 'ready_o', 'ariane_pkg::amo_t', 'amo_op_i', 'paddr_i', 'data_i', 'data_size_i', 'ariane_pkg::amo_req_t', 'amo_req_o', 'ariane_pkg::amo_resp_t', 'amo_resp_i', 'amo_valid_commit_i', 'no_st_pending_i', ')'],
            'outputs': ['ready_o', 'ariane_pkg::amo_t', 'amo_op_i', 'paddr_i', 'data_i', 'data_size_i', 'ariane_pkg::amo_req_t', 'amo_req_o', 'ariane_pkg::amo_resp_t', 'amo_resp_i', 'amo_valid_commit_i', 'no_st_pending_i', ')'],
            'internals': []
        },
        'ariane_regfile': {
            'inputs': ['clk_i', 'rst_ni', 'test_en_i', 'raddr_i', 'rdata_o', 'waddr_i', 'wdata_i', 'we_i', ')'],
            'outputs': ['rdata_o', 'waddr_i', 'wdata_i', 'we_i', ')'],
            'internals': []
        },
        'ariane_regfile_fpga': {
            'inputs': ['clk_i', 'rst_ni', 'test_en_i', 'raddr_i', 'rdata_o', 'waddr_i', 'wdata_i', 'we_i', ')'],
            'outputs': ['rdata_o', 'waddr_i', 'wdata_i', 'we_i', ')'],
            'internals': []
        },
        'axi_adapter': {
            'inputs': ['clk_i', 'rst_ni', 'req_i', 'ariane_pkg::ad_req_t', 'type_i', 'ariane_pkg::amo_t', 'amo_i', 'gnt_o', 'addr_i', 'we_i', 'wdata_i', 'be_i', 'size_i', 'id_i', 'valid_o', 'rdata_o', 'id_o', 'critical_word_o', 'critical_word_valid_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'outputs': ['gnt_o', 'addr_i', 'we_i', 'wdata_i', 'be_i', 'size_i', 'id_i', 'valid_o', 'rdata_o', 'id_o', 'critical_word_o', 'critical_word_valid_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'internals': []
        },
        'axi_shim': {
            'inputs': ['clk_i', 'rst_ni', 'rd_req_i', 'rd_gnt_o', 'rd_addr_i', 'rd_blen_i', 'rd_size_i', 'rd_id_i', 'rd_lock_i', 'rd_rdy_i', 'rd_last_o', 'rd_valid_o', 'rd_data_o', 'rd_user_o', 'rd_id_o', 'rd_exokay_o', 'wr_req_i', 'wr_gnt_o', 'wr_addr_i', 'wr_data_i', 'wr_user_i', 'wr_be_i', 'wr_blen_i', 'wr_size_i', 'wr_id_i', 'wr_lock_i', 'wr_atop_i', 'wr_rdy_i', 'wr_valid_o', 'wr_id_o', 'wr_exokay_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'outputs': ['rd_gnt_o', 'rd_addr_i', 'rd_blen_i', 'rd_size_i', 'rd_id_i', 'rd_lock_i', 'rd_rdy_i', 'rd_last_o', 'rd_valid_o', 'rd_data_o', 'rd_user_o', 'rd_id_o', 'rd_exokay_o', 'wr_req_i', 'wr_gnt_o', 'wr_addr_i', 'wr_data_i', 'wr_user_i', 'wr_be_i', 'wr_blen_i', 'wr_size_i', 'wr_id_i', 'wr_lock_i', 'wr_atop_i', 'wr_rdy_i', 'wr_valid_o', 'wr_id_o', 'wr_exokay_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'internals': []
        },
        'bht': {
            'inputs': ['clk_i', 'rst_ni', 'flush_bp_i', 'debug_mode_i', 'vpc_i', 'bht_update_t', 'bht_update_i', 'ariane_pkg::bht_prediction_t', 'bht_prediction_o', ')'],
            'outputs': ['ariane_pkg::bht_prediction_t', 'bht_prediction_o', ')', 'assign', '='],
            'internals': []
        },
        'bht2lvl': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'vpc_i', 'bht_update_t', 'bht_update_i', 'ariane_pkg::bht_prediction_t', 'bht_prediction_o', ')'],
            'outputs': ['ariane_pkg::bht_prediction_t', 'bht_prediction_o', ')', 'assign', '='],
            'internals': []
        },
        'branch_unit': {
            'inputs': ['clk_i', 'rst_ni', 'v_i', 'debug_mode_i', 'fu_data_t', 'fu_data_i', 'pc_i', 'is_zcmt_i', 'is_compressed_instr_i', 'branch_valid_i', 'branch_comp_res_i', 'branch_result_o', 'branchpredict_sbe_t', 'branch_predict_i', 'bp_resolve_t', 'resolved_branch_o', 'resolve_branch_o', 'exception_t', 'branch_exception_o', ')'],
            'outputs': ['branch_result_o', 'branchpredict_sbe_t', 'branch_predict_i', 'bp_resolve_t', 'resolved_branch_o', 'resolve_branch_o', 'exception_t', 'branch_exception_o', ')'],
            'internals': []
        },
        'cache_ctrl': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'bypass_i', 'busy_o', 'dcache_req_i_t', 'req_port_i', 'dcache_req_o_t', 'req_port_o', 'req_o', 'addr_o', 'gnt_i', 'cache_line_t', 'data_o', 'cl_be_t', 'be_o', 'tag_o', 'cache_line_t', 'data_i', 'we_o', 'hit_way_i', 'miss_req_t', 'miss_req_o', 'miss_gnt_i', 'active_serving_i', 'critical_word_i', 'critical_word_valid_i', 'bypass_gnt_i', 'bypass_valid_i', 'bypass_data_i', 'mshr_addr_o', 'mshr_addr_matches_i', 'mshr_index_matches_i', ')'],
            'outputs': ['busy_o', 'dcache_req_i_t', 'req_port_i', 'dcache_req_o_t', 'req_port_o', 'req_o', 'addr_o', 'gnt_i', 'cache_line_t', 'data_o', 'cl_be_t', 'be_o', 'tag_o', 'cache_line_t', 'data_i', 'we_o', 'hit_way_i', 'miss_req_t', 'miss_req_o', 'miss_gnt_i', 'active_serving_i', 'critical_word_i', 'critical_word_valid_i', 'bypass_gnt_i', 'bypass_valid_i', 'bypass_data_i', 'mshr_addr_o', 'mshr_addr_matches_i', 'mshr_index_matches_i', ')'],
            'internals': []
        },
        'commit_stage': {
            'inputs': ['clk_i', 'rst_ni', 'halt_i', 'flush_dcache_i', 'exception_t', 'exception_o', 'dirty_fp_state_o', 'single_step_i', 'scoreboard_entry_t', 'commit_instr_i', 'commit_drop_i', 'commit_ack_o', 'commit_macro_ack_o', 'waddr_o', 'wdata_o', 'we_gpr_o', 'we_fpr_o', 'amo_resp_t', 'amo_resp_i', 'pc_o', 'fu_op', 'csr_op_o', 'csr_wdata_o', 'csr_rdata_i', 'csr_write_fflags_o', 'exception_t', 'csr_exception_i', 'commit_lsu_o', 'commit_lsu_ready_i', 'commit_tran_id_o', 'amo_valid_commit_o', 'no_st_pending_i', 'commit_csr_o', 'fence_i_o', 'fence_o', 'flush_commit_o', 'sfence_vma_o', 'hfence_vvma_o', 'hfence_gvma_o', 'break_from_trigger_i', ')'],
            'outputs': ['exception_t', 'exception_o', 'dirty_fp_state_o', 'single_step_i', 'scoreboard_entry_t', 'commit_instr_i', 'commit_drop_i', 'commit_ack_o', 'commit_macro_ack_o', 'waddr_o', 'wdata_o', 'we_gpr_o', 'we_fpr_o', 'amo_resp_t', 'amo_resp_i', 'pc_o', 'fu_op', 'csr_op_o', 'csr_wdata_o', 'csr_rdata_i', 'csr_write_fflags_o', 'exception_t', 'csr_exception_i', 'commit_lsu_o', 'commit_lsu_ready_i', 'commit_tran_id_o', 'amo_valid_commit_o', 'no_st_pending_i', 'commit_csr_o', 'fence_i_o', 'fence_o', 'flush_commit_o', 'sfence_vma_o', 'hfence_vvma_o', 'hfence_gvma_o', 'break_from_trigger_i', ')'],
            'internals': []
        },
        'compressed_instr_decoder': {
            'inputs': ['clk_i', 'rst_ni', 'compressed_valid_i', 'x_compressed_req_t', 'compressed_req_i', 'compressed_ready_o', 'x_compressed_resp_t', 'compressed_resp_o', ')'],
            'outputs': ['compressed_ready_o', 'x_compressed_resp_t', 'compressed_resp_o', ')'],
            'internals': []
        },
        'controller': {
            'inputs': ['clk_i', 'rst_ni', 'v_i', 'set_pc_commit_o', 'flush_if_o', 'flush_unissued_instr_o', 'flush_id_o', 'flush_ex_o', 'flush_bp_o', 'flush_icache_o', 'flush_dcache_o', 'flush_dcache_ack_i', 'flush_tlb_o', 'flush_tlb_vvma_o', 'flush_tlb_gvma_o', 'halt_csr_i', 'halt_acc_i', 'halt_frontend_o', 'halt_o', 'eret_i', 'ex_valid_i', 'set_debug_pc_i', 'bp_resolve_t', 'resolved_branch_i', 'flush_csr_i', 'fence_i_i', 'fence_i', 'sfence_vma_i', 'hfence_vvma_i', 'hfence_gvma_i', 'flush_commit_i', 'flush_acc_i', ')'],
            'outputs': ['set_pc_commit_o', 'flush_if_o', 'flush_unissued_instr_o', 'flush_id_o', 'flush_ex_o', 'flush_bp_o', 'flush_icache_o', 'flush_dcache_o', 'flush_dcache_ack_i', 'flush_tlb_o', 'flush_tlb_vvma_o', 'flush_tlb_gvma_o', 'halt_csr_i', 'halt_acc_i', 'halt_frontend_o', 'halt_o', 'eret_i', 'ex_valid_i', 'set_debug_pc_i', 'bp_resolve_t', 'resolved_branch_i', 'flush_csr_i', 'fence_i_i', 'fence_i', 'sfence_vma_i', 'hfence_vvma_i', 'hfence_gvma_i', 'flush_commit_i', 'flush_acc_i', ')'],
            'internals': []
        },
        'copro_alu': {
            'inputs': ['clk_i', 'rst_ni', 'opcode_t', 'opcode_i', 'hartid_t', 'hartid_i', 'id_t', 'id_i', 'rd_i', 'result_o', 'hartid_t', 'hartid_o', 'id_t', 'id_o', 'rd_o', 'valid_o', 'we_o', ')'],
            'outputs': ['result_o', 'hartid_t', 'hartid_o', 'id_t', 'id_o', 'rd_o', 'valid_o', 'we_o', ')'],
            'internals': []
        },
        'csr_buffer': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'fu_data_t', 'fu_data_i', 'csr_ready_o', 'csr_valid_i', 'csr_result_o', 'csr_commit_i', 'csr_addr_o', ')'],
            'outputs': ['csr_ready_o', 'csr_valid_i', 'csr_result_o', 'csr_commit_i', 'csr_addr_o', ')'],
            'internals': []
        },
        'csr_regfile': {
            'inputs': ['clk_i', 'rst_ni', 'time_irq_i', 'flush_o', 'halt_csr_o', 'scoreboard_entry_t', 'commit_instr_i', 'commit_ack_i', 'boot_addr_i', 'hart_id_i', 'exception_t', 'ex_i', 'fu_op', 'csr_op_i', 'csr_addr_i', 'csr_wdata_i', 'csr_rdata_o', 'dirty_fp_state_i', 'csr_write_fflags_i', 'dirty_v_state_i', 'pc_i', 'exception_t', 'csr_exception_o', 'epc_o', 'eret_o', 'trap_vector_base_o', 'riscv::priv_lvl_t', 'priv_lvl_o', 'v_o', 'acc_fflags_ex_i', 'acc_fflags_ex_valid_i', 'riscv::xs_t', 'fs_o', 'riscv::xs_t', 'vfs_o', 'fflags_o', 'frm_o', 'fprec_o', 'riscv::xs_t', 'vs_o', 'irq_ctrl_t', 'irq_ctrl_o', 'en_translation_o', 'en_g_translation_o', 'en_ld_st_translation_o', 'en_ld_st_g_translation_o', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_o', 'ld_st_v_o', 'csr_hs_ld_st_inst_i', 'sum_o', 'vs_sum_o', 'mxr_o', 'vmxr_o', 'satp_ppn_o', 'asid_o', 'vsatp_ppn_o', 'vs_asid_o', 'hgatp_ppn_o', 'vmid_o', 'irq_i', 'ipi_i', 'debug_req_i', 'set_debug_pc_o', 'tvm_o', 'tw_o', 'vtw_o', 'tsr_o', 'hu_o', 'debug_mode_o', 'single_step_o', 'icache_en_o', 'dcache_en_o', 'acc_cons_en_o', 'perf_addr_o', 'perf_data_o', 'perf_data_i', 'perf_we_o', 'riscv::pmpcfg_t', 'pmpcfg_o', 'pmpaddr_o', 'mcountinhibit_o', 'rvfi_probes_csr_t', 'rvfi_csr_o', 'jvt_t', 'jvt_o', 'debug_from_trigger_o', 'vaddr_from_lsu_i', 'orig_instr_i', 'store_result_i', 'break_from_trigger_o', ')'],
            'outputs': ['flush_o', 'halt_csr_o', 'scoreboard_entry_t', 'commit_instr_i', 'commit_ack_i', 'boot_addr_i', 'hart_id_i', 'exception_t', 'ex_i', 'fu_op', 'csr_op_i', 'csr_addr_i', 'csr_wdata_i', 'csr_rdata_o', 'dirty_fp_state_i', 'csr_write_fflags_i', 'dirty_v_state_i', 'pc_i', 'exception_t', 'csr_exception_o', 'epc_o', 'eret_o', 'trap_vector_base_o', 'riscv::priv_lvl_t', 'priv_lvl_o', 'v_o', 'acc_fflags_ex_i', 'acc_fflags_ex_valid_i', 'riscv::xs_t', 'fs_o', 'riscv::xs_t', 'vfs_o', 'fflags_o', 'frm_o', 'fprec_o', 'riscv::xs_t', 'vs_o', 'irq_ctrl_t', 'irq_ctrl_o', 'en_translation_o', 'en_g_translation_o', 'en_ld_st_translation_o', 'en_ld_st_g_translation_o', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_o', 'ld_st_v_o', 'csr_hs_ld_st_inst_i', 'sum_o', 'vs_sum_o', 'mxr_o', 'vmxr_o', 'satp_ppn_o', 'asid_o', 'vsatp_ppn_o', 'vs_asid_o', 'hgatp_ppn_o', 'vmid_o', 'irq_i', 'ipi_i', 'debug_req_i', 'set_debug_pc_o', 'tvm_o', 'tw_o', 'vtw_o', 'tsr_o', 'hu_o', 'debug_mode_o', 'single_step_o', 'icache_en_o', 'dcache_en_o', 'acc_cons_en_o', 'perf_addr_o', 'perf_data_o', 'perf_data_i', 'perf_we_o', 'riscv::pmpcfg_t', 'pmpcfg_o', 'pmpaddr_o', 'mcountinhibit_o', 'rvfi_probes_csr_t', 'rvfi_csr_o', 'jvt_t', 'jvt_o', 'debug_from_trigger_o', 'vaddr_from_lsu_i', 'orig_instr_i', 'store_result_i', 'break_from_trigger_o', ')', 'trap_vector_base_o', '=', "2'b0}"],
            'internals': []
        },
        'cva6': {
            'inputs': ['clk_i', 'rst_ni', 'boot_addr_i', 'hart_id_i', 'irq_i', 'ipi_i', 'time_irq_i', 'debug_req_i', 'rvfi_probes_t', 'rvfi_probes_o', 'cvxif_req_t', 'cvxif_req_o', 'cvxif_resp_t', 'cvxif_resp_i', 'noc_req_t', 'noc_req_o', 'noc_resp_t', 'noc_resp_i', ')'],
            'outputs': ['rvfi_probes_t', 'rvfi_probes_o', 'cvxif_req_t', 'cvxif_req_o', 'cvxif_resp_t', 'cvxif_resp_i', 'noc_req_t', 'noc_req_o', 'noc_resp_t', 'noc_resp_i', ')'],
            'internals': []
        },
        'cva6_accel_first_pass_decoder': {
            'inputs': ['instruction_i', 'riscv::xs_t', 'fs_i', 'riscv::xs_t', 'vs_i', 'is_accel_o', 'scoreboard_entry_t', 'instruction_o', 'illegal_instr_o', 'is_control_flow_instr_o', ')'],
            'outputs': ['is_accel_o', 'scoreboard_entry_t', 'instruction_o', 'illegal_instr_o', 'is_control_flow_instr_o', ')'],
            'internals': []
        },
        'cva6_fifo_v3': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'testmode_i', 'full_o', 'empty_o', 'usage_o', 'dtype', 'data_i', 'push_i', 'dtype', 'data_o', 'pop_i', ')'],
            'outputs': ['full_o', 'empty_o', 'usage_o', 'dtype', 'data_i', 'push_i', 'dtype', 'data_o', 'pop_i', ')'],
            'internals': []
        },
        'cva6_hpdcache_if_adapter': {
            'inputs': ['clk_i', 'rst_ni', 'hpdcache_req_sid_t', 'hpdcache_req_sid_i', 'dcache_req_i_t', 'cva6_req_i', 'dcache_req_o_t', 'cva6_req_o', 'ariane_pkg::amo_req_t', 'cva6_amo_req_i', 'ariane_pkg::amo_resp_t', 'cva6_amo_resp_o', 'cva6_dcache_flush_i', 'cva6_dcache_flush_ack_o', 'hpdcache_req_valid_o', 'hpdcache_req_ready_i', 'hpdcache_req_t', 'hpdcache_req_o', 'hpdcache_req_abort_o', 'hpdcache_tag_t', 'hpdcache_req_tag_o', 'hpdcache_pkg::hpdcache_pma_t', 'hpdcache_req_pma_o', 'hpdcache_rsp_valid_i', 'hpdcache_rsp_t', 'hpdcache_rsp_i', ')'],
            'outputs': ['dcache_req_o_t', 'cva6_req_o', 'ariane_pkg::amo_req_t', 'cva6_amo_req_i', 'ariane_pkg::amo_resp_t', 'cva6_amo_resp_o', 'cva6_dcache_flush_i', 'cva6_dcache_flush_ack_o', 'hpdcache_req_valid_o', 'hpdcache_req_ready_i', 'hpdcache_req_t', 'hpdcache_req_o', 'hpdcache_req_abort_o', 'hpdcache_tag_t', 'hpdcache_req_tag_o', 'hpdcache_pkg::hpdcache_pma_t', 'hpdcache_req_pma_o', 'hpdcache_rsp_valid_i', 'hpdcache_rsp_t', 'hpdcache_rsp_i', ')'],
            'internals': []
        },
        'cva6_hpdcache_subsystem': {
            'inputs': ['clk_i', 'rst_ni', 'noc_req_t', 'noc_req_o', 'noc_resp_t', 'noc_resp_i', 'icache_en_i', 'icache_flush_i', 'icache_miss_o', 'icache_areq_t', 'icache_areq_i', 'icache_arsp_t', 'icache_areq_o', 'icache_dreq_t', 'icache_dreq_i', 'icache_drsp_t', 'icache_dreq_o', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'ariane_pkg::amo_req_t', 'dcache_amo_req_i', 'ariane_pkg::amo_resp_t', 'dcache_amo_resp_o', 'cmo_req_t', 'dcache_cmo_req_i', 'cmo_rsp_t', 'dcache_cmo_resp_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'hwpf_base_set_i', 'hwpf_base_i', 'hwpf_base_o', 'hwpf_param_set_i', 'hwpf_param_i', 'hwpf_param_o', 'hwpf_throttle_set_i', 'hwpf_throttle_i', 'hwpf_throttle_o', 'hwpf_status_o', ')'],
            'outputs': ['noc_req_t', 'noc_req_o', 'noc_resp_t', 'noc_resp_i', 'icache_en_i', 'icache_flush_i', 'icache_miss_o', 'icache_areq_t', 'icache_areq_i', 'icache_arsp_t', 'icache_areq_o', 'icache_dreq_t', 'icache_dreq_i', 'icache_drsp_t', 'icache_dreq_o', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'ariane_pkg::amo_req_t', 'dcache_amo_req_i', 'ariane_pkg::amo_resp_t', 'dcache_amo_resp_o', 'cmo_req_t', 'dcache_cmo_req_i', 'cmo_rsp_t', 'dcache_cmo_resp_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'hwpf_base_set_i', 'hwpf_base_i', 'hwpf_base_o', 'hwpf_param_set_i', 'hwpf_param_i', 'hwpf_param_o', 'hwpf_throttle_set_i', 'hwpf_throttle_i', 'hwpf_throttle_o', 'hwpf_status_o', ')'],
            'internals': []
        },
        'cva6_hpdcache_subsystem_axi_arbiter': {
            'inputs': ['clk_i', 'rst_ni', 'icache_miss_valid_i', 'icache_miss_ready_o', 'icache_req_t', 'icache_miss_i', 'hpdcache_mem_id_t', 'icache_miss_id_i', 'icache_miss_resp_valid_o', 'icache_rtrn_t', 'icache_miss_resp_o', 'dcache_read_ready_o', 'dcache_read_valid_i', 'hpdcache_mem_req_t', 'dcache_read_i', 'dcache_read_resp_ready_i', 'dcache_read_resp_valid_o', 'hpdcache_mem_resp_r_t', 'dcache_read_resp_o', 'dcache_write_ready_o', 'dcache_write_valid_i', 'hpdcache_mem_req_t', 'dcache_write_i', 'dcache_write_data_ready_o', 'dcache_write_data_valid_i', 'hpdcache_mem_req_w_t', 'dcache_write_data_i', 'dcache_write_resp_ready_i', 'dcache_write_resp_valid_o', 'hpdcache_mem_resp_w_t', 'dcache_write_resp_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'outputs': ['icache_miss_ready_o', 'icache_req_t', 'icache_miss_i', 'hpdcache_mem_id_t', 'icache_miss_id_i', 'icache_miss_resp_valid_o', 'icache_rtrn_t', 'icache_miss_resp_o', 'dcache_read_ready_o', 'dcache_read_valid_i', 'hpdcache_mem_req_t', 'dcache_read_i', 'dcache_read_resp_ready_i', 'dcache_read_resp_valid_o', 'hpdcache_mem_resp_r_t', 'dcache_read_resp_o', 'dcache_write_ready_o', 'dcache_write_valid_i', 'hpdcache_mem_req_t', 'dcache_write_i', 'dcache_write_data_ready_o', 'dcache_write_data_valid_i', 'hpdcache_mem_req_w_t', 'dcache_write_data_i', 'dcache_write_resp_ready_i', 'dcache_write_resp_valid_o', 'hpdcache_mem_resp_w_t', 'dcache_write_resp_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'internals': []
        },
        'cva6_hpdcache_wrapper': {
            'inputs': ['clk_i', 'rst_ni', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'ariane_pkg::amo_req_t', 'dcache_amo_req_i', 'ariane_pkg::amo_resp_t', 'dcache_amo_resp_o', 'cmo_req_t', 'dcache_cmo_req_i', 'cmo_rsp_t', 'dcache_cmo_resp_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'hwpf_base_set_i', 'hwpf_base_i', 'hwpf_base_o', 'hwpf_param_set_i', 'hwpf_param_i', 'hwpf_param_o', 'hwpf_throttle_set_i', 'hwpf_throttle_i', 'hwpf_throttle_o', 'hwpf_status_o', 'dcache_mem_req_read_ready_i', 'dcache_mem_req_read_valid_o', 'hpdcache_mem_req_t', 'dcache_mem_req_read_o', 'dcache_mem_resp_read_ready_o', 'dcache_mem_resp_read_valid_i', 'hpdcache_mem_resp_r_t', 'dcache_mem_resp_read_i', 'dcache_mem_req_write_ready_i', 'dcache_mem_req_write_valid_o', 'hpdcache_mem_req_t', 'dcache_mem_req_write_o', 'dcache_mem_req_write_data_ready_i', 'dcache_mem_req_write_data_valid_o', 'hpdcache_mem_req_w_t', 'dcache_mem_req_write_data_o', 'dcache_mem_resp_write_ready_o', 'dcache_mem_resp_write_valid_i', 'hpdcache_mem_resp_w_t', 'dcache_mem_resp_write_i', ')'],
            'outputs': ['dcache_flush_ack_o', 'dcache_miss_o', 'ariane_pkg::amo_req_t', 'dcache_amo_req_i', 'ariane_pkg::amo_resp_t', 'dcache_amo_resp_o', 'cmo_req_t', 'dcache_cmo_req_i', 'cmo_rsp_t', 'dcache_cmo_resp_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'hwpf_base_set_i', 'hwpf_base_i', 'hwpf_base_o', 'hwpf_param_set_i', 'hwpf_param_i', 'hwpf_param_o', 'hwpf_throttle_set_i', 'hwpf_throttle_i', 'hwpf_throttle_o', 'hwpf_status_o', 'dcache_mem_req_read_ready_i', 'dcache_mem_req_read_valid_o', 'hpdcache_mem_req_t', 'dcache_mem_req_read_o', 'dcache_mem_resp_read_ready_o', 'dcache_mem_resp_read_valid_i', 'hpdcache_mem_resp_r_t', 'dcache_mem_resp_read_i', 'dcache_mem_req_write_ready_i', 'dcache_mem_req_write_valid_o', 'hpdcache_mem_req_t', 'dcache_mem_req_write_o', 'dcache_mem_req_write_data_ready_i', 'dcache_mem_req_write_data_valid_o', 'hpdcache_mem_req_w_t', 'dcache_mem_req_write_data_o', 'dcache_mem_resp_write_ready_o', 'dcache_mem_resp_write_valid_i', 'hpdcache_mem_resp_w_t', 'dcache_mem_resp_write_i', ')'],
            'internals': []
        },
        'cva6_icache': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'en_i', 'miss_o', 'icache_areq_t', 'areq_i', 'icache_arsp_t', 'areq_o', 'icache_dreq_t', 'dreq_i', 'icache_drsp_t', 'dreq_o', 'mem_rtrn_vld_i', 'icache_rtrn_t', 'mem_rtrn_i', 'mem_data_req_o', 'mem_data_ack_i', 'icache_req_t', 'mem_data_o', ')', 'in)'],
            'outputs': ['miss_o', 'icache_areq_t', 'areq_i', 'icache_arsp_t', 'areq_o', 'icache_dreq_t', 'dreq_i', 'icache_drsp_t', 'dreq_o', 'mem_rtrn_vld_i', 'icache_rtrn_t', 'mem_rtrn_i', 'mem_data_req_o', 'mem_data_ack_i', 'icache_req_t', 'mem_data_o', ')'],
            'internals': []
        },
        'cva6_rvfi': {
            'inputs': ['clk_i', 'rst_ni', 'rvfi_probes_t', 'rvfi_probes_i', 'rvfi_instr_t', 'rvfi_instr_o', 'rvfi_to_iti_t', 'rvfi_to_iti_o', 'rvfi_csr_t', 'rvfi_csr_o', ')', 'fu_op', 'amo_op', 'mem_old_val'],
            'outputs': ['rvfi_instr_t', 'rvfi_instr_o', 'rvfi_to_iti_t', 'rvfi_to_iti_o', 'rvfi_csr_t', 'rvfi_csr_o', ')'],
            'internals': []
        },
        'cva6_rvfi_probes': {
            'inputs': ['flush_i', 'issue_instr_ack_i', 'fetch_entry_valid_i', 'instruction_i', 'is_compressed_i', ':', 'issue_pointer_i', 'commit_pointer_i', 'flush_unissued_instr_i', 'decoded_instr_valid_i', 'decoded_instr_ack_i', 'rs1_i', 'rs2_i', 'scoreboard_entry_t', 'commit_instr_i', 'commit_drop_i', 'exception_t', 'ex_commit_i', 'riscv::priv_lvl_t', 'priv_lvl_i', 'lsu_ctrl_t', 'lsu_ctrl_i', 'wbdata_i', 'commit_ack_i', 'mem_paddr_i', 'debug_mode_i', 'wdata_i', 'rvfi_probes_csr_t', 'csr_i', 'irq_i', 'bp_resolve_t', 'resolved_branch_i', 'flu_trans_id_ex_id_i', 'rvfi_probes_t', 'rvfi_probes_o', ')'],
            'outputs': ['rvfi_probes_t', 'rvfi_probes_o', ')'],
            'internals': []
        },
        'cvxif_compressed_if_driver': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'hart_id_i', 'is_compressed_i', 'is_illegal_i', 'instruction_i', 'is_compressed_o', 'is_illegal_o', 'instruction_o', 'stall_i', 'stall_o', 'compressed_ready_i', 'x_compressed_resp_t', 'compressed_resp_i', 'compressed_valid_o', 'x_compressed_req_t', 'compressed_req_o', ')'],
            'outputs': ['is_compressed_o', 'is_illegal_o', 'instruction_o', 'stall_i', 'stall_o', 'compressed_ready_i', 'x_compressed_resp_t', 'compressed_resp_i', 'compressed_valid_o', 'x_compressed_req_t', 'compressed_req_o', ')'],
            'internals': []
        },
        'cvxif_example_coprocessor': {
            'inputs': ['clk_i', 'rst_ni', 'cvxif_req_t', 'cvxif_req_i', 'cvxif_resp_t', 'cvxif_resp_o', ')'],
            'outputs': ['cvxif_resp_t', 'cvxif_resp_o', ')'],
            'internals': []
        },
        'cvxif_fu': {
            'inputs': ['clk_i', 'rst_ni', 'v_i', 'x_valid_i', 'x_trans_id_i', 'x_illegal_i', 'x_off_instr_i', 'x_ready_o', 'x_trans_id_o', 'exception_t', 'x_exception_o', 'x_result_o', 'x_valid_o', 'x_we_o', 'x_rd_o', 'result_valid_i', 'x_result_t', 'result_i', 'result_ready_o', ')'],
            'outputs': ['x_ready_o', 'x_trans_id_o', 'exception_t', 'x_exception_o', 'x_result_o', 'x_valid_o', 'x_we_o', 'x_rd_o', 'result_valid_i', 'x_result_t', 'result_i', 'result_ready_o', ')'],
            'internals': []
        },
        'cvxif_issue_register_commit_if_driver': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'hart_id_i', 'issue_ready_i', 'x_issue_resp_t', 'issue_resp_i', 'issue_valid_o', 'x_issue_req_t', 'issue_req_o', 'commit_valid_o', 'x_commit_t', 'commit_o', 'valid_i', 'x_off_instr_i', 'x_trans_id_i', 'rs_valid_i', ')'],
            'outputs': ['issue_valid_o', 'x_issue_req_t', 'issue_req_o', 'commit_valid_o', 'x_commit_t', 'commit_o', 'valid_i', 'x_off_instr_i', 'x_trans_id_i', 'rs_valid_i', ')'],
            'internals': []
        },
        'decoder': {
            'inputs': ['debug_req_i', 'pc_i', 'is_compressed_i', 'compressed_instr_i', 'is_illegal_i', 'instruction_i', 'is_macro_instr_i', 'is_last_macro_instr_i', 'is_double_rd_macro_instr_i', 'is_zcmt_i', 'jump_address_i', 'branchpredict_sbe_t', 'branch_predict_i', 'exception_t', 'ex_i', 'irq_i', 'irq_ctrl_t', 'irq_ctrl_i', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'debug_mode_i', 'riscv::xs_t', 'fs_i', 'riscv::xs_t', 'vfs_i', 'frm_i', 'riscv::xs_t', 'vs_i', 'tvm_i', 'tw_i', 'vtw_i', 'tsr_i', 'hu_i', 'scoreboard_entry_t', 'instruction_o', 'orig_instr_o', 'is_control_flow_instr_o', 'debug_from_trigger_i', ')'],
            'outputs': ['scoreboard_entry_t', 'instruction_o', 'orig_instr_o', 'is_control_flow_instr_o', 'debug_from_trigger_i', ')'],
            'internals': []
        },
        'ex_stage': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'debug_mode_i', 'rs1_forwarding_i', 'rs2_forwarding_i', 'fu_data_t', 'fu_data_i', 'alu_bypass_t', 'alu_bypass_i', 'pc_i', 'is_zcmt_i', 'is_compressed_instr_i', 'tinst_i', 'flu_result_o', 'flu_trans_id_o', 'exception_t', 'flu_exception_o', 'flu_ready_o', 'flu_valid_o', 'alu_valid_i', 'aes_valid_i', 'branch_valid_i', 'branchpredict_sbe_t', 'branch_predict_i', 'bp_resolve_t', 'resolved_branch_o', 'resolve_branch_o', 'csr_valid_i', 'csr_addr_o', 'csr_commit_i', 'mult_valid_i', 'lsu_ready_o', 'lsu_valid_i', 'load_valid_o', 'load_result_o', 'load_trans_id_o', 'exception_t', 'load_exception_o', 'store_valid_o', 'store_result_o', 'store_trans_id_o', 'exception_t', 'store_exception_o', 'lsu_commit_i', 'lsu_commit_ready_o', 'commit_tran_id_i', 'stall_st_pending_i', 'no_st_pending_o', 'amo_valid_commit_i', 'fpu_ready_o', 'fpu_valid_i', 'fpu_fmt_i', 'fpu_rm_i', 'fpu_frm_i', 'fpu_prec_i', 'fpu_trans_id_o', 'fpu_result_o', 'fpu_valid_o', 'exception_t', 'fpu_exception_o', 'fpu_early_valid_o', 'alu2_valid_i', 'x_valid_i', 'x_ready_o', 'x_off_instr_i', 'x_trans_id_o', 'exception_t', 'x_exception_o', 'x_result_o', 'x_valid_o', 'x_we_o', 'x_rd_o', 'x_result_valid_i', 'x_result_t', 'x_result_i', 'x_result_ready_o', 'x_transaction_rejected_i', 'acc_valid_i', 'acc_mmu_req_t', 'acc_mmu_req_i', 'acc_mmu_resp_t', 'acc_mmu_resp_o', 'enable_translation_i', 'enable_g_translation_i', 'en_ld_st_translation_i', 'en_ld_st_g_translation_i', 'flush_tlb_i', 'flush_tlb_vvma_i', 'flush_tlb_gvma_i', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_i', 'ld_st_v_i', 'csr_hs_ld_st_inst_o', 'sum_i', 'vs_sum_i', 'mxr_i', 'vmxr_i', 'satp_ppn_i', 'asid_i', 'vsatp_ppn_i', 'vs_asid_i', 'hgatp_ppn_i', 'vmid_i', 'icache_arsp_t', 'icache_areq_i', 'icache_areq_t', 'icache_areq_o', 'dcache_req_o_t', 'dcache_req_ports_i', 'dcache_req_i_t', 'dcache_req_ports_o', 'dcache_wbuffer_empty_i', 'dcache_wbuffer_not_ni_i', 'amo_req_t', 'amo_req_o', 'amo_resp_t', 'amo_resp_i', 'itlb_miss_o', 'dtlb_miss_o', 'riscv::pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', 'lsu_ctrl_t', 'rvfi_lsu_ctrl_o', 'rvfi_mem_paddr_o', 'orig_instr_aes_i', ')'],
            'outputs': ['flu_result_o', 'flu_trans_id_o', 'exception_t', 'flu_exception_o', 'flu_ready_o', 'flu_valid_o', 'alu_valid_i', 'aes_valid_i', 'branch_valid_i', 'branchpredict_sbe_t', 'branch_predict_i', 'bp_resolve_t', 'resolved_branch_o', 'resolve_branch_o', 'csr_valid_i', 'csr_addr_o', 'csr_commit_i', 'mult_valid_i', 'lsu_ready_o', 'lsu_valid_i', 'load_valid_o', 'load_result_o', 'load_trans_id_o', 'exception_t', 'load_exception_o', 'store_valid_o', 'store_result_o', 'store_trans_id_o', 'exception_t', 'store_exception_o', 'lsu_commit_i', 'lsu_commit_ready_o', 'commit_tran_id_i', 'stall_st_pending_i', 'no_st_pending_o', 'amo_valid_commit_i', 'fpu_ready_o', 'fpu_valid_i', 'fpu_fmt_i', 'fpu_rm_i', 'fpu_frm_i', 'fpu_prec_i', 'fpu_trans_id_o', 'fpu_result_o', 'fpu_valid_o', 'exception_t', 'fpu_exception_o', 'fpu_early_valid_o', 'alu2_valid_i', 'x_valid_i', 'x_ready_o', 'x_off_instr_i', 'x_trans_id_o', 'exception_t', 'x_exception_o', 'x_result_o', 'x_valid_o', 'x_we_o', 'x_rd_o', 'x_result_valid_i', 'x_result_t', 'x_result_i', 'x_result_ready_o', 'x_transaction_rejected_i', 'acc_valid_i', 'acc_mmu_req_t', 'acc_mmu_req_i', 'acc_mmu_resp_t', 'acc_mmu_resp_o', 'enable_translation_i', 'enable_g_translation_i', 'en_ld_st_translation_i', 'en_ld_st_g_translation_i', 'flush_tlb_i', 'flush_tlb_vvma_i', 'flush_tlb_gvma_i', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_i', 'ld_st_v_i', 'csr_hs_ld_st_inst_o', 'sum_i', 'vs_sum_i', 'mxr_i', 'vmxr_i', 'satp_ppn_i', 'asid_i', 'vsatp_ppn_i', 'vs_asid_i', 'hgatp_ppn_i', 'vmid_i', 'icache_arsp_t', 'icache_areq_i', 'icache_areq_t', 'icache_areq_o', 'dcache_req_o_t', 'dcache_req_ports_i', 'dcache_req_i_t', 'dcache_req_ports_o', 'dcache_wbuffer_empty_i', 'dcache_wbuffer_not_ni_i', 'amo_req_t', 'amo_req_o', 'amo_resp_t', 'amo_resp_i', 'itlb_miss_o', 'dtlb_miss_o', 'riscv::pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', 'lsu_ctrl_t', 'rvfi_lsu_ctrl_o', 'rvfi_mem_paddr_o', 'orig_instr_aes_i', ')'],
            'internals': []
        },
        'fpu_wrap': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'fpu_valid_i', 'fpu_ready_o', 'fu_data_t', 'fu_data_i', 'fpu_fmt_i', 'fpu_rm_i', 'fpu_frm_i', 'fpu_prec_i', 'fpu_trans_id_o', 'result_o', 'fpu_valid_o', 'exception_t', 'fpu_exception_o', 'fpu_early_valid_o', ')'],
            'outputs': ['fpu_ready_o', 'fu_data_t', 'fu_data_i', 'fpu_fmt_i', 'fpu_rm_i', 'fpu_frm_i', 'fpu_prec_i', 'fpu_trans_id_o', 'result_o', 'fpu_valid_o', 'exception_t', 'fpu_exception_o', 'fpu_early_valid_o', ')'],
            'internals': []
        },
        'id_stage': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'debug_req_i', 'fetch_entry_t', 'fetch_entry_i', 'fetch_entry_valid_i', 'fetch_entry_ready_o', 'scoreboard_entry_t', 'issue_entry_o', 'scoreboard_entry_t', 'issue_entry_o_prev', 'orig_instr_o', 'issue_entry_valid_o', 'is_ctrl_flow_o', 'issue_instr_ack_i', 'rvfi_is_compressed_o', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::xs_t', 'fs_i', 'riscv::xs_t', 'vfs_i', 'frm_i', 'riscv::xs_t', 'vs_i', 'irq_i', 'irq_ctrl_t', 'irq_ctrl_i', 'debug_mode_i', 'tvm_i', 'tw_i', 'vtw_i', 'tsr_i', 'hu_i', 'hart_id_i', 'compressed_ready_i', 'jvt_t', 'jvt_i', 'x_compressed_resp_t', 'compressed_resp_i', 'compressed_valid_o', 'x_compressed_req_t', 'compressed_req_o', 'debug_from_trigger_i', 'dcache_req_o_t', 'dcache_req_ports_i', 'dcache_req_i_t', 'dcache_req_ports_o', ')'],
            'outputs': ['fetch_entry_ready_o', 'scoreboard_entry_t', 'issue_entry_o', 'scoreboard_entry_t', 'issue_entry_o_prev', 'orig_instr_o', 'issue_entry_valid_o', 'is_ctrl_flow_o', 'issue_instr_ack_i', 'rvfi_is_compressed_o', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::xs_t', 'fs_i', 'riscv::xs_t', 'vfs_i', 'frm_i', 'riscv::xs_t', 'vs_i', 'irq_i', 'irq_ctrl_t', 'irq_ctrl_i', 'debug_mode_i', 'tvm_i', 'tw_i', 'vtw_i', 'tsr_i', 'hu_i', 'hart_id_i', 'compressed_ready_i', 'jvt_t', 'jvt_i', 'x_compressed_resp_t', 'compressed_resp_i', 'compressed_valid_o', 'x_compressed_req_t', 'compressed_req_o', 'debug_from_trigger_i', 'dcache_req_o_t', 'dcache_req_ports_i', 'dcache_req_i_t', 'dcache_req_ports_o', ')'],
            'internals': []
        },
        'instr_decoder': {
            'inputs': ['clk_i', 'rst_ni', 'issue_valid_i', 'x_issue_req_t', 'issue_req_i', 'issue_ready_o', 'x_issue_resp_t', 'issue_resp_o', 'opcode_t', 'opcode_o', 'hartid_t', 'hartid_o', 'id_t', 'id_o', 'rd_o', ')'],
            'outputs': ['issue_ready_o', 'x_issue_resp_t', 'issue_resp_o', 'opcode_t', 'opcode_o', 'hartid_t', 'hartid_o', 'id_t', 'id_o', 'rd_o', ')'],
            'internals': []
        },
        'instr_queue': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'instr_i', 'addr_i', 'valid_i', 'ready_o', 'consumed_o', 'ariane_pkg::frontend_exception_t', 'exception_i', 'exception_addr_i', 'exception_gpaddr_i', 'exception_tinst_i', 'exception_gva_i', 'predict_address_i', 'ariane_pkg::cf_t', 'cf_type_i', 'replay_o', 'replay_addr_o', 'fetch_entry_t', 'fetch_entry_o', 'fetch_entry_valid_o', 'fetch_entry_ready_i', ')', 'assign', '='],
            'outputs': ['ready_o', 'consumed_o', 'ariane_pkg::frontend_exception_t', 'exception_i', 'exception_addr_i', 'exception_gpaddr_i', 'exception_tinst_i', 'exception_gva_i', 'predict_address_i', 'ariane_pkg::cf_t', 'cf_type_i', 'replay_o', 'replay_addr_o', 'fetch_entry_t', 'fetch_entry_o', 'fetch_entry_valid_o', 'fetch_entry_ready_i', ')'],
            'internals': []
        },
        'instr_scan': {
            'inputs': ['instr_i', 'rvi_return_o', 'rvi_call_o', 'rvi_branch_o', 'rvi_jalr_o', 'rvi_jump_o', 'rvi_imm_o', 'rvc_branch_o', 'rvc_jump_o', 'rvc_jr_o', 'rvc_return_o', 'rvc_jalr_o', 'rvc_call_o', 'rvc_imm_o', ')'],
            'outputs': ['rvi_return_o', 'rvi_call_o', 'rvi_branch_o', 'rvi_jalr_o', 'rvi_jump_o', 'rvi_imm_o', 'rvc_branch_o', 'rvc_jump_o', 'rvc_jr_o', 'rvc_return_o', 'rvc_jalr_o', 'rvc_call_o', 'rvc_imm_o', ')'],
            'internals': []
        },
        'interfaces': {
            'inputs': ['clk_i', 'rst_ni', 'boot_addr_i', 'flush_bp_i', 'flush_i', 'halt_i', 'halt_frontend_i', 'set_pc_commit_i', 'pc_commit_i', 'ex_valid_i', 'bp_resolve_t', 'resolved_branch_i', 'eret_i', 'epc_i', 'trap_vector_base_i', 'set_debug_pc_i', 'debug_mode_i', 'icache_dreq_t', 'icache_dreq_o', 'icache_drsp_t', 'icache_dreq_i', 'fetch_entry_t', 'fetch_entry_o', 'fetch_entry_valid_o', 'fetch_entry_ready_i', ')'],
            'outputs': ['icache_dreq_t', 'icache_dreq_o', 'icache_drsp_t', 'icache_dreq_i', 'fetch_entry_t', 'fetch_entry_o', 'fetch_entry_valid_o', 'fetch_entry_ready_i', ')'],
            'internals': []
        },
        'is': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'flush_vvma_i', 'flush_gvma_i', 's_st_enbl_i', 'g_st_enbl_i', 'v_i', 'tlb_update_cva6_t', 'update_i', 'lu_access_i', 'lu_asid_i', 'lu_vmid_i', 'lu_vaddr_i', 'lu_gpaddr_o', 'pte_cva6_t', 'lu_content_o', 'pte_cva6_t', 'lu_g_content_o', 'asid_to_be_flushed_i', 'vmid_to_be_flushed_i', 'vaddr_to_be_flushed_i', 'gpaddr_to_be_flushed_i', 'lu_is_page_o', 'lu_hit_o', ')'],
            'outputs': ['lu_gpaddr_o', 'pte_cva6_t', 'lu_content_o', 'pte_cva6_t', 'lu_g_content_o', 'asid_to_be_flushed_i', 'vmid_to_be_flushed_i', 'vaddr_to_be_flushed_i', 'gpaddr_to_be_flushed_i', 'lu_is_page_o', 'lu_hit_o', ')'],
            'internals': []
        },
        'issue_read_operands': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'stall_i', 'scoreboard_entry_t', 'issue_instr_i', 'scoreboard_entry_t', 'issue_instr_i_prev', 'orig_instr_i', 'issue_instr_valid_i', 'issue_ack_o', 'forwarding_t', 'fwd_i', 'fu_data_t', 'fu_data_o', 'alu_bypass_t', 'alu_bypass_o', 'rs1_forwarding_o', 'rs2_forwarding_o', 'pc_o', 'is_zcmt_o', 'is_compressed_instr_o', 'flu_ready_i', 'alu_valid_o', 'aes_valid_o', 'branch_valid_o', 'tinst_o', 'branchpredict_sbe_t', 'branch_predict_o', 'lsu_ready_i', 'lsu_valid_o', 'mult_valid_o', 'fpu_ready_i', 'fpu_early_valid_i', 'fpu_valid_o', 'fpu_fmt_o', 'fpu_rm_o', 'alu2_valid_o', 'csr_valid_o', 'cvxif_valid_o', 'cvxif_ready_i', 'cvxif_off_instr_o', 'hart_id_i', 'x_issue_ready_i', 'x_issue_resp_t', 'x_issue_resp_i', 'x_issue_valid_o', 'x_issue_req_t', 'x_issue_req_o', 'x_commit_valid_o', 'x_commit_t', 'x_commit_o', 'x_transaction_accepted_o', 'x_transaction_rejected_o', 'x_issue_writeback_o', 'x_id_o', 'waddr_i', 'wdata_i', 'we_gpr_i', 'we_fpr_i', 'stall_issue_o', 'rvfi_rs1_o', 'rvfi_rs2_o', 'orig_instr_aes_bits', ')'],
            'outputs': ['issue_ack_o', 'forwarding_t', 'fwd_i', 'fu_data_t', 'fu_data_o', 'alu_bypass_t', 'alu_bypass_o', 'rs1_forwarding_o', 'rs2_forwarding_o', 'pc_o', 'is_zcmt_o', 'is_compressed_instr_o', 'flu_ready_i', 'alu_valid_o', 'aes_valid_o', 'branch_valid_o', 'tinst_o', 'branchpredict_sbe_t', 'branch_predict_o', 'lsu_ready_i', 'lsu_valid_o', 'mult_valid_o', 'fpu_ready_i', 'fpu_early_valid_i', 'fpu_valid_o', 'fpu_fmt_o', 'fpu_rm_o', 'alu2_valid_o', 'csr_valid_o', 'cvxif_valid_o', 'cvxif_ready_i', 'cvxif_off_instr_o', 'hart_id_i', 'x_issue_ready_i', 'x_issue_resp_t', 'x_issue_resp_i', 'x_issue_valid_o', 'x_issue_req_t', 'x_issue_req_o', 'x_commit_valid_o', 'x_commit_t', 'x_commit_o', 'x_transaction_accepted_o', 'x_transaction_rejected_o', 'x_issue_writeback_o', 'x_id_o', 'waddr_i', 'wdata_i', 'we_gpr_i', 'we_fpr_i', 'stall_issue_o', 'rvfi_rs1_o', 'rvfi_rs2_o', 'orig_instr_aes_bits', ')'],
            'internals': []
        },
        'issue_stage': {
            'inputs': ['clk_i', 'rst_ni', 'sb_full_o', 'flush_unissued_instr_i', 'flush_i', 'stall_i', 'scoreboard_entry_t', 'decoded_instr_i', 'scoreboard_entry_t', 'decoded_instr_i_prev', 'orig_instr_i', 'decoded_instr_valid_i', 'is_ctrl_flow_i', 'decoded_instr_ack_o', 'rs1_forwarding_o', 'rs2_forwarding_o', 'fu_data_t', 'fu_data_o', 'alu_bypass_t', 'alu_bypass_o', 'pc_o', 'is_zcmt_o', 'is_compressed_instr_o', 'tinst_o', 'flu_ready_i', 'alu_valid_o', 'aes_valid_o', 'branch_valid_o', 'branchpredict_sbe_t', 'branch_predict_o', 'resolve_branch_i', 'lsu_ready_i', 'lsu_valid_o', 'mult_valid_o', 'fpu_ready_i', 'fpu_valid_o', 'fpu_fmt_o', 'fpu_rm_o', 'fpu_early_valid_i', 'alu2_valid_o', 'csr_valid_o', 'xfu_valid_o', 'xfu_ready_i', 'x_off_instr_o', 'hart_id_i', 'x_issue_ready_i', 'x_issue_resp_t', 'x_issue_resp_i', 'x_issue_valid_o', 'x_issue_req_t', 'x_issue_req_o', 'x_commit_valid_o', 'x_commit_t', 'x_commit_o', 'x_transaction_rejected_o', 'scoreboard_entry_t', 'issue_instr_o', 'issue_instr_hs_o', 'trans_id_i', 'bp_resolve_t', 'resolved_branch_i', 'wbdata_i', 'exception_t', 'ex_ex_i', 'wt_valid_i', 'x_we_i', 'x_rd_i', 'waddr_i', 'wdata_i', 'we_gpr_i', 'we_fpr_i', 'scoreboard_entry_t', 'commit_instr_o', 'commit_drop_o', 'commit_ack_i', 'stall_issue_o', 'rvfi_issue_pointer_o', 'rvfi_commit_pointer_o', 'rvfi_rs1_o', 'rvfi_rs2_o', 'orig_instr_aes_bits', ')'],
            'outputs': ['sb_full_o', 'flush_unissued_instr_i', 'flush_i', 'stall_i', 'scoreboard_entry_t', 'decoded_instr_i', 'scoreboard_entry_t', 'decoded_instr_i_prev', 'orig_instr_i', 'decoded_instr_valid_i', 'is_ctrl_flow_i', 'decoded_instr_ack_o', 'rs1_forwarding_o', 'rs2_forwarding_o', 'fu_data_t', 'fu_data_o', 'alu_bypass_t', 'alu_bypass_o', 'pc_o', 'is_zcmt_o', 'is_compressed_instr_o', 'tinst_o', 'flu_ready_i', 'alu_valid_o', 'aes_valid_o', 'branch_valid_o', 'branchpredict_sbe_t', 'branch_predict_o', 'resolve_branch_i', 'lsu_ready_i', 'lsu_valid_o', 'mult_valid_o', 'fpu_ready_i', 'fpu_valid_o', 'fpu_fmt_o', 'fpu_rm_o', 'fpu_early_valid_i', 'alu2_valid_o', 'csr_valid_o', 'xfu_valid_o', 'xfu_ready_i', 'x_off_instr_o', 'hart_id_i', 'x_issue_ready_i', 'x_issue_resp_t', 'x_issue_resp_i', 'x_issue_valid_o', 'x_issue_req_t', 'x_issue_req_o', 'x_commit_valid_o', 'x_commit_t', 'x_commit_o', 'x_transaction_rejected_o', 'scoreboard_entry_t', 'issue_instr_o', 'issue_instr_hs_o', 'trans_id_i', 'bp_resolve_t', 'resolved_branch_i', 'wbdata_i', 'exception_t', 'ex_ex_i', 'wt_valid_i', 'x_we_i', 'x_rd_i', 'waddr_i', 'wdata_i', 'we_gpr_i', 'we_fpr_i', 'scoreboard_entry_t', 'commit_instr_o', 'commit_drop_o', 'commit_ack_i', 'stall_issue_o', 'rvfi_issue_pointer_o', 'rvfi_commit_pointer_o', 'rvfi_rs1_o', 'rvfi_rs2_o', 'orig_instr_aes_bits', ')'],
            'internals': []
        },
        'load_store_unit': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'stall_st_pending_i', 'no_st_pending_o', 'amo_valid_commit_i', 'tinst_i', 'fu_data_t', 'fu_data_i', 'lsu_ready_o', 'lsu_valid_i', 'load_trans_id_o', 'load_result_o', 'load_valid_o', 'exception_t', 'load_exception_o', 'store_trans_id_o', 'store_result_o', 'store_valid_o', 'exception_t', 'store_exception_o', 'commit_i', 'commit_ready_o', 'commit_tran_id_i', 'enable_translation_i', 'enable_g_translation_i', 'en_ld_st_translation_i', 'en_ld_st_g_translation_i', 'acc_mmu_req_t', 'acc_mmu_req_i', 'acc_mmu_resp_t', 'acc_mmu_resp_o', 'icache_arsp_t', 'icache_areq_i', 'icache_areq_t', 'icache_areq_o', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_i', 'ld_st_v_i', 'csr_hs_ld_st_inst_o', 'sum_i', 'vs_sum_i', 'mxr_i', 'vmxr_i', 'satp_ppn_i', 'asid_i', 'vsatp_ppn_i', 'vs_asid_i', 'hgatp_ppn_i', 'vmid_i', 'asid_to_be_flushed_i', 'vmid_to_be_flushed_i', 'vaddr_to_be_flushed_i', 'gpaddr_to_be_flushed_i', 'flush_tlb_i', 'flush_tlb_vvma_i', 'flush_tlb_gvma_i', 'itlb_miss_o', 'dtlb_miss_o', 'dcache_req_o_t', 'dcache_req_ports_i', 'dcache_req_i_t', 'dcache_req_ports_o', 'dcache_wbuffer_empty_i', 'dcache_wbuffer_not_ni_i', 'amo_req_t', 'amo_req_o', 'amo_resp_t', 'amo_resp_i', 'riscv::pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', 'lsu_ctrl_t', 'rvfi_lsu_ctrl_o', 'rvfi_mem_paddr_o', ')'],
            'outputs': ['no_st_pending_o', 'amo_valid_commit_i', 'tinst_i', 'fu_data_t', 'fu_data_i', 'lsu_ready_o', 'lsu_valid_i', 'load_trans_id_o', 'load_result_o', 'load_valid_o', 'exception_t', 'load_exception_o', 'store_trans_id_o', 'store_result_o', 'store_valid_o', 'exception_t', 'store_exception_o', 'commit_i', 'commit_ready_o', 'commit_tran_id_i', 'enable_translation_i', 'enable_g_translation_i', 'en_ld_st_translation_i', 'en_ld_st_g_translation_i', 'acc_mmu_req_t', 'acc_mmu_req_i', 'acc_mmu_resp_t', 'acc_mmu_resp_o', 'icache_arsp_t', 'icache_areq_i', 'icache_areq_t', 'icache_areq_o', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_i', 'ld_st_v_i', 'csr_hs_ld_st_inst_o', 'sum_i', 'vs_sum_i', 'mxr_i', 'vmxr_i', 'satp_ppn_i', 'asid_i', 'vsatp_ppn_i', 'vs_asid_i', 'hgatp_ppn_i', 'vmid_i', 'asid_to_be_flushed_i', 'vmid_to_be_flushed_i', 'vaddr_to_be_flushed_i', 'gpaddr_to_be_flushed_i', 'flush_tlb_i', 'flush_tlb_vvma_i', 'flush_tlb_gvma_i', 'itlb_miss_o', 'dtlb_miss_o', 'dcache_req_o_t', 'dcache_req_ports_i', 'dcache_req_i_t', 'dcache_req_ports_o', 'dcache_wbuffer_empty_i', 'dcache_wbuffer_not_ni_i', 'amo_req_t', 'amo_req_o', 'amo_resp_t', 'amo_resp_i', 'riscv::pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', 'lsu_ctrl_t', 'rvfi_lsu_ctrl_o', 'rvfi_mem_paddr_o', ')'],
            'internals': []
        },
        'load_unit': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'valid_i', 'lsu_ctrl_t', 'lsu_ctrl_i', 'pop_ld_o', 'valid_o', 'trans_id_o', 'result_o', 'exception_t', 'ex_o', 'translation_req_o', 'vaddr_o', 'tinst_o', 'hs_ld_st_inst_o', 'hlvx_inst_o', 'paddr_i', 'exception_t', 'ex_i', 'dtlb_hit_i', 'dtlb_ppn_i', 'page_offset_o', 'page_offset_matches_i', 'store_buffer_empty_i', 'commit_tran_id_i', 'dcache_req_o_t', 'req_port_i', 'dcache_req_i_t', 'req_port_o', 'dcache_wbuffer_not_ni_i', ')'],
            'outputs': ['pop_ld_o', 'valid_o', 'trans_id_o', 'result_o', 'exception_t', 'ex_o', 'translation_req_o', 'vaddr_o', 'tinst_o', 'hs_ld_st_inst_o', 'hlvx_inst_o', 'paddr_i', 'exception_t', 'ex_i', 'dtlb_hit_i', 'dtlb_ppn_i', 'page_offset_o', 'page_offset_matches_i', 'store_buffer_empty_i', 'commit_tran_id_i', 'dcache_req_o_t', 'req_port_i', 'dcache_req_i_t', 'req_port_o', 'dcache_wbuffer_not_ni_i', ')', 'ldbuf_r', '=', 'req_port_i.data_rvalid'],
            'internals': []
        },
        'logic': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'lsu_bypass': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'lsu_ctrl_t', 'lsu_req_i', 'lsu_req_valid_i', 'pop_ld_i', 'pop_st_i', 'lsu_ctrl_t', 'lsu_ctrl_o', 'ready_o', ')'],
            'outputs': ['lsu_ctrl_t', 'lsu_ctrl_o', 'ready_o', ')'],
            'internals': []
        },
        'macro_decoder': {
            'inputs': ['instr_i', 'clk_i', 'rst_ni', 'is_macro_instr_i', 'illegal_instr_i', 'is_compressed_i', 'issue_ack_i', 'instr_o', 'illegal_instr_o', 'is_compressed_o', 'fetch_stall_o', 'is_last_macro_instr_o', 'is_double_rd_macro_instr_o', ')'],
            'outputs': ['instr_o', 'illegal_instr_o', 'is_compressed_o', 'fetch_stall_o', 'is_last_macro_instr_o', 'is_double_rd_macro_instr_o', ')'],
            'internals': []
        },
        'miss_handler': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'flush_ack_o', 'miss_o', 'busy_i', 'miss_req_i', 'bypass_gnt_o', 'bypass_valid_o', 'bypass_data_o', 'axi_req_t', 'axi_bypass_o', 'axi_rsp_t', 'axi_bypass_i', 'miss_gnt_o', 'active_serving_o', 'critical_word_o', 'critical_word_valid_o', 'axi_req_t', 'axi_data_o', 'axi_rsp_t', 'axi_data_i', 'mshr_addr_i', 'mshr_addr_matches_o', 'mshr_index_matches_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'req_o', 'addr_o', 'cache_line_t', 'data_o', 'cl_be_t', 'be_o', 'cache_line_t', 'data_i', 'we_o', ')', 'in)', 'valid_dirty)', 'clk_i', 'rst_ni', 'req_t', 'req_i', 'rsp_t', 'rsp_o', 'req_t', 'req_o', 'rsp_t', 'rsp_i', ')'],
            'outputs': ['flush_ack_o', 'miss_o', 'busy_i', 'miss_req_i', 'bypass_gnt_o', 'bypass_valid_o', 'bypass_data_o', 'axi_req_t', 'axi_bypass_o', 'axi_rsp_t', 'axi_bypass_i', 'miss_gnt_o', 'active_serving_o', 'critical_word_o', 'critical_word_valid_o', 'axi_req_t', 'axi_data_o', 'axi_rsp_t', 'axi_data_i', 'mshr_addr_i', 'mshr_addr_matches_o', 'mshr_index_matches_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'req_o', 'addr_o', 'cache_line_t', 'data_o', 'cl_be_t', 'be_o', 'cache_line_t', 'data_i', 'we_o', ')', 'rsp_t', 'rsp_o', 'req_t', 'req_o', 'rsp_t', 'rsp_i', ')'],
            'internals': []
        },
        'mult': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'fu_data_t', 'fu_data_i', 'mult_valid_i', 'result_o', 'mult_valid_o', 'mult_ready_o', 'mult_trans_id_o', ')'],
            'outputs': ['result_o', 'mult_valid_o', 'mult_ready_o', 'mult_trans_id_o', ')'],
            'internals': []
        },
        'multiplier': {
            'inputs': ['clk_i', 'rst_ni', 'trans_id_i', 'mult_valid_i', 'fu_op', 'operation_i', 'operand_a_i', 'operand_b_i', 'result_o', 'mult_valid_o', 'mult_trans_id_o', ')'],
            'outputs': ['result_o', 'mult_valid_o', 'mult_trans_id_o', ')'],
            'internals': []
        },
        'needs': {
            'inputs': ['fu_op', 'op)', 'fu_op', 'op)', 'fu_op', 'op)', 'fu_op', 'op)', 'fu_op', 'op)', 'fu_op', 'op)', 's_st_enbl', 'g_st_enbl', 'is_s_1G', 'is_g_1G)', 's_st_enbl', 'g_st_enbl', 'is_s_1G', 'is_s_2M', 'is_g_1G', 'is_g_2M)', 's_st_enbl', 'is_1G', 'is_2M', 'vaddr', 'riscv::pte_t', 'pte)', 's_st_enbl', 'is_1G', 'is_2M', 'vpn', 'riscv::pte_t', 'pte)'],
            'outputs': [],
            'internals': []
        },
        'perf_counters': {
            'inputs': ['clk_i', 'rst_ni', 'debug_mode_i', 'addr_i', 'we_i', 'data_i', 'data_o', 'scoreboard_entry_t', 'commit_instr_i', 'commit_ack_i', 'l1_icache_miss_i', 'l1_dcache_miss_i', 'itlb_miss_i', 'dtlb_miss_i', 'sb_full_i', 'if_empty_i', 'exception_t', 'ex_i', 'eret_i', 'bp_resolve_t', 'resolved_branch_i', 'exception_t', 'branch_exceptions_i', 'icache_dreq_t', 'l1_icache_access_i', 'dcache_req_i_t', 'l1_dcache_access_i', 'i_tlb_flush_i', 'stall_issue_i', 'mcountinhibit_i', ')'],
            'outputs': ['data_o', 'scoreboard_entry_t', 'commit_instr_i', 'commit_ack_i', 'l1_icache_miss_i', 'l1_dcache_miss_i', 'itlb_miss_i', 'dtlb_miss_i', 'sb_full_i', 'if_empty_i', 'exception_t', 'ex_i', 'eret_i', 'bp_resolve_t', 'resolved_branch_i', 'exception_t', 'branch_exceptions_i', 'icache_dreq_t', 'l1_icache_access_i', 'dcache_req_i_t', 'l1_dcache_access_i', 'i_tlb_flush_i', 'stall_issue_i', 'mcountinhibit_i', ')'],
            'internals': []
        },
        'pmp': {
            'inputs': ['addr_i', 'riscv::pmp_access_t', 'access_type_i', 'riscv::priv_lvl_t', 'priv_lvl_i', 'conf_addr_i', 'riscv::pmpcfg_t', 'conf_i', 'allow_o', ')'],
            'outputs': ['allow_o', ')'],
            'internals': []
        },
        'pmp_data_if': {
            'inputs': ['clk_i', 'rst_ni', 'icache_areq_t', 'icache_areq_i', 'icache_areq_t', 'icache_areq_o', 'icache_fetch_vaddr_i', 'lsu_valid_i', 'lsu_paddr_i', 'lsu_vaddr_i', 'exception_t', 'lsu_exception_i', 'lsu_is_store_i', 'lsu_valid_o', 'lsu_paddr_o', 'exception_t', 'lsu_exception_o', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_i', 'ld_st_v_i', 'riscv::pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', ')'],
            'outputs': ['icache_areq_t', 'icache_areq_o', 'icache_fetch_vaddr_i', 'lsu_valid_i', 'lsu_paddr_i', 'lsu_vaddr_i', 'exception_t', 'lsu_exception_i', 'lsu_is_store_i', 'lsu_valid_o', 'lsu_paddr_o', 'exception_t', 'lsu_exception_o', 'riscv::priv_lvl_t', 'priv_lvl_i', 'v_i', 'riscv::priv_lvl_t', 'ld_st_priv_lvl_i', 'ld_st_v_i', 'riscv::pmpcfg_t', 'pmpcfg_i', 'pmpaddr_i', ')'],
            'internals': []
        },
        'pmp_entry': {
            'inputs': ['addr_i', 'conf_addr_i', 'conf_addr_prev_i', 'riscv::pmp_addr_mode_t', 'conf_addr_mode_i', 'match_o', ')'],
            'outputs': ['match_o', ')'],
            'internals': []
        },
        'pmp_tb': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ras': {
            'inputs': ['clk_i', 'rst_ni', 'flush_bp_i', 'push_i', 'pop_i', 'data_i', 'ras_t', 'data_o', ')'],
            'outputs': ['ras_t', 'data_o', ')'],
            'internals': []
        },
        'raw_checker': {
            'inputs': ['clk_i', 'rst_ni', 'rs_i', 'rs_fpr_i', 'rd_i', 'rd_fpr_i', 'still_issued_i', 'issue_pointer_i', 'idx_o', 'valid_o', ')'],
            'outputs': ['idx_o', 'valid_o', ')'],
            'internals': []
        },
        'scoreboard': {
            'inputs': ['clk_i', 'rst_ni', 'sb_full_o', 'flush_unissued_instr_i', 'flush_i', 'x_transaction_accepted_i', 'x_issue_writeback_i', 'x_id_i', 'scoreboard_entry_t', 'commit_instr_o', 'commit_drop_o', 'commit_ack_i', 'scoreboard_entry_t', 'decoded_instr_i', 'orig_instr_i', 'decoded_instr_valid_i', 'decoded_instr_ack_o', 'scoreboard_entry_t', 'issue_instr_o', 'orig_instr_o', 'issue_instr_valid_o', 'issue_ack_i', 'forwarding_t', 'fwd_o', 'bp_resolve_t', 'resolved_branch_i', 'trans_id_i', 'wbdata_i', 'exception_t', 'ex_i', 'wt_valid_i', 'x_we_i', 'x_rd_i', 'rvfi_issue_pointer_o', 'rvfi_commit_pointer_o', ')'],
            'outputs': ['sb_full_o', 'flush_unissued_instr_i', 'flush_i', 'x_transaction_accepted_i', 'x_issue_writeback_i', 'x_id_i', 'scoreboard_entry_t', 'commit_instr_o', 'commit_drop_o', 'commit_ack_i', 'scoreboard_entry_t', 'decoded_instr_i', 'orig_instr_i', 'decoded_instr_valid_i', 'decoded_instr_ack_o', 'scoreboard_entry_t', 'issue_instr_o', 'orig_instr_o', 'issue_instr_valid_o', 'issue_ack_i', 'forwarding_t', 'fwd_o', 'bp_resolve_t', 'resolved_branch_i', 'trans_id_i', 'wbdata_i', 'exception_t', 'ex_i', 'wt_valid_i', 'x_we_i', 'x_rd_i', 'rvfi_issue_pointer_o', 'rvfi_commit_pointer_o', ')'],
            'internals': []
        },
        'serdiv': {
            'inputs': ['clk_i', 'rst_ni', 'id_i', 'op_a_i', 'op_b_i', 'opcode_i', 'in_vld_i', 'in_rdy_o', 'flush_i', 'out_vld_o', 'out_rdy_i', 'id_o', 'res_o', ')', '=', '&', 'op_a_sign)', '?', "1'b1}", ':', 'op_a_i', '=', '&', 'op_b_sign)', '?', '~op_b_i', ':', 'op_b_i'],
            'outputs': ['in_rdy_o', 'flush_i', 'out_vld_o', 'out_rdy_i', 'id_o', 'res_o', ')'],
            'internals': []
        },
        'std_cache_subsystem': {
            'inputs': ['clk_i', 'rst_ni', 'riscv::priv_lvl_t', 'priv_lvl_i', 'icache_en_i', 'icache_flush_i', 'icache_miss_o', 'icache_areq_t', 'icache_areq_i', 'icache_arsp_t', 'icache_areq_o', 'icache_dreq_t', 'icache_dreq_i', 'icache_drsp_t', 'icache_dreq_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'wbuffer_empty_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'outputs': ['icache_miss_o', 'icache_areq_t', 'icache_areq_i', 'icache_arsp_t', 'icache_areq_o', 'icache_dreq_t', 'icache_dreq_i', 'icache_drsp_t', 'icache_dreq_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'wbuffer_empty_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'axi_req_t', 'axi_req_o', 'axi_rsp_t', 'axi_resp_i', ')'],
            'internals': []
        },
        'std_nbdcache': {
            'inputs': ['clk_i', 'rst_ni', 'enable_i', 'flush_i', 'flush_ack_o', 'miss_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'dcache_req_i_t', 'req_ports_i', 'dcache_req_o_t', 'req_ports_o', 'axi_req_t', 'axi_data_o', 'axi_rsp_t', 'axi_data_i', 'axi_req_t', 'axi_bypass_o', 'axi_rsp_t', 'axi_bypass_i', ')'],
            'outputs': ['flush_ack_o', 'miss_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'dcache_req_i_t', 'req_ports_i', 'dcache_req_o_t', 'req_ports_o', 'axi_req_t', 'axi_data_o', 'axi_rsp_t', 'axi_data_i', 'axi_req_t', 'axi_bypass_o', 'axi_rsp_t', 'axi_bypass_i', ')'],
            'internals': []
        },
        'store_buffer': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'stall_st_pending_i', 'no_st_pending_o', 'store_buffer_empty_o', 'page_offset_i', 'page_offset_matches_o', 'commit_i', 'commit_ready_o', 'ready_o', 'valid_i', 'valid_without_flush_i', 'paddr_i', 'rvfi_mem_paddr_o', 'data_i', 'be_i', 'data_size_i', 'dcache_req_o_t', 'req_port_i', 'dcache_req_i_t', 'req_port_o', ')'],
            'outputs': ['no_st_pending_o', 'store_buffer_empty_o', 'page_offset_i', 'page_offset_matches_o', 'commit_i', 'commit_ready_o', 'ready_o', 'valid_i', 'valid_without_flush_i', 'paddr_i', 'rvfi_mem_paddr_o', 'data_i', 'be_i', 'data_size_i', 'dcache_req_o_t', 'req_port_i', 'dcache_req_i_t', 'req_port_o', ')'],
            'internals': []
        },
        'store_unit': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'stall_st_pending_i', 'no_st_pending_o', 'store_buffer_empty_o', 'valid_i', 'lsu_ctrl_t', 'lsu_ctrl_i', 'pop_st_o', 'commit_i', 'commit_ready_o', 'amo_valid_commit_i', 'valid_o', 'trans_id_o', 'result_o', 'exception_t', 'ex_o', 'translation_req_o', 'vaddr_o', 'rvfi_mem_paddr_o', 'tinst_o', 'hs_ld_st_inst_o', 'hlvx_inst_o', 'paddr_i', 'exception_t', 'ex_i', 'dtlb_hit_i', 'page_offset_i', 'page_offset_matches_o', 'amo_req_t', 'amo_req_o', 'amo_resp_t', 'amo_resp_i', 'dcache_req_o_t', 'req_port_i', 'dcache_req_i_t', 'req_port_o', ')'],
            'outputs': ['no_st_pending_o', 'store_buffer_empty_o', 'valid_i', 'lsu_ctrl_t', 'lsu_ctrl_i', 'pop_st_o', 'commit_i', 'commit_ready_o', 'amo_valid_commit_i', 'valid_o', 'trans_id_o', 'result_o', 'exception_t', 'ex_o', 'translation_req_o', 'vaddr_o', 'rvfi_mem_paddr_o', 'tinst_o', 'hs_ld_st_inst_o', 'hlvx_inst_o', 'paddr_i', 'exception_t', 'ex_i', 'dtlb_hit_i', 'page_offset_i', 'page_offset_matches_o', 'amo_req_t', 'amo_req_o', 'amo_resp_t', 'amo_resp_i', 'dcache_req_o_t', 'req_port_i', 'dcache_req_i_t', 'req_port_o', ')'],
            'internals': []
        },
        'tag_cmp': {
            'inputs': ['clk_i', 'rst_ni', 'req_i', 'gnt_o', 'addr_i', 'l_data_t', 'wdata_i', 'we_i', 'l_be_t', 'be_i', 'l_data_t', 'rdata_o', 'tag_i', 'hit_way_o', 'req_o', 'addr_o', 'l_data_t', 'wdata_o', 'we_o', 'l_be_t', 'be_o', 'l_data_t', 'rdata_i', ')'],
            'outputs': ['gnt_o', 'addr_i', 'l_data_t', 'wdata_i', 'we_i', 'l_be_t', 'be_i', 'l_data_t', 'rdata_o', 'tag_i', 'hit_way_o', 'req_o', 'addr_o', 'l_data_t', 'wdata_o', 'we_o', 'l_be_t', 'be_o', 'l_data_t', 'rdata_i', ')'],
            'internals': []
        },
        'takes': {
            'inputs': ['clk_i', 'rst_ni', 'flush_i', 'valid_i', 'serving_unaligned_o', 'address_i', 'data_i', 'valid_o', 'addr_o', 'instr_o', ')'],
            'outputs': ['serving_unaligned_o', 'address_i', 'data_i', 'valid_o', 'addr_o', 'instr_o', ')'],
            'internals': []
        },
        'to': {
            'inputs': ['clk_i', 'rst_ni', 'icache_data_req_i', 'icache_data_ack_o', 'icache_req_t', 'icache_data_i', 'icache_rtrn_vld_o', 'icache_rtrn_t', 'icache_rtrn_o', 'dcache_data_req_i', 'dcache_data_ack_o', 'dcache_req_t', 'dcache_data_i', 'dcache_rtrn_vld_o', 'dcache_rtrn_t', 'dcache_rtrn_o', 'l15_req_t', 'l15_req_o', 'l15_rtrn_t', 'l15_rtrn_i', ')'],
            'outputs': ['icache_data_ack_o', 'icache_req_t', 'icache_data_i', 'icache_rtrn_vld_o', 'icache_rtrn_t', 'icache_rtrn_o', 'dcache_data_req_i', 'dcache_data_ack_o', 'dcache_req_t', 'dcache_data_i', 'dcache_rtrn_vld_o', 'dcache_rtrn_t', 'dcache_rtrn_o', 'l15_req_t', 'l15_req_o', 'l15_rtrn_t', 'l15_rtrn_i', ')'],
            'internals': []
        },
        'trigger_module': {
            'inputs': ['clk_i', 'rst_ni', 'scoreboard_entry_t', 'commit_instr_i', 'commit_ack_i', 'exception_t', 'ex_i', 'riscv::priv_lvl_t', 'priv_lvl_i', 'debug_mode_i', 'mret_i', 'sret_i', 'vaddr_from_lsu_i', 'orig_instr_i', 'store_result_i', 'scontext_i', 'tdata1_i', 'tdata2_i', 'tdata3_i', 'tselect_i', 'tselect_we', 'tdata1_we', 'tdata2_we', 'tdata3_we', 'tselect_o', 'tdata1_o', 'tdata2_o', 'tdata3_o', 'flush_o', 'break_from_trigger_o', 'debug_from_trigger_o', 'debug_from_mcontrol_o', ')'],
            'outputs': ['tselect_o', 'tdata1_o', 'tdata2_o', 'tdata3_o', 'flush_o', 'break_from_trigger_o', 'debug_from_trigger_o', 'debug_from_mcontrol_o', ')'],
            'internals': []
        },
        'wt_cache_subsystem': {
            'inputs': ['clk_i', 'rst_ni', 'icache_en_i', 'icache_flush_i', 'icache_miss_o', 'icache_areq_t', 'icache_areq_i', 'icache_arsp_t', 'icache_areq_o', 'icache_dreq_t', 'icache_dreq_i', 'icache_drsp_t', 'icache_dreq_o', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'miss_vld_bits_o', 'amo_req_t', 'dcache_amo_req_i', 'amo_resp_t', 'dcache_amo_resp_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'noc_req_t', 'noc_req_o', 'noc_resp_t', 'noc_resp_i', 'inval_addr_i', 'inval_valid_i', 'inval_ready_o', ')'],
            'outputs': ['icache_miss_o', 'icache_areq_t', 'icache_areq_i', 'icache_arsp_t', 'icache_areq_o', 'icache_dreq_t', 'icache_dreq_i', 'icache_drsp_t', 'icache_dreq_o', 'dcache_enable_i', 'dcache_flush_i', 'dcache_flush_ack_o', 'dcache_miss_o', 'miss_vld_bits_o', 'amo_req_t', 'dcache_amo_req_i', 'amo_resp_t', 'dcache_amo_resp_o', 'dcache_req_i_t', 'dcache_req_ports_i', 'dcache_req_o_t', 'dcache_req_ports_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'noc_req_t', 'noc_req_o', 'noc_resp_t', 'noc_resp_i', 'inval_addr_i', 'inval_valid_i', 'inval_ready_o', ')'],
            'internals': []
        },
        'wt_dcache': {
            'inputs': ['clk_i', 'rst_ni', 'enable_i', 'flush_i', 'flush_ack_o', 'miss_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'dcache_req_i_t', 'req_ports_i', 'dcache_req_o_t', 'req_ports_o', 'miss_vld_bits_o', 'mem_rtrn_vld_i', 'dcache_rtrn_t', 'mem_rtrn_i', 'mem_data_req_o', 'mem_data_ack_i', 'dcache_req_t', 'mem_data_o', ')'],
            'outputs': ['flush_ack_o', 'miss_o', 'wbuffer_empty_o', 'wbuffer_not_ni_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'dcache_req_i_t', 'req_ports_i', 'dcache_req_o_t', 'req_ports_o', 'miss_vld_bits_o', 'mem_rtrn_vld_i', 'dcache_rtrn_t', 'mem_rtrn_i', 'mem_data_req_o', 'mem_data_ack_i', 'dcache_req_t', 'mem_data_o', ')'],
            'internals': []
        },
        'wt_dcache_ctrl': {
            'inputs': ['clk_i', 'rst_ni', 'cache_en_i', 'dcache_req_i_t', 'req_port_i', 'dcache_req_o_t', 'req_port_o', 'miss_req_o', 'miss_ack_i', 'miss_we_o', 'miss_wdata_o', 'miss_wuser_o', 'miss_vld_bits_o', 'miss_paddr_o', 'miss_nc_o', 'miss_size_o', 'miss_id_o', 'miss_replay_i', 'miss_rtrn_vld_i', 'wr_cl_vld_i', 'rd_tag_o', 'rd_idx_o', 'rd_off_o', 'rd_req_o', 'rd_tag_only_o', 'rd_ack_i', 'rd_data_i', 'rd_user_i', 'rd_vld_bits_i', 'rd_hit_oh_i', ')'],
            'outputs': ['dcache_req_o_t', 'req_port_o', 'miss_req_o', 'miss_ack_i', 'miss_we_o', 'miss_wdata_o', 'miss_wuser_o', 'miss_vld_bits_o', 'miss_paddr_o', 'miss_nc_o', 'miss_size_o', 'miss_id_o', 'miss_replay_i', 'miss_rtrn_vld_i', 'wr_cl_vld_i', 'rd_tag_o', 'rd_idx_o', 'rd_off_o', 'rd_req_o', 'rd_tag_only_o', 'rd_ack_i', 'rd_data_i', 'rd_user_i', 'rd_vld_bits_i', 'rd_hit_oh_i', ')'],
            'internals': []
        },
        'wt_dcache_mem': {
            'inputs': ['clk_i', 'rst_ni', 'rd_tag_i', 'rd_idx_i', 'rd_off_i', 'rd_req_i', 'rd_tag_only_i', 'rd_prio_i', 'rd_ack_o', 'rd_vld_bits_o', 'rd_hit_oh_o', 'rd_data_o', 'rd_user_o', 'wr_cl_vld_i', 'wr_cl_nc_i', 'wr_cl_we_i', 'wr_cl_tag_i', 'wr_cl_idx_i', 'wr_cl_off_i', 'wr_cl_data_i', 'wr_cl_user_i', 'wr_cl_data_be_i', 'wr_vld_bits_i', 'wr_req_i', 'wr_ack_o', 'wr_idx_i', 'wr_off_i', 'wr_data_i', 'wr_user_i', 'wr_data_be_i', 'wbuffer_t', 'wbuffer_data_i', ')', 'in)'],
            'outputs': ['rd_ack_o', 'rd_vld_bits_o', 'rd_hit_oh_o', 'rd_data_o', 'rd_user_o', 'wr_cl_vld_i', 'wr_cl_nc_i', 'wr_cl_we_i', 'wr_cl_tag_i', 'wr_cl_idx_i', 'wr_cl_off_i', 'wr_cl_data_i', 'wr_cl_user_i', 'wr_cl_data_be_i', 'wr_vld_bits_i', 'wr_req_i', 'wr_ack_o', 'wr_idx_i', 'wr_off_i', 'wr_data_i', 'wr_user_i', 'wr_data_be_i', 'wbuffer_t', 'wbuffer_data_i', ')'],
            'internals': []
        },
        'wt_dcache_missunit': {
            'inputs': ['clk_i', 'rst_ni', 'enable_i', 'flush_i', 'flush_ack_o', 'miss_o', 'wbuffer_empty_i', 'cache_en_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'miss_req_i', 'miss_ack_o', 'miss_nc_i', 'miss_we_i', 'miss_wdata_i', 'miss_wuser_i', 'miss_paddr_i', 'miss_vld_bits_i', 'miss_size_i', 'miss_id_i', 'miss_replay_o', 'miss_rtrn_vld_o', 'miss_rtrn_id_o', 'tx_paddr_i', 'tx_vld_i', 'wr_cl_vld_o', 'wr_cl_nc_o', 'wr_cl_we_o', 'wr_cl_tag_o', 'wr_cl_idx_o', 'wr_cl_off_o', 'wr_cl_data_o', 'wr_cl_user_o', 'wr_cl_data_be_o', 'wr_vld_bits_o', 'mem_rtrn_vld_i', 'dcache_rtrn_t', 'mem_rtrn_i', 'mem_data_req_o', 'mem_data_ack_i', 'dcache_req_t', 'mem_data_o', ')', 'in)', 'paddr', 'size)'],
            'outputs': ['flush_ack_o', 'miss_o', 'wbuffer_empty_i', 'cache_en_o', 'amo_req_t', 'amo_req_i', 'amo_resp_t', 'amo_resp_o', 'miss_req_i', 'miss_ack_o', 'miss_nc_i', 'miss_we_i', 'miss_wdata_i', 'miss_wuser_i', 'miss_paddr_i', 'miss_vld_bits_i', 'miss_size_i', 'miss_id_i', 'miss_replay_o', 'miss_rtrn_vld_o', 'miss_rtrn_id_o', 'tx_paddr_i', 'tx_vld_i', 'wr_cl_vld_o', 'wr_cl_nc_o', 'wr_cl_we_o', 'wr_cl_tag_o', 'wr_cl_idx_o', 'wr_cl_off_o', 'wr_cl_data_o', 'wr_cl_user_o', 'wr_cl_data_be_o', 'wr_vld_bits_o', 'mem_rtrn_vld_i', 'dcache_rtrn_t', 'mem_rtrn_i', 'mem_data_req_o', 'mem_data_ack_i', 'dcache_req_t', 'mem_data_o', ')'],
            'internals': []
        },
        'wt_dcache_wbuffer': {
            'inputs': ['clk_i', 'rst_ni', 'cache_en_i', 'empty_o', 'not_ni_o', 'dcache_req_i_t', 'req_port_i', 'dcache_req_o_t', 'req_port_o', 'miss_ack_i', 'miss_paddr_o', 'miss_req_o', 'miss_we_o', 'miss_wdata_o', 'miss_wuser_o', 'miss_vld_bits_o', 'miss_nc_o', 'miss_size_o', 'miss_id_o', 'miss_rtrn_vld_i', 'miss_rtrn_id_i', 'rd_tag_o', 'rd_idx_o', 'rd_off_o', 'rd_req_o', 'rd_tag_only_o', 'rd_ack_i', 'rd_data_i', 'rd_vld_bits_i', 'rd_hit_oh_i', 'wr_cl_vld_i', 'wr_cl_idx_i', 'wr_req_o', 'wr_ack_i', 'wr_idx_o', 'wr_off_o', 'wr_data_o', 'wr_data_be_o', 'wr_user_o', 'wbuffer_t', 'wbuffer_data_o', 'tx_paddr_o', 'tx_vld_o', ')', 'offset', 'size)', 'offset', 'size)', 'data', 'offset', 'size)', 'data', 'offset', 'size)'],
            'outputs': ['empty_o', 'not_ni_o', 'dcache_req_i_t', 'req_port_i', 'dcache_req_o_t', 'req_port_o', 'miss_ack_i', 'miss_paddr_o', 'miss_req_o', 'miss_we_o', 'miss_wdata_o', 'miss_wuser_o', 'miss_vld_bits_o', 'miss_nc_o', 'miss_size_o', 'miss_id_o', 'miss_rtrn_vld_i', 'miss_rtrn_id_i', 'rd_tag_o', 'rd_idx_o', 'rd_off_o', 'rd_req_o', 'rd_tag_only_o', 'rd_ack_i', 'rd_data_i', 'rd_vld_bits_i', 'rd_hit_oh_i', 'wr_cl_vld_i', 'wr_cl_idx_i', 'wr_req_o', 'wr_ack_i', 'wr_idx_o', 'wr_off_o', 'wr_data_o', 'wr_data_be_o', 'wr_user_o', 'wbuffer_t', 'wbuffer_data_o', 'tx_paddr_o', 'tx_vld_o', ')'],
            'internals': []
        },
        'zcmt_decoder': {
            'inputs': ['clk_i', 'rst_ni', 'instr_i', 'pc_i', 'is_zcmt_instr_i', 'illegal_instr_i', 'is_compressed_i', 'jvt_t', 'jvt_i', 'dcache_req_o_t', 'req_port_i', 'instr_o', 'illegal_instr_o', 'is_compressed_o', 'fetch_stall_o', 'dcache_req_i_t', 'req_port_o', 'jump_address_o', ')'],
            'outputs': ['instr_o', 'illegal_instr_o', 'is_compressed_o', 'fetch_stall_o', 'dcache_req_i_t', 'req_port_o', 'jump_address_o', ')'],
            'internals': []
        },
    },
    
# Copy this into classify_signals.py PROCESSOR_SIGNALS dict

    'RSD': {
        'ActiveList': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Axi4LiteDualPortBlockRAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Axi4LitePlToPsControlRegister': {
            'inputs': ['we', 'SerialDataPath', 'wv', 'PC_Path', 'lastCommittedPC', ')'],
            'outputs': ['AddrPath', 'memory_addr', 'MemoryEntryDataPath', 'memory_data', 'memory_we', 'done', ')'],
            'internals': []
        },
        'Axi4Memory': {
            'inputs': ['AddrPath', 'memAccessAddr', 'MemoryEntryDataPath', 'memAccessWriteData', 'memAccessRE', 'memAccessWE', 'memAccessReadBusy', 'memAccessWriteBusy', 'MemAccessSerial', 'nextMemReadSerial', 'MemWriteSerial', 'nextMemWriteSerial', 'memReadDataReady', 'MemoryEntryDataPath', 'memReadData', 'MemAccessSerial', 'memReadSerial', 'MemAccessResponse', 'memAccessResponse', ')', 'bit_depth)'],
            'outputs': ['memAccessReadBusy', 'memAccessWriteBusy', 'MemAccessSerial', 'nextMemReadSerial', 'MemWriteSerial', 'nextMemWriteSerial', 'memReadDataReady', 'MemoryEntryDataPath', 'memReadData', 'MemAccessSerial', 'memReadSerial', 'MemAccessResponse', 'memAccessResponse', ')'],
            'internals': []
        },
        'BTB': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Bimodal': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'BitCounter': {
            'inputs': ['DataPath', 'fuOpA_In', 'DataPath', 'dataOut', ')', 'clk', 'rst', 'stall', 'DataPath', 'fuOpA_In', 'DataPath', 'dataOut', ')'],
            'outputs': ['DataPath', 'dataOut', ')', 'DataPath', 'dataOut', ')'],
            'internals': []
        },
        'BlockDualPortRAM': {
            'inputs': ['clk', 'we', 'wa', 'wv', 'ra', 'rv', ')', 'clk', ')', 'clk', ')', 'clk', 'we', 'wa', 'wv', 'ra', 'rv', ')', 'clk', 'we', 'wa', 'wv', 'ra', 'rv', ')', 'clk', 'we', 'wa', 'wv', 'ra', 'rv', ')', 'clk', 'we', 'rwa', 'wv', 'rv', ')', 'clk', 'we', 'wa', 'wv', 'ra', 'rv', ')', 'clk', 'we', 'wa', 'wv', 'ra', 'rv', ')', 'clk', 'we', '0', 'rwa', '0', 'wv', '0', '0', ')', 'clk', 'WRITE_NUM', ')', 'clk', ')', 'clk', 'WRITE_NUM', ')', 'clk', ')', 'clk', ')', 'clk', ')', 'clk', ')', 'clk', ')'],
            'outputs': ['rv', ')', ')', ')', 'rv', ')', 'rv', ')', 'rv', ')', 'rv', ')', 'rv', ')', 'rv', ')', '0', ')', ')', 'of', 'a', 'port(%x)', 'is', 'incorrect."', 'i)', ')', ')', 'of', 'a', 'port(%x)', 'is', 'incorrect."', 'i)', ')', ')', 'of', 'a', 'port(%x)', 'is', 'incorrect."', 'i)', ')', ')', ')', 'of', 'a', 'port(%x)', 'is', 'incorrect."', 'i)', ')', ')', ')', 'of', 'a', 'port(%x)', 'is', 'incorrect"', 'i)', ')', ')'],
            'internals': []
        },
        'BranchPredictor': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'BypassCtrlStage': {
            'inputs': ['clk', 'rst', 'PipelineControll', 'ctrl', 'BypassCtrlOperand', 'in', 'BypassCtrlOperand', 'out', ')', 'PRegNumPath', 'read', 'BypassCtrlOperand', 'intEX', 'INT_ISSUE_WIDTH', 'BypassCtrlOperand', 'intWB', 'INT_ISSUE_WIDTH', 'BypassCtrlOperand', 'memMA', 'LOAD_ISSUE_WIDTH', 'BypassCtrlOperand', 'memWB', 'LOAD_ISSUE_WIDTH', ')'],
            'outputs': ['BypassCtrlOperand', 'out', ')'],
            'internals': []
        },
        'BypassStage': {
            'inputs': ['clk', 'rst', 'PipelineControll', 'ctrl', 'BypassOperand', 'in', 'BypassOperand', 'out', ')', 'BypassSelect', 'sel', 'BypassOperand', 'intEX', 'INT_ISSUE_WIDTH', 'BypassOperand', 'intWB', 'INT_ISSUE_WIDTH', 'BypassOperand', 'memMA', 'LOAD_ISSUE_WIDTH', 'BypassOperand', 'memWB', 'LOAD_ISSUE_WIDTH', ')'],
            'outputs': ['BypassOperand', 'out', ')'],
            'internals': []
        },
        'CSR_Unit': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'CacheFlushManager': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'CommitStage': {
            'inputs': ['CommitLaneCountPath', 'finishedOpNum', 'ExecutionState', ')', 'ActiveListCountPath', 'activeListCount', 'ExecutionState', ')', 'last', ')', 'startCommit', 'ActiveListCountPath', 'activeListCount', 'ExecutionState', 'isBranch', 'isStore', 'unableToStartRecovery', ')'],
            'outputs': ['CommitLaneCountPath', 'finishedInsnRange', 'CommitLaneCountPath', 'finishedOpNum', 'ExecutionState', ')', 'CommitLaneCountPath', 'finishedOpNum', 'ActiveListCountPath', 'activeListCount', 'ExecutionState', ')', 'CommitLaneIndexPath', 'CommitLaneIndexPath', 'last', ')', 'toRecoveryPhase', 'CommitLaneIndexPath', 'recoveredIndex', 'RefetchType', 'refetchType', 'ExecutionState', 'recoveryCause', 'startCommit', 'ActiveListCountPath', 'activeListCount', 'ExecutionState', 'isBranch', 'isStore', 'unableToStartRecovery', ')'],
            'internals': []
        },
        'ComplexIntegerExecutionStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ComplexIntegerIssueStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ComplexIntegerRegisterReadStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ComplexIntegerRegisterWriteStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ControlQueue': {
            'inputs': ['clk', 'rst', 'push', 'pop', '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0', 'pushedData', 'full', 'empty', '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0', 'headData', ')'],
            'outputs': ['full', 'empty', '`PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0', 'headData', ')'],
            'internals': []
        },
        'Controller': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Core': {
            'inputs': ['clk', 'rst', 'rstStart', 'MemAccessSerial', 'nextMemReadSerial', 'MemWriteSerial', 'nextMemWriteSerial', 'MemoryEntryDataPath', 'memReadData', 'memReadDataReady', 'MemAccessSerial', 'memReadSerial', 'MemAccessResponse', 'memAccessResponse', 'memAccessReadBusy', 'memAccessWriteBusy', 'reqExternalInterrupt', 'ExternalInterruptCodePath', 'externalInterruptCode', 'DebugRegister', 'debugRegister', 'PC_Path', 'lastCommittedPC', 'PhyAddrPath', 'memAccessAddr', 'MemoryEntryDataPath', 'memAccessWriteData', 'memAccessRE', 'memAccessWE', 'serialWE', 'SerialDataPath', 'serialWriteData', ')'],
            'outputs': ['DebugRegister', 'debugRegister', 'PC_Path', 'lastCommittedPC', 'PhyAddrPath', 'memAccessAddr', 'MemoryEntryDataPath', 'memAccessWriteData', 'memAccessRE', 'memAccessWE', 'serialWE', 'SerialDataPath', 'serialWriteData', ')'],
            'internals': []
        },
        'DCacheController': {
            'inputs': ['DCacheLinePath', 'fetchedLine', 'DCacheLinePath', 'storedLine', 'storedDirty', ')', 'PhyAddrPath', 'addr)', 'PhyAddrPath', 'addr)', 'PhyAddrPath', 'addr)', 'PhyAddrPath', 'addr)', 'DCacheIndexPath', 'index', 'DCacheTagPath', 'tag)', 'PhyAddrPath', 'addr)'],
            'outputs': ['DCacheLinePath', 'dstLine', 'DCacheLinePath', 'fetchedLine', 'DCacheLinePath', 'storedLine', 'storedDirty', ')'],
            'internals': []
        },
        'Debug': {
            'inputs': [],
            'outputs': ['PC_Path', 'lastCommittedPC', ')'],
            'internals': []
        },
        'DecodedBranchResolver': {
            'inputs': ['clk', 'rst', 'stall', 'decodeComplete', 'RISCV_ISF_Common', ':', 'isf', 'BranchPred', ':', 'brPredIn', 'PC_Path', 'InsnInfo', ':', 'insnInfo', 'flushTriggered', 'BranchPred', 'PC_Path', 'recoveredPC', ')'],
            'outputs': ['flushTriggered', 'BranchPred', 'PC_Path', 'recoveredPC', ')'],
            'internals': []
        },
        'Decoder': {
            'inputs': ['OpInfo', 'src', 'MicroOpIndex', 'mid', 'split', 'last', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'RISCV_ISF_Common', 'isf', ')', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'RISCV_ISF_Common', 'isf', ')', 'illegalPC', ')', 'RISCV_ISF_Common', 'isf', 'illegalPC', ')', 'InsnPath', 'insn', 'illegalPC', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', ')'],
            'outputs': ['OpInfo', 'op', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'RISCV_ISF_Common', 'isf', 'LScalarRegNumPath', 'srcRegNumA', 'LScalarRegNumPath', 'srcRegNumB', 'LScalarRegNumPath', 'dstRegNum', 'unsupported', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', ')', 'OpInfo', 'opInfo', 'illegalPC', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', 'RISCV_ISF_Common', 'isf', 'illegalPC', ')', 'OpInfo', 'microOps', 'InsnInfo', 'insnInfo', ')'],
            'internals': []
        },
        'DestinationRAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'DispatchStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Divider': {
            'inputs': ['clk', 'rst', 'req', 'DataPath', 'dividend', 'DataPath', 'divisor', 'isSigned', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')', 'clk', 'rst', 'req', 'DataPath', 'dividend', 'DataPath', 'divisor', 'isSigned', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')', 'DividerPath', 'dividend', ')'],
            'outputs': ['finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')'],
            'internals': []
        },
        'DividerUnit': {
            'inputs': ['clk', 'rst', 'req', 'DataPath', 'fuOpA_In', 'DataPath', 'fuOpB_In', 'IntDIV_Code', 'divCode', 'finished', 'DataPath', 'dataOut', ')', 'clk', 'stall', 'req', 'DataPath', 'fuOpA_In', 'DataPath', 'fuOpB_In', 'IntDIV_Code', 'divCode', 'finished', 'DataPath', 'dataOut', ')'],
            'outputs': ['finished', 'DataPath', 'dataOut', ')', 'finished', 'DataPath', 'dataOut', ')'],
            'internals': []
        },
        'FP32DivSqrter': {
            'inputs': ['clk', 'rst', 'lhs', 'rhs', 'is_divide', 'req', 'finished', 'result', ')'],
            'outputs': ['finished', 'result', ')'],
            'internals': []
        },
        'FP32PipelinedAdder': {
            'inputs': ['clk', 'lhs', 'rhs', 'result', ')', 'lhs', 'rhs', 'FAddStage1RegPath', 'stg0Out', ')', 'clk', 'FAddStage1RegPath', 'stg1In', 'FAddStage2RegPath', 'stg1Out', ')', 'x)', 'clk', 'FAddStage2RegPath', 'stg2In', 'result', ')'],
            'outputs': ['result', ')', 'FAddStage1RegPath', 'stg0Out', ')', 'FAddStage2RegPath', 'stg1Out', ')', 'result', ')'],
            'internals': []
        },
        'FP32PipelinedFMA': {
            'inputs': ['clk', 'mullhs', 'mulrhs', 'addend', 'result', ')', 'clk', 'FMAStage1RegPath', 'stg0Out', 'mullhs', 'mulrhs', 'addend', 'is_subtract', 'mlhs', 'mrhs', 'maddend', ')', 'clk', 'FMAStage1RegPath', 'stg1In', 'FMAStage2RegPath', 'stg1Out', ')', 'clk', 'FMAStage2RegPath', 'stg2In', 'FMAStage3RegPath', 'stg2Out', 'fma_result', ')', 'clk', 'FMAStage3RegPath', 'stg3In', 'FMAStage4RegPath', 'stg3Out', ')', 'clk', 'FMAStage4RegPath', 'stg4In', 'result', ')'],
            'outputs': ['result', ')', 'FMAStage1RegPath', 'stg0Out', 'mullhs', 'mulrhs', 'addend', 'is_subtract', 'mlhs', 'mrhs', 'maddend', ')', 'FMAStage2RegPath', 'stg1Out', ')', 'FMAStage3RegPath', 'stg2Out', 'fma_result', ')', 'FMAStage4RegPath', 'stg3Out', ')', 'result', ')'],
            'internals': []
        },
        'FP32PipelinedMultiplier': {
            'inputs': ['clk', 'lhs', 'rhs', 'result', ')', 'lhs', 'rhs', 'FMulStage1RegPath', 'stg0Out', ')', 'clk', 'FMulStage1RegPath', 'stg1In', 'FMulStage2RegPath', 'stg1Out', ')', 'clk', 'FMulStage2RegPath', 'stg2In', 'result', ')'],
            'outputs': ['result', ')', 'FMulStage1RegPath', 'stg0Out', ')', 'FMulStage2RegPath', 'stg1Out', ')', 'result', ')'],
            'internals': []
        },
        'FP32PipelinedOther': {
            'inputs': ['x', ')', 'lhs', 'fmt_unsigned', 'Rounding_Mode', 'rm', 'result', 'FFlags_Path', 'fflags', ')', 'lhs', 'fmt_unsigned', 'Rounding_Mode', 'rm', 'result', 'FFlags_Path', 'fflags', ')', 'clk', 'lhs', 'rhs', 'FPU_Code', 'fpuCode', 'Rounding_Mode', 'rm', 'result', 'FFlags_Path', 'fflags', ')'],
            'outputs': ['result', 'FFlags_Path', 'fflags', ')', 'result', 'FFlags_Path', 'fflags', ')', 'result', 'FFlags_Path', 'fflags', ')'],
            'internals': []
        },
        'FPDivSqrtUnit': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'FPExecutionStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'FPIssueStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'FPRegisterReadStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'FPRegisterWriteStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'FetchStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'FlipFlop': {
            'inputs': ['in', 'clk', 'rst', ')', 'in', 'we', 'clk', 'rst', ')'],
            'outputs': ['out', 'in', 'clk', 'rst', ')', 'out', 'in', 'we', 'clk', 'rst', ')'],
            'internals': []
        },
        'FreeList': {
            'inputs': ['clk', 'rst', 'push', 'pop', 'ENTRY_WIDTH-1:0', 'pushedData', 'full', 'empty', 'ENTRY_WIDTH-1:0', 'headData', ')', 'clk', 'rst', 'rstStart', 'push', 'PUSH_WIDTH', 'pop', 'POP_WIDTH', 'ENTRY_BIT_SIZE-1:0', 'pushedData', 'PUSH_WIDTH', '$clog2(SIZE):0', 'count', 'ENTRY_BIT_SIZE-1:0', 'poppedData', 'POP_WIDTH', ')'],
            'outputs': ['full', 'empty', 'ENTRY_WIDTH-1:0', 'headData', ')', '$clog2(SIZE):0', 'count', 'ENTRY_BIT_SIZE-1:0', 'poppedData', 'POP_WIDTH', ')'],
            'internals': []
        },
        'Gshare': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ICacheArray': {
            'inputs': ['clk', 'rst', 'rstStart', 'we', 'ICacheIndexPath', 'writeIndex', 'ICacheTagPath', 'writeTag', 'ICacheLinePath', 'writeLineData', 'ICacheIndexPath', 'readIndex', 'ICacheTagPath', 'readTag', 'ICacheLinePath', 'readLineData', 'hit', 'valid', ')', 'clk', 'rst', 'rstStart', 'ICacheIndexPath', 'writeIndex', 'ICacheWayPath', 'writeWay', 'writeHit', 'NRUAccessStatePath', 'writeNRUState', 'ICacheIndexPath', 'readIndex', 'NRUAccessStatePath', 'readNRUState', 'ICacheIndexPath', 'rstIndex', ')', 'hitIn', 'ICacheLineInsnIndexPath', 'headWordPtr', 'hitOut', 'FETCH_WIDTH', ')'],
            'outputs': ['ICacheLinePath', 'readLineData', 'hit', 'valid', ')', 'NRUAccessStatePath', 'readNRUState', 'ICacheIndexPath', 'rstIndex', ')', 'hitOut', 'FETCH_WIDTH', ')'],
            'internals': []
        },
        'IO_Unit': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'IntAdder': {
            'inputs': ['DataPath', 'srcA', 'invA', 'DataPath', 'srcB', 'invB', 'carryIn', ')', 'DataPath', 'src', 'inv', ')', 'IntALU_Code', 'aluCode', 'DataPath', 'fuOpA_In', 'DataPath', 'fuOpB_In', ')'],
            'outputs': ['IntAdderResult', 'dst', 'overflowOut', 'DataPath', 'srcA', 'invA', 'DataPath', 'srcB', 'invB', 'carryIn', ')', 'DataPath', 'aluDataOut', 'IntALU_Code', 'aluCode', 'DataPath', 'fuOpA_In', 'DataPath', 'fuOpB_In', ')'],
            'internals': []
        },
        'IntegerExecutionStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'IntegerIssueStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'IntegerRegisterReadStage': {
            'inputs': ['OpOperandType', 'opType', 'DataPath', 'DataPath', 'immV', 'DataPath', 'pcV', ')'],
            'outputs': [],
            'internals': []
        },
        'IntegerRegisterWriteStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'InterruptController': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'IssueQueue': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'LRU_Counter': {
            'inputs': ['clk', 'rst', 'INDEX_BIT_WIDTH-1:0', 'index', 'PORT_WIDTH', 'access', 'PORT_WIDTH', '$clog2(WAY_NUM)-1:0', 'accessWay', 'PORT_WIDTH', '$clog2(WAY_NUM)-1:0', 'leastRecentlyAccessedWay', 'PORT_WIDTH', ')'],
            'outputs': ['$clog2(WAY_NUM)-1:0', 'leastRecentlyAccessedWay', 'PORT_WIDTH', ')'],
            'internals': []
        },
        'LoadQueue': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'LoadStoreUnit': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Main': {
            'inputs': ['clk_p', 'clk_n', 'negResetIn', 'rxd', '`ifndef', 'RSD_DISABLE_DEBUG_REGISTER', 'DebugRegister', 'debugRegister', '`endif', '`ifdef', 'RSD_SYNTHESIS_ATLYS', 'DDR2CLK0', 'DDR2CLK1', 'DDR2CKE', 'DDR2RASN', 'DDR2CASN', 'DDR2WEN', 'DDR2RZQ', 'DDR2ZIO', 'DDR2LDM', 'DDR2UDM', 'DDR2ODT', 'DDR2BA', 'DDR2A', 'DDR2DQ', 'DDR2UDQS', 'DDR2UDQSN', 'DDR2LDQS', 'DDR2LDQSN', '`endif', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', ')'],
            'outputs': ['DebugRegister', 'debugRegister', '`endif', '`ifdef', 'RSD_SYNTHESIS_ATLYS', 'DDR2CLK0', 'DDR2CLK1', 'DDR2CKE', 'DDR2RASN', 'DDR2CASN', 'DDR2WEN', 'DDR2RZQ', 'DDR2ZIO', 'DDR2LDM', 'DDR2UDM', 'DDR2ODT', 'DDR2BA', 'DDR2A', 'DDR2DQ', 'DDR2UDQS', 'DDR2UDQSN', 'DDR2LDQS', 'DDR2LDQSN', '`endif', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', ')'],
            'internals': []
        },
        'Main_Zynq': {
            'inputs': ['clk', 'negResetIn', 'LED_Path', 'ledOut', '`else', 'clk_p', 'clk_n', 'negResetIn', 'rxd', '`endif', '`ifndef', 'RSD_DISABLE_DEBUG_REGISTER', 'DebugRegister', 'debugRegister', '`endif', '`ifdef', 'RSD_USE_EXTERNAL_MEMORY', 'Axi4MemoryIF', 'axi4MemoryIF', '`endif', '`ifdef', 'RSD_SYNTHESIS_ZEDBOARD', 'Axi4LiteControlRegisterIF', 'axi4LitePlToPsControlRegisterIF', 'Axi4LiteControlRegisterIF', 'axi4LitePsToPlControlRegisterIF', '`else', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', '`endif', ')'],
            'outputs': ['LED_Path', 'ledOut', '`else', 'clk_p', 'clk_n', 'negResetIn', 'rxd', '`endif', '`ifndef', 'RSD_DISABLE_DEBUG_REGISTER', 'DebugRegister', 'debugRegister', '`endif', '`ifdef', 'RSD_USE_EXTERNAL_MEMORY', 'Axi4MemoryIF', 'axi4MemoryIF', '`endif', '`ifdef', 'RSD_SYNTHESIS_ZEDBOARD', 'Axi4LiteControlRegisterIF', 'axi4LitePlToPsControlRegisterIF', 'Axi4LiteControlRegisterIF', 'axi4LitePsToPlControlRegisterIF', '`else', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', '`endif', ')'],
            'internals': []
        },
        'Memory': {
            'inputs': ['clk', 'rst', 'AddrPath', 'memAccessAddr', 'MemoryEntryDataPath', 'memAccessWriteData', 'memAccessRE', 'memAccessWE', 'memAccessBusy', 'MemAccessSerial', 'nextMemReadSerial', 'MemWriteSerial', 'nextMemWriteSerial', 'memReadDataReady', 'MemoryEntryDataPath', 'memReadData', 'MemAccessSerial', 'memReadSerial', 'MemAccessResponse', 'memAccessResponse', ')'],
            'outputs': ['memAccessBusy', 'MemAccessSerial', 'nextMemReadSerial', 'MemWriteSerial', 'nextMemWriteSerial', 'memReadDataReady', 'MemoryEntryDataPath', 'memReadData', 'MemAccessSerial', 'memReadSerial', 'MemAccessResponse', 'memAccessResponse', ')'],
            'internals': []
        },
        'MemoryAccessController': {
            'inputs': ['MemAccessSerial', 'nextMemReadSerial', 'MemWriteSerial', 'nextMemWriteSerial', 'MemoryEntryDataPath', 'memReadData', 'memReadDataReady', 'MemAccessSerial', 'memReadSerial', 'MemAccessResponse', 'memAccessResponse', 'memAccessReadBusy', 'memAccessWriteBusy', 'PhyAddrPath', 'memAccessAddr', 'MemoryEntryDataPath', 'memAccessWriteData', 'memAccessRE', 'memAccessWE', ')'],
            'outputs': ['PhyAddrPath', 'memAccessAddr', 'MemoryEntryDataPath', 'memAccessWriteData', 'memAccessRE', 'memAccessWE', ')'],
            'internals': []
        },
        'MemoryAccessStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'MemoryDependencyPredictor': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'MemoryExecutionStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'MemoryIssueStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'MemoryLatencySimulator': {
            'inputs': ['clk', 'rst', 'push', 'MemoryLatencySimRequestPath', 'pushedData', 'hasRequest', 'MemoryLatencySimRequestPath', 'requestData', ')'],
            'outputs': ['hasRequest', 'MemoryLatencySimRequestPath', 'requestData', ')'],
            'internals': []
        },
        'MemoryReadReqQueue': {
            'inputs': ['clk', 'rst', 'push', 'pop', 'MemoryReadReq', 'pushedData', 'full', 'empty', 'MemoryReadReq', 'headData', ')'],
            'outputs': ['full', 'empty', 'MemoryReadReq', 'headData', ')'],
            'internals': []
        },
        'MemoryRegisterReadStage': {
            'inputs': ['OpOperandType', 'opType', 'DataPath', 'DataPath', 'immV', 'DataPath', 'pcV', ')'],
            'outputs': [],
            'internals': []
        },
        'MemoryRegisterWriteStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'MemoryTagAccessStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'MemoryWriteDataQueue': {
            'inputs': ['clk', 'rst', 'push', 'pop', 'MemoryEntryDataPath', 'pushedData', 'full', 'empty', 'MemoryEntryDataPath', 'headData', 'headPtr', 'tailPtr', ')'],
            'outputs': ['full', 'empty', 'MemoryEntryDataPath', 'headData', 'headPtr', 'tailPtr', ')'],
            'internals': []
        },
        'MicroOpPicker': {
            'inputs': ['AllDecodedMicroOpPath', 'req', 'AllDecodedMicroOpPath', 'serialize', 'AllDecodedMicroOpIndex', 'AllDecodedMicroOpPath', 'next', ')'],
            'outputs': ['AllDecodedMicroOpIndex', 'AllDecodedMicroOpPath', 'next', ')'],
            'internals': []
        },
        'MulDivUnit': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Multiplier': {
            'inputs': ['BIT_WIDTH-1:0', 'srcA', 'BIT_WIDTH-1:0', 'srcB', '2*BIT_WIDTH-1:', 'dst', ')', 'BIT_WIDTH-1:0', 'in', 'sign', 'BIT_WIDTH:0', 'out', ')', 'clk', 'stall', 'BIT_WIDTH-1:0', 'srcA', 'BIT_WIDTH-1:0', 'srcB', 'signA', 'signB', '2*BIT_WIDTH-1:0', 'dst', ')'],
            'outputs': ['2*BIT_WIDTH-1:', 'dst', ')', 'BIT_WIDTH:0', 'out', ')', '2*BIT_WIDTH-1:0', 'dst', ')'],
            'internals': []
        },
        'MultiplierUnit': {
            'inputs': ['DataPath', 'fuOpA_In', 'DataPath', 'fuOpB_In', 'getUpper', 'DataPath', 'dataOut', ')', 'clk', 'stall', 'DataPath', 'fuOpA_In', 'DataPath', 'fuOpB_In', 'getUpper', 'IntMUL_Code', 'mulCode', 'DataPath', 'dataOut', ')'],
            'outputs': ['DataPath', 'dataOut', ')', 'DataPath', 'dataOut', ')'],
            'internals': []
        },
        'NextPCStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'OrgShifter': {
            'inputs': ['ShiftOperandType', 'shiftOperandType', 'ShiftType', 'shiftType', 'ShiftAmountPath', 'immShiftAmount', 'ShiftAmountPath', 'DataPath', 'dataIn', 'carryIn', 'DataPath', 'dataOut', 'carryOut', ')', 'ShiftType', 'shiftType', 'ShiftAmountPath', 'shiftAmount', 'DataPath', 'dataIn', 'shiftIn', 'carryIn', ')', 'ShiftOperandType', 'shiftOperandType', 'ShiftType', 'shiftType', 'ShiftAmountPath', 'immShiftAmount', 'ShiftAmountPath', 'DataPath', 'dataIn', 'carryIn', 'DataPath', 'dataOut', 'carryOut', ')'],
            'outputs': ['DataPath', 'dataOut', 'carryOut', ')', 'DataPath', 'dataOut', 'carryOut', ')'],
            'internals': []
        },
        'PC': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'PerformanceCounter': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Picker': {
            'inputs': ['req', 'grant', ')', 'req', 'grant', ')', 'headPtr', 'tailPtr', 'request', 'grantPtr', 'picked', ')', 'shiftIn', 'shiftAmount', 'shiftOut', ')', 'shiftIn', 'shiftAmount', 'shiftOut', ')'],
            'outputs': ['grant', ')', 'grant', ')', 'grantPtr', 'picked', ')', 'shiftOut', ')', 'shiftOut', ')'],
            'internals': []
        },
        'PipelinedRefDivider': {
            'inputs': ['clk', 'stall', 'DataPath', 'dividend', 'DataPath', 'divisor', 'isSigned', 'DataPath', 'quotient', 'DataPath', 'remainder', ')'],
            'outputs': ['DataPath', 'quotient', 'DataPath', 'remainder', ')'],
            'internals': []
        },
        'PreDecodeStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ProducerMatrix': {
            'inputs': ['clk', 'DISPATCH_WIDTH', 'dispatchedSrcRegReady', 'DISPATCH_WIDTH', 'ISSUE_QUEUE_SRC_REG_NUM', 'IssueQueueIndexPath', 'DISPATCH_WIDTH-1:0', 'ISSUE_QUEUE_SRC_REG_NUM-1:0', 'dispatchedSrcRegPtr', 'dependStoreBitVector', 'IssueQueueIndexPath', 'DISPATCH_WIDTH', 'IssueQueueOneHotPath', 'WAKEUP_WIDTH', '+', 'STORE_ISSUE_WIDTH', 'ISSUE_QUEUE_ENTRY_NUM', ')'],
            'outputs': ['ISSUE_QUEUE_ENTRY_NUM', ')'],
            'internals': []
        },
        'QueuePointer': {
            'inputs': ['clk', 'rst', 'push', 'pop', 'full', 'empty', 'headPtr', 'tailPtr', ')', 'clk', 'rst', 'push', 'pop', 'full', 'empty', 'headPtr', 'tailPtr', 'count', ')', 'clk', 'rst', 'push', 'pop', 'pushCount', 'popCount', 'headPtr', 'tailPtr', 'count', ')', 'clk', 'rst', 'push', 'pop', 'pushCount', 'popCount', 'setTail', 'setTailPtr', 'headPtr', 'tailPtr', 'count', ')', 'clk', 'rst', 'pushTail', 'popTail', 'popHead', 'pushTailCount', 'popTailCount', 'popHeadCount', 'headPtr', 'tailPtr', 'count', ')', 'clk', 'rst', 'pushTail', 'popTail', 'popHead', 'pushTailCount', 'popTailCount', 'popHeadCount', 'setTail', 'setTailPtr', 'headPtr', 'tailPtr', 'count', ')'],
            'outputs': ['full', 'empty', 'headPtr', 'tailPtr', ')', 'full', 'empty', 'headPtr', 'tailPtr', 'count', ')', 'headPtr', 'tailPtr', 'count', ')', 'headPtr', 'tailPtr', 'count', ')', 'headPtr', 'tailPtr', 'count', ')', 'headPtr', 'tailPtr', 'count', ')'],
            'internals': []
        },
        'RMT': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ReadyBitTable': {
            'inputs': ['clk', 'rst', 'rstStart', 'WAKEUP_WIDTH', 'wakeupDstValid', 'WAKEUP_WIDTH', 'wakeupDstRegNum', 'WAKEUP_WIDTH', 'DISPATCH_WIDTH', 'dispatchedDstValid', 'DISPATCH_WIDTH', 'dispatchedDstRegNum', 'DISPATCH_WIDTH', 'dispatchedSrcValid', 'DISPATCH_WIDTH', 'SRC_OP_NUM', 'dispatchedSrcRegNum', 'DISPATCH_WIDTH', 'SRC_OP_NUM', 'DISPATCH_WIDTH', 'SRC_OP_NUM', ')'],
            'outputs': ['DISPATCH_WIDTH', 'SRC_OP_NUM', ')'],
            'internals': []
        },
        'RecoveryManager': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'RefDivider': {
            'inputs': ['clk', 'rst', 'req', 'DataPath', 'dividend', 'DataPath', 'divisor', 'isSigned', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')', 'clk', 'rst', 'req', 'DataPath', 'dividend', 'DataPath', 'divisor', 'isSigned', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')'],
            'outputs': ['finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', ')'],
            'internals': []
        },
        'RegisterFile': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'RenameLogic': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'RenameLogicCommitter': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'RenameStageSerializer': {
            'inputs': ['clk', 'rst', 'stall', 'clear', 'activeListEmpty', 'storeQueueEmpty', 'OpInfo', 'opInfo', 'valid', 'serialize', ')'],
            'outputs': ['serialize', ')'],
            'internals': []
        },
        'ReplayQueue': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ResetController': {
            'inputs': ['clk', 'rstTrigger', 'locked', 'rst', 'rstStart', ')'],
            'outputs': ['rst', 'rstStart', ')'],
            'internals': []
        },
        'RetirementRMT': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'ScheduleStage': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'Scheduler': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'SelectLogic': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'StoreCommitter': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'StoreQueue': {
            'inputs': ['DataPath', 'dataIn', 'LSQ_BlockDataPath', 'blockDataIn', 'PhyAddrPath', 'addr', 'MemAccessMode', 'mode', ')'],
            'outputs': ['LSQ_BlockDataPath', 'dataOut', 'DataPath', 'dataIn', 'LSQ_BlockDataPath', 'blockDataIn', 'PhyAddrPath', 'addr', 'MemAccessMode', 'mode', ')'],
            'internals': []
        },
        'TestBenchClockGenerator': {
            'inputs': ['rstOut', 'clk', 'rst', ')'],
            'outputs': ['clk', 'rst', ')'],
            'internals': []
        },
        'TestBlockDualPortRAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestBlockDualPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'ra', 'wa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'ra', 'wa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'internals': []
        },
        'TestBlockMultiPortRAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestBlockMultiPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'internals': []
        },
        'TestBlockTrueDualPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', '$clog2(ENTRY_NUM)-1:0', 'ENTRY_BIT_SIZE-1:0', 'ENTRY_BIT_SIZE-1:0', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', '$clog2(ENTRY_NUM)-1:0', 'ENTRY_BIT_SIZE-1:0', 'ENTRY_BIT_SIZE-1:0', '`endif', ')'],
            'internals': []
        },
        'TestCacheSystem': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestCacheSystemTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'icRE', 'AddrPath', 'icNextReadAddrIn', 'MEM_ISSUE_WIDTH-1:0', 'dcRE', 'AddrPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadAddrIn', 'dcWE', 'DataPath', 'dcWriteDataIn', 'AddrPath', 'dcWriteAddrIn', 'MemAccessSizeType', 'dcWriteAccessSize', 'FETCH_WIDTH-1:0', 'icReadHit', 'DataPath', 'FETCH_WIDTH-1:0', 'icReadDataOut', 'MEM_ISSUE_WIDTH-1:0', 'dcReadHit', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadDataOut', 'dcWriteHit', 'MemAccessResult', 'dcMemAccessResult', 'dcFillReq', 'dcFillAck', 'dcMiss', 'dcReplace', 'dcFillerBusy', 'AddrPath', 'dcFillAddr', 'dcMissAddr', 'dcReplaceAddr', 'WayPtr', 'dcFillWayPtr', 'dcVictimWayPtr', 'LineDataPath', 'dcFillData', 'dcReplaceData', ')'],
            'outputs': ['rstOut', 'icRE', 'AddrPath', 'icNextReadAddrIn', 'MEM_ISSUE_WIDTH-1:0', 'dcRE', 'AddrPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadAddrIn', 'dcWE', 'DataPath', 'dcWriteDataIn', 'AddrPath', 'dcWriteAddrIn', 'MemAccessSizeType', 'dcWriteAccessSize', 'FETCH_WIDTH-1:0', 'icReadHit', 'DataPath', 'FETCH_WIDTH-1:0', 'icReadDataOut', 'MEM_ISSUE_WIDTH-1:0', 'dcReadHit', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadDataOut', 'dcWriteHit', 'MemAccessResult', 'dcMemAccessResult', 'dcFillReq', 'dcFillAck', 'dcMiss', 'dcReplace', 'dcFillerBusy', 'AddrPath', 'dcFillAddr', 'dcMissAddr', 'dcReplaceAddr', 'WayPtr', 'dcFillWayPtr', 'dcVictimWayPtr', 'LineDataPath', 'dcFillData', 'dcReplaceData', ')'],
            'internals': []
        },
        'TestDCache': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestDCacheFiller': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestDCacheFillerTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'dcMiss', 'AddrPath', 'dcMissAddr', 'WayPtr', 'dcVictimWayPtr', 'MemAccessResult', 'dcMemAccessResult', 'dcFillAck', 'dcReplace', 'AddrPath', 'dcReplaceAddr', 'LineDataPath', 'dcReplaceData', 'dcFillReq', 'dcFillerBusy', 'AddrPath', 'dcFillAddr', 'WayPtr', 'dcFillWayPtr', 'LineDataPath', 'dcFillData', 'MemAccessReq', 'dcMemAccessReq', ')'],
            'outputs': ['rstOut', 'dcMiss', 'AddrPath', 'dcMissAddr', 'WayPtr', 'dcVictimWayPtr', 'MemAccessResult', 'dcMemAccessResult', 'dcFillAck', 'dcReplace', 'AddrPath', 'dcReplaceAddr', 'LineDataPath', 'dcReplaceData', 'dcFillReq', 'dcFillerBusy', 'AddrPath', 'dcFillAddr', 'WayPtr', 'dcFillWayPtr', 'LineDataPath', 'dcFillData', 'MemAccessReq', 'dcMemAccessReq', ')'],
            'internals': []
        },
        'TestDCacheTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'MEM_ISSUE_WIDTH-1:0', 'dcRE', 'AddrPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadAddrIn', 'dcWE', 'DataPath', 'dcWriteDataIn', 'AddrPath', 'dcWriteAddrIn', 'MemAccessSizeType', 'dcWriteAccessSize', 'dcFillReq', 'dcFillerBusy', 'AddrPath', 'dcFillAddr', 'WayPtr', 'dcFillWayPtr', 'LineDataPath', 'dcFillData', 'MEM_ISSUE_WIDTH-1:0', 'dcReadHit', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadDataOut', 'dcWriteHit', 'dcFillAck', 'dcMiss', 'dcReplace', 'AddrPath', 'dcMissAddr', 'dcReplaceAddr', 'WayPtr', 'dcVictimWayPtr', 'LineDataPath', 'dcReplaceData', ')'],
            'outputs': ['rstOut', 'MEM_ISSUE_WIDTH-1:0', 'dcRE', 'AddrPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadAddrIn', 'dcWE', 'DataPath', 'dcWriteDataIn', 'AddrPath', 'dcWriteAddrIn', 'MemAccessSizeType', 'dcWriteAccessSize', 'dcFillReq', 'dcFillerBusy', 'AddrPath', 'dcFillAddr', 'WayPtr', 'dcFillWayPtr', 'LineDataPath', 'dcFillData', 'MEM_ISSUE_WIDTH-1:0', 'dcReadHit', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'dcReadDataOut', 'dcWriteHit', 'dcFillAck', 'dcMiss', 'dcReplace', 'AddrPath', 'dcMissAddr', 'dcReplaceAddr', 'WayPtr', 'dcVictimWayPtr', 'LineDataPath', 'dcReplaceData', ')'],
            'internals': []
        },
        'TestDRAM_Controller': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestDRAM_ControllerTop': {
            'inputs': ['clk_p', 'clk_n', 'negResetIn', 'rxd', '`ifdef', 'RSD_SYNTHESIS_ATLYS', 'DDR2CLK0', 'DDR2CLK1', 'DDR2CKE', 'DDR2RASN', 'DDR2CASN', 'DDR2WEN', 'DDR2RZQ', 'DDR2ZIO', 'DDR2LDM', 'DDR2UDM', 'DDR2ODT', 'DDR2BA', 'DDR2A', 'DDR2DQ', 'DDR2UDQS', 'DDR2UDQSN', 'DDR2LDQS', 'DDR2LDQSN', '`endif', 'posResetOut', 'txd', 'ledOut', ')'],
            'outputs': ['DDR2CLK0', 'DDR2CLK1', 'DDR2CKE', 'DDR2RASN', 'DDR2CASN', 'DDR2WEN', 'DDR2RZQ', 'DDR2ZIO', 'DDR2LDM', 'DDR2UDM', 'DDR2ODT', 'DDR2BA', 'DDR2A', 'DDR2DQ', 'DDR2UDQS', 'DDR2UDQSN', 'DDR2LDQS', 'DDR2LDQSN', '`endif', 'posResetOut', 'txd', 'ledOut', ')'],
            'internals': []
        },
        'TestDistributedDualPortRAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestDistributedDualPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'ra', 'wa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'ra', 'wa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'internals': []
        },
        'TestDistributedMultiBankRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'internals': []
        },
        'TestDistributedMultiPortRAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestDistributedMultiPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'internals': []
        },
        'TestDistributedSharedMultiPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'rwa', 'ENTRY_BIT_SIZE-1:0', 'wv', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM-1', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'rwa', 'ENTRY_BIT_SIZE-1:0', 'wv', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM-1', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'internals': []
        },
        'TestDistributedSinglePortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'rwa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'rwa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'internals': []
        },
        'TestDivider': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestICache': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestICacheFiller': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestICacheFillerTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'icMiss', 'AddrPath', 'icMissAddr', 'WayPtr', 'icVictimWayPtr', 'MemAccessResult', 'icMemAccessResult', 'icFill', 'icFillerBusy', 'AddrPath', 'icFillAddr', 'WayPtr', 'icFillWayPtr', 'LineDataPath', 'icFillData', 'MemReadAccessReq', 'icMemAccessReq', ')'],
            'outputs': ['rstOut', 'icMiss', 'AddrPath', 'icMissAddr', 'WayPtr', 'icVictimWayPtr', 'MemAccessResult', 'icMemAccessResult', 'icFill', 'icFillerBusy', 'AddrPath', 'icFillAddr', 'WayPtr', 'icFillWayPtr', 'LineDataPath', 'icFillData', 'MemReadAccessReq', 'icMemAccessReq', ')'],
            'internals': []
        },
        'TestICacheSystem': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestICacheSystemTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'icRE', 'AddrPath', 'icNextReadAddrIn', 'MemAccessReq', 'dcMemAccessReq', 'FETCH_WIDTH-1:0', 'icReadHit', 'DataPath', 'FETCH_WIDTH-1:0', 'icReadDataOut', 'MemAccessResult', 'dcMemAccessResult', ')'],
            'outputs': ['rstOut', 'icRE', 'AddrPath', 'icNextReadAddrIn', 'MemAccessReq', 'dcMemAccessReq', 'FETCH_WIDTH-1:0', 'icReadHit', 'DataPath', 'FETCH_WIDTH-1:0', 'icReadDataOut', 'MemAccessResult', 'dcMemAccessResult', ')'],
            'internals': []
        },
        'TestICacheTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'icRE', 'AddrPath', 'icNextReadAddrIn', 'icFill', 'icFillerBusy', 'AddrPath', 'icFillAddr', 'WayPtr', 'icFillWayPtr', 'LineDataPath', 'icFillData', 'FETCH_WIDTH-1:0', 'icReadHit', 'DataPath', 'FETCH_WIDTH-1:0', 'icReadDataOut', 'icMiss', 'AddrPath', 'icMissAddr', 'WayPtr', 'icVictimWayPtr', ')'],
            'outputs': ['rstOut', 'icRE', 'AddrPath', 'icNextReadAddrIn', 'icFill', 'icFillerBusy', 'AddrPath', 'icFillAddr', 'WayPtr', 'icFillWayPtr', 'LineDataPath', 'icFillData', 'FETCH_WIDTH-1:0', 'icReadHit', 'DataPath', 'FETCH_WIDTH-1:0', 'icReadDataOut', 'icMiss', 'AddrPath', 'icMissAddr', 'WayPtr', 'icVictimWayPtr', ')'],
            'internals': []
        },
        'TestInitializedBlockRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'ra', 'wa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', '$clog2(ENTRY_NUM)-1:0', 'ra', 'wa', 'ENTRY_BIT_SIZE-1:0', 'wv', 'ENTRY_BIT_SIZE-1:0', 'rv', '`endif', ')'],
            'internals': []
        },
        'TestIntALU': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestLRU_Counter': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestLRU_CounterTop': {
            'inputs': ['clk_p', 'clk_n', 'rst', 'PORT_WIDTH-1:0', 'INDEX_BIT_WIDTH-1:0', 'index', 'PORT_WIDTH-1:0', 'access', 'PORT_WIDTH-1:0', '$clog2(WAY_NUM)-1:0', 'accessWay', 'PORT_WIDTH-1:0', '$clog2(WAY_NUM)-1:0', 'leastRecentlyAccessedWay', ')'],
            'outputs': ['PORT_WIDTH-1:0', '$clog2(WAY_NUM)-1:0', 'leastRecentlyAccessedWay', ')'],
            'internals': []
        },
        'TestMain': {
            'inputs': ['commitNumInThisCycle', 'DataPath', 'LREG_NUM', ')'],
            'outputs': ['DataPath', 'LREG_NUM', ')'],
            'internals': []
        },
        'TestMemory': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestMemoryTop': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'MemReadAccessReq', 'icMemAccessReq', 'MemAccessReq', 'dcMemAccessReq', 'MemAccessResult', 'icMemAccessResult', 'MemAccessResult', 'dcMemAccessResult', ')'],
            'outputs': ['rstOut', 'MemReadAccessReq', 'icMemAccessReq', 'MemAccessReq', 'dcMemAccessReq', 'MemAccessResult', 'icMemAccessResult', 'MemAccessResult', 'dcMemAccessResult', ')'],
            'internals': []
        },
        'TestMultiWidthFreeList': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestMultiWidthFreeListTop': {
            'inputs': ['clk_p', 'clk_n', 'rst', 'PUSH_WIDTH-1:0', 'push', 'POP_WIDTH-1:0', 'pop', 'PUSH_WIDTH-1:0', 'ENTRY_WIDTH-1:0', 'pushedData', 'full', 'empty', 'POP_WIDTH-1:0', 'ENTRY_WIDTH-1:0', 'poppedData', ')'],
            'outputs': ['full', 'empty', 'POP_WIDTH-1:0', 'ENTRY_WIDTH-1:0', 'poppedData', ')'],
            'internals': []
        },
        'TestMultiWidthQueuePointer': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestMultiWidthQueuePointerTop': {
            'inputs': ['clk_p', 'clk_n', 'rst', 'push', 'pop', '$clog2(PUSH_WIDTH):0', 'pushCount', '$clog2(POP_WIDTH):0', 'popCount', 'full', 'empty', '$clog2(SIZE)-1:0', 'headPtr', '$clog2(SIZE)-1:0', 'tailPtr', '$clog2(SIZE):0', 'count', ')'],
            'outputs': ['full', 'empty', '$clog2(SIZE)-1:0', 'headPtr', '$clog2(SIZE)-1:0', 'tailPtr', '$clog2(SIZE):0', 'count', ')'],
            'internals': []
        },
        'TestRefDividerTop': {
            'inputs': ['clk_p', 'clk_n', 'rst', 'req', 'DataPath', 'dividend', 'DataPath', 'divisor', 'isSigned', 'finished', 'DataPath', 'quotient', 'DataPath', 'remainder', 'refFinished', 'DataPath', 'refQuotient', 'DataPath', 'refRemainder', ')'],
            'outputs': ['finished', 'DataPath', 'quotient', 'DataPath', 'remainder', 'refFinished', 'DataPath', 'refQuotient', 'DataPath', 'refRemainder', ')'],
            'internals': []
        },
        'TestRegisterFile': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestRegisterFileTop': {
            'inputs': ['clk_p', 'clk_n', 'rst', 'PRegNumPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcRegNumA', 'PRegNumPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcRegNumB', 'PRegNumPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcFlagNum', 'INT_ISSUE_WIDTH-1:0', 'intDstRegWE', 'INT_ISSUE_WIDTH-1:0', 'intDstFlagWE', 'PRegNumPath', 'INT_ISSUE_WIDTH-1:0', 'intDstRegNum', 'PRegNumPath', 'INT_ISSUE_WIDTH-1:0', 'intDstFlagNum', 'DataPath', 'INT_ISSUE_WIDTH-1:0', 'intDstRegData', 'FlagPath', 'INT_ISSUE_WIDTH-1:0', 'intDstFlagData', 'PRegNumPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcRegNumA', 'PRegNumPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcRegNumB', 'PRegNumPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcFlagNum', 'MEM_ISSUE_WIDTH-1:0', 'memDstRegWE', 'MEM_ISSUE_WIDTH-1:0', 'memDstFlagWE', 'PRegNumPath', 'MEM_ISSUE_WIDTH-1:0', 'memDstRegNum', 'PRegNumPath', 'MEM_ISSUE_WIDTH-1:0', 'memDstFlagNum', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'memDstRegData', 'FlagPath', 'MEM_ISSUE_WIDTH-1:0', 'memDstFlagData', 'DataPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcRegDataA', 'DataPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcRegDataB', 'FlagPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcFlagData', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcRegDataA', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcRegDataB', 'FlagPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcFlagData', ')'],
            'outputs': ['DataPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcRegDataA', 'DataPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcRegDataB', 'FlagPath', 'INT_ISSUE_WIDTH-1:0', 'intSrcFlagData', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcRegDataA', 'DataPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcRegDataB', 'FlagPath', 'MEM_ISSUE_WIDTH-1:0', 'memSrcFlagData', ')'],
            'internals': []
        },
        'TestRegisterMultiPortRAM_Top': {
            'inputs': ['clk', 'rst', 'ibit', 'obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'outputs': ['obit', '`else', 'clk_p', 'clk_n', 'we', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'wa', 'WRITE_NUM', 'ENTRY_BIT_SIZE-1:0', 'wv', 'WRITE_NUM', '$clog2(ENTRY_NUM)-1:0', 'ra', 'READ_NUM', 'ENTRY_BIT_SIZE-1:0', 'rv', 'READ_NUM', '`endif', ')'],
            'internals': []
        },
        'TestSourceCAM': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'TestSourceCAM_Top': {
            'inputs': ['clk_p', 'clk_n', 'rstTrigger', 'rstOut', 'DISPATCH_WIDTH-1:0', 'dispatch', 'IssueQueueIndexPath', 'DISPATCH_WIDTH-1:0', 'dispatchPtr', 'PRegNumPath', 'DISPATCH_WIDTH-1:0', 'SRC_OP_NUM-1:0', 'dispatchedSrcRegNum', 'DISPATCH_WIDTH-1:0', 'SRC_OP_NUM-1:0', 'dispatchedSrcReady', 'WAKEUP_WIDTH-1:0', 'wakeup', 'SchedulerRegTag', 'WAKEUP_WIDTH-1:0', 'wakeupDstTag', 'IssueQueueOneHotPath', 'opReady', ')'],
            'outputs': ['rstOut', 'DISPATCH_WIDTH-1:0', 'dispatch', 'IssueQueueIndexPath', 'DISPATCH_WIDTH-1:0', 'dispatchPtr', 'PRegNumPath', 'DISPATCH_WIDTH-1:0', 'SRC_OP_NUM-1:0', 'dispatchedSrcRegNum', 'DISPATCH_WIDTH-1:0', 'SRC_OP_NUM-1:0', 'dispatchedSrcReady', 'WAKEUP_WIDTH-1:0', 'wakeup', 'SchedulerRegTag', 'WAKEUP_WIDTH-1:0', 'wakeupDstTag', 'IssueQueueOneHotPath', 'opReady', ')'],
            'internals': []
        },
        'Top': {
            'inputs': ['clk_p', 'clk_n', 'negResetIn', 'rxd', '`elsif', 'RSD_SYNTHESIS_ATLYS', 'clk_p', 'clk_n', 'negResetIn', 'rxd', '`elsif', 'RSD_SYNTHESIS_ZEDBOARD', 'clk', 'negResetIn', '`else', '"Error!"', '`endif', '`ifndef', 'RSD_DISABLE_DEBUG_REGISTER', 'DebugRegister', 'debugRegister', '`endif', '`ifdef', 'RSD_SYNTHESIS_ATLYS', 'DDR2CLK0', 'DDR2CLK1', 'DDR2CKE', 'DDR2RASN', 'DDR2CASN', 'DDR2WEN', 'DDR2RZQ', 'DDR2ZIO', 'DDR2LDM', 'DDR2UDM', 'DDR2ODT', 'DDR2BA', 'DDR2A', 'DDR2DQ', 'DDR2UDQS', 'DDR2UDQSN', 'DDR2LDQS', 'DDR2LDQSN', '`endif', '`ifndef', 'RSD_SYNTHESIS', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', '`elsif', 'RSD_SYNTHESIS_ATLYS', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', '`elsif', 'RSD_SYNTHESIS_ZEDBOARD', 'LED_Path', 'ledOut', 'Axi4LiteControlRegisterIF.Axi4LiteRead', 'axi4LitePlToPsControlRegisterIF', 'Axi4LiteControlRegisterIF.Axi4Lite', 'axi4LitePsToPlControlRegisterIF', '`else', '"Error!"', '`endif', ')'],
            'outputs': ['DebugRegister', 'debugRegister', '`endif', '`ifdef', 'RSD_SYNTHESIS_ATLYS', 'DDR2CLK0', 'DDR2CLK1', 'DDR2CKE', 'DDR2RASN', 'DDR2CASN', 'DDR2WEN', 'DDR2RZQ', 'DDR2ZIO', 'DDR2LDM', 'DDR2UDM', 'DDR2ODT', 'DDR2BA', 'DDR2A', 'DDR2DQ', 'DDR2UDQS', 'DDR2UDQSN', 'DDR2LDQS', 'DDR2LDQSN', '`endif', '`ifndef', 'RSD_SYNTHESIS', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', '`elsif', 'RSD_SYNTHESIS_ATLYS', 'serialWE', 'SerialDataPath', 'serialWriteData', 'posResetOut', 'LED_Path', 'ledOut', 'txd', '`elsif', 'RSD_SYNTHESIS_ZEDBOARD', 'LED_Path', 'ledOut', 'Axi4LiteControlRegisterIF.Axi4LiteRead', 'axi4LitePlToPsControlRegisterIF', 'Axi4LiteControlRegisterIF.Axi4Lite', 'axi4LitePsToPlControlRegisterIF', '`else', '"Error!"', '`endif', ')'],
            'internals': []
        },
        'WakeupLogic': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'WakeupPipelineRegister': {
            'inputs': [],
            'outputs': [],
            'internals': []
        },
        'for': {
            'inputs': ['clk', 'rst', 'dispatch', 'DISPATCH_WIDTH', 'IssueQueueIndexPath', 'dispatchPtr', 'DISPATCH_WIDTH', 'dispatchedSrcRegNum', 'DISPATCH_WIDTH', 'SRC_OP_NUM', 'dispatchedSrcReady', 'DISPATCH_WIDTH', 'SRC_OP_NUM', 'wakeup', 'WAKEUP_WIDTH', 'wakeupDstValid', 'WAKEUP_WIDTH', 'wakeupDstRegNum', 'WAKEUP_WIDTH', 'IssueQueueOneHotPath', 'opReady', ')'],
            'outputs': ['IssueQueueOneHotPath', 'opReady', ')'],
            'internals': []
        },
        'is': {
            'inputs': ['clk', 'rst', 'rstStart', ')', 'selected', 'selectedPtr', 'selectedVector', 'stall', 'write', 'writePtr', 'writeSrcTag', 'writeDstTag', 'intIssueReq', '`ifndef', 'RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE', 'complexIssueReq', '`endif', 'loadIssueReq', 'storeIssueReq', '`ifdef', 'RSD_MARCH_FP_PIPE', 'fpIssueReq', '`endif', 'notIssued', 'dispatchStore', 'dispatchLoad', 'memDependencyPred', ')', 'clk', 'rst', 'rstStart', 'write', 'writePtr', 'writeDstTag', 'wakeupPtr', 'wakeupDstTag', ')', 'clk', 'rst', 'rstStart', 'stall', 'write', 'writePtr', 'writeSrcTag', 'writeDstTag', 'wakeup', 'wakeupDstTag', 'wakeupVector', 'notIssued', 'dispatchStore', 'dispatchLoad', 'memDependencyPred', 'opReady', ')', 'opReady', 'intIssueReq', '`ifndef', 'RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE', 'complexIssueReq', '`endif', 'loadIssueReq', 'storeIssueReq', '`ifdef', 'RSD_MARCH_FP_PIPE', 'fpIssueReq', '`endif', 'selected', 'selectedPtr', 'selectedVector', ')', 'clk', 'rst', 'stall', 'selected', 'selectedPtr', 'selectedVector', 'wakeup', 'wakeupPtr', 'wakeupVector', 'releaseEntry', 'releasePtr', ')', 'releaseEntry', 'releasePtr', ')'],
            'outputs': ['stall', 'write', 'writePtr', 'writeSrcTag', 'writeDstTag', 'intIssueReq', '`ifndef', 'RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE', 'complexIssueReq', '`endif', 'loadIssueReq', 'storeIssueReq', '`ifdef', 'RSD_MARCH_FP_PIPE', 'fpIssueReq', '`endif', 'notIssued', 'dispatchStore', 'dispatchLoad', 'memDependencyPred', ')', 'wakeupDstTag', ')', 'opReady', ')', 'selected', 'selectedPtr', 'selectedVector', ')', 'wakeup', 'wakeupPtr', 'wakeupVector', 'releaseEntry', 'releasePtr', ')'],
            'internals': []
        },
        'logic': {
            'inputs': ['clk', 'rst', ')', 'clk', 'rst', 'exceptionDetectedInCommitStage', 'refetchTypeFromCommitStage', 'exceptionDetectedInRwStage', 'refetchTypeFromRwStage', 'renameLogicRecoveryRMT', 'issueQueueReturnIndex', 'replayQueueFlushedOpExist', 'wakeupPipelineRegFlushedOpExist', 'recoveredPC_FromCommitStage', 'recoveredPC_FromRwStage', 'faultingDataAddr', 'notIssued', 'flushIQ_Entry', 'recoveryCauseFromCommitStage', 'phase', 'toRecoveryPhase', 'recoveredPC_FromRwCommit', 'toCommitPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'unableToStartRecovery', 'recoveryFromRwStage', 'loadQueueRecoveryTailPtr', 'storeQueueRecoveryTailPtr', ')', 'phase', 'unableToStartRecovery', 'renameLogicRecoveryRMT', 'exceptionDetectedInCommitStage', 'recoveryOpIndex', 'refetchTypeFromCommitStage', 'recoveryCauseFromCommitStage', ')', 'toCommitPhase', 'toRecoveryPhase', 'recoveredPC_FromRwCommit', 'recoverFromRename', 'recoveredPC_FromRename', ')', 'toRecoveryPhase', 'inRecoveryAL', 'renameLogicRecoveryRMT', ')', 'toRecoveryPhase', 'toCommitPhase', 'inRecoveryAL', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', 'notIssued', 'selected', 'selectedPtr', 'recoveryFromRwStage', 'flushIQ_Entry', 'issueQueueReturnIndex', 'selectedActiveListPtr', ')', 'toRecoveryPhase', 'flushIQ_Entry', 'notIssued', ')', 'toRecoveryPhase', 'flushIQ_Entry', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', 'recoveryFromRwStage', 'replayQueueFlushedOpExist', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', 'selectedActiveListPtr', 'flushIQ_Entry', 'recoveryFromRwStage', 'wakeupPipelineRegFlushedOpExist', ')', 'toRecoveryPhase', 'loadQueueRecoveryTailPtr', 'loadQueueHeadPtr', ')', 'toRecoveryPhase', 'storeQueueRecoveryTailPtr', 'storeQueueHeadPtr', ')', 'toRecoveryPhase', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'flushAllInsns', ')', 'toRecoveryPhase', 'toCommitPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'unableToStartRecovery', 'exceptionDetectedInRwStage', 'refetchTypeFromRwStage', 'recoveredPC_FromCommitStage', 'recoveredPC_FromRwStage', 'faultingDataAddr', 'flushAllInsns', ')', 'unableToStartRecovery', ')'],
            'outputs': ['phase', 'toRecoveryPhase', 'recoveredPC_FromRwCommit', 'toCommitPhase', 'flushRangeHeadPtr', 'flushRangeTailPtr', 'unableToStartRecovery', 'recoveryFromRwStage', 'loadQueueRecoveryTailPtr', 'storeQueueRecoveryTailPtr', ')', 'recoverFromRename', 'recoveredPC_FromRename', ')', 'exceptionDetectedInCommitStage', 'recoveryOpIndex', 'refetchTypeFromCommitStage', 'recoveryCauseFromCommitStage', ')', 'renameLogicRecoveryRMT', ')', 'inRecoveryAL', ')', 'flushIQ_Entry', 'issueQueueReturnIndex', 'selectedActiveListPtr', ')', 'notIssued', ')', 'selected', 'selectedPtr', ')', 'replayQueueFlushedOpExist', ')', 'wakeupPipelineRegFlushedOpExist', ')', 'loadQueueHeadPtr', ')', 'storeQueueHeadPtr', ')', 'exceptionDetectedInRwStage', 'refetchTypeFromRwStage', 'recoveredPC_FromCommitStage', 'recoveredPC_FromRwStage', 'faultingDataAddr', 'flushAllInsns', ')'],
            'internals': []
        },
    },
}


# ============================================================================
# CLASSIFICATION LOGIC
# ============================================================================

def exact_keyword_match(signal_name: str, keywords: List[str]) -> bool:
    """
    Check if signal name contains any keyword (case-insensitive, exact substring match)
    
    Examples:
        'wr_en_i' matches 'en' ✓
        'enable_o' matches 'enable' ✓
        'counter' matches 'en' ✗ (substring but we want word boundaries)
    """
    signal_lower = signal_name.lower()
    
    for keyword in keywords:
        keyword_lower = keyword.lower()
        
        # Exact substring match
        if keyword_lower in signal_lower:
            # Check if it's a word boundary match
            # (e.g., 'en' in 'wr_en_i' but not 'en' in 'counter')
            idx = signal_lower.find(keyword_lower)
            
            # Check character before
            before_ok = (idx == 0 or signal_lower[idx-1] in ['_', '-', '.'])
            
            # Check character after
            after_idx = idx + len(keyword_lower)
            after_ok = (after_idx >= len(signal_lower) or 
                       signal_lower[after_idx] in ['_', '-', '.', 'i', 'o', 'q'])
            
            if before_ok and after_ok:
                return True
    
    return False


def classify_signal(signal_name: str, pattern_name: str, role: str) -> bool:
    """
    Check if signal matches pattern for given role (trigger/payload)
    
    Args:
        signal_name: Signal name to classify
        pattern_name: Pattern name (DoS, Leak, etc.)
        role: 'trigger' or 'payload'
    
    Returns:
        True if signal matches pattern keywords
    """
    keywords = PATTERN_RULES[pattern_name][f'{role}_keywords']
    return exact_keyword_match(signal_name, keywords)


def classify_module_signals(module_name: str, signals: Dict[str, List[str]]) -> Dict:
    """
    Classify all signals in a module by trojan pattern
    
    Returns:
        Dict with pattern -> {triggers: [...], payloads: [...]}
    """
    all_signals = []
    for signal_list in signals.values():
        all_signals.extend(signal_list)
    
    classification = {}
    
    for pattern_name in PATTERN_RULES.keys():
        triggers = []
        payloads = []
        
        for signal in all_signals:
            # Check if trigger
            if classify_signal(signal, pattern_name, 'trigger'):
                triggers.append(signal)
            
            # Check if payload
            if classify_signal(signal, pattern_name, 'payload'):
                payloads.append(signal)
        
        classification[pattern_name] = {
            'triggers': sorted(set(triggers)),
            'payloads': sorted(set(payloads))
        }
    
    return classification


# ============================================================================
# CSV OUTPUT
# ============================================================================

def save_processor_csv(processor_name: str, classifications: Dict, output_dir: Path):
    """
    Save classifications to CSV file
    
    CSV Format:
    Module,Pattern,Role,Signal
    ibex_alu,DoS,trigger,imd_val_we_o
    ibex_alu,DoS,payload,shift_amt
    ...
    """
    output_file = output_dir / f"{processor_name}_signals.csv"
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Module', 'Pattern', 'Role', 'Signal'])
        
        for module_name, module_classification in sorted(classifications.items()):
            for pattern_name, signals in sorted(module_classification.items()):
                # Write triggers
                for signal in signals['triggers']:
                    writer.writerow([module_name, pattern_name, 'trigger', signal])
                
                # Write payloads
                for signal in signals['payloads']:
                    writer.writerow([module_name, pattern_name, 'payload', signal])
    
    return output_file


def generate_summary_report(processor_name: str, classifications: Dict) -> str:
    """Generate text summary of classification"""
    lines = []
    lines.append("=" * 80)
    lines.append(f"{processor_name.upper()} SIGNAL CLASSIFICATION SUMMARY")
    lines.append("=" * 80)
    
    total_modules = len(classifications)
    lines.append(f"\nTotal Modules: {total_modules}\n")
    
    for module_name, module_classification in sorted(classifications.items()):
        lines.append(f"\n{module_name}:")
        lines.append("-" * 60)
        
        for pattern_name, signals in sorted(module_classification.items()):
            trigger_count = len(signals['triggers'])
            payload_count = len(signals['payloads'])
            
            if trigger_count > 0 or payload_count > 0:
                lines.append(f"  {pattern_name:15} - Triggers: {trigger_count:2}, Payloads: {payload_count:2}")
                
                if trigger_count > 0:
                    lines.append(f"    Triggers: {', '.join(signals['triggers'][:3])}")
                    if trigger_count > 3:
                        lines.append(f"              ... and {trigger_count - 3} more")
                
                if payload_count > 0:
                    lines.append(f"    Payloads: {', '.join(signals['payloads'][:3])}")
                    if payload_count > 3:
                        lines.append(f"              ... and {payload_count - 3} more")
    
    # Overall statistics
    lines.append("\n" + "=" * 80)
    lines.append("OVERALL STATISTICS")
    lines.append("=" * 80)
    
    pattern_stats = defaultdict(lambda: {'triggers': 0, 'payloads': 0, 'modules': 0})
    
    for module_classification in classifications.values():
        for pattern_name, signals in module_classification.items():
            if signals['triggers'] or signals['payloads']:
                pattern_stats[pattern_name]['triggers'] += len(signals['triggers'])
                pattern_stats[pattern_name]['payloads'] += len(signals['payloads'])
                pattern_stats[pattern_name]['modules'] += 1
    
    for pattern_name in sorted(pattern_stats.keys()):
        stats = pattern_stats[pattern_name]
        lines.append(f"\n{pattern_name}:")
        lines.append(f"  Applicable modules: {stats['modules']}")
        lines.append(f"  Total trigger signals: {stats['triggers']}")
        lines.append(f"  Total payload signals: {stats['payloads']}")
    
    return '\n'.join(lines)


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main classification workflow"""
    print("=" * 80)
    print("HARDWARE TROJAN SIGNAL CLASSIFIER")
    print("=" * 80)
    
    output_dir = Path("signal_classifications")
    output_dir.mkdir(exist_ok=True)
    
    for processor_name, modules in PROCESSOR_SIGNALS.items():
        if not modules:
            print(f"\n⚠️  Skipping {processor_name}: No modules defined")
            continue
        
        print(f"\n📊 Processing {processor_name.upper()}...")
        print(f"   Modules: {len(modules)}")
        
        # Classify all modules
        classifications = {}
        for module_name, signals in modules.items():
            print(f"   Classifying {module_name}...", end='')
            classifications[module_name] = classify_module_signals(module_name, signals)
            print(" ✓")
        
        # Save CSV
        csv_file = save_processor_csv(processor_name, classifications, output_dir)
        print(f"   ✅ Saved: {csv_file}")
        
        # Generate summary
        summary = generate_summary_report(processor_name, classifications)
        summary_file = output_dir / f"{processor_name}_summary.txt"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"   ✅ Saved: {summary_file}")
        
        # Print summary
        print(summary)
    
    print("\n" + "=" * 80)
    print("✅ CLASSIFICATION COMPLETE!")
    print("=" * 80)
    print(f"\nOutput directory: {output_dir.absolute()}")
    print("\nGenerated files:")
    for f in sorted(output_dir.glob("*")):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
