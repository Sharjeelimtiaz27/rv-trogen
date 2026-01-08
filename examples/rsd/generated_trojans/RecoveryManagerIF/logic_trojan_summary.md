# Trojan Generation Summary

**Module:** logic
**File:** RecoveryManagerIF.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- unableToStartRecovery
- recoverFromRename
- renameLogicRecoveryRMT
- flushIQ_Entry
- storeQueueHeadPtr

**Payload Signals (5):**
- unableToStartRecovery
- recoverFromRename
- renameLogicRecoveryRMT
- flushIQ_Entry
- storeQueueHeadPtr

**Generated File:** T1_logic_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- selected
- replayQueueFlushedOpExist
- wakeupPipelineRegFlushedOpExist

**Payload Signals (1):**
- storeQueueHeadPtr

**Generated File:** T2_logic_Integrity.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- wakeupPipelineRegFlushedOpExist

**Generated File:** T3_logic_Leak.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- unableToStartRecovery
- replayQueueFlushedOpExist
- wakeupPipelineRegFlushedOpExist
- storeQueueHeadPtr

**Payload Signals (0):**

**Generated File:** T4_logic_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- loadQueueHeadPtr

**Payload Signals (0):**

**Generated File:** T5_logic_Covert.sv

---

