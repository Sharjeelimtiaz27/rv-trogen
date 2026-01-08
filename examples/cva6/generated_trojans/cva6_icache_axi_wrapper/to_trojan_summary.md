# Trojan Generation Summary

**Module:** to
**File:** cva6_icache_axi_wrapper.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- en_i
- icache_areq_t
- icache_dreq_t
- axi_req_t
- icache_mem_data_req
- ... and 3 more

**Payload Signals (8):**
- en_i
- icache_areq_t
- icache_dreq_t
- axi_req_t
- icache_mem_data_req
- ... and 3 more

**Generated File:** T1_to_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- icache_mem_data_req
- icache_mem_data_ack

**Payload Signals (2):**
- icache_mem_data_req
- icache_mem_data_ack

**Generated File:** T2_to_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- icache_areq_t
- icache_dreq_t
- axi_req_t
- icache_mem_data_req
- icache_mem_data_ack
- ... and 3 more

**Payload Signals (3):**
- icache_mem_data_ack
- axi_rd_valid
- req_valid_d

**Generated File:** T3_to_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- icache_mem_data_req
- icache_mem_data_ack

**Generated File:** T4_to_Leak.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- icache_mem_data_req
- icache_mem_data_ack

**Payload Signals (0):**

**Generated File:** T5_to_Covert.sv

---

