# Trojan Generation Summary

**Module:** is
**File:** cva6_mmu.sv
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
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- lsu_req_i
- ... and 7 more

**Payload Signals (12):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- lsu_req_i
- ... and 7 more

**Generated File:** T1_is_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- canonical_addr_check

**Payload Signals (2):**
- lsu_is_store_i
- lsu_is_store_n

**Generated File:** T2_is_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- lsu_req_i
- dcache_req_o_t
- icache_areq_t
- lsu_valid_o
- dcache_req_i_t
- ... and 2 more

**Payload Signals (2):**
- lsu_valid_o
- valid

**Generated File:** T3_is_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- iaccess_err
- i_g_st_access_err
- daccess_err
- d_g_st_access_err
- ptw_access_exception
- ... and 3 more

**Payload Signals (1):**
- reserved

**Generated File:** T4_is_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- csr_hs_ld_st_inst_o
- canonical_addr_check

**Generated File:** T5_is_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- csr_hs_ld_st_inst_o
- canonical_addr_check

**Payload Signals (0):**

**Generated File:** T6_is_Privilege.sv

---

