# Trojan Generation Summary

**Module:** load_unit
**File:** load_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- valid_i
- dcache_req_o_t
- valid_o
- translation_req_o
- dcache_req_i_t
- ... and 1 more

**Payload Signals (6):**
- valid_i
- dcache_req_o_t
- valid_o
- translation_req_o
- dcache_req_i_t
- ... and 1 more

**Generated File:** T1_load_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- lsu_ctrl_t

**Payload Signals (3):**
- address
- paddr_ni
- rdata_sign_bit

**Generated File:** T2_load_unit_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- pop_ld_o
- address
- paddr_ni
- rdata_sign_bit

**Payload Signals (3):**
- store_buffer_empty_i
- inflight_stores
- rdata_sign_bit

**Generated File:** T3_load_unit_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- valid_i
- dcache_req_o_t
- pop_ld_o
- valid_o
- translation_req_o
- ... and 3 more

**Payload Signals (3):**
- valid_i
- valid_o
- stall_ni

**Generated File:** T4_load_unit_Availability.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- lsu_ctrl_t
- address
- paddr_ni

**Payload Signals (0):**

**Generated File:** T5_load_unit_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- rdata_sign_bit

**Payload Signals (0):**

**Generated File:** T6_load_unit_Covert.sv

---

