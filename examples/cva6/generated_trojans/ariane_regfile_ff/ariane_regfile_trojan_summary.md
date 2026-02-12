# Trojan Generation Summary

**Module:** ariane_regfile
**File:** ariane_regfile_ff.sv
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
- test_en_i
- we_i
- we_i
- we_dec

**Payload Signals (4):**
- test_en_i
- we_i
- we_i
- we_dec

**Generated File:** T1_ariane_regfile_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- test_en_i
- we_i
- we_i
- we_dec

**Payload Signals (7):**
- raddr_i
- rdata_o
- waddr_i
- wdata_i
- rdata_o
- ... and 2 more

**Generated File:** T2_ariane_regfile_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- raddr_i
- rdata_o
- waddr_i
- wdata_i
- rdata_o
- ... and 2 more

**Payload Signals (4):**
- rdata_o
- wdata_i
- rdata_o
- wdata_i

**Generated File:** T3_ariane_regfile_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- rdata_o
- wdata_i
- rdata_o
- wdata_i

**Payload Signals (4):**
- rdata_o
- wdata_i
- rdata_o
- wdata_i

**Generated File:** T4_ariane_regfile_Covert.sv

---

