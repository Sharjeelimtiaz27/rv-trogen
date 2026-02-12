# Trojan Generation Summary

**Module:** issue_stage
**File:** issue_stage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (49):**
- decoded_instr_valid_i
- flu_ready_i
- alu_valid_o
- aes_valid_o
- branch_valid_o
- ... and 44 more

**Payload Signals (49):**
- decoded_instr_valid_i
- flu_ready_i
- alu_valid_o
- aes_valid_o
- branch_valid_o
- ... and 44 more

**Generated File:** T1_issue_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (8):**
- csr_valid_o
- x_we_i
- we_gpr_i
- we_fpr_i
- csr_valid_o
- ... and 3 more

**Payload Signals (12):**
- fu_data_t
- fu_data_o
- csr_valid_o
- wbdata_i
- waddr_i
- ... and 7 more

**Generated File:** T2_issue_stage_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- fu_data_t
- fu_data_o
- wbdata_i
- waddr_i
- wdata_i
- ... and 7 more

**Payload Signals (8):**
- fu_data_t
- fu_data_o
- wbdata_i
- wdata_i
- fu_data_t
- ... and 3 more

**Generated File:** T3_issue_stage_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (37):**
- decoded_instr_valid_i
- alu_valid_o
- aes_valid_o
- branch_valid_o
- lsu_ready_i
- ... and 32 more

**Payload Signals (48):**
- stall_i
- decoded_instr_valid_i
- decoded_instr_ack_o
- flu_ready_i
- alu_valid_o
- ... and 43 more

**Generated File:** T4_issue_stage_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- fu_data_t
- fu_data_o
- wbdata_i
- wdata_i
- fu_data_t
- ... and 3 more

**Payload Signals (47):**
- decoded_instr_valid_i
- fu_data_t
- fu_data_o
- flu_ready_i
- alu_valid_o
- ... and 42 more

**Generated File:** T5_issue_stage_Covert.sv

---

