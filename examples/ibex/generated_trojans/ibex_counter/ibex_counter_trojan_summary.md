# Trojan Generation Summary

**Module:** ibex_counter
**File:** ibex_counter.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- counterh_we_i
- counter_we_i
- we

**Payload Signals (0):**

**Generated File:** T1_ibex_counter_Privilege.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- counter_load

**Payload Signals (0):**

**Generated File:** T2_ibex_counter_Covert.sv

---

