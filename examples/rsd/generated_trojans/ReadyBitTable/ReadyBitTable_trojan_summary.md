# Trojan Generation Summary

**Module:** ReadyBitTable
**File:** ReadyBitTable.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid
- dispatchedSrcReady
- readyWE
- ... and 2 more

**Payload Signals (7):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid
- dispatchedSrcReady
- readyWE
- ... and 2 more

**Generated File:** T1_ReadyBitTable_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- input

**Payload Signals (1):**
- output

**Generated File:** T2_ReadyBitTable_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid

**Payload Signals (7):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid
- dispatchedSrcReady
- readyWE
- ... and 2 more

**Generated File:** T3_ReadyBitTable_Availability.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- readyWE

**Payload Signals (0):**

**Generated File:** T4_ReadyBitTable_Privilege.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- input

**Payload Signals (0):**

**Generated File:** T5_ReadyBitTable_Covert.sv

---

