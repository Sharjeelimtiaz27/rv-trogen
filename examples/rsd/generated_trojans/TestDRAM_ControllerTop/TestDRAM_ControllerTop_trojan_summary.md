# Trojan Generation Summary

**Module:** TestDRAM_ControllerTop
**File:** TestDRAM_ControllerTop.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- DDR2WEN
- DDR2WEN
- memWE

**Payload Signals (4):**
- DDR2WEN
- DDR2WEN
- memCaribrationDone
- memWE

**Generated File:** T1_TestDRAM_ControllerTop_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- DDR2WEN
- DDR2WEN
- memWE

**Payload Signals (5):**
- posResetOut
- ledOut
- posResetOut
- ledOut
- memReadDataReady

**Generated File:** T2_TestDRAM_ControllerTop_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (5):**
- posResetOut
- ledOut
- posResetOut
- ledOut
- memReadDataReady

**Generated File:** T3_TestDRAM_ControllerTop_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (5):**
- posResetOut
- ledOut
- posResetOut
- ledOut
- memReadDataReady

**Generated File:** T4_TestDRAM_ControllerTop_Covert.sv

---

