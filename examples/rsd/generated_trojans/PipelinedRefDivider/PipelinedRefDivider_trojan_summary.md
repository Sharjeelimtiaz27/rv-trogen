# Trojan Generation Summary

**Module:** PipelinedRefDivider
**File:** PipelinedRefDivider.sv
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

**Generated File:** T1_PipelinedRefDivider_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- req

**Payload Signals (1):**
- stall

**Generated File:** T2_PipelinedRefDivider_Availability.sv

---

