# Trojan Generation Summary

**Module:** cva6
**File:** cva6.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (70):**
- debug_req_i
- cvxif_req_t
- noc_req_t
- valid
- fetch_valid
- ... and 65 more

**Payload Signals (68):**
- debug_req_i
- cvxif_req_t
- noc_req_t
- valid
- fetch_valid
- ... and 63 more

**Generated File:** T1_cva6_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (26):**
- debug_req_i
- mode
- halt_acc_ctrl
- debug_mode
- debug_from_trigger
- ... and 21 more

**Payload Signals (37):**
- data_req
- data_we
- data_size
- data_gnt
- data_rvalid
- ... and 32 more

**Generated File:** T2_cva6_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (53):**
- mode
- data_we
- halt_acc_ctrl
- csr_hs_ld_st_inst_ex
- x_we_ex_id
- ... and 48 more

**Payload Signals (4):**
- mode
- dirty_fp_state
- dirty_v_state
- debug_mode

**Generated File:** T3_cva6_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (8):**
- data_req
- data_we
- data_size
- data_gnt
- data_rvalid
- ... and 3 more

**Payload Signals (9):**
- data_req
- data_we
- data_size
- data_gnt
- data_rvalid
- ... and 4 more

**Generated File:** T4_cva6_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (38):**
- debug_req_i
- cvxif_req_t
- noc_req_t
- valid
- fetch_valid
- ... and 33 more

**Payload Signals (46):**
- valid
- fetch_valid
- ready
- ex_valid
- tag_valid
- ... and 41 more

**Generated File:** T5_cva6_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- fetch_valid
- fetch_req
- data_req
- data_we
- data_size
- ... and 3 more

**Payload Signals (4):**
- debug_req_i
- debug_mode
- debug_from_trigger
- set_debug_pc

**Generated File:** T6_cva6_Covert.sv

---

