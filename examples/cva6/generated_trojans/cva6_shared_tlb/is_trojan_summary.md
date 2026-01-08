# Trojan Generation Summary

**Module:** is
**File:** cva6_shared_tlb.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- s_st_enbl_i
- g_st_enbl_i
- s_ld_st_enbl_i
- g_ld_st_enbl_i
- itlb_req_o
- ... and 3 more

**Payload Signals (8):**
- s_st_enbl_i
- g_st_enbl_i
- s_ld_st_enbl_i
- g_ld_st_enbl_i
- itlb_req_o
- ... and 3 more

**Generated File:** T1_is_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- itlb_req_o
- itlb_req_d
- dtlb_req_d
- all_ways_valid

**Payload Signals (1):**
- all_ways_valid

**Generated File:** T2_is_Availability.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- output

**Generated File:** T3_is_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (4):**
- itlb_access_i
- dtlb_access_i
- shared_tlb_access_o
- shared_tlb_access_q

**Payload Signals (0):**

**Generated File:** T4_is_Covert.sv

---

