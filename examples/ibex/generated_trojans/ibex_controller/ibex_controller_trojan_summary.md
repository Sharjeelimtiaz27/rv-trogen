# Trojan Generation Summary

**Module:** ibex_controller
**File:** ibex_controller.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (22):**
- instr_valid_i
- instr_bp_taken_i
- irq_pending_i
- debug_req_i
- trigger_match_i
- ... and 17 more

**Payload Signals (21):**
- instr_valid_i
- instr_bp_taken_i
- irq_pending_i
- debug_req_i
- ready_wb_i
- ... and 16 more

**Generated File:** T1_ibex_controller_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (18):**
- irq_nm_ext_i
- debug_req_i
- debug_single_step_i
- debug_ebreakm_i
- debug_ebreaku_i
- ... and 13 more

**Payload Signals (13):**
- csr_pipe_flush_i
- lsu_addr_last_i
- csr_mstatus_mie_i
- debug_csr_save_o
- csr_save_if_o
- ... and 8 more

**Generated File:** T2_ibex_controller_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (23):**
- csr_pipe_flush_i
- lsu_addr_last_i
- csr_mstatus_mie_i
- ctrl_busy_o
- controller_run_o
- ... and 18 more

**Payload Signals (9):**
- csr_mstatus_mie_i
- nmi_mode_o
- debug_mode_o
- debug_mode_entering_o
- nmi_mode_q
- ... and 4 more

**Generated File:** T3_ibex_controller_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- lsu_addr_last_i
- mem_resp_intg_err_addr_q

**Payload Signals (6):**
- store_err_i
- csr_restore_mret_id_o
- csr_restore_dret_id_o
- store_err_q
- store_err_prio
- ... and 1 more

**Generated File:** T4_ibex_controller_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- instr_valid_i
- debug_req_i
- trigger_match_i
- instr_valid_clear_o
- instr_req_o
- ... and 5 more

**Payload Signals (8):**
- instr_valid_i
- stall_id_i
- stall_wb_i
- ready_wb_i
- ctrl_busy_o
- ... and 3 more

**Generated File:** T5_ibex_controller_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- instr_fetch_err_i
- instr_fetch_err_plus2_i
- load_err_i
- load_err_q
- instr_fetch_err_prio
- ... and 2 more

**Payload Signals (15):**
- debug_req_i
- debug_single_step_i
- debug_ebreakm_i
- debug_ebreaku_i
- ctrl_busy_o
- ... and 10 more

**Generated File:** T6_ibex_controller_Covert.sv

---

