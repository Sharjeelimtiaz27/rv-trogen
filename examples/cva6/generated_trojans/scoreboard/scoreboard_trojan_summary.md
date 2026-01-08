# Trojan Generation Summary

**Module:** scoreboard
**File:** scoreboard.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- scoreboard_entry_t
- scoreboard_entry_t
- scoreboard_entry_t

**Payload Signals (3):**
- scoreboard_entry_t
- scoreboard_entry_t
- scoreboard_entry_t

**Generated File:** T1_scoreboard_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- x_issue_writeback_i
- x_we_i
- writeback_t

**Payload Signals (0):**

**Generated File:** T2_scoreboard_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (2):**
- x_issue_writeback_i
- writeback_t

**Generated File:** T3_scoreboard_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (0):**

**Payload Signals (2):**
- x_issue_writeback_i
- writeback_t

**Generated File:** T4_scoreboard_Availability.sv

---

