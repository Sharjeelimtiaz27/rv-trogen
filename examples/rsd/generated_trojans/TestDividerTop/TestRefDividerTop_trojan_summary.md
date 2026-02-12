# Trojan Generation Summary

**Module:** TestRefDividerTop
**File:** TestDividerTop.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- req

**Payload Signals (1):**
- req

**Generated File:** T1_TestRefDividerTop_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 5 more

**Payload Signals (10):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 5 more

**Generated File:** T2_TestRefDividerTop_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 5 more

**Payload Signals (10):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 5 more

**Generated File:** T3_TestRefDividerTop_Covert.sv

---

