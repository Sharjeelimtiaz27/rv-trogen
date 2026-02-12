# Trojan Generation Summary

**Module:** csr_regfile
**File:** csr_regfile.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (24):**
- acc_fflags_ex_valid_i
- en_translation_o
- en_g_translation_o
- en_ld_st_translation_o
- en_ld_st_g_translation_o
- ... and 19 more

**Payload Signals (20):**
- acc_fflags_ex_valid_i
- en_translation_o
- en_g_translation_o
- en_ld_st_translation_o
- en_ld_st_g_translation_o
- ... and 15 more

**Generated File:** T1_csr_regfile_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (32):**
- halt_csr_o
- csr_op_i
- csr_addr_i
- csr_wdata_i
- csr_rdata_o
- ... and 27 more

**Payload Signals (42):**
- halt_csr_o
- boot_addr_i
- csr_op_i
- csr_addr_i
- csr_wdata_i
- ... and 37 more

**Generated File:** T2_csr_regfile_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (35):**
- halt_csr_o
- boot_addr_i
- csr_op_i
- csr_addr_i
- csr_wdata_i
- ... and 30 more

**Payload Signals (12):**
- riscv::priv_lvl_t
- priv_lvl_o
- riscv::priv_lvl_t
- ld_st_priv_lvl_o
- debug_mode_o
- ... and 7 more

**Generated File:** T3_csr_regfile_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (33):**
- boot_addr_i
- fu_op
- csr_op_i
- csr_addr_i
- csr_wdata_i
- ... and 28 more

**Payload Signals (19):**
- csr_wdata_i
- csr_rdata_o
- csr_write_fflags_i
- perf_data_o
- perf_data_i
- ... and 14 more

**Generated File:** T4_csr_regfile_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (16):**
- fu_op
- csr_op_i
- acc_fflags_ex_valid_i
- debug_req_i
- debug_from_trigger_o
- ... and 11 more

**Payload Signals (4):**
- commit_ack_i
- acc_fflags_ex_valid_i
- commit_ack_i
- acc_fflags_ex_valid_i

**Generated File:** T5_csr_regfile_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (15):**
- csr_wdata_i
- csr_rdata_o
- perf_data_o
- perf_data_i
- csr_wdata_i
- ... and 10 more

**Payload Signals (19):**
- csr_wdata_i
- csr_rdata_o
- acc_fflags_ex_valid_i
- perf_data_o
- perf_data_i
- ... and 14 more

**Generated File:** T6_csr_regfile_Covert.sv

---

