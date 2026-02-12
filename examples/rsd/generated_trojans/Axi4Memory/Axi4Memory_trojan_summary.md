# Trojan Generation Summary

**Module:** Axi4Memory
**File:** Axi4Memory.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- memAccessWE
- axi_awvalid
- pushFreeReadReqID
- pushedFreeReadReqID
- popFreeReadReqID
- ... and 10 more

**Payload Signals (17):**
- memAccessWE
- axi_awvalid
- pushFreeReadReqID
- pushedFreeReadReqID
- popFreeReadReqID
- ... and 12 more

**Generated File:** T1_Axi4Memory_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (19):**
- memAccessWriteData
- memAccessWE
- memAccessWriteBusy
- MemWriteSerial
- nextMemWriteSerial
- ... and 14 more

**Payload Signals (21):**
- AddrPath
- memAccessAddr
- MemoryEntryDataPath
- memAccessWriteData
- memReadDataReady
- ... and 16 more

**Generated File:** T2_Axi4Memory_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (24):**
- AddrPath
- memAccessAddr
- MemoryEntryDataPath
- memAccessWriteData
- memReadDataReady
- ... and 19 more

**Payload Signals (28):**
- MemoryEntryDataPath
- memAccessWriteData
- memAccessWriteBusy
- MemWriteSerial
- nextMemWriteSerial
- ... and 23 more

**Generated File:** T3_Axi4Memory_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (14):**
- axi_awvalid
- pushFreeReadReqID
- pushedFreeReadReqID
- popFreeReadReqID
- popedFreeReadReqID
- ... and 9 more

**Payload Signals (5):**
- axi_awvalid
- axi_wvalid
- axi_arvalid
- writes_done
- reads_done

**Generated File:** T4_Axi4Memory_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (31):**
- memAccessAddr
- MemoryEntryDataPath
- memAccessWriteData
- memAccessRE
- memAccessWE
- ... and 26 more

**Payload Signals (19):**
- MemoryEntryDataPath
- memAccessWriteData
- memReadDataReady
- MemoryEntryDataPath
- memReadData
- ... and 14 more

**Generated File:** T5_Axi4Memory_Covert.sv

---

