# Trojan Generation Summary

**Module:** store_unit
**File:** store_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (16):**
- stall_st_pending_i
- valid_i
- amo_valid_commit_i
- dcache_req_o_t
- no_st_pending_o
- ... and 11 more

**Payload Signals (16):**
- stall_st_pending_i
- valid_i
- amo_valid_commit_i
- dcache_req_o_t
- no_st_pending_o
- ... and 11 more

**Generated File:** T1_store_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- lsu_ctrl_t

**Payload Signals (4):**
- addr
- data
- data_tmp
- st_data_size_n

**Generated File:** T2_store_unit_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- pop_st_o
- addr
- data
- data_tmp
- st_data_size_n

**Payload Signals (7):**
- store_buffer_empty_o
- data
- data_tmp
- st_valid_without_flush
- st_data_size_n
- ... and 2 more

**Generated File:** T3_store_unit_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (14):**
- valid_i
- amo_valid_commit_i
- dcache_req_o_t
- pop_st_o
- valid_o
- ... and 9 more

**Payload Signals (10):**
- stall_st_pending_i
- valid_i
- amo_valid_commit_i
- commit_ready_o
- valid_o
- ... and 5 more

**Generated File:** T4_store_unit_Availability.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- lsu_ctrl_t
- addr

**Payload Signals (0):**

**Generated File:** T5_store_unit_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- data
- data_tmp
- st_data_size_n

**Payload Signals (0):**

**Generated File:** T6_store_unit_Covert.sv

---

