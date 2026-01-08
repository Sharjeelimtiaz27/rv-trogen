# Trojan Generation Summary

**Module:** csr_regfile
**File:** csr_regfile.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (17):**
- scoreboard_entry_t
- acc_fflags_ex_valid_i
- debug_req_i
- en_translation_o
- en_g_translation_o
- ... and 12 more

**Payload Signals (13):**
- scoreboard_entry_t
- acc_fflags_ex_valid_i
- debug_req_i
- en_translation_o
- en_g_translation_o
- ... and 8 more

**Generated File:** T1_csr_regfile_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (9):**
- debug_req_i
- irq_ctrl_t
- set_debug_pc_o
- debug_mode_o
- debug_from_trigger_o
- ... and 4 more

**Payload Signals (9):**
- csr_addr_i
- csr_write_fflags_i
- csr_hs_ld_st_inst_i
- halt_csr_o
- perf_addr_o
- ... and 4 more

**Generated File:** T2_csr_regfile_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (16):**
- csr_addr_i
- csr_write_fflags_i
- csr_hs_ld_st_inst_i
- halt_csr_o
- irq_ctrl_t
- ... and 11 more

**Payload Signals (6):**
- dirty_fp_state_i
- dirty_v_state_i
- debug_mode_o
- SMODE_STATUS_READ_MASK
- dirty_fp_state_csr
- ... and 1 more

**Generated File:** T3_csr_regfile_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- fu_op
- csr_addr_i
- perf_addr_o
- tselect_we
- csr_wdata

**Payload Signals (3):**
- csr_write_fflags_i
- output
- csr_wdata

**Generated File:** T4_csr_regfile_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- fu_op
- acc_fflags_ex_valid_i
- debug_req_i
- debug_from_trigger_o
- break_from_trigger_o
- ... and 3 more

**Payload Signals (1):**
- acc_fflags_ex_valid_i

**Generated File:** T5_csr_regfile_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- read_access_exception
- virtual_read_access_exception
- mtvec_rst_load_q
- csr_wdata

**Payload Signals (7):**
- debug_req_i
- set_debug_pc_o
- debug_mode_o
- debug_from_trigger_o
- debug_mode_q
- ... and 2 more

**Generated File:** T6_csr_regfile_Covert.sv

---

