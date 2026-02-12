# Trojan Generation Summary

**Module:** wt_dcache_missunit
**File:** wt_dcache_missunit.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (17):**
- enable_i
- cache_en_o
- amo_req_t
- amo_req_i
- miss_req_i
- ... and 12 more

**Payload Signals (17):**
- enable_i
- cache_en_o
- amo_req_t
- amo_req_i
- miss_req_i
- ... and 12 more

**Generated File:** T1_wt_dcache_missunit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- miss_we_i
- wr_cl_we_o
- miss_we_i
- wr_cl_we_o

**Payload Signals (19):**
- miss_wdata_i
- miss_paddr_i
- tx_paddr_i
- wr_cl_data_o
- wr_cl_data_be_o
- ... and 14 more

**Generated File:** T2_wt_dcache_missunit_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (18):**
- miss_wdata_i
- miss_paddr_i
- tx_paddr_i
- wr_cl_data_o
- wr_cl_data_be_o
- ... and 13 more

**Payload Signals (13):**
- miss_wdata_i
- wr_cl_data_o
- wr_cl_data_be_o
- mem_data_req_o
- mem_data_ack_i
- ... and 8 more

**Generated File:** T3_wt_dcache_missunit_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- amo_req_t
- amo_req_i
- miss_req_i
- mem_data_req_o
- dcache_req_t
- ... and 5 more

**Payload Signals (6):**
- flush_ack_o
- miss_ack_o
- mem_data_ack_i
- flush_ack_o
- miss_ack_o
- ... and 1 more

**Generated File:** T4_wt_dcache_missunit_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- miss_wdata_i
- wr_cl_data_o
- wr_cl_data_be_o
- mem_data_req_o
- mem_data_ack_i
- ... and 7 more

**Payload Signals (13):**
- miss_wdata_i
- wr_cl_data_o
- wr_cl_data_be_o
- mem_data_req_o
- mem_data_ack_i
- ... and 8 more

**Generated File:** T5_wt_dcache_missunit_Covert.sv

---

