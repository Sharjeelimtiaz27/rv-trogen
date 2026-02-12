# Trojan Generation Summary

**Module:** MemoryLatencySimulator
**File:** MemoryLatencySimulator.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- MemoryLatencySimRequestPath
- hasRequest
- MemoryLatencySimRequestPath
- requestData
- hasRequest
- ... and 2 more

**Payload Signals (7):**
- MemoryLatencySimRequestPath
- hasRequest
- MemoryLatencySimRequestPath
- requestData
- hasRequest
- ... and 2 more

**Generated File:** T1_MemoryLatencySimulator_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- pushedData
- requestData
- requestData
- pop

**Payload Signals (3):**
- pushedData
- requestData
- requestData

**Generated File:** T2_MemoryLatencySimulator_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- pushedData
- requestData
- requestData

**Payload Signals (3):**
- pushedData
- requestData
- requestData

**Generated File:** T3_MemoryLatencySimulator_Covert.sv

---

