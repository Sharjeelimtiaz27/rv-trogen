# Trojan Generation Summary

**Module:** IntegerExecutionStage
**File:** IntegerExecutionStage.sv
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
- regValid

**Payload Signals (1):**
- regValid

**Generated File:** T1_IntegerExecutionStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- regValid

**Payload Signals (1):**
- regValid

**Generated File:** T2_IntegerExecutionStage_Availability.sv

---

