# Trojan Generation Summary

**Module:** cva6_hpdcache_subsystem
**File:** cva6_hpdcache_subsystem.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (42):**
- noc_req_t
- noc_req_o
- icache_en_i
- icache_areq_t
- icache_areq_i
- ... and 37 more

**Payload Signals (42):**
- noc_req_t
- noc_req_o
- icache_en_i
- icache_areq_t
- icache_areq_i
- ... and 37 more

**Generated File:** T1_cva6_hpdcache_subsystem_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (6):**
- dcache_write_ready
- dcache_write_valid
- dcache_write_data_ready
- dcache_write_data_valid
- dcache_write_resp_ready
- ... and 1 more

**Payload Signals (2):**
- dcache_write_data_ready
- dcache_write_data_valid

**Generated File:** T2_cva6_hpdcache_subsystem_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- dcache_write_ready
- dcache_write_valid
- dcache_write_data_ready
- dcache_write_data_valid
- dcache_write_resp_ready
- ... and 1 more

**Payload Signals (2):**
- hwpf_status_o
- hwpf_status_o

**Generated File:** T3_cva6_hpdcache_subsystem_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- dcache_write_data_ready
- dcache_write_data_valid

**Payload Signals (6):**
- dcache_write_ready
- dcache_write_valid
- dcache_write_data_ready
- dcache_write_data_valid
- dcache_write_resp_ready
- ... and 1 more

**Generated File:** T4_cva6_hpdcache_subsystem_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (38):**
- noc_req_t
- noc_req_o
- icache_areq_t
- icache_areq_i
- icache_areq_o
- ... and 33 more

**Payload Signals (8):**
- dcache_flush_ack_o
- dcache_flush_ack_o
- icache_miss_resp_valid
- dcache_read_valid
- dcache_read_resp_valid
- ... and 3 more

**Generated File:** T5_cva6_hpdcache_subsystem_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- dcache_write_data_ready
- dcache_write_data_valid

**Payload Signals (7):**
- icache_miss_resp_valid
- dcache_read_valid
- dcache_read_resp_valid
- dcache_write_valid
- dcache_write_data_ready
- ... and 2 more

**Generated File:** T6_cva6_hpdcache_subsystem_Covert.sv

---

