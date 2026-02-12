# Trojan Generation Summary

**Module:** FP32PipelinedOther
**File:** FP32PipelinedOther.sv
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
- lower_bits

**Payload Signals (1):**
- lower_bits

**Generated File:** T1_FP32PipelinedOther_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- Rounding_Mode
- Rounding_Mode
- Rounding_Mode
- lower_bits

**Payload Signals (7):**
- result
- result
- result
- result
- result
- ... and 2 more

**Generated File:** T2_FP32PipelinedOther_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- Rounding_Mode
- Rounding_Mode
- Rounding_Mode
- lower_bits

**Payload Signals (3):**
- Rounding_Mode
- Rounding_Mode
- Rounding_Mode

**Generated File:** T3_FP32PipelinedOther_Privilege.sv

---

