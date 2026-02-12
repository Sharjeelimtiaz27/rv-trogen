# Trojan Generation Summary

**Module:** RegisterFile
**File:** RegisterFile.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- regWE
- fpRegWE

**Payload Signals (2):**
- regWE
- fpRegWE

**Generated File:** T1_RegisterFile_DoS.sv

---

