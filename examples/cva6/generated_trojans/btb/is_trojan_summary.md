# Trojan Generation Summary

**Module:** is
**File:** btb.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- btb_ram_we_prediction
- btb_ram_we_update

**Payload Signals (2):**
- btb_ram_we_prediction
- btb_ram_we_update

**Generated File:** T1_is_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- debug_mode_i
- btb_ram_we_prediction
- btb_ram_we_update

**Payload Signals (5):**
- btb_ram_addr_prediction
- btb_ram_wdata_prediction
- btb_ram_rdata_prediction
- btb_ram_addr_update
- btb_ram_wdata_update

**Generated File:** T2_is_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (5):**
- debug_mode_i
- btb_ram_we_prediction
- btb_ram_addr_prediction
- btb_ram_we_update
- btb_ram_addr_update

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_is_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (7):**
- btb_ram_csel_prediction
- btb_ram_addr_prediction
- btb_ram_wdata_prediction
- btb_ram_rdata_prediction
- btb_ram_csel_update
- ... and 2 more

**Payload Signals (3):**
- btb_ram_wdata_prediction
- btb_ram_rdata_prediction
- btb_ram_wdata_update

**Generated File:** T4_is_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- btb_ram_wdata_prediction
- btb_ram_rdata_prediction
- btb_ram_wdata_update

**Payload Signals (3):**
- btb_ram_wdata_prediction
- btb_ram_rdata_prediction
- btb_ram_wdata_update

**Generated File:** T5_is_Covert.sv

---

