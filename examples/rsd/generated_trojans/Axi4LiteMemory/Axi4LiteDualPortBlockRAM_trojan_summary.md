# Trojan Generation Summary

**Module:** Axi4LiteDualPortBlockRAM
**File:** Axi4LiteMemory.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- axi_awready
- axi_wready
- axi_bvalid
- axi_arready
- axi_rvalid
- ... and 4 more

**Payload Signals (9):**
- axi_awready
- axi_wready
- axi_bvalid
- axi_arready
- axi_rvalid
- ... and 4 more

**Generated File:** T1_Axi4LiteDualPortBlockRAM_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- axi_bvalid
- axi_rvalid

**Payload Signals (5):**
- axi_awready
- axi_wready
- axi_bvalid
- axi_arready
- axi_rvalid

**Generated File:** T2_Axi4LiteDualPortBlockRAM_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- slv_reg_rden
- slv_reg_wren

**Generated File:** T3_Axi4LiteDualPortBlockRAM_Leak.sv

---

