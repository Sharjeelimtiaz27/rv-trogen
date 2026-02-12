# Trojan Generation Summary

**Module:** cva6_icache
**File:** cva6_icache.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (22):**
- en_i
- icache_areq_t
- areq_i
- areq_o
- icache_dreq_t
- ... and 17 more

**Payload Signals (22):**
- en_i
- icache_areq_t
- areq_i
- areq_o
- icache_dreq_t
- ... and 17 more

**Generated File:** T1_cva6_icache_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- cl_we
- vld_we
- tag_write_duplicate_test

**Payload Signals (14):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 9 more

**Generated File:** T2_cva6_icache_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 9 more

**Payload Signals (12):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 7 more

**Generated File:** T3_cva6_icache_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (19):**
- icache_areq_t
- areq_i
- areq_o
- icache_dreq_t
- dreq_i
- ... and 14 more

**Payload Signals (3):**
- mem_data_ack_i
- mem_data_ack_i
- all_ways_valid

**Generated File:** T4_cva6_icache_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 5 more

**Payload Signals (12):**
- mem_data_req_o
- mem_data_ack_i
- mem_data_o
- mem_data_req_o
- mem_data_ack_i
- ... and 7 more

**Generated File:** T5_cva6_icache_Covert.sv

---

