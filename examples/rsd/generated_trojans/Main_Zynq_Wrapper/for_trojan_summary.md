# Trojan Generation Summary

**Module:** for
**File:** Main_Zynq_Wrapper.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- DebugRegister

**Payload Signals (1):**
- DebugRegister

**Generated File:** T1_for_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- serialWE

**Payload Signals (0):**

**Generated File:** T2_for_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- posResetOut

**Generated File:** T3_for_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- DebugRegister

**Generated File:** T4_for_Covert.sv

---

