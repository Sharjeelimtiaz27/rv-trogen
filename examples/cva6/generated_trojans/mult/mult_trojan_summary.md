# Trojan Generation Summary

**Module:** mult
**File:** mult.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- mult_valid_i
- mult_valid_o
- mult_ready_o
- mult_valid_o
- mult_ready_o
- ... and 5 more

**Payload Signals (10):**
- mult_valid_i
- mult_valid_o
- mult_ready_o
- mult_valid_o
- mult_ready_o
- ... and 5 more

**Generated File:** T1_mult_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- fu_data_t
- fu_data_i
- div_valid_op
- mul_valid_op

**Payload Signals (7):**
- fu_data_t
- fu_data_i
- result_o
- result_o
- mul_result
- ... and 2 more

**Generated File:** T2_mult_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- mult_valid_i
- mult_valid_o
- mult_valid_o
- mul_valid
- div_valid
- ... and 2 more

**Payload Signals (10):**
- mult_valid_i
- mult_valid_o
- mult_ready_o
- mult_valid_o
- mult_ready_o
- ... and 5 more

**Generated File:** T3_mult_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fu_data_t
- fu_data_i

**Payload Signals (17):**
- fu_data_t
- fu_data_i
- mult_valid_i
- result_o
- mult_valid_o
- ... and 12 more

**Generated File:** T4_mult_Covert.sv

---

