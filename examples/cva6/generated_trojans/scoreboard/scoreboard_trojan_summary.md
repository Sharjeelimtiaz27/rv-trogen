# Trojan Generation Summary

**Module:** scoreboard
**File:** scoreboard.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- decoded_instr_valid_i
- issue_instr_valid_o
- wt_valid_i
- x_we_i
- decoded_instr_valid_i
- ... and 3 more

**Payload Signals (8):**
- decoded_instr_valid_i
- issue_instr_valid_o
- wt_valid_i
- x_we_i
- decoded_instr_valid_i
- ... and 3 more

**Generated File:** T1_scoreboard_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- x_issue_writeback_i
- x_we_i
- x_issue_writeback_i
- x_we_i

**Payload Signals (2):**
- wbdata_i
- wbdata_i

**Generated File:** T2_scoreboard_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- commit_drop_o
- wbdata_i
- commit_drop_o
- wbdata_i

**Payload Signals (4):**
- x_issue_writeback_i
- wbdata_i
- x_issue_writeback_i
- wbdata_i

**Generated File:** T3_scoreboard_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- commit_drop_o
- decoded_instr_valid_i
- issue_instr_valid_o
- wt_valid_i
- commit_drop_o
- ... and 3 more

**Payload Signals (12):**
- commit_ack_i
- decoded_instr_valid_i
- decoded_instr_ack_o
- issue_instr_valid_o
- issue_ack_i
- ... and 7 more

**Generated File:** T4_scoreboard_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- wbdata_i
- wbdata_i

**Payload Signals (8):**
- decoded_instr_valid_i
- issue_instr_valid_o
- wbdata_i
- wt_valid_i
- decoded_instr_valid_i
- ... and 3 more

**Generated File:** T5_scoreboard_Covert.sv

---

