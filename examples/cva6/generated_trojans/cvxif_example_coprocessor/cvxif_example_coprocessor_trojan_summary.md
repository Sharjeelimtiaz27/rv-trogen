# Trojan Generation Summary

**Module:** cvxif_example_coprocessor
**File:** cvxif_example_coprocessor.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- cvxif_req_t
- cvxif_req_i
- register_valid
- we
- alu_valid

**Payload Signals (5):**
- cvxif_req_t
- cvxif_req_i
- register_valid
- we
- alu_valid

**Generated File:** T1_cvxif_example_coprocessor_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- we

**Payload Signals (1):**
- result

**Generated File:** T2_cvxif_example_coprocessor_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- cvxif_req_t
- cvxif_req_i
- register_valid
- alu_valid

**Payload Signals (2):**
- register_valid
- alu_valid

**Generated File:** T3_cvxif_example_coprocessor_Availability.sv

---

