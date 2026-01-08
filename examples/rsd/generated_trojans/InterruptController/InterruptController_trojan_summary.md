# Trojan Generation Summary

**Module:** InterruptController
**File:** InterruptController.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- reqInterrupt
- reqTimerInterrupt

**Payload Signals (2):**
- reqInterrupt
- reqTimerInterrupt

**Generated File:** T1_InterruptController_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.40
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- reqInterrupt
- reqTimerInterrupt

**Payload Signals (0):**

**Generated File:** T2_InterruptController_Availability.sv

---

