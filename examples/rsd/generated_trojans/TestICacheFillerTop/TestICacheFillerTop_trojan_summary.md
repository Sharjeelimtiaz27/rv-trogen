# Trojan Generation Summary

**Module:** TestICacheFillerTop
**File:** TestICacheFillerTop.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- MemReadAccessReq
- icMemAccessReq
- MemReadAccessReq
- icMemAccessReq

**Payload Signals (4):**
- MemReadAccessReq
- icMemAccessReq
- MemReadAccessReq
- icMemAccessReq

**Generated File:** T1_TestICacheFillerTop_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- AddrPath
- icMissAddr
- AddrPath
- icFillAddr
- LineDataPath
- ... and 7 more

**Payload Signals (10):**
- rstOut
- MemAccessResult
- icMemAccessResult
- LineDataPath
- icFillData
- ... and 5 more

**Generated File:** T2_TestICacheFillerTop_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- MemAccessResult
- icMemAccessResult
- LineDataPath
- icFillData
- MemReadAccessReq
- ... and 7 more

**Payload Signals (10):**
- rstOut
- MemAccessResult
- icMemAccessResult
- LineDataPath
- icFillData
- ... and 5 more

**Generated File:** T3_TestICacheFillerTop_Covert.sv

---

