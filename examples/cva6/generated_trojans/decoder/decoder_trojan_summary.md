# Trojan Generation Summary

**Module:** decoder
**File:** decoder.sv
**Type:** Combinational
**Total Candidates:** 3

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- debug_req_i
- debug_mode_i
- debug_from_trigger_i
- debug_from_trigger_i

**Payload Signals (1):**
- jump_address_i

**Generated File:** T1_decoder_Leak.sv

---

### T2: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- debug_req_i
- debug_from_trigger_i
- debug_from_trigger_i

**Payload Signals (1):**
- debug_req_i

**Generated File:** T2_decoder_DoS.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- jump_address_i
- debug_mode_i

**Payload Signals (3):**
- riscv::priv_lvl_t
- priv_lvl_i
- debug_mode_i

**Generated File:** T3_decoder_Privilege.sv

---

