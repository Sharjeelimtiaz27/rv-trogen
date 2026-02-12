# Trojan Generation Summary

**Module:** StoreQueue
**File:** StoreQueue.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- MemAccessMode
- mode
- MemAccessMode
- mode

**Payload Signals (14):**
- DataPath
- dataIn
- LSQ_BlockDataPath
- blockDataIn
- PhyAddrPath
- ... and 9 more

**Generated File:** T1_StoreQueue_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (8):**
- PhyAddrPath
- addr
- MemAccessMode
- mode
- PhyAddrPath
- ... and 3 more

**Payload Signals (4):**
- MemAccessMode
- mode
- MemAccessMode
- mode

**Generated File:** T2_StoreQueue_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- DataPath
- dataIn
- LSQ_BlockDataPath
- blockDataIn
- PhyAddrPath
- ... and 9 more

**Payload Signals (10):**
- DataPath
- dataIn
- LSQ_BlockDataPath
- blockDataIn
- LSQ_BlockDataPath
- ... and 5 more

**Generated File:** T3_StoreQueue_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- DataPath
- dataIn
- LSQ_BlockDataPath
- blockDataIn
- MemAccessMode
- ... and 7 more

**Payload Signals (10):**
- DataPath
- dataIn
- LSQ_BlockDataPath
- blockDataIn
- LSQ_BlockDataPath
- ... and 5 more

**Generated File:** T4_StoreQueue_Covert.sv

---

