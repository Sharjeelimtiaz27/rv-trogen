# Trojan Generation Summary

**Module:** controller
**File:** controller.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- ex_valid_i
- ex_valid_i

**Payload Signals (2):**
- ex_valid_i
- ex_valid_i

**Generated File:** T1_controller_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (6):**
- halt_csr_i
- set_debug_pc_i
- flush_csr_i
- halt_csr_i
- set_debug_pc_i
- ... and 1 more

**Payload Signals (4):**
- halt_csr_i
- flush_csr_i
- halt_csr_i
- flush_csr_i

**Generated File:** T2_controller_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- ex_valid_i
- ex_valid_i

**Payload Signals (4):**
- flush_dcache_ack_i
- ex_valid_i
- flush_dcache_ack_i
- ex_valid_i

**Generated File:** T3_controller_Availability.sv

---

