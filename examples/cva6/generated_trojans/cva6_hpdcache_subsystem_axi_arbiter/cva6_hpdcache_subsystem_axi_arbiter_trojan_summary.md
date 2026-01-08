# Trojan Generation Summary

**Module:** cva6_hpdcache_subsystem_axi_arbiter
**File:** cva6_hpdcache_subsystem_axi_arbiter.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (29):**
- icache_miss_valid_i
- icache_req_t
- dcache_read_valid_i
- hpdcache_mem_req_t
- dcache_read_resp_ready_i
- ... and 24 more

**Payload Signals (29):**
- icache_miss_valid_i
- icache_req_t
- dcache_read_valid_i
- hpdcache_mem_req_t
- dcache_read_resp_ready_i
- ... and 24 more

**Generated File:** T1_cva6_hpdcache_subsystem_axi_arbiter_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- dcache_write_data_valid_i
- dcache_write_data_ready_o
- icache_miss_resp_data_w
- icache_miss_resp_data_r

**Payload Signals (8):**
- dcache_write_valid_i
- dcache_write_data_valid_i
- dcache_write_resp_ready_i
- dcache_write_ready_o
- dcache_write_data_ready_o
- ... and 3 more

**Generated File:** T2_cva6_hpdcache_subsystem_axi_arbiter_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (23):**
- icache_miss_valid_i
- icache_req_t
- dcache_read_valid_i
- hpdcache_mem_req_t
- dcache_write_valid_i
- ... and 18 more

**Payload Signals (21):**
- icache_miss_valid_i
- dcache_read_valid_i
- dcache_read_resp_ready_i
- dcache_write_valid_i
- dcache_write_data_valid_i
- ... and 16 more

**Generated File:** T3_cva6_hpdcache_subsystem_axi_arbiter_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- dcache_write_data_valid_i
- dcache_write_data_ready_o
- icache_miss_resp_data_w
- icache_miss_resp_data_r

**Generated File:** T4_cva6_hpdcache_subsystem_axi_arbiter_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- dcache_write_valid_i
- dcache_write_data_valid_i
- dcache_write_resp_ready_i
- dcache_write_ready_o
- dcache_write_data_ready_o
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T5_cva6_hpdcache_subsystem_axi_arbiter_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- dcache_write_data_valid_i
- dcache_write_data_ready_o
- icache_miss_resp_data_w
- icache_miss_resp_data_r

**Payload Signals (0):**

**Generated File:** T6_cva6_hpdcache_subsystem_axi_arbiter_Covert.sv

---

