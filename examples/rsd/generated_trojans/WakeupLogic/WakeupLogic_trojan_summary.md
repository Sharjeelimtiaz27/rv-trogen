# Trojan Generation Summary

**Module:** WakeupLogic
**File:** WakeupLogic.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid

**Payload Signals (3):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid

**Generated File:** T1_WakeupLogic_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid

**Payload Signals (3):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid

**Generated File:** T2_WakeupLogic_Availability.sv

---

