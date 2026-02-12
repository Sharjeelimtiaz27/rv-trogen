# Trojan Generation Summary

**Module:** FlipFlop
**File:** FlipFlop.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- we
- we

**Payload Signals (2):**
- we
- we

**Generated File:** T1_FlipFlop_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- we
- we

**Payload Signals (2):**
- out
- out

**Generated File:** T2_FlipFlop_Leak.sv

---

