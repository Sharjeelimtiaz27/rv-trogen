# Trojan Generation Summary

**Module:** ScheduleStage
**File:** ScheduleStage.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- valid

**Payload Signals (1):**
- valid

**Generated File:** T1_ScheduleStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 0.80
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- valid

**Payload Signals (1):**
- valid

**Generated File:** T2_ScheduleStage_Availability.sv

---

