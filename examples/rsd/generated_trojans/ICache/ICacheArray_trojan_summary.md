# Trojan Generation Summary

**Module:** ICacheArray
**File:** ICache.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- we
- valid
- valid
- weWay
- nruStateWE

**Payload Signals (5):**
- we
- valid
- valid
- weWay
- nruStateWE

**Generated File:** T1_ICacheArray_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- we
- writeIndex
- writeTag
- writeLineData
- writeIndex
- ... and 5 more

**Payload Signals (5):**
- writeLineData
- readLineData
- hitOut
- readLineData
- hitOut

**Generated File:** T2_ICacheArray_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (3):**
- writeLineData
- readLineData
- readLineData

**Payload Signals (11):**
- writeIndex
- writeTag
- writeLineData
- readLineData
- writeIndex
- ... and 6 more

**Generated File:** T3_ICacheArray_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- valid

**Payload Signals (2):**
- valid
- valid

**Generated File:** T4_ICacheArray_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- writeLineData
- readLineData
- NRUAccessStatePath
- NRUAccessStatePath
- readLineData
- ... and 1 more

**Payload Signals (7):**
- writeLineData
- readLineData
- valid
- hitOut
- readLineData
- ... and 2 more

**Generated File:** T5_ICacheArray_Covert.sv

---

