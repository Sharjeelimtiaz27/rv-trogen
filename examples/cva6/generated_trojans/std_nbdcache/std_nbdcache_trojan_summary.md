# Trojan Generation Summary

**Module:** std_nbdcache
**File:** std_nbdcache.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (25):**
- enable_i
- amo_req_t
- amo_req_i
- dcache_req_i_t
- req_ports_i
- ... and 20 more

**Payload Signals (25):**
- enable_i
- amo_req_t
- amo_req_i
- dcache_req_i_t
- req_ports_i
- ... and 20 more

**Generated File:** T1_std_nbdcache_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- we
- we_ram

**Payload Signals (10):**
- axi_data_o
- axi_data_i
- axi_data_o
- axi_data_i
- data
- ... and 5 more

**Generated File:** T2_std_nbdcache_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- axi_data_o
- axi_data_i
- axi_data_o
- axi_data_i
- data
- ... and 5 more

**Payload Signals (6):**
- axi_data_o
- axi_data_i
- axi_data_o
- axi_data_i
- data
- ... and 1 more

**Generated File:** T3_std_nbdcache_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (22):**
- amo_req_t
- amo_req_i
- dcache_req_i_t
- req_ports_i
- dcache_req_o_t
- ... and 17 more

**Payload Signals (5):**
- flush_ack_o
- flush_ack_o
- valid
- critical_word_valid
- bypass_valid

**Generated File:** T4_std_nbdcache_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- axi_data_o
- axi_data_i
- axi_data_o
- axi_data_i
- data
- ... and 1 more

**Payload Signals (9):**
- axi_data_o
- axi_data_i
- axi_data_o
- axi_data_i
- data
- ... and 4 more

**Generated File:** T5_std_nbdcache_Covert.sv

---

