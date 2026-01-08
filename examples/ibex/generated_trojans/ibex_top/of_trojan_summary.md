# Trojan Generation Summary

**Module:** of
**File:** ibex_top.sv
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
- test_en_i
- instr_rvalid_i
- data_rvalid_i
- scramble_key_valid_i
- debug_req_i
- ... and 28 more

**Payload Signals (33):**
- test_en_i
- instr_rvalid_i
- data_rvalid_i
- scramble_key_valid_i
- debug_req_i
- ... and 28 more

**Generated File:** T1_of_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (22):**
- test_en_i
- irq_external_i
- debug_req_i
- scan_rst_ni
- rvfi_ext_pre_mip
- ... and 17 more

**Payload Signals (50):**
- boot_addr_i
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- ... and 45 more

**Generated File:** T2_of_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (25):**
- boot_addr_i
- instr_addr_o
- data_we_o
- data_addr_o
- rvfi_mem_addr
- ... and 20 more

**Payload Signals (1):**
- rvfi_ext_debug_mode

**Generated File:** T3_of_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (44):**
- boot_addr_i
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- ... and 39 more

**Payload Signals (34):**
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- data_rdata_i
- ... and 29 more

**Generated File:** T4_of_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (50):**
- instr_rvalid_i
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- ... and 45 more

**Payload Signals (13):**
- instr_rvalid_i
- data_rvalid_i
- scramble_key_valid_i
- rvfi_valid
- rvfi_ext_ic_scr_key_valid
- ... and 8 more

**Generated File:** T5_of_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (39):**
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- data_rdata_i
- ... and 34 more

**Payload Signals (11):**
- test_en_i
- debug_req_i
- rvfi_ext_debug_req
- rvfi_ext_debug_mode
- unused_core_busy
- ... and 6 more

**Generated File:** T6_of_Covert.sv

---

