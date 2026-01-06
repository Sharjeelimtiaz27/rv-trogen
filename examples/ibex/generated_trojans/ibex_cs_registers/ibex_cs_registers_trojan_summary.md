# Trojan Generation Summary

**Module:** ibex_cs_registers
**File:** ibex_cs_registers.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (33):**
- csr_op_en_i
- debug_mode_entering_i
- ic_scr_key_valid_i
- branch_taken_i
- irq_pending_o
- ... and 28 more

**Payload Signals (32):**
- csr_op_en_i
- debug_mode_entering_i
- ic_scr_key_valid_i
- branch_taken_i
- irq_pending_o
- ... and 27 more

**Generated File:** T1_ibex_cs_registers_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (17):**
- irq_external_i
- nmi_mode_i
- debug_mode_i
- debug_mode_entering_i
- debug_csr_save_i
- ... and 12 more

**Payload Signals (47):**
- csr_mtvec_init_i
- boot_addr_i
- csr_access_i
- csr_wdata_i
- csr_op_en_i
- ... and 42 more

**Generated File:** T2_ibex_cs_registers_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (55):**
- csr_mtvec_init_i
- boot_addr_i
- csr_access_i
- csr_wdata_i
- csr_op_en_i
- ... and 50 more

**Payload Signals (8):**
- nmi_mode_i
- debug_mode_i
- debug_mode_entering_i
- csr_mstatus_tw_o
- csr_mstatus_mie_o
- ... and 3 more

**Generated File:** T3_ibex_cs_registers_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (18):**
- boot_addr_i
- csr_wdata_i
- csr_op_en_i
- csr_rdata_o
- data_ind_timing_o
- ... and 13 more

**Payload Signals (18):**
- csr_wdata_i
- csr_restore_mret_i
- csr_restore_dret_i
- mem_store_i
- csr_rdata_o
- ... and 13 more

**Generated File:** T4_ibex_cs_registers_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (16):**
- csr_wdata_i
- csr_op_en_i
- ic_scr_key_valid_i
- csr_rdata_o
- trigger_match_o
- ... and 11 more

**Payload Signals (9):**
- ic_scr_key_valid_i
- iside_wait_i
- dside_wait_i
- mul_wait_i
- div_wait_i
- ... and 4 more

**Generated File:** T5_ibex_cs_registers_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (16):**
- csr_access_i
- csr_wdata_i
- ic_scr_key_valid_i
- mem_load_i
- csr_rdata_o
- ... and 11 more

**Payload Signals (25):**
- debug_mode_i
- debug_mode_entering_i
- debug_csr_save_i
- iside_wait_i
- dside_wait_i
- ... and 20 more

**Generated File:** T6_ibex_cs_registers_Covert.sv

---

