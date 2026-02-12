# Trojan Generation Summary

**Module:** cvxif_issue_register_commit_if_driver
**File:** cvxif_issue_register_commit_if_driver.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (13):**
- issue_ready_i
- issue_valid_o
- x_issue_req_t
- issue_req_o
- commit_valid_o
- ... and 8 more

**Payload Signals (13):**
- issue_ready_i
- issue_valid_o
- x_issue_req_t
- issue_req_o
- commit_valid_o
- ... and 8 more

**Generated File:** T1_cvxif_issue_register_commit_if_driver_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (12):**
- issue_valid_o
- x_issue_req_t
- issue_req_o
- commit_valid_o
- valid_i
- ... and 7 more

**Payload Signals (9):**
- issue_ready_i
- issue_valid_o
- commit_valid_o
- valid_i
- rs_valid_i
- ... and 4 more

**Generated File:** T2_cvxif_issue_register_commit_if_driver_Availability.sv

---

