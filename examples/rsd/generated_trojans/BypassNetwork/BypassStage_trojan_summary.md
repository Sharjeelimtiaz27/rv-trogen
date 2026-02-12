# Trojan Generation Summary

**Module:** BypassStage
**File:** BypassNetwork.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (9):**
- BypassOperand
- BypassOperand
- BypassSelect
- sel
- BypassOperand
- ... and 4 more

**Payload Signals (2):**
- out
- out

**Generated File:** T1_BypassStage_Integrity.sv

---

