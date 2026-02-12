# Trojan Generation Summary

**Module:** TestDCacheFillerTop
**File:** TestDCacheFillerTop.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- dcFillReq
- MemAccessReq
- dcMemAccessReq
- dcFillReq
- MemAccessReq
- ... and 1 more

**Payload Signals (6):**
- dcFillReq
- MemAccessReq
- dcMemAccessReq
- dcFillReq
- MemAccessReq
- ... and 1 more

**Generated File:** T1_TestDCacheFillerTop_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (20):**
- AddrPath
- dcMissAddr
- AddrPath
- dcReplaceAddr
- LineDataPath
- ... and 15 more

**Payload Signals (14):**
- rstOut
- MemAccessResult
- dcMemAccessResult
- LineDataPath
- dcReplaceData
- ... and 9 more

**Generated File:** T2_TestDCacheFillerTop_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (16):**
- MemAccessResult
- dcMemAccessResult
- LineDataPath
- dcReplaceData
- LineDataPath
- ... and 11 more

**Payload Signals (14):**
- rstOut
- MemAccessResult
- dcMemAccessResult
- LineDataPath
- dcReplaceData
- ... and 9 more

**Generated File:** T3_TestDCacheFillerTop_Covert.sv

---

