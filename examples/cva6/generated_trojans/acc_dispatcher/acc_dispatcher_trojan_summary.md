# Trojan Generation Summary

**Module:** acc_dispatcher
**File:** acc_dispatcher.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (26):**
- acc_cons_en_i
- acc_mmu_en_i
- scoreboard_entry_t
- scoreboard_entry_t
- acc_no_st_pending_i
- ... and 21 more

**Payload Signals (26):**
- acc_cons_en_i
- acc_mmu_en_i
- scoreboard_entry_t
- scoreboard_entry_t
- acc_no_st_pending_i
- ... and 21 more

**Generated File:** T1_acc_dispatcher_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- ctrl_halt_o

**Payload Signals (5):**
- priv_lvl_t
- fcsr_frm_i
- fu_data_t
- csr_addr_i
- inval_addr_o

**Generated File:** T2_acc_dispatcher_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- fcsr_frm_i
- csr_addr_i
- ctrl_halt_o
- inval_addr_o

**Payload Signals (2):**
- priv_lvl_t
- dirty_v_state_o

**Generated File:** T3_acc_dispatcher_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- fu_data_t
- csr_addr_i
- inval_addr_o
- acc_insn_queue_pop

**Payload Signals (6):**
- fu_data_t
- wait_acc_store_d
- acc_spec_stores_overflow
- acc_spec_stores_pending
- acc_disp_stores_overflow
- ... and 1 more

**Generated File:** T4_acc_dispatcher_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (14):**
- fu_data_t
- dcache_req_i_t
- dcache_req_o_t
- acc_fflags_valid_o
- acc_valid_o
- ... and 9 more

**Payload Signals (12):**
- inval_ready_i
- acc_fflags_valid_o
- issue_stall_o
- acc_valid_o
- acc_valid_ex_o
- ... and 7 more

**Generated File:** T5_acc_dispatcher_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- priv_lvl_t
- fu_data_t
- acc_spec_loads_overflow
- acc_spec_loads_pending
- acc_disp_loads_overflow
- ... and 1 more

**Payload Signals (1):**
- wait_acc_store_d

**Generated File:** T6_acc_dispatcher_Covert.sv

---

