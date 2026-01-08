# Trojan Generation Summary

**Module:** issue_read_operands
**File:** issue_read_operands.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- scoreboard_entry_t
- scoreboard_entry_t
- flu_ready_i
- lsu_ready_i
- fpu_ready_i
- ... and 10 more

**Payload Signals (15):**
- scoreboard_entry_t
- scoreboard_entry_t
- flu_ready_i
- lsu_ready_i
- fpu_ready_i
- ... and 10 more

**Generated File:** T1_issue_read_operands_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- fu_data_t
- flipflop

**Payload Signals (2):**
- fu_data_t
- x_issue_writeback_o

**Generated File:** T2_issue_read_operands_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- fpu_early_valid_i
- fu_data_t
- x_issue_valid_o
- x_issue_req_t
- x_register_valid_o
- ... and 4 more

**Payload Signals (14):**
- stall_i
- flu_ready_i
- lsu_ready_i
- fpu_ready_i
- fpu_early_valid_i
- ... and 9 more

**Generated File:** T3_issue_read_operands_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- x_register_ready_i
- fu_data_t
- x_register_valid_o
- x_register_t

**Generated File:** T4_issue_read_operands_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- x_issue_writeback_o
- cvxif_req_allowed

**Payload Signals (0):**

**Generated File:** T5_issue_read_operands_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T6_issue_read_operands_Covert.sv

---

