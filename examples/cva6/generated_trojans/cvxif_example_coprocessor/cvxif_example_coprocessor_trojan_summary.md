# Trojan Generation Summary

**Module:** cvxif_example_coprocessor
**File:** cvxif_example_coprocessor.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- cvxif_req_t
- compressed_valid
- issue_valid
- register_valid
- alu_valid

**Payload Signals (5):**
- cvxif_req_t
- compressed_valid
- issue_valid
- register_valid
- alu_valid

**Generated File:** T1_cvxif_example_coprocessor_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- cvxif_req_t
- compressed_valid
- issue_valid
- register_valid
- alu_valid

**Payload Signals (4):**
- compressed_valid
- issue_valid
- register_valid
- alu_valid

**Generated File:** T2_cvxif_example_coprocessor_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- register_valid

**Generated File:** T3_cvxif_example_coprocessor_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- we

**Payload Signals (0):**

**Generated File:** T4_cvxif_example_coprocessor_Privilege.sv

---

