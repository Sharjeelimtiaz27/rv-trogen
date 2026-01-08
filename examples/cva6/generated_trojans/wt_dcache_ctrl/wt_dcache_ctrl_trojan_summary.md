# Trojan Generation Summary

**Module:** wt_dcache_ctrl
**File:** wt_dcache_ctrl.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- cache_en_i
- dcache_req_i_t
- dcache_req_o_t
- miss_req_o
- rd_req_o

**Payload Signals (5):**
- cache_en_i
- dcache_req_i_t
- dcache_req_o_t
- miss_req_o
- rd_req_o

**Generated File:** T1_wt_dcache_ctrl_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- data_size_d

**Payload Signals (1):**
- data_size_d

**Generated File:** T2_wt_dcache_ctrl_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- dcache_req_i_t
- dcache_req_o_t
- miss_req_o
- rd_req_o
- data_size_d

**Payload Signals (2):**
- miss_ack_i
- rd_ack_i

**Generated File:** T3_wt_dcache_ctrl_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- data_size_d

**Generated File:** T4_wt_dcache_ctrl_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- miss_we_o

**Payload Signals (0):**

**Generated File:** T5_wt_dcache_ctrl_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data_size_d

**Payload Signals (0):**

**Generated File:** T6_wt_dcache_ctrl_Covert.sv

---

