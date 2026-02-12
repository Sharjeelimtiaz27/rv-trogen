# Trojan Generation Summary

**Module:** cache_ctrl
**File:** cache_ctrl.sv
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
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- req_o
- ... and 18 more

**Payload Signals (23):**
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- req_o
- ... and 18 more

**Generated File:** T1_cache_ctrl_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- we_o
- we_o
- we

**Payload Signals (13):**
- addr_o
- data_o
- data_i
- bypass_data_i
- mshr_addr_o
- ... and 8 more

**Generated File:** T2_cache_ctrl_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (13):**
- addr_o
- data_o
- data_i
- bypass_data_i
- mshr_addr_o
- ... and 8 more

**Payload Signals (7):**
- data_o
- data_i
- bypass_data_i
- data_o
- data_i
- ... and 2 more

**Generated File:** T3_cache_ctrl_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (18):**
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- req_o
- ... and 13 more

**Payload Signals (12):**
- busy_o
- gnt_i
- miss_gnt_i
- critical_word_valid_i
- bypass_gnt_i
- ... and 7 more

**Generated File:** T4_cache_ctrl_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- data_o
- data_i
- bypass_data_i
- data_o
- data_i
- ... and 2 more

**Payload Signals (13):**
- busy_o
- data_o
- data_i
- critical_word_valid_i
- bypass_valid_i
- ... and 8 more

**Generated File:** T5_cache_ctrl_Covert.sv

---

