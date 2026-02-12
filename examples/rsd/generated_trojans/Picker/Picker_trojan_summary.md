# Trojan Generation Summary

**Module:** Picker
**File:** Picker.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- req
- req
- request
- reqTmp
- shiftedReq

**Payload Signals (5):**
- req
- req
- request
- reqTmp
- shiftedReq

**Generated File:** T1_Picker_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 0.80
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- req
- req
- request
- reqTmp
- shiftedReq

**Payload Signals (7):**
- grant
- grant
- grantPtr
- grant
- grant
- ... and 2 more

**Generated File:** T2_Picker_Availability.sv

---

