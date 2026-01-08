# Trojan Generation Summary

**Module:** ControlQueue
**File:** ControlQueue.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- pop

**Payload Signals (0):**

**Generated File:** T1_ControlQueue_Integrity.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- pop

**Payload Signals (0):**

**Generated File:** T2_ControlQueue_Availability.sv

---

