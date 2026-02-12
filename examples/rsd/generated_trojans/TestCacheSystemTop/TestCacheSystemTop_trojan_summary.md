# Trojan Generation Summary

**Module:** TestCacheSystemTop
**File:** TestCacheSystemTop.sv
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

**Generated File:** T1_TestCacheSystemTop_DoS.sv

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

**Payload Signals (44):**
- rstOut
- AddrPath
- icNextReadAddrIn
- AddrPath
- dcReadAddrIn
- ... and 39 more

**Generated File:** T2_TestCacheSystemTop_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (38):**
- AddrPath
- icNextReadAddrIn
- AddrPath
- dcReadAddrIn
- DataPath
- ... and 33 more

**Payload Signals (30):**
- rstOut
- DataPath
- dcWriteDataIn
- dcWriteAddrIn
- dcWriteAccessSize
- ... and 25 more

**Generated File:** T3_TestCacheSystemTop_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (26):**
- DataPath
- dcWriteDataIn
- MemAccessSizeType
- dcWriteAccessSize
- DataPath
- ... and 21 more

**Payload Signals (24):**
- rstOut
- DataPath
- dcWriteDataIn
- DataPath
- icReadDataOut
- ... and 19 more

**Generated File:** T4_TestCacheSystemTop_Covert.sv

---

