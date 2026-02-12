# Trojan Generation Summary

**Module:** is
**File:** WakeupSelectIF.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- intIssueReq
- complexIssueReq
- loadIssueReq
- storeIssueReq
- fpIssueReq
- ... and 10 more

**Payload Signals (15):**
- intIssueReq
- complexIssueReq
- loadIssueReq
- storeIssueReq
- fpIssueReq
- ... and 10 more

**Generated File:** T1_is_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- selected
- selectedPtr
- selectedVector
- opReady
- opReady
- ... and 10 more

**Payload Signals (15):**
- write
- writePtr
- writeSrcTag
- writeDstTag
- write
- ... and 10 more

**Generated File:** T2_is_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (18):**
- intIssueReq
- complexIssueReq
- loadIssueReq
- storeIssueReq
- fpIssueReq
- ... and 13 more

**Payload Signals (4):**
- stall
- stall
- stall
- stall

**Generated File:** T3_is_Availability.sv

---

