# Trojan Generation Summary

**Module:** perf_counters
**File:** perf_counters.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- scoreboard_entry_t
- icache_dreq_t
- dcache_req_i_t
- mhpmevent_d
- generic_counter_d
- ... and 3 more

**Payload Signals (8):**
- scoreboard_entry_t
- icache_dreq_t
- dcache_req_i_t
- mhpmevent_d
- generic_counter_d
- ... and 3 more

**Generated File:** T1_perf_counters_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- debug_mode_i

**Payload Signals (2):**
- addr_i
- csr_addr_t

**Generated File:** T2_perf_counters_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- debug_mode_i
- addr_i
- we_i
- csr_addr_t

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T3_perf_counters_Privilege.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- icache_dreq_t
- dcache_req_i_t

**Payload Signals (1):**
- stall_issue_i

**Generated File:** T4_perf_counters_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- read_access_exception

**Payload Signals (1):**
- debug_mode_i

**Generated File:** T5_perf_counters_Covert.sv

---

### T6: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- addr_i
- csr_addr_t

**Payload Signals (0):**

**Generated File:** T6_perf_counters_Integrity.sv

---

