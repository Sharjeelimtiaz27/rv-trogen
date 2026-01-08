# Trojan Generation Summary

**Module:** cva6_icache
**File:** cva6_icache.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (13):**
- en_i
- icache_areq_t
- icache_dreq_t
- mem_data_req_o
- icache_req_t
- ... and 8 more

**Payload Signals (13):**
- en_i
- icache_areq_t
- icache_dreq_t
- mem_data_req_o
- icache_req_t
- ... and 8 more

**Generated File:** T1_cva6_icache_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- mem_data_ack_i
- mem_data_req_o
- paddr_is_nc
- addr_ni

**Payload Signals (2):**
- mem_data_ack_i
- mem_data_req_o

**Generated File:** T2_cva6_icache_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- icache_areq_t
- icache_dreq_t
- mem_data_ack_i
- mem_data_req_o
- icache_req_t
- ... and 2 more

**Payload Signals (3):**
- mem_data_ack_i
- valid
- all_ways_valid

**Generated File:** T3_cva6_icache_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (4):**
- mem_data_ack_i
- mem_data_req_o
- paddr_is_nc
- addr_ni

**Generated File:** T4_cva6_icache_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- paddr_is_nc
- cl_we
- vld_we
- addr_ni

**Payload Signals (0):**

**Generated File:** T5_cva6_icache_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- mem_data_ack_i
- mem_data_req_o

**Payload Signals (0):**

**Generated File:** T6_cva6_icache_Covert.sv

---

