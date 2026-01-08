# Trojan Generation Summary

**Module:** MemoryRegisterWriteStage
**File:** MemoryRegisterWriteStage.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- valid
- makeMSHRCanBeInvalid

**Payload Signals (2):**
- valid
- makeMSHRCanBeInvalid

**Generated File:** T1_MemoryRegisterWriteStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- makeMSHRCanBeInvalid

**Payload Signals (3):**
- stall
- valid
- makeMSHRCanBeInvalid

**Generated File:** T2_MemoryRegisterWriteStage_Availability.sv

---

