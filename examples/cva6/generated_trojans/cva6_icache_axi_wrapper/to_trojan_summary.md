# Trojan Generation Summary

**Module:** to
**File:** cva6_icache_axi_wrapper.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (20):**
- en_i
- icache_areq_t
- areq_i
- areq_o
- icache_dreq_t
- ... and 15 more

**Payload Signals (20):**
- en_i
- icache_areq_t
- areq_i
- areq_o
- icache_dreq_t
- ... and 15 more

**Generated File:** T1_to_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- axi_rd_addr

**Payload Signals (2):**
- riscv::priv_lvl_t
- priv_lvl_i

**Generated File:** T2_to_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- icache_mem_data_req
- icache_mem_data_ack
- axi_rd_addr
- axi_rd_data

**Payload Signals (4):**
- icache_mem_data_req
- icache_mem_data_ack
- axi_rd_data
- axi_rd_id_out

**Generated File:** T3_to_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (19):**
- icache_areq_t
- areq_i
- areq_o
- icache_dreq_t
- dreq_i
- ... and 14 more

**Payload Signals (1):**
- axi_rd_valid

**Generated File:** T4_to_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- icache_mem_data_req
- icache_mem_data_ack
- axi_rd_data

**Payload Signals (5):**
- icache_mem_data_req
- icache_mem_data_ack
- axi_rd_valid
- axi_rd_data
- axi_rd_id_out

**Generated File:** T5_to_Covert.sv

---

