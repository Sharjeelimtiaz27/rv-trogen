# Trojan Generation Summary

**Module:** StoreCommitter
**File:** StoreCommitter.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- valid
- dcWriteReq
- dcWriteByteWE
- releaseStoreQueueHead

**Payload Signals (4):**
- valid
- dcWriteReq
- dcWriteByteWE
- releaseStoreQueueHead

**Generated File:** T1_StoreCommitter_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- valid
- dcWriteReq
- releaseStoreQueueHead

**Payload Signals (2):**
- stallStoreTagStage
- valid

**Generated File:** T2_StoreCommitter_Availability.sv

---

