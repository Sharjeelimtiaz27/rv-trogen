# Trojan Generation Summary

**Module:** mult
**File:** mult.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- mult_valid_i
- silencing
- mult_valid_o
- mult_ready_o
- mul_valid
- ... and 4 more

**Payload Signals (9):**
- mult_valid_i
- silencing
- mult_valid_o
- mult_ready_o
- mul_valid
- ... and 4 more

**Generated File:** T1_mult_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (6):**
- fu_data_t
- operands
- operands
- div_valid_op
- mul_valid_op
- ... and 1 more

**Payload Signals (1):**
- fu_data_t

**Generated File:** T2_mult_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- fu_data_t
- mult_valid_i
- operands
- operands
- mult_valid_o
- ... and 5 more

**Payload Signals (8):**
- mult_valid_i
- mult_valid_o
- mult_ready_o
- mul_valid
- div_valid
- ... and 3 more

**Generated File:** T3_mult_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- fu_data_t

**Generated File:** T4_mult_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T5_mult_Covert.sv

---

