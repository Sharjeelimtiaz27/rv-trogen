# Trojan Generation Summary

**Module:** RefDivider
**File:** RefDivider.sv
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
- req

**Payload Signals (1):**
- req

**Generated File:** T1_RefDivider_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- nextFinished

**Payload Signals (1):**
- regSigned

**Generated File:** T2_RefDivider_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- req

**Payload Signals (0):**

**Generated File:** T3_RefDivider_Availability.sv

---

