# Trojan Generation Summary

**Module:** Core
**File:** Core.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- reqExternalInterrupt
- memAccessWE
- serialWE
- memAccessWE
- serialWE

**Payload Signals (5):**
- reqExternalInterrupt
- memAccessWE
- serialWE
- memAccessWE
- serialWE

**Generated File:** T1_Core_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (11):**
- MemWriteSerial
- nextMemWriteSerial
- memAccessWriteBusy
- memAccessWriteData
- memAccessWE
- ... and 6 more

**Payload Signals (15):**
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- PhyAddrPath
- memAccessAddr
- ... and 10 more

**Generated File:** T2_Core_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- PhyAddrPath
- memAccessAddr
- ... and 10 more

**Payload Signals (14):**
- MemWriteSerial
- nextMemWriteSerial
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- ... and 9 more

**Generated File:** T3_Core_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (23):**
- MemAccessSerial
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- MemAccessSerial
- ... and 18 more

**Payload Signals (11):**
- MemoryEntryDataPath
- memReadData
- memReadDataReady
- MemoryEntryDataPath
- memAccessWriteData
- ... and 6 more

**Generated File:** T4_Core_Covert.sv

---

