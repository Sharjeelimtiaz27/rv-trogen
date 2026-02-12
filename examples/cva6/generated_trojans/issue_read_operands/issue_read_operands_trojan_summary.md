# Trojan Generation Summary

**Module:** issue_read_operands
**File:** issue_read_operands.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (51):**
- issue_instr_valid_i
- flu_ready_i
- alu_valid_o
- aes_valid_o
- branch_valid_o
- ... and 46 more

**Payload Signals (51):**
- issue_instr_valid_i
- flu_ready_i
- alu_valid_o
- aes_valid_o
- branch_valid_o
- ... and 46 more

**Generated File:** T1_issue_read_operands_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- csr_valid_o
- x_issue_writeback_o
- we_gpr_i
- we_fpr_i
- csr_valid_o
- ... and 5 more

**Payload Signals (17):**
- fu_data_t
- fu_data_o
- csr_valid_o
- waddr_i
- wdata_i
- ... and 12 more

**Generated File:** T2_issue_read_operands_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- fu_data_t
- fu_data_o
- waddr_i
- wdata_i
- fu_data_t
- ... and 10 more

**Payload Signals (12):**
- fu_data_t
- fu_data_o
- x_issue_writeback_o
- wdata_i
- fu_data_t
- ... and 7 more

**Generated File:** T3_issue_read_operands_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (38):**
- issue_instr_valid_i
- alu_valid_o
- aes_valid_o
- branch_valid_o
- lsu_ready_i
- ... and 33 more

**Payload Signals (46):**
- stall_i
- issue_instr_valid_i
- issue_ack_o
- flu_ready_i
- alu_valid_o
- ... and 41 more

**Generated File:** T4_issue_read_operands_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- fu_data_t
- fu_data_o
- wdata_i
- fu_data_t
- fu_data_o
- ... and 5 more

**Payload Signals (51):**
- issue_instr_valid_i
- fu_data_t
- fu_data_o
- flu_ready_i
- alu_valid_o
- ... and 46 more

**Generated File:** T5_issue_read_operands_Covert.sv

---

