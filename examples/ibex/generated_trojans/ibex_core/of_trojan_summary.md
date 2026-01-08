# Trojan Generation Summary

**Module:** of
**File:** ibex_core.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (56):**
- instr_rvalid_i
- data_rvalid_i
- ic_scr_key_valid_i
- debug_req_i
- instr_req_o
- ... and 51 more

**Payload Signals (59):**
- instr_rvalid_i
- data_rvalid_i
- ic_scr_key_valid_i
- debug_req_i
- instr_req_o
- ... and 54 more

**Generated File:** T1_of_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (41):**
- irq_external_i
- debug_req_i
- rvfi_ext_pre_mip
- rvfi_ext_post_mip
- rvfi_ext_nmi
- ... and 36 more

**Payload Signals (99):**
- boot_addr_i
- data_gnt_i
- data_rvalid_i
- data_err_i
- ic_scr_key_valid_i
- ... and 94 more

**Generated File:** T2_of_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (65):**
- boot_addr_i
- instr_addr_o
- data_we_o
- data_addr_o
- rf_raddr_a_o
- ... and 60 more

**Payload Signals (8):**
- rvfi_ext_debug_mode
- multdiv_signed_mode_ex
- nmi_mode
- csr_mstatus_mie
- csr_mstatus_tw
- ... and 3 more

**Generated File:** T3_of_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (84):**
- boot_addr_i
- data_gnt_i
- data_rvalid_i
- data_err_i
- instr_addr_o
- ... and 79 more

**Payload Signals (68):**
- data_gnt_i
- data_rvalid_i
- data_err_i
- data_req_o
- data_we_o
- ... and 63 more

**Generated File:** T4_of_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (90):**
- instr_rvalid_i
- data_gnt_i
- data_rvalid_i
- data_err_i
- ic_scr_key_valid_i
- ... and 85 more

**Payload Signals (35):**
- instr_rvalid_i
- data_rvalid_i
- ic_scr_key_valid_i
- rvfi_valid
- rvfi_ext_ic_scr_key_valid
- ... and 30 more

**Generated File:** T5_of_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (69):**
- data_gnt_i
- data_rvalid_i
- data_err_i
- ic_scr_key_valid_i
- data_req_o
- ... and 64 more

**Payload Signals (28):**
- debug_req_i
- rvfi_ext_debug_req
- rvfi_ext_debug_mode
- data_ind_timing
- ctrl_busy
- ... and 23 more

**Generated File:** T6_of_Covert.sv

---

