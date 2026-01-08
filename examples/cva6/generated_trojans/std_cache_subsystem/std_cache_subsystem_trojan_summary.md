# Trojan Generation Summary

**Module:** std_cache_subsystem
**File:** std_cache_subsystem.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- icache_en_i
- icache_areq_t
- icache_dreq_t
- amo_req_t
- dcache_enable_i
- ... and 3 more

**Payload Signals (8):**
- icache_en_i
- icache_areq_t
- icache_dreq_t
- amo_req_t
- dcache_enable_i
- ... and 3 more

**Generated File:** T1_std_cache_subsystem_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- icache_areq_t
- icache_dreq_t
- amo_req_t
- dcache_req_i_t
- dcache_req_o_t
- ... and 1 more

**Payload Signals (1):**
- dcache_flush_ack_o

**Generated File:** T2_std_cache_subsystem_Availability.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- w_select
- r_select
- b_select

**Payload Signals (0):**

**Generated File:** T3_std_cache_subsystem_Integrity.sv

---

