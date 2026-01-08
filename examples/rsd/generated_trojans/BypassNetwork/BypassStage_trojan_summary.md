# Trojan Generation Summary

**Module:** BypassStage
**File:** BypassNetwork.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- PipelineControll

**Payload Signals (0):**

**Generated File:** T1_BypassStage_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- PipelineControll

**Payload Signals (0):**

**Generated File:** T2_BypassStage_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- BypassOperand
- BypassSelect
- BypassOperand

**Payload Signals (0):**

**Generated File:** T3_BypassStage_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- BypassOperand
- BypassOperand

**Payload Signals (0):**

**Generated File:** T4_BypassStage_Availability.sv

---

