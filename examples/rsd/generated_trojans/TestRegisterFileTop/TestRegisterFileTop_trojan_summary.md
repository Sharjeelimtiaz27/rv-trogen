# Trojan Generation Summary

**Module:** TestRegisterFileTop
**File:** TestRegisterFileTop.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- intDstRegWE
- intDstFlagWE
- memDstRegWE
- memDstFlagWE

**Payload Signals (4):**
- intDstRegWE
- intDstFlagWE
- memDstRegWE
- memDstFlagWE

**Generated File:** T1_TestRegisterFileTop_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- intDstRegWE
- intDstFlagWE
- memDstRegWE
- memDstFlagWE

**Payload Signals (26):**
- DataPath
- intDstRegData
- intDstFlagData
- DataPath
- memDstRegData
- ... and 21 more

**Generated File:** T2_TestRegisterFileTop_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (26):**
- DataPath
- intDstRegData
- intDstFlagData
- DataPath
- memDstRegData
- ... and 21 more

**Payload Signals (26):**
- DataPath
- intDstRegData
- intDstFlagData
- DataPath
- memDstRegData
- ... and 21 more

**Generated File:** T3_TestRegisterFileTop_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (26):**
- DataPath
- intDstRegData
- intDstFlagData
- DataPath
- memDstRegData
- ... and 21 more

**Payload Signals (26):**
- DataPath
- intDstRegData
- intDstFlagData
- DataPath
- memDstRegData
- ... and 21 more

**Generated File:** T4_TestRegisterFileTop_Covert.sv

---

