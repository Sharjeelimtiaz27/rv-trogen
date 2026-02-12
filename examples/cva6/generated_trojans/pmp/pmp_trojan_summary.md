# Trojan Generation Summary

**Module:** pmp
**File:** pmp.sv
**Type:** Combinational
**Total Candidates:** 1

---

## Generated Trojans

### T1: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- addr_i
- conf_addr_i
- conf_addr_prev

**Payload Signals (2):**
- riscv::priv_lvl_t
- priv_lvl_i

**Generated File:** T1_pmp_Privilege.sv

---

