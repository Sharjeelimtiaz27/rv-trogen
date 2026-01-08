# Trojan Generation Summary

**Module:** to
**File:** wt_l15_adapter.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (11):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- l15_req_t
- ... and 6 more

**Payload Signals (11):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- l15_req_t
- ... and 6 more

**Generated File:** T1_to_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- l15_data_next_entry

**Payload Signals (14):**
- icache_data_req_i
- dcache_data_req_i
- icache_data_ack_o
- dcache_data_ack_o
- l15_address
- ... and 9 more

**Generated File:** T2_to_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (15):**
- icache_data_req_i
- dcache_data_req_i
- icache_data_ack_o
- dcache_data_ack_o
- l15_address
- ... and 10 more

**Payload Signals (14):**
- icache_data_req_i
- dcache_data_req_i
- icache_data_ack_o
- dcache_data_ack_o
- l15_blockstore
- ... and 9 more

**Generated File:** T3_to_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (21):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- icache_data_ack_o
- ... and 16 more

**Payload Signals (7):**
- icache_data_ack_o
- dcache_data_ack_o
- l15_req_ack
- l15_invalidate_cacheline
- l15_ack
- ... and 2 more

**Generated File:** T4_to_Availability.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- l15_address
- l15_inval_address_15_4

**Payload Signals (0):**

**Generated File:** T5_to_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (13):**
- icache_data_req_i
- dcache_data_req_i
- icache_data_ack_o
- dcache_data_ack_o
- l15_prefetch
- ... and 8 more

**Payload Signals (0):**

**Generated File:** T6_to_Covert.sv

---

