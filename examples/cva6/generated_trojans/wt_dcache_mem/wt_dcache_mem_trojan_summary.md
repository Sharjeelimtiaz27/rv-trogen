# Trojan Generation Summary

**Module:** wt_dcache_mem
**File:** wt_dcache_mem.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- rd_req_i
- wr_cl_we_i
- wr_req_i
- wr_cl_we_i
- wr_req_i
- ... and 5 more

**Payload Signals (10):**
- rd_req_i
- wr_cl_we_i
- wr_req_i
- wr_cl_we_i
- wr_req_i
- ... and 5 more

**Generated File:** T1_wt_dcache_mem_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- wr_cl_we_i
- wr_cl_we_i
- bank_we
- vld_we
- tag_write_duplicate_test

**Payload Signals (20):**
- rd_data_o
- wr_cl_data_i
- wr_cl_data_be_i
- wr_data_i
- wr_data_be_i
- ... and 15 more

**Generated File:** T2_wt_dcache_mem_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (19):**
- rd_data_o
- wr_cl_data_i
- wr_cl_data_be_i
- wr_data_i
- wr_data_be_i
- ... and 14 more

**Payload Signals (19):**
- rd_data_o
- wr_cl_data_i
- wr_cl_data_be_i
- wr_data_i
- wr_data_be_i
- ... and 14 more

**Generated File:** T3_wt_dcache_mem_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- rd_req_i
- wr_req_i
- wr_req_i
- bank_req
- vld_req
- ... and 1 more

**Payload Signals (4):**
- rd_ack_o
- wr_ack_o
- rd_ack_o
- wr_ack_o

**Generated File:** T4_wt_dcache_mem_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (17):**
- rd_data_o
- wr_cl_data_i
- wr_cl_data_be_i
- wr_data_i
- wr_data_be_i
- ... and 12 more

**Payload Signals (18):**
- rd_data_o
- wr_cl_data_i
- wr_cl_data_be_i
- wr_data_i
- wr_data_be_i
- ... and 13 more

**Generated File:** T5_wt_dcache_mem_Covert.sv

---

