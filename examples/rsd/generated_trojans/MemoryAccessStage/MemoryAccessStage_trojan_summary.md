# Trojan Generation Summary

**Module:** MemoryAccessStage
**File:** MemoryAccessStage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- valid
- regValid

**Payload Signals (2):**
- valid
- regValid

**Generated File:** T1_MemoryAccessStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- regValid

**Payload Signals (3):**
- valid
- regValid
- stall

**Generated File:** T2_MemoryAccessStage_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- isCSR
- regValid

**Generated File:** T3_MemoryAccessStage_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- isCSR

**Payload Signals (0):**

**Generated File:** T4_MemoryAccessStage_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- isStore

**Generated File:** T5_MemoryAccessStage_Integrity.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- isLoad

**Payload Signals (0):**

**Generated File:** T6_MemoryAccessStage_Covert.sv

---

