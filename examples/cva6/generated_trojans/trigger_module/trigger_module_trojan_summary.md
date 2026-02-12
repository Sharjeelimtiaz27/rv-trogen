# Trojan Generation Summary

**Module:** trigger_module
**File:** trigger_module.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- tselect_we
- tdata1_we
- tdata2_we
- tdata3_we
- break_from_trigger_o
- ... and 3 more

**Payload Signals (4):**
- tselect_we
- tdata1_we
- tdata2_we
- tdata3_we

**Generated File:** T1_trigger_module_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (9):**
- debug_mode_i
- tselect_we
- tdata1_we
- tdata2_we
- tdata3_we
- ... and 4 more

**Payload Signals (14):**
- vaddr_from_lsu_i
- store_result_i
- tdata1_i
- tdata2_i
- tdata3_i
- ... and 9 more

**Generated File:** T2_trigger_module_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- debug_mode_i
- vaddr_from_lsu_i
- tselect_we
- tdata1_we
- tdata2_we
- ... and 1 more

**Payload Signals (3):**
- riscv::priv_lvl_t
- priv_lvl_i
- debug_mode_i

**Generated File:** T3_trigger_module_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (17):**
- vaddr_from_lsu_i
- tdata1_i
- tdata2_i
- tdata3_i
- tselect_i
- ... and 12 more

**Payload Signals (13):**
- store_result_i
- tdata1_i
- tdata2_i
- tdata3_i
- tdata1_we
- ... and 8 more

**Generated File:** T4_trigger_module_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (6):**
- vaddr_from_lsu_i
- store_result_i
- break_from_trigger_o
- debug_from_trigger_o
- break_from_trigger_o
- ... and 1 more

**Payload Signals (1):**
- commit_ack_i

**Generated File:** T5_trigger_module_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (12):**
- tdata1_i
- tdata2_i
- tdata3_i
- tdata1_we
- tdata2_we
- ... and 7 more

**Payload Signals (13):**
- store_result_i
- tdata1_i
- tdata2_i
- tdata3_i
- tdata1_we
- ... and 8 more

**Generated File:** T6_trigger_module_Covert.sv

---

