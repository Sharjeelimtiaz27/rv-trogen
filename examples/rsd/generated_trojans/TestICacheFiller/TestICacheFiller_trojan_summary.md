# Trojan Generation Summary

**Module:** TestICacheFiller
**File:** TestICacheFiller.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (0):**

**Payload Signals (1):**
- icFillerBusy

**Generated File:** T1_TestICacheFiller_Availability.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- icFillerBusy

**Generated File:** T2_TestICacheFiller_Covert.sv

---

