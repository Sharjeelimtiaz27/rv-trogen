# Trojan Generation Summary

**Module:** pmp_entry
**File:** pmp_entry.sv
**Type:** Combinational
**Total Candidates:** 2

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- riscv::pmp_addr_mode_t
- conf_addr_mode_i

**Payload Signals (6):**
- addr_i
- conf_addr_i
- conf_addr_prev_i
- riscv::pmp_addr_mode_t
- conf_addr_mode_i
- ... and 1 more

**Generated File:** T1_pmp_entry_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- addr_i
- conf_addr_i
- conf_addr_prev_i
- riscv::pmp_addr_mode_t
- conf_addr_mode_i
- ... and 1 more

**Payload Signals (2):**
- riscv::pmp_addr_mode_t
- conf_addr_mode_i

**Generated File:** T2_pmp_entry_Privilege.sv

---

