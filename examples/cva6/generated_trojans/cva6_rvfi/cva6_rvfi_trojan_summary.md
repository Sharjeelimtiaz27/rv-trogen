# Trojan Generation Summary

**Module:** cva6_rvfi
**File:** cva6_rvfi.sv
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
- ex_commit_valid
- branch_valid_iti
- is_taken_iti
- valid
- branch_valid
- ... and 1 more

**Payload Signals (6):**
- ex_commit_valid
- branch_valid_iti
- is_taken_iti
- valid
- branch_valid
- ... and 1 more

**Generated File:** T1_cva6_rvfi_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- operand_a_sext
- operand_a_zext
- SMODE_STATUS_READ_MASK
- debug_mode

**Payload Signals (1):**
- rvfi_csr_t

**Generated File:** T2_cva6_rvfi_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- rvfi_csr_t
- SMODE_STATUS_READ_MASK
- debug_mode

**Payload Signals (2):**
- SMODE_STATUS_READ_MASK
- debug_mode

**Generated File:** T3_cva6_rvfi_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- fu_op
- is_word_op
- operand_a_sext
- operand_a_zext
- adder_operand_a

**Payload Signals (1):**
- result64

**Generated File:** T4_cva6_rvfi_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (9):**
- fu_op
- is_word_op
- operand_a_sext
- operand_a_zext
- adder_operand_a
- ... and 4 more

**Payload Signals (4):**
- ex_commit_valid
- branch_valid_iti
- valid
- branch_valid

**Generated File:** T5_cva6_rvfi_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- debug_mode

**Generated File:** T6_cva6_rvfi_Covert.sv

---

