# Trojan Generation Summary

**Module:** std_nbdcache
**File:** std_nbdcache.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- enable_i
- amo_req_t
- dcache_req_i_t
- dcache_req_o_t
- axi_req_t
- ... and 3 more

**Payload Signals (8):**
- enable_i
- amo_req_t
- dcache_req_i_t
- dcache_req_o_t
- axi_req_t
- ... and 3 more

**Generated File:** T1_std_nbdcache_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- amo_req_t
- dcache_req_i_t
- dcache_req_o_t
- axi_req_t
- axi_req_t
- ... and 2 more

**Payload Signals (3):**
- flush_ack_o
- valid
- critical_word_valid

**Generated File:** T2_std_nbdcache_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- we_ram

**Payload Signals (0):**

**Generated File:** T3_std_nbdcache_Privilege.sv

---

