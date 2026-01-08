# Trojan Generation Summary

**Module:** axi_shim
**File:** axi_shim.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- rd_req_i
- wr_req_i
- rd_valid_o
- wr_valid_o
- axi_req_t
- ... and 1 more

**Payload Signals (6):**
- rd_req_i
- wr_req_i
- rd_valid_o
- wr_valid_o
- axi_req_t
- ... and 1 more

**Generated File:** T1_axi_shim_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- rd_req_i
- wr_req_i
- wr_atop_i
- rd_valid_o
- wr_valid_o
- ... and 2 more

**Payload Signals (2):**
- rd_valid_o
- wr_valid_o

**Generated File:** T2_axi_shim_Availability.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- wr_atop_i

**Payload Signals (0):**

**Generated File:** T3_axi_shim_Integrity.sv

---

