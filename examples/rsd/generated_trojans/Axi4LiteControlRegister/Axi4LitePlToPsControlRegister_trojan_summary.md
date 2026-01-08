# Trojan Generation Summary

**Module:** Axi4LitePlToPsControlRegister
**File:** Axi4LiteControlRegister.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- axi_arready
- axi_rvalid
- slv_reg_rden
- generation
- axi_awready
- ... and 4 more

**Payload Signals (10):**
- axi_arready
- axi_rvalid
- slv_reg_rden
- generation
- done
- ... and 5 more

**Generated File:** T1_Axi4LitePlToPsControlRegister_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- axi_rvalid
- pop
- axi_bvalid

**Payload Signals (6):**
- axi_arready
- axi_rvalid
- done
- axi_awready
- axi_wready
- ... and 1 more

**Generated File:** T2_Axi4LitePlToPsControlRegister_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (3):**
- AddrPath
- slv_reg_rden
- slv_reg_wren

**Generated File:** T3_Axi4LitePlToPsControlRegister_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- we
- AddrPath
- memory_we

**Payload Signals (0):**

**Generated File:** T4_Axi4LitePlToPsControlRegister_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- AddrPath
- pop

**Payload Signals (0):**

**Generated File:** T5_Axi4LitePlToPsControlRegister_Integrity.sv

---

