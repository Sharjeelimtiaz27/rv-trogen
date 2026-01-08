# Trojan Generation Summary

**Module:** FP32PipelinedOther
**File:** FP32PipelinedOther.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- is_invalid

**Payload Signals (1):**
- is_invalid

**Generated File:** T1_FP32PipelinedOther_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- is_invalid

**Payload Signals (1):**
- is_invalid

**Generated File:** T2_FP32PipelinedOther_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- lower_bits

**Payload Signals (0):**

**Generated File:** T3_FP32PipelinedOther_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (5):**
- result
- result
- result
- int_result
- resultOut

**Generated File:** T4_FP32PipelinedOther_Integrity.sv

---

