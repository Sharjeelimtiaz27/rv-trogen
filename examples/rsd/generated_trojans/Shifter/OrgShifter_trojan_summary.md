# Trojan Generation Summary

**Module:** OrgShifter
**File:** Shifter.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (18):**
- ShiftOperandType
- shiftOperandType
- DataPath
- dataIn
- DataPath
- ... and 13 more

**Payload Signals (19):**
- DataPath
- dataIn
- DataPath
- dataOut
- carryOut
- ... and 14 more

**Generated File:** T1_OrgShifter_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (14):**
- DataPath
- dataIn
- DataPath
- dataOut
- DataPath
- ... and 9 more

**Payload Signals (19):**
- DataPath
- dataIn
- DataPath
- dataOut
- carryOut
- ... and 14 more

**Generated File:** T2_OrgShifter_Covert.sv

---

