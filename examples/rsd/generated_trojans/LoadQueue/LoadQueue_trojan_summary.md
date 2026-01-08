# Trojan Generation Summary

**Module:** LoadQueue
**File:** LoadQueue.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- executedLoadRegValid

**Payload Signals (1):**
- executedLoadRegValid

**Generated File:** T1_LoadQueue_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- executedLoadRegValid

**Payload Signals (1):**
- executedLoadRegValid

**Generated File:** T2_LoadQueue_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- executedLoadRegValid

**Generated File:** T3_LoadQueue_Leak.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- executedLoadRegValid

**Payload Signals (0):**

**Generated File:** T4_LoadQueue_Covert.sv

---

