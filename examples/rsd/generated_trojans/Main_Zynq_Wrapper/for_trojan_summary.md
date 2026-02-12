# Trojan Generation Summary

**Module:** for
**File:** Main_Zynq_Wrapper.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- serialWE
- serialWE

**Payload Signals (2):**
- serialWE
- serialWE

**Generated File:** T1_for_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- serialWE
- serialWriteData
- serialWE
- serialWriteData

**Payload Signals (10):**
- ledOut
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- ... and 5 more

**Generated File:** T2_for_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- SerialDataPath
- serialWriteData
- SerialDataPath
- serialWriteData

**Payload Signals (10):**
- ledOut
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- ... and 5 more

**Generated File:** T3_for_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- SerialDataPath
- serialWriteData
- SerialDataPath
- serialWriteData

**Payload Signals (10):**
- ledOut
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- ... and 5 more

**Generated File:** T4_for_Covert.sv

---

