# Trojan Generation Summary

**Module:** wt_dcache_ctrl
**File:** wt_dcache_ctrl.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (13):**
- cache_en_i
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- ... and 8 more

**Payload Signals (13):**
- cache_en_i
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- ... and 8 more

**Generated File:** T1_wt_dcache_ctrl_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- miss_we_o
- miss_we_o

**Payload Signals (6):**
- miss_wdata_o
- miss_paddr_o
- rd_data_i
- miss_wdata_o
- miss_paddr_o
- ... and 1 more

**Generated File:** T2_wt_dcache_ctrl_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (6):**
- miss_wdata_o
- miss_paddr_o
- rd_data_i
- miss_wdata_o
- miss_paddr_o
- ... and 1 more

**Payload Signals (4):**
- miss_wdata_o
- rd_data_i
- miss_wdata_o
- rd_data_i

**Generated File:** T3_wt_dcache_ctrl_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- dcache_req_i_t
- req_port_i
- dcache_req_o_t
- req_port_o
- miss_req_o
- ... and 5 more

**Payload Signals (4):**
- miss_ack_i
- rd_ack_i
- miss_ack_i
- rd_ack_i

**Generated File:** T4_wt_dcache_ctrl_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- miss_wdata_o
- rd_data_i
- miss_wdata_o
- rd_data_i

**Payload Signals (4):**
- miss_wdata_o
- rd_data_i
- miss_wdata_o
- rd_data_i

**Generated File:** T5_wt_dcache_ctrl_Covert.sv

---

