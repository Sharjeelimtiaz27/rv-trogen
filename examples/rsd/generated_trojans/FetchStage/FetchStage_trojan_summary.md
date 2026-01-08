# Trojan Generation Summary

**Module:** FetchStage
**File:** FetchStage.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (1):**
- regStall

**Generated File:** T1_FetchStage_Leak.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (0):**

**Payload Signals (2):**
- stall
- regStall

**Generated File:** T2_FetchStage_Availability.sv

---

