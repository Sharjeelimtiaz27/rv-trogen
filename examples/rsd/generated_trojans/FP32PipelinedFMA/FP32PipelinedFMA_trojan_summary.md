# Trojan Generation Summary

**Module:** FP32PipelinedFMA
**File:** FP32PipelinedFMA.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (12):**
- addend
- addend
- maddend
- addend_sign
- addend_expo
- ... and 7 more

**Payload Signals (12):**
- addend
- addend
- maddend
- addend_sign
- addend_expo
- ... and 7 more

**Generated File:** T1_FP32PipelinedFMA_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- prop_inf_sign

**Payload Signals (7):**
- fma_result
- result
- result
- result_is_nan
- result_is_inf
- ... and 2 more

**Generated File:** T2_FP32PipelinedFMA_Integrity.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (8):**
- FMAStage1RegPath
- FMAStage2RegPath
- FMAStage3RegPath
- FMAStage4RegPath
- FMAStage1RegPath
- ... and 3 more

**Generated File:** T3_FP32PipelinedFMA_Leak.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- prop_inf_sign

**Payload Signals (0):**

**Generated File:** T4_FP32PipelinedFMA_Availability.sv

---

