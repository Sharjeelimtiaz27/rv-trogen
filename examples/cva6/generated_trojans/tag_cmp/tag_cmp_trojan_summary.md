# Trojan Generation Summary

**Module:** tag_cmp
**File:** tag_cmp.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- req_i
- we_i
- req_o
- we_o
- we_i
- ... and 2 more

**Payload Signals (7):**
- req_i
- we_i
- req_o
- we_o
- we_i
- ... and 2 more

**Generated File:** T1_tag_cmp_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- we_i
- we_o
- we_i
- we_o

**Payload Signals (20):**
- addr_i
- l_data_t
- wdata_i
- l_data_t
- rdata_o
- ... and 15 more

**Generated File:** T2_tag_cmp_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (21):**
- addr_i
- l_data_t
- wdata_i
- l_data_t
- rdata_o
- ... and 16 more

**Payload Signals (16):**
- l_data_t
- wdata_i
- l_data_t
- rdata_o
- l_data_t
- ... and 11 more

**Generated File:** T3_tag_cmp_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- req_i
- req_o
- req_o

**Payload Signals (2):**
- gnt_o
- gnt_o

**Generated File:** T4_tag_cmp_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (16):**
- l_data_t
- wdata_i
- l_data_t
- rdata_o
- l_data_t
- ... and 11 more

**Payload Signals (16):**
- l_data_t
- wdata_i
- l_data_t
- rdata_o
- l_data_t
- ... and 11 more

**Generated File:** T5_tag_cmp_Covert.sv

---

