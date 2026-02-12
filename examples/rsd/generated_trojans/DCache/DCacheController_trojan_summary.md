# Trojan Generation Summary

**Module:** DCacheController
**File:** DCache.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- dcFlushReqAck
- memValid
- storedLineByteWE
- dcWriteReqReg
- portStoredLineByteWE

**Payload Signals (5):**
- dcFlushReqAck
- memValid
- storedLineByteWE
- dcWriteReqReg
- portStoredLineByteWE

**Generated File:** T1_DCacheController_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- storedLineByteWE
- dcWriteReqReg
- dcWriteUncachableReg
- portStoredLineByteWE

**Payload Signals (10):**
- PhyAddrPath
- addr)
- PhyAddrPath
- addr)
- PhyAddrPath
- ... and 5 more

**Generated File:** T2_DCacheController_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- PhyAddrPath
- addr)
- PhyAddrPath
- addr)
- PhyAddrPath
- ... and 5 more

**Payload Signals (2):**
- dcWriteReqReg
- dcWriteUncachableReg

**Generated File:** T3_DCacheController_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- dcFlushReqAck
- memValid
- dcWriteReqReg

**Payload Signals (1):**
- memValid

**Generated File:** T4_DCacheController_Availability.sv

---

