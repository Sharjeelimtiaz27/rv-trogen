# Trojan Generation Summary

**Module:** ibex_dummy_instr
**File:** ibex_dummy_instr.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- dummy_instr_en_i
- dummy_instr_seed_en_i
- fetch_valid_i
- id_in_ready_i
- dummy_cnt_en
- ... and 1 more

**Payload Signals (6):**
- dummy_instr_en_i
- dummy_instr_seed_en_i
- fetch_valid_i
- id_in_ready_i
- dummy_cnt_en
- ... and 1 more

**Generated File:** T1_ibex_dummy_instr_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- dummy_instr_data_o
- dummy_opcode

**Payload Signals (1):**
- dummy_instr_data_o

**Generated File:** T2_ibex_dummy_instr_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- fetch_valid_i
- dummy_instr_data_o
- dummy_opcode

**Payload Signals (2):**
- fetch_valid_i
- id_in_ready_i

**Generated File:** T3_ibex_dummy_instr_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- dummy_instr_data_o

**Generated File:** T4_ibex_dummy_instr_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fetch_valid_i
- dummy_instr_data_o

**Payload Signals (0):**

**Generated File:** T5_ibex_dummy_instr_Covert.sv

---

