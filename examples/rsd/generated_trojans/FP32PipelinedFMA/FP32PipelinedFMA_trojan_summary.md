# Trojan Generation Summary

**Module:** FP32PipelinedFMA
**File:** FP32PipelinedFMA.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- prop_inf_sign
- pipeReg.prop_inf_sign

**Payload Signals (22):**
- result
- stg0Out
- stg1Out
- stg2Out
- fma_result
- ... and 17 more

**Generated File:** T1_FP32PipelinedFMA_Integrity.sv

---

