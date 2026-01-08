# Trojan Generation Summary

**Module:** commit_stage
**File:** commit_stage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- scoreboard_entry_t
- commit_lsu_ready_i
- no_st_pending_i
- break_from_trigger_i
- amo_valid_commit_o
- ... and 5 more

**Payload Signals (9):**
- scoreboard_entry_t
- commit_lsu_ready_i
- no_st_pending_i
- amo_valid_commit_o
- fence_i_o
- ... and 4 more

**Generated File:** T1_commit_stage_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- csr_write_fflags_o
- commit_csr_o

**Payload Signals (1):**
- dirty_fp_state_o

**Generated File:** T2_commit_stage_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- fu_op

**Payload Signals (1):**
- csr_write_fflags_o

**Generated File:** T3_commit_stage_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- break_from_trigger_i
- fu_op
- amo_valid_commit_o

**Payload Signals (2):**
- commit_lsu_ready_i
- amo_valid_commit_o

**Generated File:** T4_commit_stage_Availability.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- csr_write_fflags_o
- commit_csr_o

**Generated File:** T5_commit_stage_Leak.sv

---

