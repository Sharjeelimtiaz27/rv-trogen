# Trojan Generation Summary

**Module:** ComplexIntegerRegisterWriteStage
**File:** ComplexIntegerRegisterWriteStage.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- valid
- regValid

**Payload Signals (2):**
- valid
- regValid

**Generated File:** T1_ComplexIntegerRegisterWriteStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- regValid

**Payload Signals (2):**
- valid
- regValid

**Generated File:** T2_ComplexIntegerRegisterWriteStage_Availability.sv

---

