# Trojan Generation Summary

**Module:** amo_alu
**File:** amo_alu.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- amo_op_i
- amo_operand_a_i
- amo_operand_b_i

**Payload Signals (2):**
- amo_result_o
- amo_result_o

**Generated File:** T1_amo_alu_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- amo_operand_a_i
- amo_operand_b_i

**Payload Signals (2):**
- amo_result_o
- amo_result_o

**Generated File:** T2_amo_alu_Covert.sv

---

