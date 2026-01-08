# Trojan Generation Summary

**Module:** cva6_accel_first_pass_decoder
**File:** cva6_accel_first_pass_decoder_stub.sv
**Type:** Combinational
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- scoreboard_entry_t

**Payload Signals (1):**
- scoreboard_entry_t

**Generated File:** T1_cva6_accel_first_pass_decoder_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- is_control_flow_instr_o

**Payload Signals (0):**

**Generated File:** T2_cva6_accel_first_pass_decoder_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.40
**Description:** Escalates privilege level to machine mode

**Trigger Signals (1):**
- is_control_flow_instr_o

**Payload Signals (0):**

**Generated File:** T3_cva6_accel_first_pass_decoder_Privilege.sv

---

