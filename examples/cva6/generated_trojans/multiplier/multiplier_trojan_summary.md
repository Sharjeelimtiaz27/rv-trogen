# Trojan Generation Summary

**Module:** multiplier
**File:** multiplier.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- mult_valid_i
- mult_valid_o
- mult_valid_o
- mult_valid_q
- mult_valid

**Payload Signals (5):**
- mult_valid_i
- mult_valid_o
- mult_valid_o
- mult_valid_q
- mult_valid

**Generated File:** T1_multiplier_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- fu_op
- operation_i
- operand_a_i
- operand_b_i

**Payload Signals (2):**
- result_o
- result_o

**Generated File:** T2_multiplier_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- mult_valid_i
- fu_op
- operation_i
- operand_a_i
- operand_b_i
- ... and 4 more

**Payload Signals (5):**
- mult_valid_i
- mult_valid_o
- mult_valid_o
- mult_valid_q
- mult_valid

**Generated File:** T3_multiplier_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- operand_a_i
- operand_b_i

**Payload Signals (7):**
- mult_valid_i
- result_o
- mult_valid_o
- result_o
- mult_valid_o
- ... and 2 more

**Generated File:** T4_multiplier_Covert.sv

---

