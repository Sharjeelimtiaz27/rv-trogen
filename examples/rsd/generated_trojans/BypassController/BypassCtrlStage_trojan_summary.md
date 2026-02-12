# Trojan Generation Summary

**Module:** BypassCtrlStage
**File:** BypassController.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- writeReg

**Payload Signals (2):**
- out
- out

**Generated File:** T1_BypassCtrlStage_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- BypassCtrlOperand
- BypassCtrlOperand
- BypassCtrlOperand
- BypassCtrlOperand
- BypassCtrlOperand
- ... and 2 more

**Payload Signals (3):**
- out
- out
- writeReg

**Generated File:** T2_BypassCtrlStage_Integrity.sv

---

