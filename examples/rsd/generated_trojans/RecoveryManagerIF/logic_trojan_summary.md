# Trojan Generation Summary

**Module:** logic
**File:** RecoveryManagerIF.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- storeQueueRecoveryTailPtr
- storeQueueRecoveryTailPtr
- storeQueueHeadPtr
- storeQueueRecoveryTailPtr
- storeQueueHeadPtr

**Payload Signals (5):**
- storeQueueRecoveryTailPtr
- storeQueueRecoveryTailPtr
- storeQueueHeadPtr
- storeQueueRecoveryTailPtr
- storeQueueHeadPtr

**Generated File:** T1_logic_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (18):**
- replayQueueFlushedOpExist
- wakeupPipelineRegFlushedOpExist
- faultingDataAddr
- recoveryOpIndex
- selected
- ... and 13 more

**Payload Signals (3):**
- faultingDataAddr
- faultingDataAddr
- faultingDataAddr

**Generated File:** T2_logic_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- faultingDataAddr
- faultingDataAddr
- faultingDataAddr

**Payload Signals (3):**
- faultingDataAddr
- faultingDataAddr
- faultingDataAddr

**Generated File:** T3_logic_Covert.sv

---

