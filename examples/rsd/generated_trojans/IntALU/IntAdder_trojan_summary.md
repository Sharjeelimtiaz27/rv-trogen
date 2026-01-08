# Trojan Generation Summary

**Module:** IntAdder
**File:** IntALU.sv
**Type:** Combinational
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- DataPath
- DataPath
- DataPath

**Payload Signals (3):**
- DataPath
- DataPath
- DataPath

**Generated File:** T1_IntAdder_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- DataPath
- DataPath
- DataPath

**Payload Signals (6):**
- DataPath
- DataPath
- IntAdderResult
- DataPath
- overflowOut
- ... and 1 more

**Generated File:** T2_IntAdder_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- DataPath
- DataPath
- DataPath

**Payload Signals (0):**

**Generated File:** T3_IntAdder_Covert.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.40
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- DataPath
- DataPath
- DataPath

**Payload Signals (0):**

**Generated File:** T4_IntAdder_Availability.sv

---

