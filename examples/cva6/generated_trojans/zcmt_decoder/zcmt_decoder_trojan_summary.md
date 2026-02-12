# Trojan Generation Summary

**Module:** zcmt_decoder
**File:** zcmt_decoder.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- dcache_req_o_t
- req_port_i
- dcache_req_i_t
- req_port_o
- dcache_req_i_t
- ... and 1 more

**Payload Signals (6):**
- dcache_req_o_t
- req_port_i
- dcache_req_i_t
- req_port_o
- dcache_req_i_t
- ... and 1 more

**Generated File:** T1_zcmt_decoder_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- dcache_req_o_t
- req_port_i
- dcache_req_i_t
- req_port_o
- dcache_req_i_t
- ... and 1 more

**Payload Signals (2):**
- fetch_stall_o
- fetch_stall_o

**Generated File:** T2_zcmt_decoder_Availability.sv

---

