# Trojan Generation Summary

**Module:** TestMultiWidthFreeListTop
**File:** TestMultiWidthFreeListTop.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- unpackedPop

**Payload Signals (2):**
- unpackedPush
- unpackedPop

**Generated File:** T1_TestMultiWidthFreeListTop_Availability.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- unpackedPop

**Payload Signals (0):**

**Generated File:** T2_TestMultiWidthFreeListTop_Integrity.sv

---

