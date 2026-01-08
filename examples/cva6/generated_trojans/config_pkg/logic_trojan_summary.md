# Trojan Generation Summary

**Module:** logic
**File:** config_pkg.sv
**Type:** Combinational
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- len
- is_inside_nonidempotent_regions

**Payload Signals (2):**
- len
- is_inside_nonidempotent_regions

**Generated File:** T1_logic_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (7):**
- DmBaseAddress
- HaltAddress
- ExceptionAddress
- address
- is_inside_nonidempotent_regions
- ... and 2 more

**Generated File:** T2_logic_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- DmBaseAddress
- HaltAddress
- ExceptionAddress
- address

**Payload Signals (0):**

**Generated File:** T3_logic_Integrity.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.40
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- DmBaseAddress
- HaltAddress
- ExceptionAddress
- address

**Payload Signals (0):**

**Generated File:** T4_logic_Privilege.sv

---

