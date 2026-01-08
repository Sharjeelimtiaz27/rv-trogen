# Trojan Generation Summary

**Module:** NextPCStage
**File:** NextPCStage.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- address

**Payload Signals (1):**
- writePC_FromOuter

**Generated File:** T1_NextPCStage_Integrity.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- address
- regStall

**Generated File:** T2_NextPCStage_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- address
- writePC_FromOuter

**Payload Signals (0):**

**Generated File:** T3_NextPCStage_Privilege.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (0):**

**Payload Signals (2):**
- stall
- regStall

**Generated File:** T4_NextPCStage_Availability.sv

---

