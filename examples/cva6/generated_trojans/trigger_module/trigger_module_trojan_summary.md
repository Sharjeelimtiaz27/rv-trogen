# Trojan Generation Summary

**Module:** trigger_module
**File:** trigger_module.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (6):**
- scoreboard_entry_t
- break_from_trigger_o
- debug_from_trigger_o
- trigger_type_q
- break_from_trigger_q
- ... and 1 more

**Payload Signals (1):**
- scoreboard_entry_t

**Generated File:** T1_trigger_module_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (5):**
- debug_mode_i
- debug_from_trigger_o
- debug_from_mcontrol_o
- mcontrol6_debug_d
- debug_from_trigger_q

**Payload Signals (4):**
- tdata1_we
- tdata2_we
- tdata3_we
- mret_reg_q

**Generated File:** T2_trigger_module_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (7):**
- debug_mode_i
- tselect_we
- tdata1_we
- tdata2_we
- tdata3_we
- ... and 2 more

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_trigger_module_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- tselect_we
- tdata1_we
- tdata2_we
- tdata3_we

**Payload Signals (3):**
- tdata1_we
- tdata2_we
- tdata3_we

**Generated File:** T4_trigger_module_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- tdata1_we
- tdata2_we
- tdata3_we

**Payload Signals (5):**
- debug_mode_i
- debug_from_trigger_o
- debug_from_mcontrol_o
- mcontrol6_debug_d
- debug_from_trigger_q

**Generated File:** T5_trigger_module_Covert.sv

---

### T6: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (8):**
- tdata1_we
- tdata2_we
- tdata3_we
- break_from_trigger_o
- debug_from_trigger_o
- ... and 3 more

**Payload Signals (0):**

**Generated File:** T6_trigger_module_Availability.sv

---

