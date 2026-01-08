# Trojan Generation Summary

**Module:** serdiv
**File:** serdiv.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- a_reg_en

**Payload Signals (1):**
- a_reg_en

**Generated File:** T1_serdiv_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (6):**
- opcode_i
- operands
- op_a_sign
- op_b_zero
- op_b_neg_one
- ... and 1 more

**Payload Signals (2):**
- out_rdy_i
- out_vld_o

**Generated File:** T2_serdiv_Integrity.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- a_reg_en

**Generated File:** T3_serdiv_Leak.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- opcode_i
- operands
- op_a_sign
- op_b_zero
- op_b_neg_one

**Payload Signals (0):**

**Generated File:** T4_serdiv_Availability.sv

---

