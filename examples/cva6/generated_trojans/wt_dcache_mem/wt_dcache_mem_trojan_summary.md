# Trojan Generation Summary

**Module:** wt_dcache_mem
**File:** wt_dcache_mem.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- cmp_en_d
- rd_req

**Payload Signals (2):**
- cmp_en_d
- rd_req

**Generated File:** T1_wt_dcache_mem_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- rd_req

**Payload Signals (2):**
- wr_ack_o
- rd_acked

**Generated File:** T2_wt_dcache_mem_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- vld_we

**Payload Signals (0):**

**Generated File:** T3_wt_dcache_mem_Privilege.sv

---

