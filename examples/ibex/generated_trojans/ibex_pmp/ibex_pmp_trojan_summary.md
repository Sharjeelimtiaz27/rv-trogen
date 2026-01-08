# Trojan Generation Summary

**Module:** ibex_pmp
**File:** ibex_pmp.sv
**Type:** Combinational
**Total Candidates:** 6

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (3):**
- csr_pmp_mseccfg_mml
- csr_pmp_mseccfg_mmwp
- unused_csr_pmp_mseccfg_rlb

**Generated File:** T1_ibex_pmp_Leak.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- access_fault_check
- access_fail

**Payload Signals (4):**
- debug_mode_i
- unused_cfg
- unused_sigs
- unused_csr_pmp_mseccfg_rlb

**Generated File:** T2_ibex_pmp_Covert.sv

---

### T3: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- pmp_req_err_o

**Payload Signals (1):**
- pmp_req_err_o

**Generated File:** T3_ibex_pmp_DoS.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- debug_mode_i
- csr_pmp_mseccfg_mml
- csr_pmp_mseccfg_mmwp
- unused_csr_pmp_mseccfg_rlb

**Payload Signals (2):**
- debug_mode_i
- permission_check

**Generated File:** T4_ibex_pmp_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- result

**Generated File:** T5_ibex_pmp_Integrity.sv

---

### T6: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.40
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- pmp_req_err_o

**Payload Signals (0):**

**Generated File:** T6_ibex_pmp_Availability.sv

---

