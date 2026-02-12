# Trojan Generation Summary

**Module:** std_cache_subsystem
**File:** std_cache_subsystem.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (31):**
- icache_en_i
- icache_areq_t
- icache_areq_i
- icache_areq_o
- icache_dreq_t
- ... and 26 more

**Payload Signals (31):**
- icache_en_i
- icache_areq_t
- icache_areq_i
- icache_areq_o
- icache_dreq_t
- ... and 26 more

**Generated File:** T1_std_cache_subsystem_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (28):**
- icache_areq_t
- icache_areq_i
- icache_areq_o
- icache_dreq_t
- icache_dreq_i
- ... and 23 more

**Payload Signals (2):**
- dcache_flush_ack_o
- dcache_flush_ack_o

**Generated File:** T2_std_cache_subsystem_Availability.sv

---

