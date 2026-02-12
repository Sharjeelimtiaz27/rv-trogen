# Trojan Generation Summary

**Module:** alu_wrapper
**File:** alu_wrapper.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- fu_data_t
- fu_data_i

**Payload Signals (4):**
- fu_data_t
- fu_data_i
- result_o
- result_o

**Generated File:** T1_alu_wrapper_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fu_data_t
- fu_data_i

**Payload Signals (4):**
- fu_data_t
- fu_data_i
- result_o
- result_o

**Generated File:** T2_alu_wrapper_Covert.sv

---

