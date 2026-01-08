# Trojan Generation Summary

**Module:** WakeupPipelineRegister
**File:** WakeupPipelineRegister.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- valid

**Payload Signals (1):**
- valid

**Generated File:** T1_WakeupPipelineRegister_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- valid

**Payload Signals (1):**
- valid

**Generated File:** T2_WakeupPipelineRegister_Availability.sv

---

