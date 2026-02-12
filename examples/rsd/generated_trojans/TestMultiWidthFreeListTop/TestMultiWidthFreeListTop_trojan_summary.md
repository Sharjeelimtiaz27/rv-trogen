# Trojan Generation Summary

**Module:** TestMultiWidthFreeListTop
**File:** TestMultiWidthFreeListTop.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- POP_WIDTH-1:0
- pop
- pushedData
- POP_WIDTH-1:0
- poppedData
- ... and 6 more

**Payload Signals (5):**
- pushedData
- poppedData
- poppedData
- unpackedPushedData
- unpackedPoppedData

**Generated File:** T1_TestMultiWidthFreeListTop_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- pushedData
- poppedData
- poppedData
- unpackedPushedData
- unpackedPoppedData

**Payload Signals (5):**
- pushedData
- poppedData
- poppedData
- unpackedPushedData
- unpackedPoppedData

**Generated File:** T2_TestMultiWidthFreeListTop_Covert.sv

---

