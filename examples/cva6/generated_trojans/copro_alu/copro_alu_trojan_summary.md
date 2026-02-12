# Trojan Generation Summary

**Module:** copro_alu
**File:** copro_alu.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- valid_o
- we_o
- valid_o
- we_o

**Payload Signals (4):**
- valid_o
- we_o
- valid_o
- we_o

**Generated File:** T1_copro_alu_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- we_o
- we_o

**Payload Signals (2):**
- result_o
- result_o

**Generated File:** T2_copro_alu_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- opcode_t
- opcode_i

**Payload Signals (2):**
- result_o
- result_o

**Generated File:** T3_copro_alu_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- opcode_t
- opcode_i
- valid_o
- valid_o

**Payload Signals (2):**
- valid_o
- valid_o

**Generated File:** T4_copro_alu_Availability.sv

---

