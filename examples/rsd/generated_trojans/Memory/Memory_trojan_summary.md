# Trojan Generation Summary

**Module:** Memory
**File:** Memory.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- memAccessWE
- valid
- memoryWE
- pushRequestQueue

**Payload Signals (4):**
- memAccessWE
- valid
- memoryWE
- pushRequestQueue

**Generated File:** T1_Memory_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (7):**
- memAccessWriteData
- memAccessWE
- MemWriteSerial
- nextMemWriteSerial
- MemWriteSerial
- ... and 2 more

**Payload Signals (10):**
- AddrPath
- memAccessAddr
- MemoryEntryDataPath
- memAccessWriteData
- memReadDataReady
- ... and 5 more

**Generated File:** T2_Memory_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- AddrPath
- memAccessAddr
- MemoryEntryDataPath
- memAccessWriteData
- memReadDataReady
- ... and 5 more

**Payload Signals (12):**
- MemoryEntryDataPath
- memAccessWriteData
- MemWriteSerial
- nextMemWriteSerial
- memReadDataReady
- ... and 7 more

**Generated File:** T3_Memory_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- pushRequestQueue

**Payload Signals (1):**
- valid

**Generated File:** T4_Memory_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (21):**
- memAccessAddr
- MemoryEntryDataPath
- memAccessWriteData
- memAccessRE
- memAccessWE
- ... and 16 more

**Payload Signals (9):**
- MemoryEntryDataPath
- memAccessWriteData
- memReadDataReady
- MemoryEntryDataPath
- memReadData
- ... and 4 more

**Generated File:** T5_Memory_Covert.sv

---

