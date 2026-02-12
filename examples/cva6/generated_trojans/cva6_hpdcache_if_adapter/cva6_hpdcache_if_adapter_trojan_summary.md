# Trojan Generation Summary

**Module:** cva6_hpdcache_if_adapter
**File:** cva6_hpdcache_if_adapter.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (29):**
- hpdcache_req_sid_t
- hpdcache_req_sid_i
- dcache_req_i_t
- cva6_req_i
- dcache_req_o_t
- ... and 24 more

**Payload Signals (29):**
- hpdcache_req_sid_t
- hpdcache_req_sid_i
- dcache_req_i_t
- cva6_req_i
- dcache_req_o_t
- ... and 24 more

**Generated File:** T1_cva6_hpdcache_if_adapter_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- amo_addr
- amo_data
- amo_data_be

**Payload Signals (2):**
- amo_data
- amo_data_be

**Generated File:** T2_cva6_hpdcache_if_adapter_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (29):**
- hpdcache_req_sid_t
- hpdcache_req_sid_i
- dcache_req_i_t
- cva6_req_i
- dcache_req_o_t
- ... and 24 more

**Payload Signals (8):**
- cva6_dcache_flush_ack_o
- hpdcache_req_valid_o
- hpdcache_req_ready_i
- hpdcache_rsp_valid_i
- cva6_dcache_flush_ack_o
- ... and 3 more

**Generated File:** T3_cva6_hpdcache_if_adapter_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- amo_data
- amo_data_be

**Payload Signals (8):**
- hpdcache_req_valid_o
- hpdcache_req_ready_i
- hpdcache_rsp_valid_i
- hpdcache_req_valid_o
- hpdcache_req_ready_i
- ... and 3 more

**Generated File:** T4_cva6_hpdcache_if_adapter_Covert.sv

---

