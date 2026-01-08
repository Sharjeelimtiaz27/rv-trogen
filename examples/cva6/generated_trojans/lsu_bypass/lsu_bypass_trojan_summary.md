# Trojan Generation Summary

**Module:** lsu_bypass
**File:** lsu_bypass.sv
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
- lsu_req_valid_i
- ready_o
- assignment

**Payload Signals (3):**
- lsu_req_valid_i
- ready_o
- assignment

**Generated File:** T1_lsu_bypass_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- lsu_ctrl_t
- lsu_ctrl_t
- write_pointer_n
- write_pointer

**Payload Signals (2):**
- status_cnt_n
- status_cnt

**Generated File:** T2_lsu_bypass_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- pop_ld_i
- pop_st_i

**Payload Signals (2):**
- write_pointer_n
- write_pointer

**Generated File:** T3_lsu_bypass_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- lsu_req_valid_i
- pop_ld_i
- pop_st_i

**Payload Signals (2):**
- lsu_req_valid_i
- ready_o

**Generated File:** T4_lsu_bypass_Availability.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- lsu_ctrl_t
- lsu_ctrl_t

**Payload Signals (0):**

**Generated File:** T5_lsu_bypass_Leak.sv

---

