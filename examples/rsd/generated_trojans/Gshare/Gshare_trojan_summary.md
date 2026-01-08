# Trojan Generation Summary

**Module:** Gshare
**File:** Gshare.sv
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
- phtWE

**Payload Signals (0):**

**Generated File:** T1_Gshare_Privilege.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (0):**

**Payload Signals (1):**
- stall

**Generated File:** T2_Gshare_Availability.sv

---

