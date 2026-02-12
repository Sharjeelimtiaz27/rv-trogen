# Trojan Generation Summary

**Module:** id_stage
**File:** id_stage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (26):**
- debug_req_i
- fetch_entry_valid_i
- fetch_entry_ready_o
- issue_entry_valid_o
- compressed_ready_i
- ... and 21 more

**Payload Signals (24):**
- debug_req_i
- fetch_entry_valid_i
- fetch_entry_ready_o
- issue_entry_valid_o
- compressed_ready_i
- ... and 19 more

**Generated File:** T1_id_stage_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- debug_req_i
- debug_mode_i
- debug_from_trigger_i
- debug_mode_i
- debug_from_trigger_i

**Payload Signals (1):**
- jump_address

**Generated File:** T2_id_stage_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- debug_mode_i
- debug_mode_i
- jump_address

**Payload Signals (6):**
- riscv::priv_lvl_t
- priv_lvl_i
- debug_mode_i
- riscv::priv_lvl_t
- priv_lvl_i
- ... and 1 more

**Generated File:** T3_id_stage_Privilege.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (22):**
- debug_req_i
- fetch_entry_valid_i
- issue_entry_valid_o
- compressed_valid_o
- x_compressed_req_t
- ... and 17 more

**Payload Signals (17):**
- fetch_entry_valid_i
- fetch_entry_ready_o
- issue_entry_valid_o
- issue_instr_ack_i
- compressed_ready_i
- ... and 12 more

**Generated File:** T4_id_stage_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- fetch_entry_t
- fetch_entry_i
- fetch_entry_valid_i
- fetch_entry_ready_o
- fetch_entry_ready_o

**Payload Signals (11):**
- fetch_entry_valid_i
- fetch_entry_ready_o
- issue_entry_valid_o
- compressed_ready_i
- compressed_valid_o
- ... and 6 more

**Generated File:** T5_id_stage_Covert.sv

---

