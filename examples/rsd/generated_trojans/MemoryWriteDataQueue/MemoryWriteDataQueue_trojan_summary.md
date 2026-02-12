# Trojan Generation Summary

**Module:** MemoryWriteDataQueue
**File:** MemoryWriteDataQueue.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- `MEMORY_AXI4_WRITE_ID_NUM

**Payload Signals (6):**
- MemoryEntryDataPath
- pushedData
- MemoryEntryDataPath
- headData
- MemoryEntryDataPath
- ... and 1 more

**Generated File:** T1_MemoryWriteDataQueue_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- pop
- MemoryEntryDataPath
- pushedData
- MemoryEntryDataPath
- headData
- ... and 2 more

**Payload Signals (7):**
- MemoryEntryDataPath
- pushedData
- MemoryEntryDataPath
- headData
- MemoryEntryDataPath
- ... and 2 more

**Generated File:** T2_MemoryWriteDataQueue_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- MemoryEntryDataPath
- pushedData
- MemoryEntryDataPath
- headData
- MemoryEntryDataPath
- ... and 1 more

**Payload Signals (6):**
- MemoryEntryDataPath
- pushedData
- MemoryEntryDataPath
- headData
- MemoryEntryDataPath
- ... and 1 more

**Generated File:** T3_MemoryWriteDataQueue_Covert.sv

---

