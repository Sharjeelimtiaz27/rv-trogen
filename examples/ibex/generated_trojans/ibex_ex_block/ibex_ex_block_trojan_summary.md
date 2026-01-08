# Trojan Generation Summary

**Module:** ibex_ex_block
**File:** ibex_ex_block.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- mult_en_i
- div_en_i
- multdiv_ready_id_i
- ex_valid_o
- multdiv_valid

**Payload Signals (5):**
- mult_en_i
- div_en_i
- multdiv_ready_id_i
- ex_valid_o
- multdiv_valid

**Generated File:** T1_ibex_ex_block_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- multdiv_signed_mode_i
- alu_adder_result_ext

**Payload Signals (1):**
- data_ind_timing_i

**Generated File:** T2_ibex_ex_block_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- multdiv_signed_mode_i
- imd_val_we_o

**Payload Signals (1):**
- multdiv_signed_mode_i

**Generated File:** T3_ibex_ex_block_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- alu_operand_a_i
- alu_operand_b_i
- bt_a_operand_i
- bt_b_operand_i
- mult_sel_i
- ... and 7 more

**Payload Signals (8):**
- data_ind_timing_i
- alu_adder_result_ex_o
- result_ex_o
- alu_result
- alu_adder_result_ext
- ... and 3 more

**Generated File:** T4_ibex_ex_block_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (11):**
- alu_operand_a_i
- alu_operand_b_i
- bt_a_operand_i
- bt_b_operand_i
- multdiv_operand_a_i
- ... and 6 more

**Payload Signals (3):**
- multdiv_ready_id_i
- ex_valid_o
- multdiv_valid

**Generated File:** T5_ibex_ex_block_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data_ind_timing_i

**Payload Signals (4):**
- data_ind_timing_i
- unused_bt_carry
- unused_bt_a_operand
- unused_sva_multdiv_fsm_idle

**Generated File:** T6_ibex_ex_block_Covert.sv

---

