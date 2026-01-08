# Trojan Generation Summary

**Module:** TestMain
**File:** TestMain.sv
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
- enableDumpKanata
- enableDumpRegCSV

**Payload Signals (2):**
- enableDumpKanata
- enableDumpRegCSV

**Generated File:** T1_TestMain_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- DataPath

**Payload Signals (2):**
- DataPath
- enableDumpRegCSV

**Generated File:** T2_TestMain_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- DataPath

**Payload Signals (1):**
- DataPath

**Generated File:** T3_TestMain_Integrity.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- serialWE

**Payload Signals (0):**

**Generated File:** T4_TestMain_Privilege.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- DataPath

**Payload Signals (0):**

**Generated File:** T5_TestMain_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- DataPath

**Payload Signals (0):**

**Generated File:** T6_TestMain_Covert.sv

---

