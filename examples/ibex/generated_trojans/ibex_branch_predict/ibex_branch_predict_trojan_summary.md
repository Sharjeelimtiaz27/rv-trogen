# Trojan Generation Summary

**Module:** ibex_branch_predict
**File:** ibex_branch_predict.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- fetch_valid_i
- predict_branch_taken_o
- instr_b_taken

**Payload Signals (3):**
- fetch_valid_i
- predict_branch_taken_o
- instr_b_taken

**Generated File:** T1_ibex_branch_predict_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- fetch_rdata_i

**Payload Signals (1):**
- fetch_rdata_i

**Generated File:** T2_ibex_branch_predict_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- fetch_rdata_i
- fetch_valid_i

**Payload Signals (1):**
- fetch_valid_i

**Generated File:** T3_ibex_branch_predict_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- fetch_rdata_i

**Generated File:** T4_ibex_branch_predict_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- fetch_rdata_i
- fetch_pc_i
- fetch_valid_i

**Payload Signals (0):**

**Generated File:** T5_ibex_branch_predict_Covert.sv

---

