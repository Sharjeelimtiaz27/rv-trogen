# Trojan Generation Summary

**Module:** pmp_data_if
**File:** pmp_data_if.sv
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
- icache_areq_t
- lsu_valid_i
- icache_areq_t
- lsu_valid_o

**Payload Signals (4):**
- icache_areq_t
- lsu_valid_i
- icache_areq_t
- lsu_valid_o

**Generated File:** T1_pmp_data_if_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- data_allow_o
- no_locked_data

**Payload Signals (3):**
- lsu_is_store_i
- data_allow_o
- no_locked_data

**Generated File:** T2_pmp_data_if_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- icache_areq_t
- lsu_valid_i
- icache_areq_t
- lsu_valid_o
- data_allow_o
- ... and 1 more

**Payload Signals (2):**
- lsu_valid_i
- lsu_valid_o

**Generated File:** T3_pmp_data_if_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- match_any_execute_region
- data_allow_o
- no_locked_data

**Generated File:** T4_pmp_data_if_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- data_allow_o
- no_locked_data

**Payload Signals (0):**

**Generated File:** T5_pmp_data_if_Covert.sv

---

