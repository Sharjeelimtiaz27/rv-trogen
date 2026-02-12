# Trojan Generation Summary

**Module:** NextPCStage
**File:** NextPCStage.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- numValidInsns

**Payload Signals (1):**
- numValidInsns

**Generated File:** T1_NextPCStage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- writePC_FromOuter

**Payload Signals (1):**
- writePC_FromOuter

**Generated File:** T2_NextPCStage_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- numValidInsns

**Payload Signals (1):**
- numValidInsns

**Generated File:** T3_NextPCStage_Availability.sv

---

