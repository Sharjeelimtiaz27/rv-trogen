# Trojan Generation Summary

**Module:** FP32DivSqrter
**File:** FP32DivSqrter.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- req

**Payload Signals (1):**
- req

**Generated File:** T1_FP32DivSqrter_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (6):**
- regData.v_lhs_mant
- regData.v_rhs_mant
- regData.is_divide
- regData.res_is_zero
- regData.rem
- ... and 1 more

**Payload Signals (10):**
- result
- result
- result_sign
- regData.v_lhs_mant
- regData.v_rhs_mant
- ... and 5 more

**Generated File:** T2_FP32DivSqrter_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- regData.v_lhs_mant
- regData.v_rhs_mant
- regData.is_divide
- regData.res_is_zero
- regData.rem
- ... and 1 more

**Payload Signals (10):**
- result
- result
- result_sign
- regData.v_lhs_mant
- regData.v_rhs_mant
- ... and 5 more

**Generated File:** T3_FP32DivSqrter_Covert.sv

---

