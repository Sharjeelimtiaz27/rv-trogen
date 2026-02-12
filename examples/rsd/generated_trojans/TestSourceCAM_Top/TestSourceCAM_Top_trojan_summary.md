# Trojan Generation Summary

**Module:** TestSourceCAM_Top
**File:** TestSourceCAM_Top.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- SRC_OP_NUM-1:0
- SRC_OP_NUM-1:0
- opReady
- SRC_OP_NUM-1:0
- SRC_OP_NUM-1:0
- ... and 2 more

**Payload Signals (2):**
- rstOut
- rstOut

**Generated File:** T1_TestSourceCAM_Top_Integrity.sv

---

