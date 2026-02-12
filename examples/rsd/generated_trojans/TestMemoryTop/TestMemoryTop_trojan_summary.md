# Trojan Generation Summary

**Module:** TestMemoryTop
**File:** TestMemoryTop.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- MemReadAccessReq
- icMemAccessReq
- MemAccessReq
- dcMemAccessReq
- MemReadAccessReq
- ... and 3 more

**Payload Signals (8):**
- MemReadAccessReq
- icMemAccessReq
- MemAccessReq
- dcMemAccessReq
- MemReadAccessReq
- ... and 3 more

**Generated File:** T1_TestMemoryTop_DoS.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (16):**
- MemReadAccessReq
- icMemAccessReq
- MemAccessReq
- dcMemAccessReq
- MemAccessResult
- ... and 11 more

**Payload Signals (10):**
- rstOut
- MemAccessResult
- icMemAccessResult
- MemAccessResult
- dcMemAccessResult
- ... and 5 more

**Generated File:** T2_TestMemoryTop_Covert.sv

---

