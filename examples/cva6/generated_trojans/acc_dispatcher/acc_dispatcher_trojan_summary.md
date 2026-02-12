# Trojan Generation Summary

**Module:** acc_dispatcher
**File:** acc_dispatcher.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (35):**
- acc_cons_en_i
- acc_fflags_valid_o
- acc_mmu_en_i
- acc_valid_o
- acc_valid_ex_o
- ... and 30 more

**Payload Signals (35):**
- acc_cons_en_i
- acc_fflags_valid_o
- acc_mmu_en_i
- acc_valid_o
- acc_valid_ex_o
- ... and 30 more

**Generated File:** T1_acc_dispatcher_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- csr_addr_i
- csr_addr_i

**Payload Signals (12):**
- pmpaddr_i
- fu_data_t
- fu_data_i
- acc_result_o
- csr_addr_i
- ... and 7 more

**Generated File:** T2_acc_dispatcher_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- pmpaddr_i
- csr_addr_i
- inval_addr_o
- pmpaddr_i
- csr_addr_i
- ... and 1 more

**Payload Signals (4):**
- priv_lvl_t
- ld_st_priv_lvl_i
- priv_lvl_t
- ld_st_priv_lvl_i

**Generated File:** T3_acc_dispatcher_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- pmpaddr_i
- fu_data_t
- fu_data_i
- csr_addr_i
- inval_addr_o
- ... and 6 more

**Payload Signals (6):**
- fu_data_t
- fu_data_i
- acc_result_o
- fu_data_t
- fu_data_i
- ... and 1 more

**Generated File:** T4_acc_dispatcher_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (31):**
- acc_fflags_valid_o
- acc_valid_o
- acc_valid_ex_o
- dcache_req_i_t
- dcache_req_ports_i
- ... and 26 more

**Payload Signals (17):**
- acc_fflags_valid_o
- issue_stall_o
- acc_valid_o
- acc_valid_ex_o
- commit_ack_i
- ... and 12 more

**Generated File:** T5_acc_dispatcher_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- fu_data_t
- fu_data_i
- fu_data_t
- fu_data_i

**Payload Signals (17):**
- acc_fflags_valid_o
- fu_data_t
- fu_data_i
- acc_result_o
- acc_valid_o
- ... and 12 more

**Generated File:** T6_acc_dispatcher_Covert.sv

---

