# Trojan Generation Summary

**Module:** TestICacheTop
**File:** TestICacheTop.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (20):**
- AddrPath
- icNextReadAddrIn
- AddrPath
- icFillAddr
- LineDataPath
- ... and 15 more

**Payload Signals (10):**
- rstOut
- LineDataPath
- icFillData
- DataPath
- icReadDataOut
- ... and 5 more

**Generated File:** T1_TestICacheTop_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- LineDataPath
- icFillData
- DataPath
- icReadDataOut
- LineDataPath
- ... and 3 more

**Payload Signals (10):**
- rstOut
- LineDataPath
- icFillData
- DataPath
- icReadDataOut
- ... and 5 more

**Generated File:** T2_TestICacheTop_Covert.sv

---

