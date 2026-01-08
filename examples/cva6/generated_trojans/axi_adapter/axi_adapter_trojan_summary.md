# Trojan Generation Summary

**Module:** axi_adapter
**File:** axi_adapter.sv
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
- req_i
- valid_o
- critical_word_valid_o
- axi_req_t

**Payload Signals (4):**
- req_i
- valid_o
- critical_word_valid_o
- axi_req_t

**Generated File:** T1_axi_adapter_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- amo_returns_data

**Payload Signals (2):**
- any_outstanding_aw
- amo_returns_data

**Generated File:** T2_axi_adapter_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- req_i
- valid_o
- critical_word_valid_o
- axi_req_t
- amo_returns_data

**Payload Signals (2):**
- valid_o
- critical_word_valid_o

**Generated File:** T3_axi_adapter_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- amo_returns_data

**Generated File:** T4_axi_adapter_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- we_i

**Payload Signals (0):**

**Generated File:** T5_axi_adapter_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- amo_returns_data
- is_load

**Payload Signals (0):**

**Generated File:** T6_axi_adapter_Covert.sv

---

