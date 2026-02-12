# Trojan Generation Summary

**Module:** wt_dcache
**File:** wt_dcache.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (23):**
- enable_i
- amo_req_t
- amo_req_i
- dcache_req_i_t
- req_ports_i
- ... and 18 more

**Payload Signals (23):**
- enable_i
- amo_req_t
- amo_req_i
- dcache_req_i_t
- req_ports_i
- ... and 18 more

**Generated File:** T1_wt_dcache_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- wr_cl_we
- miss_we

**Payload Signals (15):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 10 more

**Generated File:** T2_wt_dcache_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 10 more

**Payload Signals (13):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 8 more

**Generated File:** T3_wt_dcache_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (20):**
- amo_req_t
- amo_req_i
- dcache_req_i_t
- req_ports_i
- dcache_req_o_t
- ... and 15 more

**Payload Signals (5):**
- flush_ack_o
- mem_data_ack_i
- flush_ack_o
- mem_data_ack_i
- valid

**Generated File:** T4_wt_dcache_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (13):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 8 more

**Payload Signals (14):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 9 more

**Generated File:** T5_wt_dcache_Covert.sv

---

