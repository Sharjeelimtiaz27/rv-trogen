# Trojan Generation Summary

**Module:** interfaces
**File:** frontend.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (10):**
- halt_frontend_i
- ex_valid_i
- icache_dreq_t
- fetch_entry_t
- valid
- ... and 5 more

**Payload Signals (10):**
- halt_frontend_i
- ex_valid_i
- icache_dreq_t
- fetch_entry_t
- valid
- ... and 5 more

**Generated File:** T1_interfaces_DoS.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T2_interfaces_Privilege.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- ex_valid_i
- icache_dreq_t
- valid
- icache_valid_q
- bp_valid

**Payload Signals (6):**
- ex_valid_i
- valid
- icache_valid_q
- instr_queue_ready
- if_ready
- ... and 1 more

**Generated File:** T3_interfaces_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- fetch_entry_t
- npc_rst_load_q

**Payload Signals (2):**
- set_debug_pc_i
- debug_mode_i

**Generated File:** T4_interfaces_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- set_debug_pc_i
- debug_mode_i

**Payload Signals (0):**

**Generated File:** T5_interfaces_Leak.sv

---

