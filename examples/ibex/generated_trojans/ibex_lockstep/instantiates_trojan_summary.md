# Trojan Generation Summary

**Module:** instantiates
**File:** ibex_lockstep.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (20):**
- instr_req_i
- instr_rvalid_i
- data_req_i
- data_rvalid_i
- ic_scr_key_valid_i
- ... and 15 more

**Payload Signals (20):**
- instr_req_i
- instr_rvalid_i
- data_req_i
- data_rvalid_i
- ic_scr_key_valid_i
- ... and 15 more

**Generated File:** T1_instantiates_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (6):**
- irq_external_i
- debug_req_i
- test_en_i
- scan_rst_ni
- irq_external
- ... and 1 more

**Payload Signals (32):**
- boot_addr_i
- instr_addr_i
- data_req_i
- data_gnt_i
- data_rvalid_i
- ... and 27 more

**Generated File:** T2_instantiates_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (25):**
- boot_addr_i
- instr_addr_i
- data_req_i
- data_gnt_i
- data_rvalid_i
- ... and 20 more

**Payload Signals (19):**
- data_req_i
- data_gnt_i
- data_rvalid_i
- data_we_i
- data_be_i
- ... and 14 more

**Generated File:** T3_instantiates_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (26):**
- instr_req_i
- instr_rvalid_i
- data_req_i
- data_gnt_i
- data_rvalid_i
- ... and 21 more

**Payload Signals (6):**
- instr_rvalid_i
- data_rvalid_i
- ic_scr_key_valid_i
- instr_rvalid
- data_rvalid
- ... and 1 more

**Generated File:** T4_instantiates_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (20):**
- data_req_i
- data_gnt_i
- data_rvalid_i
- data_we_i
- data_be_i
- ... and 15 more

**Payload Signals (3):**
- debug_req_i
- test_en_i
- debug_req

**Generated File:** T5_instantiates_Covert.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (21):**
- boot_addr_i
- instr_addr_i
- data_we_i
- data_addr_i
- rf_raddr_a_i
- ... and 16 more

**Payload Signals (0):**

**Generated File:** T6_instantiates_Privilege.sv

---

