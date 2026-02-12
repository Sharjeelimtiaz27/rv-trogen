# Trojan Generation Summary

**Module:** Main
**File:** Main_Fpga.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- DDR2WEN
- serialWE
- DDR2WEN
- serialWE
- reqExternalInterrupt

**Payload Signals (6):**
- DDR2WEN
- serialWE
- DDR2WEN
- serialWE
- memCaribrationDone
- ... and 1 more

**Generated File:** T1_Main_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (7):**
- DDR2WEN
- serialWE
- serialWriteData
- DDR2WEN
- serialWE
- ... and 2 more

**Payload Signals (9):**
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- SerialDataPath
- ... and 4 more

**Generated File:** T2_Main_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- SerialDataPath
- serialWriteData
- SerialDataPath
- serialWriteData
- memReadDataReady

**Payload Signals (10):**
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- SerialDataPath
- ... and 5 more

**Generated File:** T3_Main_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- reqExternalInterrupt

**Payload Signals (1):**
- memCaribrationDone

**Generated File:** T4_Main_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- SerialDataPath
- serialWriteData
- SerialDataPath
- serialWriteData
- memReadDataReady
- ... and 3 more

**Payload Signals (9):**
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- SerialDataPath
- ... and 4 more

**Generated File:** T5_Main_Covert.sv

---

