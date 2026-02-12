# Trojan Generation Summary

**Module:** lsu_bypass
**File:** lsu_bypass.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- lsu_req_i
- lsu_req_valid_i
- ready_o
- ready_o

**Payload Signals (4):**
- lsu_req_i
- lsu_req_valid_i
- ready_o
- ready_o

**Generated File:** T1_lsu_bypass_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- pop_ld_i
- pop_st_i

**Payload Signals (1):**
- write_pointer

**Generated File:** T2_lsu_bypass_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- lsu_ctrl_t
- lsu_req_i
- lsu_req_valid_i
- pop_ld_i
- pop_st_i
- ... and 4 more

**Payload Signals (3):**
- lsu_req_valid_i
- ready_o
- ready_o

**Generated File:** T3_lsu_bypass_Availability.sv

---

