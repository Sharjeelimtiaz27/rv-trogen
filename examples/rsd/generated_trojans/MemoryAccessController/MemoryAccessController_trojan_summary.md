# Trojan Generation Summary

**Module:** MemoryAccessController
**File:** MemoryAccessController.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (1):**
- memReadDataReady

**Generated File:** T1_MemoryAccessController_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- PhyAddrPath
- memReadDataReady

**Payload Signals (2):**
- memReadDataReady
- memAccessWriteBusy

**Generated File:** T2_MemoryAccessController_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (5):**
- memReadDataReady
- memAccessReadBusy
- memAccessWriteBusy
- icAck
- dcAck

**Generated File:** T3_MemoryAccessController_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- MemAccessSerial
- memReadDataReady
- memAccessReadBusy
- memAccessWriteBusy
- memAccessRE
- ... and 1 more

**Payload Signals (2):**
- memAccessReadBusy
- memAccessWriteBusy

**Generated File:** T4_MemoryAccessController_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- PhyAddrPath
- memReadDataReady

**Generated File:** T5_MemoryAccessController_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- PhyAddrPath
- memAccessWriteBusy
- memAccessWE

**Payload Signals (0):**

**Generated File:** T6_MemoryAccessController_Privilege.sv

---

