# Trojan Generation Summary

**Module:** DecodedBranchResolver
**File:** DecodedBranchResolver.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- insnValidOut
- insnValidIn
- insnFlushTriggering
- flushTriggered

**Payload Signals (2):**
- insnValidOut
- insnValidIn

**Generated File:** T1_DecodedBranchResolver_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- popRAS
- addrCheck
- addrIncorrect
- addrMismatch

**Payload Signals (1):**
- insnValidOut

**Generated File:** T2_DecodedBranchResolver_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- insnValidOut
- insnValidIn
- insnFlushTriggering
- flushTriggered
- popRAS

**Payload Signals (2):**
- insnValidOut
- insnValidIn

**Generated File:** T3_DecodedBranchResolver_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- addrCheck
- addrIncorrect
- addrMismatch

**Generated File:** T4_DecodedBranchResolver_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- addrCheck
- addrIncorrect
- addrMismatch

**Payload Signals (0):**

**Generated File:** T5_DecodedBranchResolver_Privilege.sv

---

