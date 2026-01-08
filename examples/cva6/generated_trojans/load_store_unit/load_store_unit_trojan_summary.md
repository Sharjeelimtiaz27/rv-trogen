# Trojan Generation Summary

**Module:** load_store_unit
**File:** load_store_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (29):**
- stall_st_pending_i
- amo_valid_commit_i
- lsu_valid_i
- enable_translation_i
- enable_g_translation_i
- ... and 24 more

**Payload Signals (29):**
- stall_st_pending_i
- amo_valid_commit_i
- lsu_valid_i
- enable_translation_i
- enable_g_translation_i
- ... and 24 more

**Generated File:** T1_load_store_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- lsu_ctrl_t

**Payload Signals (3):**
- fu_data_t
- csr_hs_ld_st_inst_o
- data_misaligned

**Generated File:** T2_load_store_unit_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- fu_data_t
- data_misaligned
- pop_st
- pop_ld

**Payload Signals (4):**
- fu_data_t
- store_valid_o
- data_misaligned
- store_buffer_empty

**Generated File:** T3_load_store_unit_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (25):**
- amo_valid_commit_i
- fu_data_t
- lsu_valid_i
- acc_mmu_req_t
- request
- ... and 20 more

**Payload Signals (14):**
- stall_st_pending_i
- amo_valid_commit_i
- lsu_valid_i
- lsu_ready_o
- load_valid_o
- ... and 9 more

**Generated File:** T4_load_store_unit_Availability.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- csr_hs_ld_st_inst_o
- lsu_ctrl_t

**Payload Signals (0):**

**Generated File:** T5_load_store_unit_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- fu_data_t
- load_valid_o
- data_misaligned

**Payload Signals (0):**

**Generated File:** T6_load_store_unit_Covert.sv

---

