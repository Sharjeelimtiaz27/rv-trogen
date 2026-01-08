# Trojan Generation Summary

**Module:** is
**File:** WakeupSelectIF.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- opReady
- releaseEntry
- opReady
- memDependencyPred
- intIssueReq
- ... and 4 more

**Payload Signals (9):**
- opReady
- releaseEntry
- opReady
- memDependencyPred
- intIssueReq
- ... and 4 more

**Generated File:** T1_is_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- selected
- opReady
- opReady
- selected
- selects

**Payload Signals (3):**
- write
- dispatchStore
- storeIssueReq

**Generated File:** T2_is_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- opReady
- opReady
- intIssueReq
- complexIssueReq
- loadIssueReq
- ... and 2 more

**Payload Signals (3):**
- opReady
- stall
- opReady

**Generated File:** T3_is_Availability.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- write

**Payload Signals (0):**

**Generated File:** T4_is_Privilege.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- dispatchLoad
- loadIssueReq

**Payload Signals (0):**

**Generated File:** T5_is_Covert.sv

---

