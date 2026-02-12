# Trojan Generation Summary

**Module:** perf_counters
**File:** perf_counters.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- we_i
- icache_dreq_t
- dcache_req_i_t
- icache_dreq_t
- dcache_req_i_t

**Payload Signals (5):**
- we_i
- icache_dreq_t
- dcache_req_i_t
- icache_dreq_t
- dcache_req_i_t

**Generated File:** T1_perf_counters_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- debug_mode_i
- we_i

**Payload Signals (5):**
- addr_i
- data_i
- data_o
- data_o
- csr_addr_t

**Generated File:** T2_perf_counters_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- debug_mode_i
- addr_i
- we_i
- csr_addr_t

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_perf_counters_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- addr_i
- data_i
- data_o
- data_o
- csr_addr_t

**Payload Signals (3):**
- data_i
- data_o
- data_o

**Generated File:** T4_perf_counters_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- icache_dreq_t
- dcache_req_i_t
- icache_dreq_t
- dcache_req_i_t

**Payload Signals (4):**
- commit_ack_i
- stall_issue_i
- commit_ack_i
- stall_issue_i

**Generated File:** T5_perf_counters_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- data_i
- data_o
- l1_icache_access_i
- l1_dcache_access_i
- data_o
- ... and 2 more

**Payload Signals (3):**
- data_i
- data_o
- data_o

**Generated File:** T6_perf_counters_Covert.sv

---

