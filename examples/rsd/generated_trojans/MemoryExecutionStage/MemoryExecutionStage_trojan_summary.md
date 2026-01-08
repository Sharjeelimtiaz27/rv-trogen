# Trojan Generation Summary

**Module:** MemoryExecutionStage
**File:** MemoryExecutionStage.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- regValid
- cacheFlushReq

**Payload Signals (2):**
- regValid
- cacheFlushReq

**Generated File:** T1_MemoryExecutionStage_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- regValid
- cacheFlushReq

**Payload Signals (2):**
- stall
- regValid

**Generated File:** T2_MemoryExecutionStage_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- regValid
- isCSR

**Generated File:** T3_MemoryExecutionStage_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- isCSR

**Payload Signals (0):**

**Generated File:** T4_MemoryExecutionStage_Privilege.sv

---

