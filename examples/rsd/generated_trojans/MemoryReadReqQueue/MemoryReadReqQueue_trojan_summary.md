# Trojan Generation Summary

**Module:** MemoryReadReqQueue
**File:** MemoryReadReqQueue.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- MemoryReadReq
- MemoryReadReq
- MemoryReadReq

**Payload Signals (3):**
- MemoryReadReq
- MemoryReadReq
- MemoryReadReq

**Generated File:** T1_MemoryReadReqQueue_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- pop
- pushedData
- headData
- headData
- `MEMORY_AXI4_READ_ID_WIDTH+`MEMORY_AXI4_ADDR_BIT_SIZE-1:0

**Payload Signals (3):**
- pushedData
- headData
- headData

**Generated File:** T2_MemoryReadReqQueue_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- pushedData
- headData
- headData

**Payload Signals (3):**
- pushedData
- headData
- headData

**Generated File:** T3_MemoryReadReqQueue_Covert.sv

---

