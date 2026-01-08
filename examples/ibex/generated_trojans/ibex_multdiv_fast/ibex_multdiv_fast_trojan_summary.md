# Trojan Generation Summary

**Module:** ibex_multdiv_fast
**File:** ibex_multdiv_fast.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (14):**
- mult_en_i
- div_en_i
- multdiv_ready_id_i
- valid_o
- mult_valid
- ... and 9 more

**Payload Signals (14):**
- mult_en_i
- div_en_i
- multdiv_ready_id_i
- valid_o
- mult_valid
- ... and 9 more

**Generated File:** T1_ibex_multdiv_fast_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (7):**
- signed_mode_i
- alu_adder_ext_i
- mac_res_ext
- next_remainder
- next_quotient
- ... and 2 more

**Payload Signals (1):**
- data_ind_timing_i

**Generated File:** T2_ibex_multdiv_fast_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- signed_mode_i
- imd_val_we_o

**Payload Signals (1):**
- signed_mode_i

**Generated File:** T3_ibex_multdiv_fast_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (19):**
- mult_sel_i
- div_sel_i
- op_a_i
- op_b_i
- data_ind_timing_i
- ... and 14 more

**Payload Signals (2):**
- data_ind_timing_i
- multdiv_result_o

**Generated File:** T4_ibex_multdiv_fast_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (19):**
- op_a_i
- op_b_i
- data_ind_timing_i
- alu_operand_a_o
- alu_operand_b_o
- ... and 14 more

**Payload Signals (4):**
- multdiv_ready_id_i
- valid_o
- mult_valid
- div_valid

**Generated File:** T5_ibex_multdiv_fast_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data_ind_timing_i

**Payload Signals (8):**
- data_ind_timing_i
- unused_mult_sel_i
- unused_imd_val
- unused_mac_res_ext
- unused_mult1_res_uns
- ... and 3 more

**Generated File:** T6_ibex_multdiv_fast_Covert.sv

---

