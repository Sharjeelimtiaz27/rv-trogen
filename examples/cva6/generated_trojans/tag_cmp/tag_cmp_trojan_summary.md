# Trojan Generation Summary

**Module:** tag_cmp
**File:** tag_cmp.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- l_data_t
- l_data_t
- l_data_t
- l_data_t

**Payload Signals (4):**
- l_data_t
- l_data_t
- l_data_t
- l_data_t

**Generated File:** T1_tag_cmp_Integrity.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- l_data_t
- l_data_t
- l_data_t
- l_data_t

**Generated File:** T2_tag_cmp_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- we_o

**Payload Signals (0):**

**Generated File:** T3_tag_cmp_Privilege.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- l_data_t
- l_data_t
- l_data_t
- l_data_t

**Payload Signals (0):**

**Generated File:** T4_tag_cmp_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- l_data_t
- l_data_t
- l_data_t
- l_data_t

**Payload Signals (0):**

**Generated File:** T5_tag_cmp_Covert.sv

---

