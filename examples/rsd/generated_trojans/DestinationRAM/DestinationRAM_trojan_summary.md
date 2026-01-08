# Trojan Generation Summary

**Module:** DestinationRAM
**File:** DestinationRAM.sv
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
- write

**Payload Signals (0):**

**Generated File:** T1_DestinationRAM_Privilege.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- write

**Generated File:** T2_DestinationRAM_Integrity.sv

---

