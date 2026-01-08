# Trojan Generation Summary

**Module:** ibex_prefetch_buffer
**File:** ibex_prefetch_buffer.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (12):**
- req_i
- ready_i
- instr_rvalid_i
- valid_o
- instr_req_o
- ... and 7 more

**Payload Signals (12):**
- req_i
- ready_i
- instr_rvalid_i
- valid_o
- instr_req_o
- ... and 7 more

**Generated File:** T1_ibex_prefetch_buffer_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (11):**
- addr_i
- instr_rdata_i
- rdata_o
- addr_o
- instr_addr_o
- ... and 6 more

**Payload Signals (4):**
- instr_rdata_i
- rdata_o
- stored_addr_d
- stored_addr_en

**Generated File:** T2_ibex_prefetch_buffer_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- req_i
- instr_rdata_i
- instr_rvalid_i
- valid_o
- rdata_o
- ... and 5 more

**Payload Signals (8):**
- ready_i
- instr_rvalid_i
- valid_o
- busy_o
- valid_new_req
- ... and 3 more

**Generated File:** T3_ibex_prefetch_buffer_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- instr_rdata_i
- rdata_o
- fetch_addr_d
- fetch_addr_en

**Payload Signals (1):**
- busy_o

**Generated File:** T4_ibex_prefetch_buffer_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (11):**
- addr_i
- instr_rdata_i
- rdata_o
- addr_o
- instr_addr_o
- ... and 6 more

**Generated File:** T5_ibex_prefetch_buffer_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (9):**
- addr_i
- addr_o
- instr_addr_o
- stored_addr_d
- stored_addr_en
- ... and 4 more

**Payload Signals (0):**

**Generated File:** T6_ibex_prefetch_buffer_Privilege.sv

---

