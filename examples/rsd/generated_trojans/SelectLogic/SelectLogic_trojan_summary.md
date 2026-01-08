# Trojan Generation Summary

**Module:** SelectLogic
**File:** SelectLogic.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (8):**
- intSelected
- compSelected
- memSelected
- loadSelected
- storeSelected
- ... and 3 more

**Payload Signals (1):**
- storeSelected

**Generated File:** T1_SelectLogic_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- loadSelected

**Payload Signals (0):**

**Generated File:** T2_SelectLogic_Covert.sv

---

