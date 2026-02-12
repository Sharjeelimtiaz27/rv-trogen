# Trojan Generation Summary

**Module:** is
**File:** cva6_shared_tlb.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- itlb_req_o
- itlb_req_o
- shared_tag_valid
- tag_req
- tag_we
- ... and 4 more

**Payload Signals (9):**
- itlb_req_o
- itlb_req_o
- shared_tag_valid
- tag_req
- tag_we
- ... and 4 more

**Generated File:** T1_is_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- tag_we
- pte_we

**Payload Signals (15):**
- itlb_vaddr_i
- dtlb_vaddr_i
- shared_tlb_vaddr_o
- shared_tlb_vaddr_o
- out
- ... and 10 more

**Generated File:** T2_is_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- itlb_vaddr_i
- dtlb_vaddr_i
- shared_tlb_vaddr_o
- shared_tlb_vaddr_o
- tag_wr_addr
- ... and 9 more

**Payload Signals (5):**
- out
- tag_wr_data
- tag_rd_data
- pte_wr_data
- pte_rd_data

**Generated File:** T3_is_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- itlb_req_o
- itlb_req_o
- shared_tag_valid
- tag_req
- pte_req
- ... and 2 more

**Payload Signals (3):**
- shared_tag_valid
- way_valid
- all_ways_valid

**Generated File:** T4_is_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- itlb_access_i
- dtlb_access_i
- shared_tlb_access_o
- shared_tlb_access_o
- tag_wr_data
- ... and 3 more

**Payload Signals (8):**
- out
- shared_tag_valid
- tag_wr_data
- tag_rd_data
- pte_wr_data
- ... and 3 more

**Generated File:** T5_is_Covert.sv

---

