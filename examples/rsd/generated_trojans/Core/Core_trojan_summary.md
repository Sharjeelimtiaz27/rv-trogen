# Trojan Generation Summary

**Module:** Core
**File:** Core.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- memReadDataReady
- reqExternalInterrupt

**Payload Signals (2):**
- memReadDataReady
- reqExternalInterrupt

**Generated File:** T1_Core_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- DebugRegister
- reqExternalInterrupt
- ControllerIF

**Payload Signals (2):**
- DebugRegister
- memReadDataReady

**Generated File:** T2_Core_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (2):**
- memReadDataReady
- memAccessWriteBusy

**Generated File:** T3_Core_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- memReadDataReady
- reqExternalInterrupt

**Payload Signals (3):**
- memReadDataReady
- memAccessReadBusy
- memAccessWriteBusy

**Generated File:** T4_Core_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- memReadDataReady
- memAccessReadBusy
- memAccessWriteBusy
- memAccessRE
- memAccessWE

**Payload Signals (3):**
- DebugRegister
- memAccessReadBusy
- memAccessWriteBusy

**Generated File:** T5_Core_Covert.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- memAccessWriteBusy
- memAccessWE
- serialWE
- ControllerIF

**Payload Signals (0):**

**Generated File:** T6_Core_Privilege.sv

---

