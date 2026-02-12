# Trojan Generation Summary

**Module:** ReplayQueue
**File:** ReplayQueue.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- intValid
- complexValid
- memValid
- fpValid
- replayEntryValidIn
- ... and 3 more

**Payload Signals (8):**
- intValid
- complexValid
- memValid
- fpValid
- replayEntryValidIn
- ... and 3 more

**Generated File:** T1_ReplayQueue_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- popEntry

**Payload Signals (1):**
- replayEntryValidOut

**Generated File:** T2_ReplayQueue_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- intValid
- complexValid
- memValid
- fpValid
- popEntry
- ... and 4 more

**Payload Signals (8):**
- intValid
- complexValid
- memValid
- fpValid
- replayEntryValidIn
- ... and 3 more

**Generated File:** T3_ReplayQueue_Availability.sv

---

