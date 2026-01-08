# Trojan Generation Summary

**Module:** MicroOpPicker
**File:** DecodeStage.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- sent
- insnValidIn
- insnValidOut
- insnFlushTriggering
- flushTriggered

**Payload Signals (4):**
- sent
- complete
- insnValidIn
- insnValidOut

**Generated File:** T1_MicroOpPicker_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- AllDecodedMicroOpPath
- mopPicked

**Payload Signals (1):**
- insnValidOut

**Generated File:** T2_MicroOpPicker_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- AllDecodedMicroOpPath
- insnValidIn
- insnValidOut
- insnFlushTriggering
- flushTriggered
- ... and 1 more

**Payload Signals (5):**
- stall
- complete
- stallBranchResolver
- insnValidIn
- insnValidOut

**Generated File:** T3_MicroOpPicker_Availability.sv

---

