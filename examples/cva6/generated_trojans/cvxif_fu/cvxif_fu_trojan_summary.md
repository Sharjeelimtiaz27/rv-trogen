# Trojan Generation Summary

**Module:** cvxif_fu
**File:** cvxif_fu.sv
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
- x_valid_i
- result_valid_i
- x_ready_o
- x_valid_o
- result_ready_o

**Payload Signals (5):**
- x_valid_i
- result_valid_i
- x_ready_o
- x_valid_o
- result_ready_o

**Generated File:** T1_cvxif_fu_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- x_valid_i
- result_valid_i
- x_valid_o

**Payload Signals (5):**
- x_valid_i
- result_valid_i
- x_ready_o
- x_valid_o
- result_ready_o

**Generated File:** T2_cvxif_fu_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- x_we_o

**Payload Signals (0):**

**Generated File:** T3_cvxif_fu_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (3):**
- result_valid_i
- x_result_t
- result_ready_o

**Generated File:** T4_cvxif_fu_Integrity.sv

---

