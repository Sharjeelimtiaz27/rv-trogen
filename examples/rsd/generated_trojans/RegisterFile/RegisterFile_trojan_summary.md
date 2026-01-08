# Trojan Generation Summary

**Module:** RegisterFile
**File:** RegisterFile.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- regWE
- fpRegWE
- PRegNumPath

**Generated File:** T1_RegisterFile_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- regWE
- fpRegWE

**Payload Signals (0):**

**Generated File:** T2_RegisterFile_Privilege.sv

---

