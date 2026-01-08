# Trojan Generation Summary

**Module:** store_buffer
**File:** store_buffer.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- stall_st_pending_i
- valid_i
- valid_without_flush_i
- dcache_req_o_t
- no_st_pending_o
- ... and 4 more

**Payload Signals (9):**
- stall_st_pending_i
- valid_i
- valid_without_flush_i
- dcache_req_o_t
- no_st_pending_o
- ... and 4 more

**Generated File:** T1_store_buffer_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- data_size_i
- data
- data_size

**Payload Signals (5):**
- valid_without_flush_i
- data_size_i
- data
- store_buffer_empty_o
- data_size

**Generated File:** T2_store_buffer_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- valid_i
- valid_without_flush_i
- data_size_i
- dcache_req_o_t
- data
- ... and 3 more

**Payload Signals (6):**
- stall_st_pending_i
- valid_i
- valid_without_flush_i
- commit_ready_o
- ready_o
- ... and 1 more

**Generated File:** T3_store_buffer_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- data_size_i
- data
- data_size

**Generated File:** T4_store_buffer_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- data_size_i
- data
- data_size

**Payload Signals (0):**

**Generated File:** T5_store_buffer_Covert.sv

---

