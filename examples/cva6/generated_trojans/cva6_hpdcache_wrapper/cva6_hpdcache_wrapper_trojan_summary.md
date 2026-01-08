# Trojan Generation Summary

**Module:** cva6_hpdcache_wrapper
**File:** cva6_hpdcache_wrapper.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (23):**
- dcache_enable_i
- cmo_req_t
- request
- dcache_req_i_t
- dcache_mem_req_read_ready_i
- ... and 18 more

**Payload Signals (23):**
- dcache_enable_i
- cmo_req_t
- request
- dcache_req_i_t
- dcache_mem_req_read_ready_i
- ... and 18 more

**Generated File:** T1_cva6_hpdcache_wrapper_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o

**Payload Signals (6):**
- dcache_mem_req_write_ready_i
- dcache_mem_req_write_data_ready_i
- dcache_mem_resp_write_valid_i
- dcache_mem_req_write_valid_o
- dcache_mem_req_write_data_valid_o
- ... and 1 more

**Generated File:** T2_cva6_hpdcache_wrapper_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (20):**
- cmo_req_t
- request
- dcache_req_i_t
- dcache_mem_req_read_ready_i
- dcache_mem_resp_read_valid_i
- ... and 15 more

**Payload Signals (14):**
- dcache_mem_req_read_ready_i
- dcache_mem_resp_read_valid_i
- dcache_mem_req_write_ready_i
- dcache_mem_req_write_data_ready_i
- dcache_mem_resp_write_valid_i
- ... and 9 more

**Generated File:** T3_cva6_hpdcache_wrapper_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o

**Generated File:** T4_cva6_hpdcache_wrapper_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- dcache_mem_req_write_ready_i
- dcache_mem_req_write_data_ready_i
- dcache_mem_resp_write_valid_i
- dcache_mem_req_write_valid_o
- dcache_mem_req_write_data_valid_o
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T5_cva6_hpdcache_wrapper_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- dcache_mem_req_write_data_ready_i
- dcache_mem_req_write_data_valid_o
- dcache_cmo_req_is_prefetch

**Payload Signals (0):**

**Generated File:** T6_cva6_hpdcache_wrapper_Covert.sv

---

