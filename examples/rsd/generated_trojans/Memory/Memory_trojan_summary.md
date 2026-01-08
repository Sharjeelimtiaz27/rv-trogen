# Trojan Generation Summary

**Module:** Memory
**File:** Memory.sv
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
- memReadDataReady
- valid
- pushRequestQueue
- hasRequest

**Payload Signals (4):**
- memReadDataReady
- valid
- pushRequestQueue
- hasRequest

**Generated File:** T1_Memory_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- memReadDataReady

**Payload Signals (2):**
- memReadDataReady
- memWriteAccessAck

**Generated File:** T2_Memory_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- memReadDataReady
- valid
- pushRequestQueue
- hasRequest

**Payload Signals (5):**
- memAccessBusy
- memReadDataReady
- valid
- memReadAccessAck
- memWriteAccessAck

**Generated File:** T3_Memory_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- memAccessBusy
- memAccessRE
- memAccessWE
- memReadDataReady
- memReadAccessAck
- ... and 1 more

**Payload Signals (1):**
- memAccessBusy

**Generated File:** T4_Memory_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- memReadDataReady

**Generated File:** T5_Memory_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- memAccessWE
- memWriteAccessAck
- memoryWE

**Payload Signals (0):**

**Generated File:** T6_Memory_Privilege.sv

---

