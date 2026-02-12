# Trojan Generation Summary

**Module:** ariane_regfile_fpga
**File:** ariane_regfile_fpga.sv
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

**Generated File:** T1_ariane_regfile_fpga_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- test_en_i
- we_i
- we_i
- we_dec
- read_after_write

**Payload Signals (11):**
- raddr_i
- rdata_o
- waddr_i
- wdata_i
- rdata_o
- ... and 6 more

**Generated File:** T2_ariane_regfile_fpga_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (13):**
- raddr_i
- rdata_o
- waddr_i
- wdata_i
- rdata_o
- ... and 8 more

**Payload Signals (6):**
- rdata_o
- wdata_i
- rdata_o
- wdata_i
- wdata_reg
- ... and 1 more

**Generated File:** T3_ariane_regfile_fpga_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- rdata_o
- wdata_i
- rdata_o
- wdata_i
- wdata_reg

**Payload Signals (5):**
- rdata_o
- wdata_i
- rdata_o
- wdata_i
- wdata_reg

**Generated File:** T4_ariane_regfile_fpga_Covert.sv

---

