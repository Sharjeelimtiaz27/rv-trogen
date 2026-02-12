# Trojan Generation Summary

**Module:** Axi4LiteDualPortBlockRAM
**File:** Axi4LiteMemory.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- axi_bvalid
- axi_rvalid

**Payload Signals (2):**
- axi_bvalid
- axi_rvalid

**Generated File:** T1_Axi4LiteDualPortBlockRAM_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- axi_awaddr
- axi_araddr
- axi_rdata
- reg_data_out

**Payload Signals (2):**
- axi_rdata
- reg_data_out

**Generated File:** T2_Axi4LiteDualPortBlockRAM_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- axi_bvalid
- axi_rvalid

**Payload Signals (2):**
- axi_bvalid
- axi_rvalid

**Generated File:** T3_Axi4LiteDualPortBlockRAM_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- axi_rdata
- reg_data_out

**Payload Signals (4):**
- axi_bvalid
- axi_rdata
- axi_rvalid
- reg_data_out

**Generated File:** T4_Axi4LiteDualPortBlockRAM_Covert.sv

---

