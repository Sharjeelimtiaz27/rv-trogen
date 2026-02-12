# Trojan Generation Summary

**Module:** BitCounter
**File:** BitCounter.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- DataPath
- fuOpA_In
- DataPath
- dataOut
- DataPath
- ... and 7 more

**Payload Signals (10):**
- DataPath
- DataPath
- dataOut
- DataPath
- DataPath
- ... and 5 more

**Generated File:** T1_BitCounter_Integrity.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- fuOpA_In
- fuOpA_In

**Payload Signals (1):**
- stall

**Generated File:** T2_BitCounter_Availability.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- DataPath
- DataPath
- dataOut
- DataPath
- DataPath
- ... and 5 more

**Payload Signals (10):**
- DataPath
- DataPath
- dataOut
- DataPath
- DataPath
- ... and 5 more

**Generated File:** T3_BitCounter_Covert.sv

---

