# Trojan Generation Summary

**Module:** interfaces
**File:** frontend.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- ex_valid_i
- icache_dreq_t
- icache_dreq_o
- icache_dreq_i
- fetch_entry_valid_o
- ... and 10 more

**Payload Signals (15):**
- ex_valid_i
- icache_dreq_t
- icache_dreq_o
- icache_dreq_i
- fetch_entry_valid_o
- ... and 10 more

**Generated File:** T1_interfaces_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- set_debug_pc_i
- debug_mode_i

**Payload Signals (10):**
- boot_addr_i
- target_address
- icache_data_q
- icache_vaddr_q
- icache_gpaddr_q
- ... and 5 more

**Generated File:** T2_interfaces_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (9):**
- boot_addr_i
- debug_mode_i
- target_address
- icache_vaddr_q
- icache_gpaddr_q
- ... and 4 more

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_interfaces_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- boot_addr_i
- target_address
- icache_data_q
- icache_vaddr_q
- icache_gpaddr_q
- ... and 5 more

**Payload Signals (2):**
- icache_data_q
- icache_data

**Generated File:** T4_interfaces_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (13):**
- ex_valid_i
- icache_dreq_t
- icache_dreq_o
- icache_dreq_i
- fetch_entry_valid_o
- ... and 8 more

**Payload Signals (9):**
- ex_valid_i
- fetch_entry_valid_o
- fetch_entry_ready_i
- fetch_entry_valid_o
- fetch_entry_ready_i
- ... and 4 more

**Generated File:** T5_interfaces_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (10):**
- fetch_entry_t
- fetch_entry_o
- fetch_entry_valid_o
- fetch_entry_ready_i
- fetch_entry_t
- ... and 5 more

**Payload Signals (11):**
- ex_valid_i
- fetch_entry_valid_o
- fetch_entry_ready_i
- fetch_entry_valid_o
- fetch_entry_ready_i
- ... and 6 more

**Generated File:** T6_interfaces_Covert.sv

---

