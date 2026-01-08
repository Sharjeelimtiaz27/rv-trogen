# Trojan Generation Summary

**Module:** cva6_rvfi_probes
**File:** cva6_rvfi_probes.sv
**Type:** Combinational
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- lsu_ctrl_t
- debug_mode_i

**Payload Signals (1):**
- rvfi_probes_csr_t

**Generated File:** T1_cva6_rvfi_probes_Leak.sv

---

### T2: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- scoreboard_entry_t

**Payload Signals (1):**
- scoreboard_entry_t

**Generated File:** T2_cva6_rvfi_probes_DoS.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- lsu_ctrl_t
- debug_mode_i
- rvfi_probes_csr_t

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_cva6_rvfi_probes_Privilege.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T4_cva6_rvfi_probes_Covert.sv

---

