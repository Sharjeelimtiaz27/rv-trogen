# Trojan Generation Summary

**Module:** load_store_unit
**File:** load_store_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (48):**
- amo_valid_commit_i
- lsu_ready_o
- lsu_valid_i
- load_valid_o
- store_valid_o
- ... and 43 more

**Payload Signals (48):**
- amo_valid_commit_i
- lsu_ready_o
- lsu_valid_i
- load_valid_o
- store_valid_o
- ... and 43 more

**Generated File:** T1_load_store_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- csr_hs_ld_st_inst_o
- csr_hs_ld_st_inst_o

**Payload Signals (25):**
- fu_data_t
- fu_data_i
- load_result_o
- store_result_o
- csr_hs_ld_st_inst_o
- ... and 20 more

**Generated File:** T2_load_store_unit_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (14):**
- csr_hs_ld_st_inst_o
- vaddr_to_be_flushed_i
- gpaddr_to_be_flushed_i
- pmpaddr_i
- rvfi_mem_paddr_o
- ... and 9 more

**Payload Signals (8):**
- riscv::priv_lvl_t
- priv_lvl_i
- riscv::priv_lvl_t
- ld_st_priv_lvl_i
- riscv::priv_lvl_t
- ... and 3 more

**Generated File:** T3_load_store_unit_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (19):**
- fu_data_t
- fu_data_i
- vaddr_to_be_flushed_i
- gpaddr_to_be_flushed_i
- pmpaddr_i
- ... and 14 more

**Payload Signals (17):**
- fu_data_t
- fu_data_i
- load_result_o
- store_trans_id_o
- store_result_o
- ... and 12 more

**Generated File:** T4_load_store_unit_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (56):**
- amo_valid_commit_i
- lsu_ready_o
- lsu_valid_i
- load_trans_id_o
- load_result_o
- ... and 51 more

**Payload Signals (18):**
- stall_st_pending_i
- amo_valid_commit_i
- lsu_ready_o
- lsu_valid_i
- load_valid_o
- ... and 13 more

**Generated File:** T5_load_store_unit_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (13):**
- fu_data_t
- fu_data_i
- load_trans_id_o
- load_result_o
- load_valid_o
- ... and 8 more

**Payload Signals (28):**
- amo_valid_commit_i
- fu_data_t
- fu_data_i
- lsu_ready_o
- lsu_valid_i
- ... and 23 more

**Generated File:** T6_load_store_unit_Covert.sv

---

