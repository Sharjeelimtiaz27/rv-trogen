# Trojan Generation Summary

**Module:** is
**File:** cva6_mmu.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (22):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- icache_areq_i
- ... and 17 more

**Payload Signals (22):**
- enable_translation_i
- enable_g_translation_i
- en_ld_st_translation_i
- en_ld_st_g_translation_i
- icache_areq_i
- ... and 17 more

**Generated File:** T1_is_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- csr_hs_ld_st_inst_o
- csr_hs_ld_st_inst_o

**Payload Signals (17):**
- lsu_vaddr_i
- csr_hs_ld_st_inst_o
- lsu_paddr_o
- vaddr_to_be_flushed_i
- gpaddr_to_be_flushed_i
- ... and 12 more

**Generated File:** T2_is_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (17):**
- lsu_vaddr_i
- csr_hs_ld_st_inst_o
- lsu_paddr_o
- vaddr_to_be_flushed_i
- gpaddr_to_be_flushed_i
- ... and 12 more

**Payload Signals (8):**
- riscv::priv_lvl_t
- priv_lvl_i
- riscv::priv_lvl_t
- ld_st_priv_lvl_i
- riscv::priv_lvl_t
- ... and 3 more

**Generated File:** T3_is_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- lsu_vaddr_i
- lsu_paddr_o
- vaddr_to_be_flushed_i
- gpaddr_to_be_flushed_i
- pmpaddr_i
- ... and 10 more

**Payload Signals (2):**
- lsu_is_store_i
- lsu_is_store_i

**Generated File:** T4_is_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (26):**
- icache_areq_i
- icache_areq_t
- icache_areq_o
- lsu_req_i
- lsu_vaddr_i
- ... and 21 more

**Payload Signals (3):**
- lsu_valid_o
- lsu_valid_o
- valid

**Generated File:** T5_is_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- iaccess_err
- i_g_st_access_err
- daccess_err
- d_g_st_access_err
- ptw_access_exception
- ... and 2 more

**Payload Signals (3):**
- lsu_valid_o
- lsu_valid_o
- valid

**Generated File:** T6_is_Covert.sv

---

