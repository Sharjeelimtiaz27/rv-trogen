# Trojan Generation Summary

**Module:** ex_stage
**File:** ex_stage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (33):**
- stall_st_pending_i
- amo_valid_commit_i
- x_result_valid_i
- acc_valid_i
- acc_mmu_req_t
- ... and 28 more

**Payload Signals (33):**
- stall_st_pending_i
- amo_valid_commit_i
- x_result_valid_i
- acc_valid_i
- acc_mmu_req_t
- ... and 28 more

**Generated File:** T1_ex_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- debug_mode_i
- lsu_ctrl_t

**Payload Signals (5):**
- fu_data_t
- csr_commit_i
- csr_addr_o
- csr_hs_ld_st_inst_o
- csr_ready

**Generated File:** T2_ex_stage_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (7):**
- debug_mode_i
- csr_commit_i
- csr_addr_o
- x_we_o
- csr_hs_ld_st_inst_o
- ... and 2 more

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_ex_stage_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- fu_data_t
- csr_addr_o

**Payload Signals (5):**
- fu_data_t
- x_result_valid_i
- x_result_t
- store_valid_o
- x_result_ready_o

**Generated File:** T4_ex_stage_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (17):**
- fu_data_t
- amo_valid_commit_i
- x_result_valid_i
- acc_valid_i
- acc_mmu_req_t
- ... and 12 more

**Payload Signals (19):**
- stall_st_pending_i
- amo_valid_commit_i
- x_result_valid_i
- acc_valid_i
- flu_ready_o
- ... and 14 more

**Generated File:** T5_ex_stage_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fu_data_t
- load_valid_o

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T6_ex_stage_Covert.sv

---

