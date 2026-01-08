# Trojan Generation Summary

**Module:** BlockDualPortRAM
**File:** RAM_Vivado.sv
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

**Payload Signals (1):**
- addrwidth

**Generated File:** T1_BlockDualPortRAM_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (20):**
- we
- we
- we
- addrwidth
- we
- ... and 15 more

**Payload Signals (0):**

**Generated File:** T2_BlockDualPortRAM_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- addrwidth

**Payload Signals (0):**

**Generated File:** T3_BlockDualPortRAM_Integrity.sv

---

