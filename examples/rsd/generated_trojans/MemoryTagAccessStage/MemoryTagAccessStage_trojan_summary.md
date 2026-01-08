# Trojan Generation Summary

**Module:** MemoryTagAccessStage
**File:** MemoryTagAccessStage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- isENV
- ldRegValid
- isFenceI
- stRegValid

**Payload Signals (4):**
- isENV
- ldRegValid
- isFenceI
- stRegValid

**Generated File:** T1_MemoryTagAccessStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- ldRegValid
- stRegValid

**Payload Signals (3):**
- stall
- ldRegValid
- stRegValid

**Generated File:** T2_MemoryTagAccessStage_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- isCSR
- ldRegValid
- stRegValid

**Generated File:** T3_MemoryTagAccessStage_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- isCSR

**Payload Signals (0):**

**Generated File:** T4_MemoryTagAccessStage_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (2):**
- storeForwardMiss
- isStore

**Generated File:** T5_MemoryTagAccessStage_Integrity.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- isLoad
- memAccessOrderViolation

**Payload Signals (0):**

**Generated File:** T6_MemoryTagAccessStage_Covert.sv

---

