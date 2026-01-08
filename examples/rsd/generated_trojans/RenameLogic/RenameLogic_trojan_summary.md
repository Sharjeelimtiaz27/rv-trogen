# Trojan Generation Summary

**Module:** RenameLogic
**File:** RenameLogic.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (6):**
- allocatePhyReg
- allocatePhyScalarReg
- releasePhyScalarReg
- allocatePhyScalarFPReg
- releasePhyScalarFPReg
- ... and 1 more

**Generated File:** T1_RenameLogic_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- watWriteReg

**Payload Signals (0):**

**Generated File:** T2_RenameLogic_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- watWriteReg

**Generated File:** T3_RenameLogic_Integrity.sv

---

