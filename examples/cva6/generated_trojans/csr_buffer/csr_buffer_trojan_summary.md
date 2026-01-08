# Trojan Generation Summary

**Module:** csr_buffer
**File:** csr_buffer.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- csr_valid_i
- csr_ready_o
- valid

**Payload Signals (3):**
- csr_valid_i
- csr_ready_o
- valid

**Generated File:** T1_csr_buffer_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- fu_data_t
- csr_addr_o
- csr_address

**Payload Signals (1):**
- fu_data_t

**Generated File:** T2_csr_buffer_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- fu_data_t
- csr_valid_i
- valid

**Payload Signals (3):**
- csr_valid_i
- csr_ready_o
- valid

**Generated File:** T3_csr_buffer_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (6):**
- fu_data_t
- csr_valid_i
- csr_commit_i
- csr_ready_o
- csr_addr_o
- ... and 1 more

**Generated File:** T4_csr_buffer_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (5):**
- csr_valid_i
- csr_commit_i
- csr_ready_o
- csr_addr_o
- csr_address

**Payload Signals (0):**

**Generated File:** T5_csr_buffer_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T6_csr_buffer_Covert.sv

---

