# Trojan Generation Summary

**Module:** axi_shim
**File:** axi_shim.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- rd_req_i
- rd_blen_i
- rd_valid_o
- wr_req_i
- wr_blen_i
- ... and 10 more

**Payload Signals (15):**
- rd_req_i
- rd_blen_i
- rd_valid_o
- wr_req_i
- wr_blen_i
- ... and 10 more

**Generated File:** T1_axi_shim_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- rd_addr_i
- rd_data_o
- wr_addr_i
- wr_data_i
- wr_atop_i
- ... and 5 more

**Payload Signals (4):**
- rd_data_o
- wr_data_i
- rd_data_o
- wr_data_i

**Generated File:** T2_axi_shim_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (13):**
- rd_req_i
- rd_valid_o
- wr_req_i
- wr_atop_i
- wr_valid_o
- ... and 8 more

**Payload Signals (8):**
- rd_gnt_o
- rd_valid_o
- wr_gnt_o
- wr_valid_o
- rd_gnt_o
- ... and 3 more

**Generated File:** T3_axi_shim_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- rd_data_o
- wr_data_i
- rd_data_o
- wr_data_i

**Payload Signals (8):**
- rd_valid_o
- rd_data_o
- wr_data_i
- wr_valid_o
- rd_valid_o
- ... and 3 more

**Generated File:** T4_axi_shim_Covert.sv

---

