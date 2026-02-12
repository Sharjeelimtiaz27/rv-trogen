# Trojan Generation Summary

**Module:** MicroOpPicker
**File:** DecodeStage.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- req

**Payload Signals (1):**
- req

**Generated File:** T1_MicroOpPicker_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- AllDecodedMicroOpPath
- req
- AllDecodedMicroOpPath
- AllDecodedMicroOpIndex
- AllDecodedMicroOpPath
- ... and 2 more

**Payload Signals (1):**
- stallBranchResolver

**Generated File:** T2_MicroOpPicker_Availability.sv

---

