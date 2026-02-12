# Trojan Generation Summary

**Module:** store_unit
**File:** store_unit.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (24):**
- valid_i
- commit_ready_o
- amo_valid_commit_i
- valid_o
- translation_req_o
- ... and 19 more

**Payload Signals (24):**
- valid_i
- commit_ready_o
- amo_valid_commit_i
- valid_o
- translation_req_o
- ... and 19 more

**Generated File:** T1_store_unit_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (9):**
- pop_st_o
- vaddr_o
- rvfi_mem_paddr_o
- paddr_i
- pop_st_o
- ... and 4 more

**Payload Signals (6):**
- store_buffer_empty_o
- result_o
- store_buffer_empty_o
- result_o
- data_tmp
- ... and 1 more

**Generated File:** T2_store_unit_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (30):**
- store_buffer_empty_o
- valid_i
- lsu_ctrl_t
- lsu_ctrl_i
- pop_st_o
- ... and 25 more

**Payload Signals (11):**
- stall_st_pending_i
- valid_i
- commit_ready_o
- amo_valid_commit_i
- valid_o
- ... and 6 more

**Generated File:** T3_store_unit_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data_tmp

**Payload Signals (13):**
- valid_i
- commit_ready_o
- amo_valid_commit_i
- valid_o
- result_o
- ... and 8 more

**Generated File:** T4_store_unit_Covert.sv

---

