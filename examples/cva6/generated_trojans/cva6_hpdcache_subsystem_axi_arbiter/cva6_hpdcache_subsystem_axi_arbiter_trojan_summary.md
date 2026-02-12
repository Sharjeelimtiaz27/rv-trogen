# Trojan Generation Summary

**Module:** cva6_hpdcache_subsystem_axi_arbiter
**File:** cva6_hpdcache_subsystem_axi_arbiter.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (42):**
- icache_miss_valid_i
- icache_miss_ready_o
- icache_req_t
- icache_miss_resp_valid_o
- dcache_read_ready_o
- ... and 37 more

**Payload Signals (42):**
- icache_miss_valid_i
- icache_miss_ready_o
- icache_req_t
- icache_miss_resp_valid_o
- dcache_read_ready_o
- ... and 37 more

**Generated File:** T1_cva6_hpdcache_subsystem_axi_arbiter_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (18):**
- dcache_write_ready_o
- dcache_write_valid_i
- dcache_write_i
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- ... and 13 more

**Payload Signals (7):**
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- dcache_write_data_i
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- ... and 2 more

**Generated File:** T2_cva6_hpdcache_subsystem_axi_arbiter_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- dcache_write_data_i
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- ... and 2 more

**Payload Signals (19):**
- dcache_write_ready_o
- dcache_write_valid_i
- dcache_write_i
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- ... and 14 more

**Generated File:** T3_cva6_hpdcache_subsystem_axi_arbiter_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (30):**
- icache_miss_valid_i
- icache_req_t
- icache_miss_resp_valid_o
- dcache_read_valid_i
- hpdcache_mem_req_t
- ... and 25 more

**Payload Signals (28):**
- icache_miss_valid_i
- icache_miss_ready_o
- icache_miss_resp_valid_o
- dcache_read_ready_o
- dcache_read_valid_i
- ... and 23 more

**Generated File:** T4_cva6_hpdcache_subsystem_axi_arbiter_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- dcache_write_data_i
- dcache_write_data_ready_o
- dcache_write_data_valid_i
- ... and 2 more

**Payload Signals (31):**
- icache_miss_valid_i
- icache_miss_ready_o
- icache_miss_resp_valid_o
- dcache_read_ready_o
- dcache_read_valid_i
- ... and 26 more

**Generated File:** T5_cva6_hpdcache_subsystem_axi_arbiter_Covert.sv

---

