# Trojan Generation Summary

**Module:** ibex_if_stage
**File:** ibex_if_stage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (27):**
- req_i
- instr_rvalid_i
- ic_scr_key_valid_i
- instr_valid_clear_i
- dummy_instr_en_i
- ... and 22 more

**Payload Signals (27):**
- req_i
- instr_rvalid_i
- ic_scr_key_valid_i
- instr_valid_clear_i
- dummy_instr_en_i
- ... and 22 more

**Generated File:** T1_ibex_if_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- next_pc

**Payload Signals (27):**
- boot_addr_i
- ic_scr_key_valid_i
- nt_branch_addr_i
- csr_mepc_i
- csr_depc_i
- ... and 22 more

**Generated File:** T2_ibex_if_stage_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (21):**
- boot_addr_i
- pc_sel_e
- nt_branch_addr_i
- exc_pc_sel_e
- instr_addr_o
- ... and 16 more

**Payload Signals (14):**
- ic_tag_write_o
- ic_data_write_o
- instr_rdata_id_o
- instr_rdata_alu_id_o
- instr_rdata_c_id_o
- ... and 9 more

**Generated File:** T3_ibex_if_stage_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (21):**
- req_i
- instr_rvalid_i
- ic_scr_key_valid_i
- instr_valid_clear_i
- instr_req_o
- ... and 16 more

**Payload Signals (15):**
- instr_rvalid_i
- ic_scr_key_valid_i
- instr_valid_clear_i
- id_in_ready_i
- instr_valid_id_o
- ... and 10 more

**Generated File:** T4_ibex_if_stage_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (23):**
- ic_scr_key_valid_i
- ic_data_write_o
- ic_scr_key_req_o
- instr_rdata_id_o
- instr_rdata_alu_id_o
- ... and 18 more

**Payload Signals (12):**
- if_busy_o
- prefetch_busy
- unused_fetch_addr_n0
- unused_boot_addr
- unused_csr_mtvec
- ... and 7 more

**Generated File:** T5_ibex_if_stage_Covert.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (20):**
- boot_addr_i
- nt_branch_addr_i
- csr_mepc_i
- csr_depc_i
- csr_mtvec_i
- ... and 15 more

**Payload Signals (0):**

**Generated File:** T6_ibex_if_stage_Privilege.sv

---

