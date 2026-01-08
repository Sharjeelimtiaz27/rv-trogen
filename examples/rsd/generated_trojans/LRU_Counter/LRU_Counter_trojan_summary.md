# Trojan Generation Summary

**Module:** LRU_Counter
**File:** LRU_Counter.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- we

**Payload Signals (0):**

**Generated File:** T1_LRU_Counter_Privilege.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- access

**Payload Signals (0):**

**Generated File:** T2_LRU_Counter_Covert.sv

---

