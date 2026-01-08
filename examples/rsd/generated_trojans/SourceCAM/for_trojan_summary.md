# Trojan Generation Summary

**Module:** for
**File:** SourceCAM.sv
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
- dispatchedSrcReady
- wakeupDstValid
- srcReady
- nextSrcReady

**Payload Signals (4):**
- dispatchedSrcReady
- wakeupDstValid
- srcReady
- nextSrcReady

**Generated File:** T1_for_DoS.sv

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

**Generated File:** T2_for_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- wakeupDstValid

**Payload Signals (4):**
- dispatchedSrcReady
- wakeupDstValid
- srcReady
- nextSrcReady

**Generated File:** T3_for_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- nextSrcReady

**Payload Signals (0):**

**Generated File:** T4_for_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- input

**Payload Signals (0):**

**Generated File:** T5_for_Covert.sv

---

