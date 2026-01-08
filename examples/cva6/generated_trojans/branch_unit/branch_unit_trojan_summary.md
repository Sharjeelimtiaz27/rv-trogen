# Trojan Generation Summary

**Module:** branch_unit
**File:** branch_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- branch_valid_i
- jump_taken

**Payload Signals (2):**
- branch_valid_i
- jump_taken

**Generated File:** T1_branch_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (1):**
- fu_data_t

**Generated File:** T2_branch_unit_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_branch_unit_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (1):**
- fu_data_t

**Generated File:** T4_branch_unit_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- fu_data_t
- branch_valid_i

**Payload Signals (1):**
- branch_valid_i

**Generated File:** T5_branch_unit_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T6_branch_unit_Covert.sv

---

