# Trojan Generation Summary

**Module:** DividerUnit
**File:** DividerUnit.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- req
- req
- valid

**Payload Signals (3):**
- req
- req
- valid

**Generated File:** T1_DividerUnit_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (16):**
- DataPath
- fuOpA_In
- DataPath
- fuOpB_In
- DataPath
- ... and 11 more

**Payload Signals (12):**
- DataPath
- DataPath
- DataPath
- dataOut
- DataPath
- ... and 7 more

**Generated File:** T2_DividerUnit_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- req
- fuOpA_In
- fuOpB_In
- req
- fuOpA_In
- ... and 2 more

**Payload Signals (2):**
- stall
- valid

**Generated File:** T3_DividerUnit_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- DataPath
- DataPath
- DataPath
- dataOut
- DataPath
- ... and 7 more

**Payload Signals (13):**
- DataPath
- DataPath
- DataPath
- dataOut
- DataPath
- ... and 8 more

**Generated File:** T4_DividerUnit_Covert.sv

---

