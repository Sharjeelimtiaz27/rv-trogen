# Trojan Generation Summary

**Module:** wt_dcache
**File:** wt_dcache.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- enable_i
- amo_req_t
- dcache_req_i_t
- dcache_req_o_t
- mem_data_req_o
- ... and 2 more

**Payload Signals (7):**
- enable_i
- amo_req_t
- dcache_req_i_t
- dcache_req_o_t
- mem_data_req_o
- ... and 2 more

**Generated File:** T1_wt_dcache_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- mem_data_ack_i
- mem_data_req_o

**Payload Signals (2):**
- mem_data_ack_i
- mem_data_req_o

**Generated File:** T2_wt_dcache_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- amo_req_t
- dcache_req_i_t
- mem_data_ack_i
- dcache_req_o_t
- mem_data_req_o
- ... and 1 more

**Payload Signals (3):**
- mem_data_ack_i
- flush_ack_o
- wr_ack

**Generated File:** T3_wt_dcache_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- mem_data_ack_i
- mem_data_req_o

**Generated File:** T4_wt_dcache_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- mem_data_ack_i
- mem_data_req_o

**Payload Signals (0):**

**Generated File:** T5_wt_dcache_Covert.sv

---

