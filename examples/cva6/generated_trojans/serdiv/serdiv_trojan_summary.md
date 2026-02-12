# Trojan Generation Summary

**Module:** serdiv
**File:** serdiv.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (8):**
- op_a_i
- op_b_i
- opcode_i
- op_a_sign)
- op_a_i
- ... and 3 more

**Payload Signals (6):**
- out_vld_o
- out_rdy_i
- out_vld_o
- out_rdy_i
- add_out
- ... and 1 more

**Generated File:** T1_serdiv_Integrity.sv

---

