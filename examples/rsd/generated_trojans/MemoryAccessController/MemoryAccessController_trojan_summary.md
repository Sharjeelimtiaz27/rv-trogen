# Trojan Generation Summary

**Module:** MemoryAccessController
**File:** MemoryAccessController.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- memAccessWE
- memAccessWE

**Payload Signals (2):**
- memAccessWE
- memAccessWE

**Generated File:** T1_MemoryAccessController_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (7):**
- MemWriteSerial
- nextMemWriteSerial
- memAccessWriteBusy
- memAccessWriteData
- memAccessWE
- ... and 2 more

**Payload Signals (11):**
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- PhyAddrPath
- memAccessAddr
- ... and 6 more

**Generated File:** T2_MemoryAccessController_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- PhyAddrPath
- memAccessAddr
- ... and 6 more

**Payload Signals (10):**
- MemWriteSerial
- nextMemWriteSerial
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- ... and 5 more

**Generated File:** T3_MemoryAccessController_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (19):**
- MemAccessSerial
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- MemAccessSerial
- ... and 14 more

**Payload Signals (7):**
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- MemoryEntryDataPath
- memAccessWriteData
- ... and 2 more

**Generated File:** T4_MemoryAccessController_Covert.sv

---

