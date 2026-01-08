# Trojan Generation Summary

**Module:** macro_decoder
**File:** macro_decoder.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- popretz_inst_q

**Payload Signals (3):**
- issue_ack_i
- fetch_stall_o
- stack_adj

**Generated File:** T1_macro_decoder_Availability.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- reg_numbers
- xreg1
- offset_reg
- instr_o_reg

**Generated File:** T2_macro_decoder_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- popretz_inst_q

**Payload Signals (0):**

**Generated File:** T3_macro_decoder_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fetch_stall_o

**Payload Signals (0):**

**Generated File:** T4_macro_decoder_Covert.sv

---

