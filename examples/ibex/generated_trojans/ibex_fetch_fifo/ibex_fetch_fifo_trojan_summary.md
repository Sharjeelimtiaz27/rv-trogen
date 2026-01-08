# Trojan Generation Summary

**Module:** ibex_fetch_fifo
**File:** ibex_fetch_fifo.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- in_valid_i
- out_ready_i
- out_valid_o
- valid
- instr_addr_en

**Payload Signals (5):**
- in_valid_i
- out_ready_i
- out_valid_o
- valid
- instr_addr_en

**Generated File:** T1_ibex_fetch_fifo_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- instr_addr_next

**Payload Signals (11):**
- in_addr_i
- in_rdata_i
- out_addr_o
- out_rdata_o
- data
- ... and 6 more

**Generated File:** T2_ibex_fetch_fifo_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- in_addr_i
- in_rdata_i
- out_addr_o
- out_rdata_o
- data
- ... and 7 more

**Payload Signals (9):**
- in_rdata_i
- out_ready_i
- out_valid_o
- out_addr_o
- out_rdata_o
- ... and 4 more

**Generated File:** T3_ibex_fetch_fifo_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- in_valid_i
- in_rdata_i
- out_valid_o
- out_rdata_o
- data
- ... and 3 more

**Payload Signals (4):**
- in_valid_i
- out_ready_i
- out_valid_o
- valid

**Generated File:** T4_ibex_fetch_fifo_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- in_rdata_i
- out_rdata_o
- data
- rdata

**Payload Signals (1):**
- unused_addr_in

**Generated File:** T5_ibex_fetch_fifo_Covert.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (7):**
- in_addr_i
- out_addr_o
- addr_incr_two
- instr_addr_next
- instr_addr_d
- ... and 2 more

**Payload Signals (0):**

**Generated File:** T6_ibex_fetch_fifo_Privilege.sv

---

