# Trojan Generation Summary

**Module:** alu
**File:** alu.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_cpop_i
- operand_a_rev
- ... and 9 more

**Payload Signals (16):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_cpop_i
- result_o
- ... and 11 more

**Generated File:** T1_alu_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_cpop_i

**Payload Signals (16):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_cpop_i
- result_o
- ... and 11 more

**Generated File:** T2_alu_Covert.sv

---

