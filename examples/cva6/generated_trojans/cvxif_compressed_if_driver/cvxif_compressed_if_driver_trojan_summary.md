# Trojan Generation Summary

**Module:** cvxif_compressed_if_driver
**File:** cvxif_compressed_if_driver.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- compressed_ready_i
- compressed_valid_o
- x_compressed_req_t
- compressed_req_o
- compressed_ready_i
- ... and 3 more

**Payload Signals (8):**
- compressed_ready_i
- compressed_valid_o
- x_compressed_req_t
- compressed_req_o
- compressed_ready_i
- ... and 3 more

**Generated File:** T1_cvxif_compressed_if_driver_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- compressed_valid_o
- x_compressed_req_t
- compressed_req_o
- compressed_valid_o
- x_compressed_req_t
- ... and 1 more

**Payload Signals (8):**
- stall_i
- stall_o
- compressed_ready_i
- compressed_valid_o
- stall_i
- ... and 3 more

**Generated File:** T2_cvxif_compressed_if_driver_Availability.sv

---

