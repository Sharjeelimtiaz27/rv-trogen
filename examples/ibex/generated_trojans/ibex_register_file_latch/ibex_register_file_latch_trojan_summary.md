# Trojan Generation Summary

**Module:** ibex_register_file_latch
**File:** ibex_register_file_latch.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- test_en_i

**Payload Signals (1):**
- test_en_i

**Generated File:** T1_ibex_register_file_latch_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- test_en_i

**Payload Signals (5):**
- raddr_a_i
- raddr_b_i
- waddr_a_i
- data
- oh_raddr_a_err

**Generated File:** T2_ibex_register_file_latch_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- raddr_a_i
- raddr_b_i
- waddr_a_i
- data
- oh_raddr_a_err

**Payload Signals (1):**
- data

**Generated File:** T3_ibex_register_file_latch_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data

**Payload Signals (3):**
- test_en_i
- unused_strobe
- unused_dummy_instr

**Generated File:** T4_ibex_register_file_latch_Covert.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- raddr_a_i
- raddr_b_i
- waddr_a_i
- we_a_i
- oh_raddr_a_err
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T5_ibex_register_file_latch_Privilege.sv

---

### T6: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- data

**Payload Signals (0):**

**Generated File:** T6_ibex_register_file_latch_Availability.sv

---

