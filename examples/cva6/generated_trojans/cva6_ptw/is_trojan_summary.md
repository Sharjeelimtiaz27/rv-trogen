# Trojan Generation Summary

**Module:** is
**File:** cva6_ptw.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (20):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- dcache_req_o_t
- ... and 15 more

**Payload Signals (20):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- dcache_req_o_t
- ... and 15 more

**Generated File:** T1_is_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- update_vaddr_o
- shared_tlb_vaddr_i
- pmpaddr_i
- bad_paddr_o
- bad_gpaddr_o
- ... and 9 more

**Payload Signals (4):**
- lsu_is_store_i
- lsu_is_store_i
- data_rvalid_q
- data_rdata_q

**Generated File:** T2_is_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (14):**
- lsu_is_store_i
- dcache_req_o_t
- req_port_i
- dcache_req_i_t
- req_port_o
- ... and 9 more

**Payload Signals (2):**
- data_rvalid_q
- shared_tlb_update_valid

**Generated File:** T3_is_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- ptw_access_exception_o
- shared_tlb_access_i
- ptw_access_exception_o
- shared_tlb_access_i
- data_rvalid_q
- ... and 2 more

**Payload Signals (3):**
- data_rvalid_q
- data_rdata_q
- shared_tlb_update_valid

**Generated File:** T4_is_Covert.sv

---

