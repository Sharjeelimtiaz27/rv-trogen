# Trojan Generation Summary

**Module:** fpu_wrap
**File:** fpu_wrap.sv
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
- fpu_valid_i
- valid
- fpu_ready_o
- fpu_valid_o
- fpu_early_valid_o
- ... and 2 more

**Payload Signals (7):**
- fpu_valid_i
- valid
- fpu_ready_o
- fpu_valid_o
- fpu_early_valid_o
- ... and 2 more

**Generated File:** T1_fpu_wrap_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- fu_data_t
- data
- fpu_op_mod_d
- fpu_vec_op_d
- hold_inputs

**Payload Signals (3):**
- fu_data_t
- data
- fpu_out_ready

**Generated File:** T2_fpu_wrap_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- fpu_valid_i
- fu_data_t
- valid
- data
- fpu_valid_o
- ... and 3 more

**Payload Signals (7):**
- fpu_valid_i
- valid
- fpu_ready_o
- fpu_valid_o
- fpu_early_valid_o
- ... and 2 more

**Generated File:** T3_fpu_wrap_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- fu_data_t
- data

**Generated File:** T4_fpu_wrap_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (0):**

**Payload Signals (1):**
- fpu_status

**Generated File:** T5_fpu_wrap_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- fu_data_t
- data
- hold_inputs

**Payload Signals (0):**

**Generated File:** T6_fpu_wrap_Covert.sv

---

