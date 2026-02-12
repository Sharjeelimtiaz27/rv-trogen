# Trojan Generation Summary

**Module:** MemoryRegisterReadStage
**File:** MemoryRegisterReadStage.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- OpOperandType
- opType
- DataPath
- DataPath
- DataPath

**Payload Signals (3):**
- DataPath
- DataPath
- DataPath

**Generated File:** T1_MemoryRegisterReadStage_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- DataPath
- DataPath
- DataPath

**Payload Signals (3):**
- DataPath
- DataPath
- DataPath

**Generated File:** T2_MemoryRegisterReadStage_Covert.sv

---

