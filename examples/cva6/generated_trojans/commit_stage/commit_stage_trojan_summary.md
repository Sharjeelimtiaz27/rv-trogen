# Trojan Generation Summary

**Module:** commit_stage
**File:** commit_stage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- we_gpr_o
- we_fpr_o
- commit_lsu_ready_i
- amo_valid_commit_o
- break_from_trigger_i
- ... and 5 more

**Payload Signals (8):**
- we_gpr_o
- we_fpr_o
- commit_lsu_ready_i
- amo_valid_commit_o
- we_gpr_o
- ... and 3 more

**Generated File:** T1_commit_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (16):**
- we_gpr_o
- we_fpr_o
- csr_op_o
- csr_wdata_o
- csr_rdata_i
- ... and 11 more

**Payload Signals (16):**
- waddr_o
- wdata_o
- csr_op_o
- csr_wdata_o
- csr_rdata_i
- ... and 11 more

**Generated File:** T2_commit_stage_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- commit_drop_i
- waddr_o
- wdata_o
- fu_op
- csr_op_o
- ... and 9 more

**Payload Signals (8):**
- wdata_o
- csr_wdata_o
- csr_rdata_i
- csr_write_fflags_o
- wdata_o
- ... and 3 more

**Generated File:** T3_commit_stage_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (14):**
- commit_drop_i
- fu_op
- csr_op_o
- commit_lsu_o
- commit_lsu_ready_i
- ... and 9 more

**Payload Signals (8):**
- commit_ack_o
- commit_macro_ack_o
- commit_lsu_ready_i
- amo_valid_commit_o
- commit_ack_o
- ... and 3 more

**Generated File:** T4_commit_stage_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- wdata_o
- csr_wdata_o
- csr_rdata_i
- wdata_o
- csr_wdata_o
- ... and 1 more

**Payload Signals (10):**
- wdata_o
- csr_wdata_o
- csr_rdata_i
- commit_lsu_ready_i
- amo_valid_commit_o
- ... and 5 more

**Generated File:** T5_commit_stage_Covert.sv

---

