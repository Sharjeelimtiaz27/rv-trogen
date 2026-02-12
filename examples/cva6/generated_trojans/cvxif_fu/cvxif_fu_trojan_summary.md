# Trojan Generation Summary

**Module:** cvxif_fu
**File:** cvxif_fu.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (11):**
- x_valid_i
- x_ready_o
- x_valid_o
- x_we_o
- result_valid_i
- ... and 6 more

**Payload Signals (11):**
- x_valid_i
- x_ready_o
- x_valid_o
- x_we_o
- result_valid_i
- ... and 6 more

**Generated File:** T1_cvxif_fu_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- x_we_o
- x_we_o

**Payload Signals (10):**
- x_result_o
- result_valid_i
- x_result_t
- result_i
- result_ready_o
- ... and 5 more

**Generated File:** T2_cvxif_fu_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- x_valid_i
- x_valid_o
- result_valid_i
- x_valid_o
- result_valid_i

**Payload Signals (9):**
- x_valid_i
- x_ready_o
- x_valid_o
- result_valid_i
- result_ready_o
- ... and 4 more

**Generated File:** T3_cvxif_fu_Availability.sv

---

