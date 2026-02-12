# Trojan Generation Summary

**Module:** takes
**File:** instr_realign.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- valid_i
- valid_o
- valid_o

**Payload Signals (3):**
- valid_i
- valid_o
- valid_o

**Generated File:** T1_takes_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (6):**
- address_i
- data_i
- addr_o
- address_i
- data_i
- ... and 1 more

**Payload Signals (2):**
- data_i
- data_i

**Generated File:** T2_takes_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- valid_i
- valid_o
- valid_o

**Payload Signals (3):**
- valid_i
- valid_o
- valid_o

**Generated File:** T3_takes_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- data_i
- data_i

**Payload Signals (5):**
- valid_i
- data_i
- valid_o
- data_i
- valid_o

**Generated File:** T4_takes_Covert.sv

---

