# Trojan Generation Summary

**Module:** is
**File:** cva6_tlb.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- s_st_enbl_i
- g_st_enbl_i
- valid
- en

**Payload Signals (4):**
- s_st_enbl_i
- g_st_enbl_i
- valid
- en

**Generated File:** T1_is_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- valid

**Payload Signals (1):**
- valid

**Generated File:** T2_is_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- gpaddr_to_be_flushed_is0
- flush_addr_napot_match
- flush_addr_matches

**Generated File:** T3_is_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- gpaddr_to_be_flushed_is0
- flush_addr_napot_match
- flush_addr_matches

**Payload Signals (0):**

**Generated File:** T4_is_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- gpaddr_to_be_flushed_is0
- flush_addr_napot_match
- flush_addr_matches

**Payload Signals (0):**

**Generated File:** T5_is_Integrity.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- lu_access_i

**Payload Signals (0):**

**Generated File:** T6_is_Covert.sv

---

