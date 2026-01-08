# Trojan Generation Summary

**Module:** WakeupLogic
**File:** WakeupLogic.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid
- dispatchedSrcRegReady
- opMatrixReady
- ... and 1 more

**Payload Signals (6):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid
- dispatchedSrcRegReady
- opMatrixReady
- ... and 1 more

**Generated File:** T1_WakeupLogic_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- opMatrixReady

**Payload Signals (1):**
- dispatchStore

**Generated File:** T2_WakeupLogic_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid
- opMatrixReady

**Payload Signals (5):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid
- dispatchedSrcRegReady
- opMatrixReady

**Generated File:** T3_WakeupLogic_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- dispatchedSrcRegValid
- dispatchedDstRegValid
- wakeupDstRegValid
- dispatchedSrcRegReady

**Generated File:** T4_WakeupLogic_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- dispatchLoad

**Payload Signals (0):**

**Generated File:** T5_WakeupLogic_Covert.sv

---

