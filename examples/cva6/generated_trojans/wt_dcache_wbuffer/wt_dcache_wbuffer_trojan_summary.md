# Trojan Generation Summary

**Module:** wt_dcache_wbuffer
**File:** wt_dcache_wbuffer.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (7):**
- cache_en_i
- dcache_req_i_t
- dcache_req_o_t
- miss_req_o
- rd_req_o
- ... and 2 more

**Payload Signals (7):**
- cache_en_i
- dcache_req_i_t
- dcache_req_o_t
- miss_req_o
- rd_req_o
- ... and 2 more

**Generated File:** T1_wt_dcache_wbuffer_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- dcache_req_i_t
- dcache_req_o_t
- miss_req_o
- rd_req_o

**Payload Signals (3):**
- miss_ack_i
- rd_ack_i
- wr_ack_i

**Generated File:** T2_wt_dcache_wbuffer_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- miss_we_o

**Payload Signals (0):**

**Generated File:** T3_wt_dcache_wbuffer_Privilege.sv

---

