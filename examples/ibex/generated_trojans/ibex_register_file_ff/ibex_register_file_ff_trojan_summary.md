# Trojan Generation Summary

**Module:** ibex_register_file_ff
**File:** ibex_register_file_ff.sv
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
- test_en_i
- unused_test_en

**Payload Signals (2):**
- test_en_i
- unused_test_en

**Generated File:** T1_ibex_register_file_ff_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- test_en_i
- unused_test_en

**Payload Signals (4):**
- raddr_a_i
- raddr_b_i
- waddr_a_i
- oh_raddr_a_err

**Generated File:** T2_ibex_register_file_ff_Leak.sv

---

### T3: Privilege - Privilege Escalation

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

**Generated File:** T3_ibex_register_file_ff_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- raddr_a_i
- raddr_b_i
- waddr_a_i
- oh_raddr_a_err

**Payload Signals (0):**

**Generated File:** T4_ibex_register_file_ff_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (4):**
- test_en_i
- unused_strobe
- unused_dummy_instr
- unused_test_en

**Generated File:** T5_ibex_register_file_ff_Covert.sv

---

