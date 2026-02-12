# Trojan Generation Summary

**Module:** ControlQueue
**File:** ControlQueue.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- pop
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- pushedData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- headData
- ... and 2 more

**Payload Signals (6):**
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- pushedData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- headData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- ... and 1 more

**Generated File:** T1_ControlQueue_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- pushedData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- headData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- ... and 1 more

**Payload Signals (6):**
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- pushedData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- headData
- `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0
- ... and 1 more

**Generated File:** T2_ControlQueue_Covert.sv

---

