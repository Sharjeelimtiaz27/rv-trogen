# Trojan Generation Summary

**Module:** TestRegisterFile
**File:** TestRegisterFile.sv
**Type:** Sequential
**Total Candidates:** 1

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

**Generated File:** T1_TestRegisterFile_DoS.sv

---

