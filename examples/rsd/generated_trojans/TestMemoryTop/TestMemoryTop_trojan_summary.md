# Trojan Generation Summary

**Module:** TestMemoryTop
**File:** TestMemoryTop.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- MemReadAccessReq

**Payload Signals (1):**
- MemReadAccessReq

**Generated File:** T1_TestMemoryTop_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (2):**
- rstOut
- MemAccessResult

**Generated File:** T2_TestMemoryTop_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- MemReadAccessReq

**Payload Signals (0):**

**Generated File:** T3_TestMemoryTop_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- MemReadAccessReq
- MemAccessResult

**Payload Signals (0):**

**Generated File:** T4_TestMemoryTop_Covert.sv

---

