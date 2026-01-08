# Trojan Generation Summary

**Module:** to
**File:** wt_axi_adapter.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (14):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- inval_valid_i
- ... and 9 more

**Payload Signals (14):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- inval_valid_i
- ... and 9 more

**Generated File:** T1_to_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (9):**
- icache_data_req_i
- dcache_data_req_i
- inval_addr_i
- icache_data_ack_o
- dcache_data_ack_o
- ... and 4 more

**Payload Signals (6):**
- icache_data_req_i
- dcache_data_req_i
- icache_data_ack_o
- dcache_data_ack_o
- icache_data_full
- ... and 1 more

**Generated File:** T2_to_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (17):**
- icache_data_req_i
- icache_req_t
- dcache_data_req_i
- dcache_req_t
- inval_valid_i
- ... and 12 more

**Payload Signals (6):**
- inval_valid_i
- icache_data_ack_o
- dcache_data_ack_o
- inval_ready_o
- axi_wr_valid
- ... and 1 more

**Generated File:** T3_to_Availability.sv

---

### T4: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (7):**
- icache_data_req_i
- dcache_data_req_i
- inval_addr_i
- icache_data_ack_o
- dcache_data_ack_o
- ... and 2 more

**Generated File:** T4_to_Leak.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- inval_addr_i

**Payload Signals (0):**

**Generated File:** T5_to_Privilege.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- icache_data_req_i
- dcache_data_req_i
- icache_data_ack_o
- dcache_data_ack_o
- icache_data_full
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T6_to_Covert.sv

---

