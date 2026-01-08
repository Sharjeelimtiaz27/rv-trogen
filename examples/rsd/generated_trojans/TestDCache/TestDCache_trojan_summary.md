# Trojan Generation Summary

**Module:** TestDCache
**File:** TestDCache.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- dcFillReq

**Payload Signals (1):**
- dcFillReq

**Generated File:** T1_TestDCache_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- dcFillReq

**Payload Signals (2):**
- dcFillerBusy
- dcFillAck

**Generated File:** T2_TestDCache_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- dcWE
- dcWriteHit

**Payload Signals (0):**

**Generated File:** T3_TestDCache_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- dcWriteHit

**Generated File:** T4_TestDCache_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- dcFillerBusy

**Generated File:** T5_TestDCache_Covert.sv

---

