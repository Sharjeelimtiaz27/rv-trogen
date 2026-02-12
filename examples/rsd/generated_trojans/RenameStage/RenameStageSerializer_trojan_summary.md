# Trojan Generation Summary

**Module:** RenameStageSerializer
**File:** RenameStage.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- storeQueueEmpty
- valid

**Payload Signals (2):**
- storeQueueEmpty
- valid

**Generated File:** T1_RenameStageSerializer_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- storeQueueEmpty
- OpInfo
- opInfo
- valid

**Payload Signals (2):**
- stall
- valid

**Generated File:** T2_RenameStageSerializer_Availability.sv

---

