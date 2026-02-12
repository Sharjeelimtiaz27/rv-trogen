# Trojan Generation Summary

**Module:** bht2lvl
**File:** bht2lvl.sv
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
- valid

**Payload Signals (1):**
- valid

**Generated File:** T1_bht2lvl_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- valid

**Payload Signals (1):**
- valid

**Generated File:** T2_bht2lvl_Availability.sv

---

