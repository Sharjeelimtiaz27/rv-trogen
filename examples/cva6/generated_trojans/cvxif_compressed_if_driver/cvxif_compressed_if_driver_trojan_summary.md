# Trojan Generation Summary

**Module:** cvxif_compressed_if_driver
**File:** cvxif_compressed_if_driver.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- compressed_ready_i
- compressed_valid_o
- x_compressed_req_t

**Payload Signals (3):**
- compressed_ready_i
- compressed_valid_o
- x_compressed_req_t

**Generated File:** T1_cvxif_compressed_if_driver_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- compressed_valid_o
- x_compressed_req_t

**Payload Signals (4):**
- stall_i
- compressed_ready_i
- stall_o
- compressed_valid_o

**Generated File:** T2_cvxif_compressed_if_driver_Availability.sv

---

