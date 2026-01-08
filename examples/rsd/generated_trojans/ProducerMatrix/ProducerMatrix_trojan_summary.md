# Trojan Generation Summary

**Module:** ProducerMatrix
**File:** ProducerMatrix.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- dispatchedSrcRegReady
- opReady

**Payload Signals (2):**
- dispatchedSrcRegReady
- opReady

**Generated File:** T1_ProducerMatrix_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- opReady

**Payload Signals (2):**
- dispatchedSrcRegReady
- opReady

**Generated File:** T2_ProducerMatrix_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- dispatchedSrcRegReady

**Generated File:** T3_ProducerMatrix_Leak.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- opReady

**Payload Signals (0):**

**Generated File:** T4_ProducerMatrix_Integrity.sv

---

