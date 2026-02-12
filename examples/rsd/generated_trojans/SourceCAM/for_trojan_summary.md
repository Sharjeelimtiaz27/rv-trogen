# Trojan Generation Summary

**Module:** for
**File:** SourceCAM.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- wakeupDstValid

**Payload Signals (1):**
- wakeupDstValid

**Generated File:** T1_for_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- SRC_OP_NUM
- SRC_OP_NUM
- wakeupDstValid
- opReady
- opReady

**Payload Signals (1):**
- wakeupDstValid

**Generated File:** T2_for_Availability.sv

---

