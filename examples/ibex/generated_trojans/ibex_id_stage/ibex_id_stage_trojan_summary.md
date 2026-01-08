# Trojan Generation Summary

**Module:** ibex_id_stage
**File:** ibex_id_stage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (32):**
- instr_valid_i
- instr_bp_taken_i
- ex_valid_i
- lsu_resp_valid_i
- lsu_req_done_i
- ... and 27 more

**Payload Signals (35):**
- instr_valid_i
- instr_bp_taken_i
- ex_valid_i
- lsu_resp_valid_i
- lsu_req_done_i
- ... and 30 more

**Generated File:** T1_ibex_id_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (15):**
- debug_req_i
- debug_single_step_i
- debug_ebreakm_i
- debug_ebreaku_i
- ctrl_busy_o
- ... and 10 more

**Payload Signals (38):**
- instr_rdata_i
- instr_rdata_alu_i
- instr_rdata_c_i
- csr_mstatus_tw_i
- illegal_csr_insn_i
- ... and 33 more

**Generated File:** T2_ibex_id_stage_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (40):**
- imd_val_we_ex_i
- csr_mstatus_tw_i
- illegal_csr_insn_i
- lsu_addr_incr_req_i
- lsu_addr_last_i
- ... and 35 more

**Payload Signals (8):**
- csr_mstatus_tw_i
- csr_mstatus_mie_i
- multdiv_signed_mode_ex_o
- nmi_mode_o
- debug_mode_o
- ... and 3 more

**Generated File:** T3_ibex_id_stage_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (36):**
- instr_rdata_i
- instr_rdata_alu_i
- instr_rdata_c_i
- data_ind_timing_i
- lsu_addr_incr_req_i
- ... and 31 more

**Payload Signals (29):**
- instr_rdata_i
- instr_rdata_alu_i
- instr_rdata_c_i
- data_ind_timing_i
- lsu_store_err_i
- ... and 24 more

**Generated File:** T4_ibex_id_stage_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (35):**
- instr_valid_i
- instr_rdata_i
- instr_rdata_alu_i
- instr_rdata_c_i
- ex_valid_i
- ... and 30 more

**Payload Signals (25):**
- instr_valid_i
- ex_valid_i
- lsu_resp_valid_i
- lsu_req_done_i
- ready_wb_i
- ... and 20 more

**Generated File:** T5_ibex_id_stage_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (25):**
- instr_rdata_i
- instr_rdata_alu_i
- instr_rdata_c_i
- instr_fetch_err_i
- instr_fetch_err_plus2_i
- ... and 20 more

**Payload Signals (20):**
- data_ind_timing_i
- debug_req_i
- debug_single_step_i
- debug_ebreakm_i
- debug_ebreaku_i
- ... and 15 more

**Generated File:** T6_ibex_id_stage_Covert.sv

---

