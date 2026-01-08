# Trojan Generation Summary

**Module:** FP32DivSqrter
**File:** FP32DivSqrter.sv
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
- req
- dividend_normalize

**Payload Signals (2):**
- req
- dividend_normalize

**Generated File:** T1_FP32DivSqrter_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- regCounter
- regResult

**Generated File:** T2_FP32DivSqrter_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (4):**
- result
- regResult
- result_sign
- result_expo

**Generated File:** T3_FP32DivSqrter_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- req

**Payload Signals (0):**

**Generated File:** T4_FP32DivSqrter_Availability.sv

---

