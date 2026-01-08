# Trojan Generation Summary

**Module:** cva6_hpdcache_subsystem
**File:** cva6_hpdcache_subsystem.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (22):**
- icache_en_i
- icache_areq_t
- icache_dreq_t
- dcache_enable_i
- cmo_req_t
- ... and 17 more

**Payload Signals (22):**
- icache_en_i
- icache_areq_t
- icache_dreq_t
- dcache_enable_i
- cmo_req_t
- ... and 17 more

**Generated File:** T1_cva6_hpdcache_subsystem_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- dcache_write_data_ready
- dcache_write_data_valid

**Payload Signals (6):**
- dcache_write_ready
- dcache_write_valid
- dcache_write_data_ready
- dcache_write_data_valid
- dcache_write_resp_ready
- ... and 1 more

**Generated File:** T2_cva6_hpdcache_subsystem_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (16):**
- icache_areq_t
- icache_dreq_t
- cmo_req_t
- request
- dcache_req_i_t
- ... and 11 more

**Payload Signals (13):**
- dcache_flush_ack_o
- icache_miss_valid
- icache_miss_resp_valid
- dcache_read_ready
- dcache_read_valid
- ... and 8 more

**Generated File:** T3_cva6_hpdcache_subsystem_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- dcache_write_data_ready
- dcache_write_data_valid

**Generated File:** T4_cva6_hpdcache_subsystem_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- dcache_write_ready
- dcache_write_valid
- dcache_write_data_ready
- dcache_write_data_valid
- dcache_write_resp_ready
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T5_cva6_hpdcache_subsystem_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- dcache_write_data_ready
- dcache_write_data_valid

**Payload Signals (0):**

**Generated File:** T6_cva6_hpdcache_subsystem_Covert.sv

---

