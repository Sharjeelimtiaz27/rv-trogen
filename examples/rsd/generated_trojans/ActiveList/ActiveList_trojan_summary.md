# Trojan Generation Summary

**Module:** ActiveList
**File:** ActiveList.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- valid
- startRecoveryAtCommit
- execStateIsDifferentFromRef

**Payload Signals (3):**
- valid
- startRecoveryAtCommit
- execStateIsDifferentFromRef

**Generated File:** T1_ActiveList_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- we
- esWE
- ffsWE
- esRefWE

**Payload Signals (1):**
- execStateIsDifferentFromRef

**Generated File:** T2_ActiveList_Privilege.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- startRecoveryAtCommit

**Payload Signals (1):**
- valid

**Generated File:** T3_ActiveList_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- regInRecovery

**Generated File:** T4_ActiveList_Leak.sv

---

