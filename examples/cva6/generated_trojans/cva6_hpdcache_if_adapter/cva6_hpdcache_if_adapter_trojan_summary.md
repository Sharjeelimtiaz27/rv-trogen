# Trojan Generation Summary

**Module:** cva6_hpdcache_if_adapter
**File:** cva6_hpdcache_if_adapter.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- hpdcache_req_sid_t
- dcache_req_i_t
- hpdcache_req_ready_i
- hpdcache_rsp_valid_i
- dcache_req_o_t
- ... and 5 more

**Payload Signals (10):**
- hpdcache_req_sid_t
- dcache_req_i_t
- hpdcache_req_ready_i
- hpdcache_rsp_valid_i
- dcache_req_o_t
- ... and 5 more

**Generated File:** T1_cva6_hpdcache_if_adapter_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- amo_addr
- amo_data

**Payload Signals (2):**
- amo_data
- forward_store

**Generated File:** T2_cva6_hpdcache_if_adapter_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- hpdcache_req_sid_t
- dcache_req_i_t
- hpdcache_req_ready_i
- hpdcache_rsp_valid_i
- dcache_req_o_t
- ... and 5 more

**Payload Signals (4):**
- hpdcache_req_ready_i
- hpdcache_rsp_valid_i
- cva6_dcache_flush_ack_o
- hpdcache_req_valid_o

**Generated File:** T3_cva6_hpdcache_if_adapter_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- amo_addr
- amo_data

**Generated File:** T4_cva6_hpdcache_if_adapter_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- amo_addr

**Payload Signals (0):**

**Generated File:** T5_cva6_hpdcache_if_adapter_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- amo_data

**Payload Signals (0):**

**Generated File:** T6_cva6_hpdcache_if_adapter_Covert.sv

---

