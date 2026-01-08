# Trojan Generation Summary

**Module:** aes
**File:** aes.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (25):**
- aes32esi_gen
- aes32esmi_gen
- aes64es_gen
- aes64esm_gen
- aes32dsi_gen
- ... and 20 more

**Payload Signals (25):**
- aes32esi_gen
- aes32esmi_gen
- aes64es_gen
- aes64esm_gen
- aes32dsi_gen
- ... and 20 more

**Generated File:** T1_aes_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (1):**
- fu_data_t

**Generated File:** T2_aes_Integrity.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- fu_data_t

**Generated File:** T3_aes_Leak.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T4_aes_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fu_data_t

**Payload Signals (0):**

**Generated File:** T5_aes_Covert.sv

---

