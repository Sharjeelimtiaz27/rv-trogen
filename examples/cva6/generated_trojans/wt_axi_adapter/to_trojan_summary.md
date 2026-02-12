# Trojan Generation Summary

**Module:** to
**File:** wt_axi_adapter.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (16):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- axi_req_t
- ... and 11 more

**Payload Signals (16):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- axi_req_t
- ... and 11 more

**Generated File:** T1_to_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (16):**
- icache_data_req_i
- icache_data_ack_o
- icache_data_i
- dcache_data_req_i
- dcache_data_ack_o
- ... and 11 more

**Payload Signals (13):**
- icache_data_req_i
- icache_data_ack_o
- icache_data_i
- dcache_data_req_i
- dcache_data_ack_o
- ... and 8 more

**Generated File:** T2_to_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (15):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- axi_req_t
- ... and 10 more

**Payload Signals (9):**
- icache_data_ack_o
- dcache_data_ack_o
- inval_valid_i
- inval_ready_o
- icache_data_ack_o
- ... and 4 more

**Generated File:** T3_to_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (13):**
- icache_data_req_i
- icache_data_ack_o
- icache_data_i
- dcache_data_req_i
- dcache_data_ack_o
- ... and 8 more

**Payload Signals (18):**
- icache_data_req_i
- icache_data_ack_o
- icache_data_i
- dcache_data_req_i
- dcache_data_ack_o
- ... and 13 more

**Generated File:** T4_to_Covert.sv

---

