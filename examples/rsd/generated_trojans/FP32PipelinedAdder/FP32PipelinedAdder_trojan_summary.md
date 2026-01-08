# Trojan Generation Summary

**Module:** FP32PipelinedAdder
**File:** FP32PipelinedAdder.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (5):**
- FAddStage1RegPath
- FAddStage2RegPath
- FAddStage1RegPath
- FAddStage2RegPath
- pipeReg

**Generated File:** T1_FP32PipelinedAdder_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (6):**
- result
- result
- stg2Out
- suber_result
- adder_result
- ... and 1 more

**Generated File:** T2_FP32PipelinedAdder_Integrity.sv

---

