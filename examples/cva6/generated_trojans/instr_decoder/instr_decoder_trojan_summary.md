# Trojan Generation Summary

**Module:** instr_decoder
**File:** instr_decoder.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- issue_valid_i
- x_issue_req_t
- register_valid_i
- issue_ready_o
- rs1_ready
- ... and 2 more

**Payload Signals (7):**
- issue_valid_i
- x_issue_req_t
- register_valid_i
- issue_ready_o
- rs1_ready
- ... and 2 more

**Generated File:** T1_instr_decoder_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- issue_valid_i
- x_issue_req_t
- register_valid_i
- opcode_t

**Payload Signals (6):**
- issue_valid_i
- register_valid_i
- issue_ready_o
- rs1_ready
- rs2_ready
- ... and 1 more

**Generated File:** T2_instr_decoder_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- register_valid_i
- x_register_t
- registers_t

**Generated File:** T3_instr_decoder_Leak.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- opcode_t

**Payload Signals (0):**

**Generated File:** T4_instr_decoder_Integrity.sv

---

