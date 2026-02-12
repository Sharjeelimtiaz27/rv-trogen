# Trojan Generation Summary

**Module:** Main_Zynq
**File:** Main_Zynq.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- serialWE
- serialWE
- reqExternalInterrupt

**Payload Signals (4):**
- serialWE
- serialWE
- memCaribrationDone
- reqExternalInterrupt

**Generated File:** T1_Main_Zynq_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- serialWE
- serialWriteData
- serialWE
- serialWriteData
- memAccessWriteBusy

**Payload Signals (11):**
- ledOut
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- ... and 6 more

**Generated File:** T2_Main_Zynq_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (9):**
- axi4LitePlToPsControlRegisterIF
- axi4LitePsToPlControlRegisterIF
- SerialDataPath
- serialWriteData
- axi4LitePlToPsControlRegisterIF
- ... and 4 more

**Payload Signals (12):**
- ledOut
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- ... and 7 more

**Generated File:** T3_Main_Zynq_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- axi4LitePlToPsControlRegisterIF
- axi4LitePsToPlControlRegisterIF
- axi4LitePlToPsControlRegisterIF
- axi4LitePsToPlControlRegisterIF
- reqExternalInterrupt

**Payload Signals (1):**
- memCaribrationDone

**Generated File:** T4_Main_Zynq_Availability.sv

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

**Payload Signals (11):**
- ledOut
- SerialDataPath
- serialWriteData
- posResetOut
- ledOut
- ... and 6 more

**Generated File:** T5_Main_Zynq_Covert.sv

---

