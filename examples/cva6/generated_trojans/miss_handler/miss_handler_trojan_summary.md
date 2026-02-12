# Trojan Generation Summary

**Module:** miss_handler
**File:** miss_handler.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (43):**
- miss_req_i
- bypass_valid_o
- axi_req_t
- active_serving_o
- critical_word_valid_o
- ... and 38 more

**Payload Signals (43):**
- miss_req_i
- bypass_valid_o
- axi_req_t
- active_serving_o
- critical_word_valid_o
- ... and 38 more

**Generated File:** T1_miss_handler_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- we_o
- we_o
- miss_req_we
- req_fsm_miss_we

**Payload Signals (24):**
- bypass_data_o
- axi_data_o
- axi_data_i
- mshr_addr_i
- mshr_addr_matches_o
- ... and 19 more

**Generated File:** T2_miss_handler_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (25):**
- bypass_data_o
- axi_data_o
- axi_data_i
- mshr_addr_i
- mshr_addr_matches_o
- ... and 20 more

**Payload Signals (14):**
- bypass_data_o
- axi_data_o
- axi_data_i
- data_o
- data_i
- ... and 9 more

**Generated File:** T3_miss_handler_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (40):**
- miss_req_i
- bypass_valid_o
- axi_req_t
- critical_word_valid_o
- axi_req_t
- ... and 35 more

**Payload Signals (17):**
- flush_ack_o
- busy_i
- bypass_gnt_o
- bypass_valid_o
- miss_gnt_o
- ... and 12 more

**Generated File:** T4_miss_handler_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (13):**
- bypass_data_o
- axi_data_o
- axi_data_i
- data_o
- data_i
- ... and 8 more

**Payload Signals (25):**
- busy_i
- bypass_valid_o
- bypass_data_o
- critical_word_valid_o
- axi_data_o
- ... and 20 more

**Generated File:** T5_miss_handler_Covert.sv

---

