# Trojan Generation Summary

**Module:** MultiplierUnit
**File:** MultiplierUnit.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (22):**
- DataPath
- fuOpA_In
- DataPath
- fuOpB_In
- DataPath
- ... and 17 more

**Payload Signals (15):**
- DataPath
- DataPath
- DataPath
- dataOut
- DataPath
- ... and 10 more

**Generated File:** T1_MultiplierUnit_Integrity.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- fuOpA_In
- fuOpB_In
- fuOpA_In
- fuOpB_In
- fuOpA_sign
- ... and 3 more

**Payload Signals (1):**
- stall

**Generated File:** T2_MultiplierUnit_Availability.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (14):**
- DataPath
- DataPath
- DataPath
- dataOut
- DataPath
- ... and 9 more

**Payload Signals (15):**
- DataPath
- DataPath
- DataPath
- dataOut
- DataPath
- ... and 10 more

**Generated File:** T3_MultiplierUnit_Covert.sv

---

