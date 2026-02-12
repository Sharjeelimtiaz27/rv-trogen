# Trojan Generation Summary

**Module:** wt_dcache_wbuffer
**File:** wt_dcache_wbuffer.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (18):**
- cache_en_i
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- ... and 13 more

**Payload Signals (18):**
- cache_en_i
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- ... and 13 more

**Generated File:** T1_wt_dcache_wbuffer_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- miss_we_o
- miss_we_o

**Payload Signals (17):**
- miss_paddr_o
- miss_wdata_o
- rd_data_i
- wr_data_o
- wr_data_be_o
- ... and 12 more

**Generated File:** T2_wt_dcache_wbuffer_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (16):**
- miss_paddr_o
- miss_wdata_o
- rd_data_i
- wr_data_o
- wr_data_be_o
- ... and 11 more

**Payload Signals (13):**
- miss_wdata_o
- rd_data_i
- wr_data_o
- wr_data_be_o
- wbuffer_data_o
- ... and 8 more

**Generated File:** T3_wt_dcache_wbuffer_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (15):**
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- miss_req_o
- ... and 10 more

**Payload Signals (7):**
- miss_ack_i
- rd_ack_i
- wr_ack_i
- miss_ack_i
- rd_ack_i
- ... and 2 more

**Generated File:** T4_wt_dcache_wbuffer_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- miss_wdata_o
- rd_data_i
- wr_data_o
- wr_data_be_o
- wbuffer_data_o
- ... and 7 more

**Payload Signals (14):**
- miss_wdata_o
- rd_data_i
- wr_data_o
- wr_data_be_o
- wbuffer_data_o
- ... and 9 more

**Generated File:** T5_wt_dcache_wbuffer_Covert.sv

---

