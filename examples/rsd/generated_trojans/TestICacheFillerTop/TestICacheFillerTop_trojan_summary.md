# Trojan Generation Summary

**Module:** TestICacheFillerTop
**File:** TestICacheFillerTop.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- rstOut

**Generated File:** T1_TestICacheFillerTop_Integrity.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (0):**

**Payload Signals (1):**
- icFillerBusy

**Generated File:** T2_TestICacheFillerTop_Availability.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- icFillerBusy

**Generated File:** T3_TestICacheFillerTop_Covert.sv

---

