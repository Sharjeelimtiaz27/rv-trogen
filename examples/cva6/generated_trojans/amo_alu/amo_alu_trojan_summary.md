# Trojan Generation Summary

**Module:** amo_alu
**File:** amo_alu.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- amo_operand_a_i
- amo_operand_b_i
- operand_b
- adder_operand_a

**Payload Signals (1):**
- amo_result_o

**Generated File:** T1_amo_alu_Integrity.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.40
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- amo_operand_a_i
- amo_operand_b_i
- operand_b
- adder_operand_a

**Payload Signals (0):**

**Generated File:** T2_amo_alu_Availability.sv

---

