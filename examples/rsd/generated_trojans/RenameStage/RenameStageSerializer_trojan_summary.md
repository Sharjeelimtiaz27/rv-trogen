# Trojan Generation Summary

**Module:** RenameStageSerializer
**File:** RenameStage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- activeListEmpty
- storeQueueEmpty
- isEnv

**Payload Signals (3):**
- activeListEmpty
- storeQueueEmpty
- isEnv

**Generated File:** T1_RenameStageSerializer_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- storeQueueEmpty

**Payload Signals (1):**
- stall

**Generated File:** T2_RenameStageSerializer_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- regFlush

**Generated File:** T3_RenameStageSerializer_Leak.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (2):**
- isStore
- storeQueueEmpty

**Generated File:** T4_RenameStageSerializer_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- isLoad

**Payload Signals (0):**

**Generated File:** T5_RenameStageSerializer_Covert.sv

---

