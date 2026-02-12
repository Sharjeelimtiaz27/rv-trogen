# Trojan Generation Summary

**Module:** TestMain
**File:** TestMain.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- serialWE

**Payload Signals (1):**
- serialWE

**Generated File:** T1_TestMain_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- serialWE

**Payload Signals (2):**
- DataPath
- DataPath

**Generated File:** T2_TestMain_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- DataPath
- DataPath

**Payload Signals (2):**
- DataPath
- DataPath

**Generated File:** T3_TestMain_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- DataPath
- DataPath

**Payload Signals (2):**
- DataPath
- DataPath

**Generated File:** T4_TestMain_Covert.sv

---

