# Trojan Generation Summary

**Module:** axi_adapter
**File:** axi_adapter.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (12):**
- req_i
- ariane_pkg::ad_req_t
- we_i
- valid_o
- critical_word_valid_o
- ... and 7 more

**Payload Signals (12):**
- req_i
- ariane_pkg::ad_req_t
- we_i
- valid_o
- critical_word_valid_o
- ... and 7 more

**Generated File:** T1_axi_adapter_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- we_i
- we_i

**Payload Signals (8):**
- addr_i
- wdata_i
- rdata_o
- addr_i
- wdata_i
- ... and 3 more

**Generated File:** T2_axi_adapter_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- addr_i
- wdata_i
- rdata_o
- addr_i
- wdata_i
- ... and 2 more

**Payload Signals (6):**
- wdata_i
- rdata_o
- wdata_i
- rdata_o
- outstanding_aw_cnt_t
- ... and 1 more

**Generated File:** T3_axi_adapter_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (11):**
- req_i
- ariane_pkg::ad_req_t
- valid_o
- critical_word_valid_o
- axi_req_t
- ... and 6 more

**Payload Signals (6):**
- gnt_o
- valid_o
- critical_word_valid_o
- gnt_o
- valid_o
- ... and 1 more

**Generated File:** T4_axi_adapter_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- wdata_i
- rdata_o
- wdata_i
- rdata_o

**Payload Signals (10):**
- wdata_i
- valid_o
- rdata_o
- critical_word_valid_o
- wdata_i
- ... and 5 more

**Generated File:** T5_axi_adapter_Covert.sv

---

