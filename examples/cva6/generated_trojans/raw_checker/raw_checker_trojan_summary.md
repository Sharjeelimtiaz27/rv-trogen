# Trojan Generation Summary

**Module:** raw_checker
**File:** raw_checker.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- valid_o
- valid_o

**Payload Signals (2):**
- valid_o
- valid_o

**Generated File:** T1_raw_checker_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid_o
- valid_o

**Payload Signals (2):**
- valid_o
- valid_o

**Generated File:** T2_raw_checker_Availability.sv

---

