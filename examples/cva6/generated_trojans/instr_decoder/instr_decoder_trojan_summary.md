# Trojan Generation Summary

**Module:** instr_decoder
**File:** instr_decoder.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- issue_valid_i
- x_issue_req_t
- issue_req_i
- issue_ready_o
- issue_ready_o

**Payload Signals (5):**
- issue_valid_i
- x_issue_req_t
- issue_req_i
- issue_ready_o
- issue_ready_o

**Generated File:** T1_instr_decoder_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- issue_valid_i
- x_issue_req_t
- issue_req_i
- opcode_t
- opcode_o
- ... and 2 more

**Payload Signals (3):**
- issue_valid_i
- issue_ready_o
- issue_ready_o

**Generated File:** T2_instr_decoder_Availability.sv

---

