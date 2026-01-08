# Trojan Generation Summary

**Module:** MultiplierUnit
**File:** MultiplierUnit.sv
**Type:** Sequential
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

**Generated File:** T1_MultiplierUnit_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- DataPath
- DataPath
- DataPath
- fuOpA_sign
- fuOpB_sign

**Payload Signals (3):**
- DataPath
- DataPath
- DataPath

**Generated File:** T2_MultiplierUnit_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- DataPath
- DataPath
- DataPath
- fuOpA_sign
- fuOpB_sign

**Payload Signals (0):**

**Generated File:** T3_MultiplierUnit_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- DataPath
- DataPath
- DataPath

**Payload Signals (0):**

**Generated File:** T4_MultiplierUnit_Covert.sv

---

