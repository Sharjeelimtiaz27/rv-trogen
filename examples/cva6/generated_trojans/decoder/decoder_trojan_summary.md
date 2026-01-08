# Trojan Generation Summary

**Module:** decoder
**File:** decoder.sv
**Type:** Combinational
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- debug_req_i
- debug_from_trigger_i
- scoreboard_entry_t

**Payload Signals (2):**
- debug_req_i
- scoreboard_entry_t

**Generated File:** T1_decoder_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- irq_ctrl_t
- debug_mode_i
- is_control_flow_instr_o
- acc_is_control_flow_instr

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T2_decoder_Privilege.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (6):**
- debug_req_i
- irq_ctrl_t
- debug_mode_i
- debug_from_trigger_i
- is_control_flow_instr_o
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T3_decoder_Leak.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (3):**
- debug_req_i
- debug_mode_i
- debug_from_trigger_i

**Generated File:** T4_decoder_Covert.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.40
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- debug_req_i
- debug_from_trigger_i

**Payload Signals (0):**

**Generated File:** T5_decoder_Availability.sv

---

