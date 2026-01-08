# Trojan Generation Summary

**Module:** ibex_multdiv_slow
**File:** ibex_multdiv_slow.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- mult_en_i
- div_en_i
- multdiv_ready_id_i
- valid_o
- next_quotient
- ... and 1 more

**Payload Signals (6):**
- mult_en_i
- div_en_i
- multdiv_ready_id_i
- valid_o
- next_quotient
- ... and 1 more

**Generated File:** T1_ibex_multdiv_slow_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- signed_mode_i
- alu_adder_ext_i
- op_a_ext
- next_quotient
- next_remainder

**Payload Signals (1):**
- data_ind_timing_i

**Generated File:** T2_ibex_multdiv_slow_Leak.sv

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

**Generated File:** T3_ibex_multdiv_slow_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (13):**
- mult_sel_i
- div_sel_i
- op_a_i
- op_b_i
- data_ind_timing_i
- ... and 8 more

**Payload Signals (2):**
- data_ind_timing_i
- multdiv_result_o

**Generated File:** T4_ibex_multdiv_slow_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (12):**
- op_a_i
- op_b_i
- data_ind_timing_i
- operands
- alu_operand_a_o
- ... and 7 more

**Payload Signals (2):**
- multdiv_ready_id_i
- valid_o

**Generated File:** T5_ibex_multdiv_slow_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data_ind_timing_i

**Payload Signals (3):**
- data_ind_timing_i
- unused_imd_val0
- unused_sva_fsm_idle

**Generated File:** T6_ibex_multdiv_slow_Covert.sv

---

