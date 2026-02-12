# Trojan Generation Summary

**Module:** Divider
**File:** Divider.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- req
- req

**Payload Signals (2):**
- req
- req

**Generated File:** T1_Divider_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 7 more

**Payload Signals (12):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 7 more

**Generated File:** T2_Divider_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 7 more

**Payload Signals (12):**
- DataPath
- DataPath
- DataPath
- DataPath
- DataPath
- ... and 7 more

**Generated File:** T3_Divider_Covert.sv

---

