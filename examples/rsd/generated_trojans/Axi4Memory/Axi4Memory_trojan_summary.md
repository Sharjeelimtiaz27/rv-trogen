# Trojan Generation Summary

**Module:** Axi4Memory
**File:** Axi4Memory.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (19):**
- memReadDataReady
- axi_awvalid
- pushFreeReadReqID
- popFreeReadReqID
- readReqIDFreeListFull
- ... and 14 more

**Payload Signals (22):**
- memReadDataReady
- axi_awvalid
- pushFreeReadReqID
- popFreeReadReqID
- readReqIDFreeListFull
- ... and 17 more

**Generated File:** T1_Axi4Memory_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- wnext
- rnext

**Payload Signals (8):**
- AddrPath
- memReadDataReady
- memoryReadDataTableWE
- pushMemoryWriteData
- popMemoryWriteData
- ... and 3 more

**Generated File:** T2_Axi4Memory_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (12):**
- AddrPath
- memAccessWE
- memAccessWriteBusy
- memoryReadDataTableWE
- pushMemoryWriteData
- ... and 7 more

**Payload Signals (1):**
- mst_exec_state

**Generated File:** T3_Axi4Memory_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (9):**
- AddrPath
- memReadDataReady
- popFreeReadReqID
- popMemoryReadReq
- memoryReadDataTableWE
- ... and 4 more

**Payload Signals (11):**
- memAccessWriteBusy
- memReadDataReady
- memoryReadDataTableWE
- pushMemoryWriteData
- popMemoryWriteData
- ... and 6 more

**Generated File:** T4_Axi4Memory_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (19):**
- memReadDataReady
- axi_awvalid
- pushFreeReadReqID
- popFreeReadReqID
- readReqIDFreeListFull
- ... and 14 more

**Payload Signals (11):**
- memAccessReadBusy
- memAccessWriteBusy
- memReadDataReady
- axi_awvalid
- axi_wvalid
- ... and 6 more

**Generated File:** T5_Axi4Memory_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- memAccessReadBusy
- memAccessRE
- memAccessWE
- memAccessWriteBusy
- memReadDataReady
- ... and 5 more

**Payload Signals (2):**
- memAccessReadBusy
- memAccessWriteBusy

**Generated File:** T6_Axi4Memory_Covert.sv

---

