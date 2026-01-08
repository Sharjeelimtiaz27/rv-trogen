# Trojan Generation Summary

**Module:** CommitStage
**File:** CommitStage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- ActiveListCountPath
- startCommit
- ActiveListCountPath
- unableToStartRecovery
- recoveryTrigger

**Payload Signals (4):**
- ActiveListCountPath
- startCommit
- ActiveListCountPath
- unableToStartRecovery

**Generated File:** T1_CommitStage_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- fflagsWE

**Payload Signals (4):**
- ExecutionState
- ExecutionState
- ExecutionState
- ExecutionState

**Generated File:** T2_CommitStage_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- isStore

**Generated File:** T3_CommitStage_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- startCommit
- unableToStartRecovery
- recoveryTrigger

**Payload Signals (0):**

**Generated File:** T4_CommitStage_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- RefetchType

**Payload Signals (0):**

**Generated File:** T5_CommitStage_Covert.sv

---

