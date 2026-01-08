# Trojan Generation Summary

**Module:** TestLRU_CounterTop
**File:** TestLRU_CounterTop.sv
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
- unpackedAccess

**Generated File:** T1_TestLRU_CounterTop_Availability.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- unpackedAccess

**Payload Signals (0):**

**Generated File:** T2_TestLRU_CounterTop_Covert.sv

---

