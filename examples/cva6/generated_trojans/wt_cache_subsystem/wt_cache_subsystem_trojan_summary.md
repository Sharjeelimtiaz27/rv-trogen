# Trojan Generation Summary

**Module:** wt_cache_subsystem
**File:** wt_cache_subsystem.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (35):**
- icache_en_i
- icache_areq_t
- icache_areq_i
- icache_areq_o
- icache_dreq_t
- ... and 30 more

**Payload Signals (35):**
- icache_en_i
- icache_areq_t
- icache_areq_i
- icache_areq_o
- icache_dreq_t
- ... and 30 more

**Generated File:** T1_wt_cache_subsystem_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- inval_addr_i
- inval_addr_i
- paddr
- data

**Payload Signals (1):**
- data

**Generated File:** T2_wt_cache_subsystem_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (30):**
- icache_areq_t
- icache_areq_i
- icache_areq_o
- icache_dreq_t
- icache_dreq_i
- ... and 25 more

**Payload Signals (6):**
- dcache_flush_ack_o
- inval_valid_i
- inval_ready_o
- dcache_flush_ack_o
- inval_valid_i
- ... and 1 more

**Generated File:** T3_wt_cache_subsystem_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data

**Payload Signals (5):**
- inval_valid_i
- inval_ready_o
- inval_valid_i
- inval_ready_o
- data

**Generated File:** T4_wt_cache_subsystem_Covert.sv

---

