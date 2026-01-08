# Trojan Generation Summary

**Module:** is
**File:** ibex_compressed_decoder.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- valid_i
- id_in_ready_i
- unused_valid
- unused_id_in_ready

**Payload Signals (4):**
- valid_i
- id_in_ready_i
- unused_valid
- unused_id_in_ready

**Generated File:** T1_is_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- cm_rlist_top_reg
- cm_pop_load_reg

**Payload Signals (1):**
- cm_push_store_reg

**Generated File:** T2_is_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- valid_i
- unused_valid
- cm_rlist_top_reg
- cm_pop_load_reg

**Payload Signals (7):**
- valid_i
- id_in_ready_i
- unused_valid
- unused_id_in_ready
- cm_stack_adj_base
- ... and 2 more

**Generated File:** T3_is_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- cm_pop_load_reg

**Payload Signals (3):**
- unused_valid
- unused_id_in_ready
- _unused

**Generated File:** T4_is_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- cm_rlist_top_reg
- cm_push_store_reg
- cm_pop_load_reg
- cm_mv_reg

**Generated File:** T5_is_Leak.sv

---

