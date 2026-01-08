# Trojan Generation Summary

**Module:** ibex_alu
**File:** ibex_alu.sv
**Type:** Combinational
**Total Candidates:** 6

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (24):**
- operand_a_i
- operand_b_i
- multdiv_operand_a_i
- multdiv_operand_b_i
- multdiv_sel_i
- ... and 19 more

**Payload Signals (32):**
- adder_result_o
- adder_result_ext_o
- result_o
- comparison_result_o
- is_equal_result_o
- ... and 27 more

**Generated File:** T1_ibex_alu_Integrity.sv

---

### T2: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- bfp_len
- gorc_op

**Payload Signals (1):**
- bfp_len

**Generated File:** T2_ibex_alu_DoS.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (7):**
- imd_val_we_o
- shift_sbmode
- crc_hmode
- crc_bmode
- shuffle_mode
- ... and 2 more

**Payload Signals (6):**
- shift_sbmode
- crc_hmode
- crc_bmode
- shuffle_mode
- clmul_rmode
- ... and 1 more

**Generated File:** T3_ibex_alu_Privilege.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.80
**Description:** Degrades performance through artificial delays

**Trigger Signals (23):**
- operand_a_i
- operand_b_i
- multdiv_operand_a_i
- multdiv_operand_b_i
- operand
- ... and 18 more

**Payload Signals (3):**
- pack_result
- packu
- packh

**Generated File:** T4_ibex_alu_Availability.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- adder_result_ext_o
- shift_sbmode
- shift_result_ext
- unused_shift_result_ext
- sext_result
- ... and 5 more

**Payload Signals (0):**

**Generated File:** T5_ibex_alu_Leak.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (6):**
- unused_shift_result_ext
- unused_imd_val_q_1
- unused_imd_val_q
- unused_butterfly_result
- unused_invbutterfly_result
- ... and 1 more

**Generated File:** T6_ibex_alu_Covert.sv

---

