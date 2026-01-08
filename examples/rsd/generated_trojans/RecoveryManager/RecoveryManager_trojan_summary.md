# Trojan Generation Summary

**Module:** RecoveryManager
**File:** RecoveryManager.sv
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
- refetchFromCSR

**Generated File:** T1_RecoveryManager_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- refetchFromCSR

**Payload Signals (0):**

**Generated File:** T2_RecoveryManager_Privilege.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- refetchFromCSR

**Payload Signals (0):**

**Generated File:** T3_RecoveryManager_Covert.sv

---

