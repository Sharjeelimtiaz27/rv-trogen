# Trojan Generation Summary

**Module:** copro_alu
**File:** copro_alu.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- valid_o
- valid_n

**Payload Signals (2):**
- valid_o
- valid_n

**Generated File:** T1_copro_alu_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- opcode_t
- valid_o
- valid_n

**Payload Signals (2):**
- valid_o
- valid_n

**Generated File:** T2_copro_alu_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- registers_t

**Generated File:** T3_copro_alu_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- we_o
- we_n

**Payload Signals (0):**

**Generated File:** T4_copro_alu_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- opcode_t

**Payload Signals (0):**

**Generated File:** T5_copro_alu_Integrity.sv

---

