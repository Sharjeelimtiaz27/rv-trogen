# Trojan Generation Summary

**Module:** BypassCtrlStage
**File:** BypassController.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- PipelineControll
- BypassCtrlOperand
- BypassCtrlOperand

**Payload Signals (2):**
- PRegNumPath
- writeReg

**Generated File:** T1_BypassCtrlStage_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- BypassCtrlOperand
- BypassCtrlOperand

**Payload Signals (1):**
- writeReg

**Generated File:** T2_BypassCtrlStage_Integrity.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- PipelineControll
- BypassCtrlOperand
- BypassCtrlOperand
- writeReg

**Payload Signals (0):**

**Generated File:** T3_BypassCtrlStage_Privilege.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- BypassCtrlOperand
- BypassCtrlOperand

**Payload Signals (0):**

**Generated File:** T4_BypassCtrlStage_Availability.sv

---

