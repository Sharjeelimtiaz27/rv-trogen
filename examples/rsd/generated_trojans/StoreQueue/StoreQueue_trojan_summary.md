# Trojan Generation Summary

**Module:** StoreQueue
**File:** StoreQueue.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- executedStoreCondEnabled
- executedStoreRegValid

**Payload Signals (2):**
- executedStoreCondEnabled
- executedStoreRegValid

**Generated File:** T1_StoreQueue_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- DataPath
- LSQ_BlockDataPath
- MemAccessMode
- LSQ_BlockDataPath
- executeStore

**Payload Signals (5):**
- DataPath
- LSQ_BlockDataPath
- PhyAddrPath
- LSQ_BlockDataPath
- executedStoreRegValid

**Generated File:** T2_StoreQueue_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- PhyAddrPath
- MemAccessMode
- sqWE

**Payload Signals (1):**
- MemAccessMode

**Generated File:** T3_StoreQueue_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- DataPath
- LSQ_BlockDataPath
- PhyAddrPath
- LSQ_BlockDataPath

**Payload Signals (7):**
- DataPath
- LSQ_BlockDataPath
- LSQ_BlockDataPath
- executeStore
- executedStoreCondEnabled
- ... and 2 more

**Generated File:** T4_StoreQueue_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- DataPath
- LSQ_BlockDataPath
- LSQ_BlockDataPath
- executedStoreRegValid

**Payload Signals (1):**
- executedStoreRegValid

**Generated File:** T5_StoreQueue_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- DataPath
- LSQ_BlockDataPath
- MemAccessMode
- LSQ_BlockDataPath
- storeLoadForwarded

**Payload Signals (1):**
- executeStore

**Generated File:** T6_StoreQueue_Covert.sv

---

