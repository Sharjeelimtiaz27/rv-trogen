# Trojan Generation Summary

**Module:** Scheduler
**File:** Scheduler.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- wakeupSelect

**Payload Signals (1):**
- dispatchStore

**Generated File:** T1_Scheduler_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- dispatchLoad

**Payload Signals (0):**

**Generated File:** T2_Scheduler_Covert.sv

---

