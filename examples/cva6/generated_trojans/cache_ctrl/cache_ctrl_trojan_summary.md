# Trojan Generation Summary

**Module:** cache_ctrl
**File:** cache_ctrl.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- dcache_req_i_t
- active_serving_i
- critical_word_valid_i
- bypass_valid_i
- dcache_req_o_t
- ... and 2 more

**Payload Signals (7):**
- dcache_req_i_t
- active_serving_i
- critical_word_valid_i
- bypass_valid_i
- dcache_req_o_t
- ... and 2 more

**Generated File:** T1_cache_ctrl_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- bypass_data_i
- mshr_addr_matches_i
- mshr_addr_o

**Payload Signals (1):**
- bypass_data_i

**Generated File:** T2_cache_ctrl_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- dcache_req_i_t
- critical_word_valid_i
- bypass_valid_i
- bypass_data_i
- dcache_req_o_t
- ... and 1 more

**Payload Signals (3):**
- critical_word_valid_i
- bypass_valid_i
- busy_o

**Generated File:** T3_cache_ctrl_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- bypass_data_i

**Payload Signals (1):**
- busy_o

**Generated File:** T4_cache_ctrl_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- bypass_data_i
- mshr_addr_matches_i
- mshr_addr_o

**Generated File:** T5_cache_ctrl_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- mshr_addr_matches_i
- we_o
- mshr_addr_o
- we

**Payload Signals (0):**

**Generated File:** T6_cache_ctrl_Privilege.sv

---

