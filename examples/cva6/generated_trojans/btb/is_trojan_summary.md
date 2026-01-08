# Trojan Generation Summary

**Module:** is
**File:** btb.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T1_is_Privilege.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (0):**

**Generated File:** T2_is_Leak.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_is_Covert.sv

---

