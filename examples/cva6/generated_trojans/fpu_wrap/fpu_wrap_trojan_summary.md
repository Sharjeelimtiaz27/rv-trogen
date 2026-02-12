# Trojan Generation Summary

**Module:** fpu_wrap
**File:** fpu_wrap.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- fpu_valid_i
- fpu_ready_o
- fpu_valid_o
- fpu_early_valid_o
- fpu_ready_o
- ... and 2 more

**Payload Signals (7):**
- fpu_valid_i
- fpu_ready_o
- fpu_valid_o
- fpu_early_valid_o
- fpu_ready_o
- ... and 2 more

**Generated File:** T1_fpu_wrap_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (8):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_i
- operand_a_i
- ... and 3 more

**Payload Signals (6):**
- fu_data_t
- fu_data_i
- result_o
- fu_data_t
- fu_data_i
- ... and 1 more

**Generated File:** T2_fpu_wrap_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- fpu_valid_i
- fpu_valid_o
- fpu_early_valid_o
- fpu_valid_o
- fpu_early_valid_o
- ... and 4 more

**Payload Signals (7):**
- fpu_valid_i
- fpu_ready_o
- fpu_valid_o
- fpu_early_valid_o
- fpu_ready_o
- ... and 2 more

**Generated File:** T3_fpu_wrap_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_i
- operand_a_i
- ... and 1 more

**Payload Signals (13):**
- fpu_valid_i
- fpu_ready_o
- fu_data_t
- fu_data_i
- result_o
- ... and 8 more

**Generated File:** T4_fpu_wrap_Covert.sv

---

