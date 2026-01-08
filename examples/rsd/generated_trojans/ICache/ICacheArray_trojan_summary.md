# Trojan Generation Summary

**Module:** ICacheArray
**File:** ICache.sv
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
- regFlushStart
- regFlushReqAck
- valid
- regMissValid

**Payload Signals (5):**
- regFlushStart
- regFlushReqAck
- flushComplete
- valid
- regMissValid

**Generated File:** T1_ICacheArray_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- we
- writeHit
- weWay
- nruStateWE

**Payload Signals (3):**
- NRUAccessStatePath
- NRUAccessStatePath
- nruStateWE

**Generated File:** T2_ICacheArray_Privilege.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- regFlushStart
- regFlushReqAck
- valid
- regMissValid

**Payload Signals (4):**
- regFlushReqAck
- flushComplete
- valid
- regMissValid

**Generated File:** T3_ICacheArray_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- regFlushStart
- regFlush
- regFlushReqAck
- regMissValid

**Generated File:** T4_ICacheArray_Leak.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (2):**
- writeHit
- hitOut

**Generated File:** T5_ICacheArray_Integrity.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- NRUAccessStatePath
- NRUAccessStatePath

**Payload Signals (0):**

**Generated File:** T6_ICacheArray_Covert.sv

---

