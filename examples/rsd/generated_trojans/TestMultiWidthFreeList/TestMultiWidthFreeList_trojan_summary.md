# Trojan Generation Summary

**Module:** TestMultiWidthFreeList
**File:** TestMultiWidthFreeList.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- POP_WIDTH-1:0
- pop
- pushedData
- poppedData

**Payload Signals (2):**
- pushedData
- poppedData

**Generated File:** T1_TestMultiWidthFreeList_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- pushedData
- poppedData

**Payload Signals (2):**
- pushedData
- poppedData

**Generated File:** T2_TestMultiWidthFreeList_Covert.sv

---

