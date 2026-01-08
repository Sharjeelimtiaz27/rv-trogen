# Trojan Generation Summary

**Module:** of
**File:** ibex_top_tracing.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (17):**
- test_en_i
- instr_rvalid_i
- data_rvalid_i
- scramble_key_valid_i
- debug_req_i
- ... and 12 more

**Payload Signals (17):**
- test_en_i
- instr_rvalid_i
- data_rvalid_i
- scramble_key_valid_i
- debug_req_i
- ... and 12 more

**Generated File:** T1_of_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (30):**
- test_en_i
- scan_rst_ni
- irq_external_i
- debug_req_i
- rvfi_ext_pre_mip
- ... and 25 more

**Payload Signals (29):**
- boot_addr_i
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- ... and 24 more

**Generated File:** T2_of_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (7):**
- boot_addr_i
- instr_addr_o
- data_we_o
- data_addr_o
- rvfi_mem_addr
- ... and 2 more

**Payload Signals (2):**
- rvfi_ext_debug_mode
- unused_rvfi_ext_debug_mode

**Generated File:** T3_of_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (24):**
- boot_addr_i
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- ... and 19 more

**Payload Signals (21):**
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- data_rdata_i
- ... and 16 more

**Generated File:** T4_of_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (34):**
- instr_rvalid_i
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- ... and 29 more

**Payload Signals (9):**
- instr_rvalid_i
- data_rvalid_i
- scramble_key_valid_i
- rvfi_valid
- rvfi_ext_ic_scr_key_valid
- ... and 4 more

**Generated File:** T5_of_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (24):**
- instr_rdata_i
- instr_rdata_intg_i
- data_gnt_i
- data_rvalid_i
- data_rdata_i
- ... and 19 more

**Payload Signals (17):**
- test_en_i
- debug_req_i
- rvfi_ext_debug_req
- rvfi_ext_debug_mode
- unused_perf_regs
- ... and 12 more

**Generated File:** T6_of_Covert.sv

---

