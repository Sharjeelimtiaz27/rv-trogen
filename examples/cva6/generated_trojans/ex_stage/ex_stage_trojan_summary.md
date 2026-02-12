# Trojan Generation Summary

**Module:** ex_stage
**File:** ex_stage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (82):**
- flu_ready_o
- flu_valid_o
- alu_valid_i
- aes_valid_i
- branch_valid_i
- ... and 77 more

**Payload Signals (82):**
- flu_ready_o
- flu_valid_o
- alu_valid_i
- aes_valid_i
- branch_valid_i
- ... and 77 more

**Generated File:** T1_ex_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (11):**
- debug_mode_i
- csr_valid_i
- csr_addr_o
- csr_commit_i
- x_we_o
- ... and 6 more

**Payload Signals (37):**
- fu_data_t
- fu_data_i
- flu_result_o
- csr_valid_i
- csr_addr_o
- ... and 32 more

**Generated File:** T2_ex_stage_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (17):**
- debug_mode_i
- csr_valid_i
- csr_addr_o
- csr_commit_i
- x_we_o
- ... and 12 more

**Payload Signals (9):**
- debug_mode_i
- riscv::priv_lvl_t
- priv_lvl_i
- riscv::priv_lvl_t
- ld_st_priv_lvl_i
- ... and 4 more

**Generated File:** T3_ex_stage_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- fu_data_t
- fu_data_i
- csr_addr_o
- pmpaddr_i
- rvfi_mem_paddr_o
- ... and 6 more

**Payload Signals (29):**
- fu_data_t
- fu_data_i
- flu_result_o
- load_result_o
- store_valid_o
- ... and 24 more

**Generated File:** T4_ex_stage_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (82):**
- flu_valid_o
- alu_valid_i
- aes_valid_i
- branch_valid_i
- csr_valid_i
- ... and 77 more

**Payload Signals (52):**
- flu_ready_o
- flu_valid_o
- alu_valid_i
- aes_valid_i
- branch_valid_i
- ... and 47 more

**Generated File:** T5_ex_stage_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- fu_data_t
- fu_data_i
- load_valid_o
- load_result_o
- load_trans_id_o
- ... and 5 more

**Payload Signals (69):**
- fu_data_t
- fu_data_i
- flu_result_o
- flu_ready_o
- flu_valid_o
- ... and 64 more

**Generated File:** T6_ex_stage_Covert.sv

---

