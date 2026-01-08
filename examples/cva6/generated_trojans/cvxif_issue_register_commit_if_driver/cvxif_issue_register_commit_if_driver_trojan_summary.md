# Trojan Generation Summary

**Module:** cvxif_issue_register_commit_if_driver
**File:** cvxif_issue_register_commit_if_driver.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- issue_ready_i
- register_ready_i
- valid_i
- issue_valid_o
- x_issue_req_t
- ... and 2 more

**Payload Signals (7):**
- issue_ready_i
- register_ready_i
- valid_i
- issue_valid_o
- x_issue_req_t
- ... and 2 more

**Generated File:** T1_cvxif_issue_register_commit_if_driver_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- valid_i
- issue_valid_o
- x_issue_req_t
- register_valid_o
- commit_valid_o

**Payload Signals (6):**
- issue_ready_i
- register_ready_i
- valid_i
- issue_valid_o
- register_valid_o
- ... and 1 more

**Generated File:** T2_cvxif_issue_register_commit_if_driver_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- register_ready_i
- register_valid_o
- x_register_t

**Generated File:** T3_cvxif_issue_register_commit_if_driver_Leak.sv

---

