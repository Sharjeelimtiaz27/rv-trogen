# Trojan Generation Summary

**Module:** ReadyBitTable
**File:** ReadyBitTable.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid

**Payload Signals (3):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid

**Generated File:** T1_ReadyBitTable_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid
- SRC_OP_NUM
- SRC_OP_NUM
- ... and 2 more

**Payload Signals (3):**
- wakeupDstValid
- dispatchedDstValid
- dispatchedSrcValid

**Generated File:** T2_ReadyBitTable_Availability.sv

---

