# Trojan Generation Summary

**Module:** amo_buffer
**File:** amo_buffer.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- valid_i
- ready_o
- ariane_pkg::amo_req_t
- amo_req_o
- amo_valid_commit_i
- ... and 5 more

**Payload Signals (10):**
- valid_i
- ready_o
- ariane_pkg::amo_req_t
- amo_req_o
- amo_valid_commit_i
- ... and 5 more

**Generated File:** T1_amo_buffer_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- amo_op_i
- paddr_i
- data_i
- data_size_i
- amo_op_i
- ... and 5 more

**Payload Signals (5):**
- data_i
- data_size_i
- data_i
- data_size_i
- data

**Generated File:** T2_amo_buffer_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- valid_i
- amo_op_i
- ariane_pkg::amo_req_t
- amo_req_o
- amo_valid_commit_i
- ... and 5 more

**Payload Signals (6):**
- valid_i
- ready_o
- amo_valid_commit_i
- ready_o
- amo_valid_commit_i
- ... and 1 more

**Generated File:** T3_amo_buffer_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- data_i
- data_size_i
- data_i
- data_size_i
- data

**Payload Signals (11):**
- valid_i
- ready_o
- data_i
- data_size_i
- amo_valid_commit_i
- ... and 6 more

**Generated File:** T4_amo_buffer_Covert.sv

---

