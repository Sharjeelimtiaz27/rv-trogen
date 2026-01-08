# Trojan Generation Summary

**Module:** multiplier
**File:** multiplier.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- mult_valid_i
- mult_valid_o
- mult_valid_q
- mult_valid

**Payload Signals (4):**
- mult_valid_i
- mult_valid_o
- mult_valid_q
- mult_valid

**Generated File:** T1_multiplier_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- clmul_rmode

**Payload Signals (1):**
- clmul_rmode

**Generated File:** T2_multiplier_Privilege.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- mult_valid_i
- fu_op
- mult_valid_o
- mult_valid_q
- mult_valid

**Payload Signals (4):**
- mult_valid_i
- mult_valid_o
- mult_valid_q
- mult_valid

**Generated File:** T3_multiplier_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- clmul_rmode

**Payload Signals (0):**

**Generated File:** T4_multiplier_Leak.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- fu_op

**Payload Signals (0):**

**Generated File:** T5_multiplier_Integrity.sv

---

