# Trojan Generation Summary

**Module:** cva6
**File:** cva6.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (57):**
- debug_req_i
- cvxif_req_t
- cvxif_req_o
- noc_req_t
- noc_req_o
- ... and 52 more

**Payload Signals (57):**
- debug_req_i
- cvxif_req_t
- cvxif_req_o
- noc_req_t
- noc_req_o
- ... and 52 more

**Generated File:** T1_cva6_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (15):**
- debug_req_i
- mode
- data_we
- csr_valid_id_ex
- x_we_ex_id
- ... and 10 more

**Payload Signals (51):**
- boot_addr_i
- predict_address
- fetch_paddr
- fetch_vaddr
- vaddr
- ... and 46 more

**Generated File:** T2_cva6_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (31):**
- boot_addr_i
- predict_address
- fetch_paddr
- fetch_vaddr
- vaddr
- ... and 26 more

**Payload Signals (2):**
- mode
- debug_mode

**Generated File:** T3_cva6_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (39):**
- boot_addr_i
- predict_address
- fetch_paddr
- fetch_vaddr
- vaddr
- ... and 34 more

**Payload Signals (29):**
- data
- result
- data_wdata
- data_wuser
- data_req
- ... and 24 more

**Generated File:** T4_cva6_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (54):**
- debug_req_i
- cvxif_req_t
- cvxif_req_o
- noc_req_t
- noc_req_o
- ... and 49 more

**Payload Signals (42):**
- valid
- fetch_valid
- ex_valid
- tag_valid
- data_rvalid
- ... and 37 more

**Generated File:** T5_cva6_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (20):**
- data
- data_wdata
- data_wuser
- data_req
- data_we
- ... and 15 more

**Payload Signals (65):**
- valid
- fetch_valid
- data
- result
- ex_valid
- ... and 60 more

**Generated File:** T6_cva6_Covert.sv

---

