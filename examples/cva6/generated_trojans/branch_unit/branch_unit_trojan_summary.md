# Trojan Generation Summary

**Module:** branch_unit
**File:** branch_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- branch_valid_i

**Payload Signals (1):**
- branch_valid_i

**Generated File:** T1_branch_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (5):**
- fu_data_t
- fu_data_i
- branch_result_o
- branch_result_o
- target_address

**Generated File:** T2_branch_unit_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- debug_mode_i
- target_address

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_branch_unit_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- fu_data_t
- fu_data_i
- target_address

**Payload Signals (4):**
- fu_data_t
- fu_data_i
- branch_result_o
- branch_result_o

**Generated File:** T4_branch_unit_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- branch_valid_i

**Payload Signals (1):**
- branch_valid_i

**Generated File:** T5_branch_unit_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fu_data_t
- fu_data_i

**Payload Signals (5):**
- fu_data_t
- fu_data_i
- branch_valid_i
- branch_result_o
- branch_result_o

**Generated File:** T6_branch_unit_Covert.sv

---

