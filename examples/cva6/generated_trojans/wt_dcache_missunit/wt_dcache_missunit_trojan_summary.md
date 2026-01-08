# Trojan Generation Summary

**Module:** wt_dcache_missunit
**File:** wt_dcache_missunit.sv
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
- enable_i
- amo_req_t
- cache_en_o
- mem_data_req_o
- dcache_req_t
- ... and 4 more

**Payload Signals (9):**
- enable_i
- amo_req_t
- cache_en_o
- mem_data_req_o
- dcache_req_t
- ... and 4 more

**Generated File:** T1_wt_dcache_missunit_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- mem_data_ack_i
- mem_data_req_o
- amo_sel

**Payload Signals (3):**
- mem_data_ack_i
- mem_data_req_o
- store_sent

**Generated File:** T2_wt_dcache_missunit_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- amo_req_t
- mem_data_ack_i
- mem_data_req_o
- dcache_req_t
- amo_req_d

**Payload Signals (4):**
- mem_data_ack_i
- flush_ack_o
- flush_ack_d
- load_ack

**Generated File:** T3_wt_dcache_missunit_Availability.sv

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

**Generated File:** T4_wt_dcache_missunit_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- mem_data_ack_i
- mem_data_req_o
- load_ack

**Payload Signals (0):**

**Generated File:** T5_wt_dcache_missunit_Covert.sv

---

