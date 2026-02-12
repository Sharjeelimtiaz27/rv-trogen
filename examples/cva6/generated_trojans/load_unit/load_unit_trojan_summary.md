# Trojan Generation Summary

**Module:** load_unit
**File:** load_unit.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- valid_i
- valid_o
- translation_req_o
- dcache_req_o_t
- req_port_i
- ... and 10 more

**Payload Signals (15):**
- valid_i
- valid_o
- translation_req_o
- dcache_req_o_t
- req_port_i
- ... and 10 more

**Generated File:** T1_load_unit_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- pop_ld_o
- vaddr_o
- paddr_i
- pop_ld_o
- vaddr_o
- ... and 7 more

**Payload Signals (8):**
- result_o
- store_buffer_empty_i
- result_o
- store_buffer_empty_i
- req_port_i.data_rvalid
- ... and 3 more

**Generated File:** T2_load_unit_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (21):**
- valid_i
- lsu_ctrl_t
- lsu_ctrl_i
- pop_ld_o
- valid_o
- ... and 16 more

**Payload Signals (5):**
- valid_i
- valid_o
- valid_o
- req_port_i.data_rvalid
- stall_ni

**Generated File:** T3_load_unit_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- req_port_i.data_rvalid
- shifted_data
- rdata_sign_bits
- rdata_offset

**Payload Signals (9):**
- valid_i
- valid_o
- result_o
- valid_o
- result_o
- ... and 4 more

**Generated File:** T4_load_unit_Covert.sv

---

