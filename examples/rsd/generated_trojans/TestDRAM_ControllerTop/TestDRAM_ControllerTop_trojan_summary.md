# Trojan Generation Summary

**Module:** TestDRAM_ControllerTop
**File:** TestDRAM_ControllerTop.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (2):**
- memCaribrationDone
- memReadDataReady

**Generated File:** T1_TestDRAM_ControllerTop_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- memReadDataReady
- cmdFull

**Payload Signals (3):**
- posResetOut
- ledOut
- memReadDataReady

**Generated File:** T2_TestDRAM_ControllerTop_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- memReadDataReady
- cmdFull

**Payload Signals (3):**
- memCaribrationDone
- memReadDataReady
- memBusy

**Generated File:** T3_TestDRAM_ControllerTop_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (1):**
- memBusy

**Generated File:** T4_TestDRAM_ControllerTop_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- memReadDataReady

**Generated File:** T5_TestDRAM_ControllerTop_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- memWE
- cmdFull

**Payload Signals (0):**

**Generated File:** T6_TestDRAM_ControllerTop_Privilege.sv

---

