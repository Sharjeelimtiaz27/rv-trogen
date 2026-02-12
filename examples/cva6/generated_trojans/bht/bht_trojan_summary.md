# Trojan Generation Summary

**Module:** bht
**File:** bht.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- valid
- bht_updated_valid

**Payload Signals (2):**
- valid
- bht_updated_valid

**Generated File:** T1_bht_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (4):**
- bht_ram_read_address_0
- bht_ram_read_address_1
- bht_ram_rdata_0
- bht_ram_rdata_1

**Generated File:** T2_bht_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (3):**
- debug_mode_i
- bht_ram_read_address_0
- bht_ram_read_address_1

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_bht_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- bht_ram_read_address_0
- bht_ram_read_address_1
- bht_ram_rdata_0
- bht_ram_rdata_1

**Payload Signals (2):**
- bht_ram_rdata_0
- bht_ram_rdata_1

**Generated File:** T4_bht_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- valid
- bht_updated_valid

**Payload Signals (2):**
- valid
- bht_updated_valid

**Generated File:** T5_bht_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (2):**
- bht_ram_rdata_0
- bht_ram_rdata_1

**Payload Signals (4):**
- valid
- bht_ram_rdata_0
- bht_ram_rdata_1
- bht_updated_valid

**Generated File:** T6_bht_Covert.sv

---

