# Trojan Generation Summary

**Module:** StoreCommitter
**File:** StoreCommitter.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- valid
- condEnabled
- dcWriteReq
- releaseStoreQueueHead

**Payload Signals (4):**
- valid
- condEnabled
- dcWriteReq
- releaseStoreQueueHead

**Generated File:** T1_StoreCommitter_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- valid
- dcWriteReq
- releaseStoreQueueHead

**Payload Signals (3):**
- stallStoreTagStage
- valid
- finishWriteBack

**Generated File:** T2_StoreCommitter_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- headStoreHasAllocatedMSHRPipeReg

**Generated File:** T3_StoreCommitter_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- dcWriteReq
- dcWriteUncachable
- finishWriteBack

**Payload Signals (0):**

**Generated File:** T4_StoreCommitter_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (7):**
- portStoreHasAllocatedMSHR
- stallStoreTagStage
- headStoreHasAllocatedMSHRPipeReg
- dcWriteReq
- dcWriteUncachable
- ... and 2 more

**Generated File:** T5_StoreCommitter_Integrity.sv

---

