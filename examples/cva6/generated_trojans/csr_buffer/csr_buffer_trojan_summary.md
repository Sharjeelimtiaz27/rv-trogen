# Trojan Generation Summary

**Module:** csr_buffer
**File:** csr_buffer.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- csr_ready_o
- csr_valid_i
- csr_ready_o
- csr_valid_i
- valid

**Payload Signals (5):**
- csr_ready_o
- csr_valid_i
- csr_ready_o
- csr_valid_i
- valid

**Generated File:** T1_csr_buffer_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- csr_ready_o
- csr_valid_i
- csr_result_o
- csr_commit_i
- csr_addr_o
- ... and 5 more

**Payload Signals (13):**
- fu_data_t
- fu_data_i
- csr_ready_o
- csr_valid_i
- csr_result_o
- ... and 8 more

**Generated File:** T2_csr_buffer_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- fu_data_t
- fu_data_i
- csr_addr_o
- csr_addr_o
- csr_address

**Payload Signals (4):**
- fu_data_t
- fu_data_i
- csr_result_o
- csr_result_o

**Generated File:** T3_csr_buffer_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- csr_valid_i
- csr_valid_i
- valid

**Payload Signals (5):**
- csr_ready_o
- csr_valid_i
- csr_ready_o
- csr_valid_i
- valid

**Generated File:** T4_csr_buffer_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fu_data_t
- fu_data_i

**Payload Signals (9):**
- fu_data_t
- fu_data_i
- csr_ready_o
- csr_valid_i
- csr_result_o
- ... and 4 more

**Generated File:** T5_csr_buffer_Covert.sv

---

