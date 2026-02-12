# Trojan Generation Summary

**Module:** BlockDualPortRAM
**File:** RAM_Vivado.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- we
- we
- we
- we
- we
- ... and 3 more

**Payload Signals (8):**
- we
- we
- we
- we
- we
- ... and 3 more

**Generated File:** T1_BlockDualPortRAM_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (10):**
- we
- we
- we
- we
- we
- ... and 5 more

**Payload Signals (1):**
- Address

**Generated File:** T2_BlockDualPortRAM_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- Address
- Select

**Payload Signals (2):**
- WRITE_NUM
- WRITE_NUM

**Generated File:** T3_BlockDualPortRAM_Integrity.sv

---

