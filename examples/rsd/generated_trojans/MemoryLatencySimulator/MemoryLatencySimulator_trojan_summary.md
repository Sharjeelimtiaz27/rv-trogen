# Trojan Generation Summary

**Module:** MemoryLatencySimulator
**File:** MemoryLatencySimulator.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- hasRequest

**Payload Signals (1):**
- hasRequest

**Generated File:** T1_MemoryLatencySimulator_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- pop

**Payload Signals (0):**

**Generated File:** T2_MemoryLatencySimulator_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- hasRequest
- pop

**Payload Signals (0):**

**Generated File:** T3_MemoryLatencySimulator_Availability.sv

---

