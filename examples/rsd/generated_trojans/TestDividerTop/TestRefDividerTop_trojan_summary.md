# Trojan Generation Summary

**Module:** TestRefDividerTop
**File:** TestDividerTop.sv
**Type:** Sequential
**Total Candidates:** 2

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

**Generated File:** T1_TestRefDividerTop_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- req

**Payload Signals (0):**

**Generated File:** T2_TestRefDividerTop_Availability.sv

---

