# Trojan Generation Summary

**Module:** DCacheController
**File:** DCache.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- dcFlushReqAck
- req
- memValid
- tagArrayValidOutTmp
- missReq
- ... and 4 more

**Payload Signals (11):**
- dcFlushReqAck
- dcFlushComplete
- req
- memValid
- tagArrayValidOutTmp
- ... and 6 more

**Generated File:** T1_DCacheController_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (13):**
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- ... and 8 more

**Payload Signals (13):**
- loadStoreBusy
- tagArrayValidOutTmp
- dataArrayDirtyOutTmp
- dataArrayWE
- dataArrayByteWE
- ... and 8 more

**Generated File:** T2_DCacheController_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (14):**
- dcFlushReqAck
- req
- memValid
- tagArrayValidOutTmp
- dataArrayDirtyOutTmp
- ... and 9 more

**Payload Signals (8):**
- dcFlushReqAck
- dcFlushComplete
- mshrBusy
- loadStoreBusy
- memValid
- ... and 3 more

**Generated File:** T3_DCacheController_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- loadStoreBusy
- dataArrayDirtyOutTmp
- dataArrayWE
- dataArrayByteWE
- dataArrayDirtyIn
- ... and 3 more

**Payload Signals (2):**
- mshrBusy
- loadStoreBusy

**Generated File:** T4_DCacheController_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (19):**
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- ... and 14 more

**Generated File:** T5_DCacheController_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (14):**
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- PhyAddrPath
- ... and 9 more

**Payload Signals (0):**

**Generated File:** T6_DCacheController_Privilege.sv

---

