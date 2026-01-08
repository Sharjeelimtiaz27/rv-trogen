# Trojan Generation Summary

**Module:** is
**File:** ibex_decoder.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- branch_taken_i
- rf_ren_a_o
- rf_ren_b_o
- mult_en_o
- div_en_o
- ... and 2 more

**Payload Signals (7):**
- branch_taken_i
- rf_ren_a_o
- rf_ren_b_o
- mult_en_o
- div_en_o
- ... and 2 more

**Generated File:** T1_is_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- multdiv_signed_mode_o
- data_sign_extension_o

**Payload Signals (12):**
- instr_rdata_i
- instr_rdata_alu_i
- rf_raddr_a_o
- rf_raddr_b_o
- rf_waddr_o
- ... and 7 more

**Generated File:** T2_is_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (9):**
- rf_we_o
- rf_raddr_a_o
- rf_raddr_b_o
- rf_waddr_o
- multdiv_signed_mode_o
- ... and 4 more

**Payload Signals (1):**
- multdiv_signed_mode_o

**Generated File:** T3_is_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- instr_rdata_i
- instr_rdata_alu_i
- rf_raddr_a_o
- rf_raddr_b_o
- rf_waddr_o
- ... and 6 more

**Payload Signals (7):**
- instr_rdata_i
- instr_rdata_alu_i
- data_req_o
- data_we_o
- data_type_o
- ... and 2 more

**Generated File:** T4_is_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (7):**
- instr_rdata_i
- instr_rdata_alu_i
- csr_access_o
- data_req_o
- data_we_o
- ... and 2 more

**Payload Signals (3):**
- unused_instr_alu
- unused_clk
- unused_rst_n

**Generated File:** T5_is_Covert.sv

---

### T6: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- instr_rdata_i
- instr_rdata_alu_i
- data_req_o
- data_we_o
- data_type_o
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T6_is_Availability.sv

---

