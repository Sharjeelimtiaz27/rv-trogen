# Trojan Generation Summary

**Module:** ReplayQueue
**File:** ReplayQueue.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- pushEntry
- popEntry
- replayEntryValidIn
- replayEntryValidOut
- noValidInst
- ... and 1 more

**Payload Signals (6):**
- pushEntry
- popEntry
- replayEntryValidIn
- replayEntryValidOut
- noValidInst
- ... and 1 more

**Generated File:** T1_ReplayQueue_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- nextReplay

**Payload Signals (2):**
- register
- replayReg

**Generated File:** T2_ReplayQueue_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- popEntry

**Payload Signals (1):**
- replayEntryValidOut

**Generated File:** T3_ReplayQueue_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- popEntry
- replayEntryValidIn
- replayEntryValidOut
- noValidInst
- mshrValid

**Payload Signals (4):**
- replayEntryValidIn
- replayEntryValidOut
- noValidInst
- mshrValid

**Generated File:** T4_ReplayQueue_Availability.sv

---

