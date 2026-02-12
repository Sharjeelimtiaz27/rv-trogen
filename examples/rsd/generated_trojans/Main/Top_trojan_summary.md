# Trojan Generation Summary

**Module:** Top
**File:** Main.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- DDR2WEN
- serialWE
- serialWE
- DDR2WEN
- serialWE
- ... and 1 more

**Payload Signals (6):**
- DDR2WEN
- serialWE
- serialWE
- DDR2WEN
- serialWE
- ... and 1 more

**Generated File:** T1_Top_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- DDR2WEN
- serialWE
- serialWriteData
- serialWE
- serialWriteData
- ... and 5 more

**Payload Signals (18):**
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- SerialDataPath
- ... and 13 more

**Generated File:** T2_Top_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (12):**
- SerialDataPath
- serialWriteData
- SerialDataPath
- serialWriteData
- axi4LitePlToPsControlRegisterIF
- ... and 7 more

**Payload Signals (18):**
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- SerialDataPath
- ... and 13 more

**Generated File:** T3_Top_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- SerialDataPath
- serialWriteData
- SerialDataPath
- serialWriteData
- SerialDataPath
- ... and 3 more

**Payload Signals (18):**
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- SerialDataPath
- ... and 13 more

**Generated File:** T4_Top_Covert.sv

---

