# Trojan Generation Summary

**Module:** alu_wrapper
**File:** alu_wrapper.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (1):**
- fu_data_t

**Generated File:** T1_alu_wrapper_Integrity.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- fu_data_t

**Generated File:** T2_alu_wrapper_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T3_alu_wrapper_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T4_alu_wrapper_Covert.sv

---

