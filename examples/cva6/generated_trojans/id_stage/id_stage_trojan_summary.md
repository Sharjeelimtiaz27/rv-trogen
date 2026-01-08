# Trojan Generation Summary

**Module:** id_stage
**File:** id_stage.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (11):**
- debug_req_i
- fetch_entry_t
- compressed_ready_i
- debug_from_trigger_i
- dcache_req_o_t
- ... and 6 more

**Payload Signals (10):**
- debug_req_i
- fetch_entry_t
- compressed_ready_i
- dcache_req_o_t
- scoreboard_entry_t
- ... and 5 more

**Generated File:** T1_id_stage_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- irq_ctrl_t
- debug_mode_i
- is_ctrl_flow

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T2_id_stage_Privilege.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- debug_req_i
- debug_from_trigger_i
- dcache_req_o_t
- compressed_valid_o
- x_compressed_req_t
- ... and 2 more

**Payload Signals (6):**
- compressed_ready_i
- compressed_valid_o
- valid
- stall_macro_deco
- stall_macro_deco_zcmp
- ... and 1 more

**Generated File:** T3_id_stage_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fetch_entry_t

**Payload Signals (3):**
- debug_req_i
- debug_mode_i
- debug_from_trigger_i

**Generated File:** T4_id_stage_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- debug_req_i
- irq_ctrl_t
- debug_mode_i
- debug_from_trigger_i
- is_ctrl_flow

**Payload Signals (0):**

**Generated File:** T5_id_stage_Leak.sv

---

