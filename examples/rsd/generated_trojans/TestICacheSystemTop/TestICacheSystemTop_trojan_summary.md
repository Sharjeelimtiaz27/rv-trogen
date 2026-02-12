# Trojan Generation Summary

**Module:** TestICacheSystemTop
**File:** TestICacheSystemTop.sv
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
- MemAccessReq
- dcMemAccessReq
- MemAccessReq
- dcMemAccessReq

**Payload Signals (4):**
- MemAccessReq
- dcMemAccessReq
- MemAccessReq
- dcMemAccessReq

**Generated File:** T1_TestICacheSystemTop_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (8):**
- AddrPath
- icNextReadAddrIn
- DataPath
- icReadDataOut
- AddrPath
- ... and 3 more

**Payload Signals (10):**
- rstOut
- DataPath
- icReadDataOut
- MemAccessResult
- dcMemAccessResult
- ... and 5 more

**Generated File:** T2_TestICacheSystemTop_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- MemAccessReq
- dcMemAccessReq
- DataPath
- icReadDataOut
- MemAccessResult
- ... and 7 more

**Payload Signals (10):**
- rstOut
- DataPath
- icReadDataOut
- MemAccessResult
- dcMemAccessResult
- ... and 5 more

**Generated File:** T3_TestICacheSystemTop_Covert.sv

---

