# Trojan Generation Summary

**Module:** TestDCacheTop
**File:** TestDCacheTop.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- dcWE
- dcFillReq
- dcWE
- dcFillReq

**Payload Signals (4):**
- dcWE
- dcFillReq
- dcWE
- dcFillReq

**Generated File:** T1_TestDCacheTop_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- dcWE
- dcWriteDataIn
- dcWriteAddrIn
- dcWriteAccessSize
- dcWriteHit
- ... and 5 more

**Payload Signals (36):**
- rstOut
- AddrPath
- dcReadAddrIn
- DataPath
- dcWriteDataIn
- ... and 31 more

**Generated File:** T2_TestDCacheTop_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (34):**
- AddrPath
- dcReadAddrIn
- DataPath
- dcWriteDataIn
- AddrPath
- ... and 29 more

**Payload Signals (24):**
- rstOut
- DataPath
- dcWriteDataIn
- dcWriteAddrIn
- dcWriteAccessSize
- ... and 19 more

**Generated File:** T3_TestDCacheTop_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (20):**
- DataPath
- dcWriteDataIn
- MemAccessSizeType
- dcWriteAccessSize
- LineDataPath
- ... and 15 more

**Payload Signals (18):**
- rstOut
- DataPath
- dcWriteDataIn
- LineDataPath
- dcFillData
- ... and 13 more

**Generated File:** T4_TestDCacheTop_Covert.sv

---

