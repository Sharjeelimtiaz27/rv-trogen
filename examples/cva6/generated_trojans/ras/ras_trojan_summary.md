# Trojan Generation Summary

**Module:** ras
**File:** ras.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- pop_i
- data_i
- data_o
- data_o

**Payload Signals (3):**
- data_i
- data_o
- data_o

**Generated File:** T1_ras_Integrity.sv

---

### T2: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- data_i
- data_o
- data_o

**Payload Signals (3):**
- data_i
- data_o
- data_o

**Generated File:** T2_ras_Covert.sv

---

