# Trojan Generation Summary

**Module:** cva6_hpdcache_wrapper
**File:** cva6_hpdcache_wrapper.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (51):**
- dcache_enable_i
- ariane_pkg::amo_req_t
- dcache_amo_req_i
- cmo_req_t
- dcache_cmo_req_i
- ... and 46 more

**Payload Signals (51):**
- dcache_enable_i
- ariane_pkg::amo_req_t
- dcache_amo_req_i
- cmo_req_t
- dcache_cmo_req_i
- ... and 46 more

**Generated File:** T1_cva6_hpdcache_wrapper_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (18):**
- dcache_mem_req_write_ready_i
- dcache_mem_req_write_valid_o
- dcache_mem_req_write_o
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- ... and 13 more

**Payload Signals (6):**
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- dcache_mem_req_write_data_o
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- ... and 1 more

**Generated File:** T2_cva6_hpdcache_wrapper_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (18):**
- dcache_mem_req_write_ready_i
- dcache_mem_req_write_valid_o
- dcache_mem_req_write_o
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- ... and 13 more

**Payload Signals (2):**
- hwpf_status_o
- hwpf_status_o

**Generated File:** T3_cva6_hpdcache_wrapper_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (9):**
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- dcache_mem_req_write_data_o
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- ... and 4 more

**Payload Signals (18):**
- dcache_mem_req_write_ready_i
- dcache_mem_req_write_valid_o
- dcache_mem_req_write_o
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- ... and 13 more

**Generated File:** T4_cva6_hpdcache_wrapper_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (48):**
- ariane_pkg::amo_req_t
- dcache_amo_req_i
- cmo_req_t
- dcache_cmo_req_i
- dcache_req_i_t
- ... and 43 more

**Payload Signals (23):**
- dcache_flush_ack_o
- dcache_mem_req_read_ready_i
- dcache_mem_req_read_valid_o
- dcache_mem_resp_read_ready_o
- dcache_mem_resp_read_valid_i
- ... and 18 more

**Generated File:** T5_cva6_hpdcache_wrapper_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- dcache_mem_req_write_data_o
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- ... and 1 more

**Payload Signals (23):**
- dcache_mem_req_read_ready_i
- dcache_mem_req_read_valid_o
- dcache_mem_resp_read_ready_o
- dcache_mem_resp_read_valid_i
- dcache_mem_req_write_ready_i
- ... and 18 more

**Generated File:** T6_cva6_hpdcache_wrapper_Covert.sv

---

