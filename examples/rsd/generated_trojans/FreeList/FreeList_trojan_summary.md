# Trojan Generation Summary

**Module:** FreeList
**File:** FreeList.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- pop
- pushedData
- headData
- pop
- POP_WIDTH
- ... and 7 more

**Payload Signals (6):**
- pushedData
- headData
- pushedData
- poppedData
- headData
- ... and 1 more

**Generated File:** T1_FreeList_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- pushedData
- headData
- pushedData
- poppedData
- headData
- ... and 1 more

**Payload Signals (6):**
- pushedData
- headData
- pushedData
- poppedData
- headData
- ... and 1 more

**Generated File:** T2_FreeList_Covert.sv

---

