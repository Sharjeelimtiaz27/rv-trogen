# Trojan Generation Summary

**Module:** FP32PipelinedMultiplier
**File:** FP32PipelinedMultiplier.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- generate_subnormal
- generate_subnormal_shift

**Payload Signals (2):**
- generate_subnormal
- generate_subnormal_shift

**Generated File:** T1_FP32PipelinedMultiplier_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (5):**
- FMulStage1RegPath
- FMulStage2RegPath
- FMulStage1RegPath
- FMulStage2RegPath
- pipeReg

**Generated File:** T2_FP32PipelinedMultiplier_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (5):**
- result
- result
- stg2Out
- result_sign
- result_expo

**Generated File:** T3_FP32PipelinedMultiplier_Integrity.sv

---

