# Trojan Generation Summary

**Module:** IntAdder
**File:** IntALU.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- DataPath
- DataPath
- DataPath
- DataPath
- fuOpA_In
- ... and 10 more

**Payload Signals (14):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 9 more

**Generated File:** T1_IntAdder_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (11):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 6 more

**Payload Signals (14):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 9 more

**Generated File:** T2_IntAdder_Covert.sv

---

