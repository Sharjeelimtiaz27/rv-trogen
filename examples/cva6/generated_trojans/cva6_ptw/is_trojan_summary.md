# Trojan Generation Summary

**Module:** is
**File:** cva6_ptw.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (11):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- dcache_req_o_t
- ... and 6 more

**Payload Signals (11):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- dcache_req_o_t
- ... and 6 more

**Generated File:** T1_is_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- data_rvalid_q

**Payload Signals (3):**
- lsu_is_store_i
- output
- data_rvalid_q

**Generated File:** T2_is_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- dcache_req_o_t
- itlb_req_i
- dcache_req_i_t
- data_rvalid_q
- shared_tlb_update_valid
- ... and 1 more

**Payload Signals (3):**
- data_rvalid_q
- shared_tlb_update_valid
- tag_valid_n

**Generated File:** T3_is_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- registers
- registers
- data_rvalid_q

**Generated File:** T4_is_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- shared_tlb_access_i
- ptw_access_exception_o
- data_rvalid_q
- allow_access

**Payload Signals (0):**

**Generated File:** T5_is_Covert.sv

---

