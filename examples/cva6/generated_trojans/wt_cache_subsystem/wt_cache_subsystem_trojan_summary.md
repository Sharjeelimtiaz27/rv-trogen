# Trojan Generation Summary

**Module:** wt_cache_subsystem
**File:** wt_cache_subsystem.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (12):**
- icache_en_i
- icache_areq_t
- icache_dreq_t
- dcache_enable_i
- amo_req_t
- ... and 7 more

**Payload Signals (12):**
- icache_en_i
- icache_areq_t
- icache_dreq_t
- dcache_enable_i
- amo_req_t
- ... and 7 more

**Generated File:** T1_wt_cache_subsystem_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- inval_addr_i
- icache_adapter_data_req
- dcache_adapter_data_req

**Payload Signals (2):**
- icache_adapter_data_req
- dcache_adapter_data_req

**Generated File:** T2_wt_cache_subsystem_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- icache_areq_t
- icache_dreq_t
- amo_req_t
- dcache_req_i_t
- inval_valid_i
- ... and 4 more

**Payload Signals (3):**
- inval_valid_i
- dcache_flush_ack_o
- inval_ready_o

**Generated File:** T3_wt_cache_subsystem_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- inval_addr_i
- icache_adapter_data_req
- dcache_adapter_data_req

**Generated File:** T4_wt_cache_subsystem_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- inval_addr_i

**Payload Signals (0):**

**Generated File:** T5_wt_cache_subsystem_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- icache_adapter_data_req
- dcache_adapter_data_req

**Payload Signals (0):**

**Generated File:** T6_wt_cache_subsystem_Covert.sv

---

