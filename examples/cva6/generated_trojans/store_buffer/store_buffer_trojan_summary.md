# Trojan Generation Summary

**Module:** store_buffer
**File:** store_buffer.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (17):**
- commit_ready_o
- ready_o
- valid_i
- valid_without_flush_i
- dcache_req_o_t
- ... and 12 more

**Payload Signals (17):**
- commit_ready_o
- ready_o
- valid_i
- valid_without_flush_i
- dcache_req_o_t
- ... and 12 more

**Generated File:** T1_store_buffer_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- paddr_i
- rvfi_mem_paddr_o
- data_i
- data_size_i
- paddr_i
- ... and 6 more

**Payload Signals (10):**
- store_buffer_empty_o
- valid_without_flush_i
- data_i
- data_size_i
- store_buffer_empty_o
- ... and 5 more

**Generated File:** T2_store_buffer_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (15):**
- store_buffer_empty_o
- valid_i
- valid_without_flush_i
- dcache_req_o_t
- req_port_i
- ... and 10 more

**Payload Signals (10):**
- stall_st_pending_i
- commit_ready_o
- ready_o
- valid_i
- valid_without_flush_i
- ... and 5 more

**Generated File:** T3_store_buffer_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- data_i
- data_size_i
- data_i
- data_size_i
- data
- ... and 1 more

**Payload Signals (15):**
- commit_ready_o
- ready_o
- valid_i
- valid_without_flush_i
- data_i
- ... and 10 more

**Generated File:** T4_store_buffer_Covert.sv

---

