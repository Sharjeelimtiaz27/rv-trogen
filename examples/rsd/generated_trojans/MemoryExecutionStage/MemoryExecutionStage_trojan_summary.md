# Trojan Generation Summary

**Module:** MemoryExecutionStage
**File:** MemoryExecutionStage.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- cacheFlushReq

**Payload Signals (1):**
- cacheFlushReq

**Generated File:** T1_MemoryExecutionStage_DoS.sv

---

