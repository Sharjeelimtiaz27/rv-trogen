# Trojan Generation Summary

**Module:** pmp_data_if
**File:** pmp_data_if.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- icache_areq_t
- icache_areq_i
- icache_areq_t
- icache_areq_o
- lsu_valid_i
- ... and 5 more

**Payload Signals (10):**
- icache_areq_t
- icache_areq_i
- icache_areq_t
- icache_areq_o
- lsu_valid_i
- ... and 5 more

**Generated File:** T1_pmp_data_if_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (10):**
- icache_fetch_vaddr_i
- lsu_paddr_i
- lsu_vaddr_i
- lsu_paddr_o
- pmpaddr_i
- ... and 5 more

**Payload Signals (8):**
- riscv::priv_lvl_t
- priv_lvl_i
- riscv::priv_lvl_t
- ld_st_priv_lvl_i
- riscv::priv_lvl_t
- ... and 3 more

**Generated File:** T2_pmp_data_if_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- icache_fetch_vaddr_i
- lsu_paddr_i
- lsu_vaddr_i
- lsu_paddr_o
- pmpaddr_i
- ... and 6 more

**Payload Signals (3):**
- lsu_is_store_i
- lsu_is_store_i
- data_allow_o

**Generated File:** T3_pmp_data_if_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (22):**
- icache_areq_t
- icache_areq_i
- icache_areq_t
- icache_areq_o
- lsu_valid_i
- ... and 17 more

**Payload Signals (4):**
- lsu_valid_i
- lsu_valid_o
- lsu_valid_i
- lsu_valid_o

**Generated File:** T4_pmp_data_if_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- icache_fetch_vaddr_i
- icache_fetch_vaddr_i
- data_allow_o

**Payload Signals (5):**
- lsu_valid_i
- lsu_valid_o
- lsu_valid_i
- lsu_valid_o
- data_allow_o

**Generated File:** T5_pmp_data_if_Covert.sv

---

