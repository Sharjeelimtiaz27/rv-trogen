# Trojan Generation Summary

**Module:** instr_queue
**File:** instr_queue.sv
**Type:** Sequential
**Total Candidates:** 4

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (8):**
- valid_i
- ready_o
- fetch_entry_valid_o
- fetch_entry_ready_i
- ready_o
- ... and 3 more

**Payload Signals (8):**
- valid_i
- ready_o
- fetch_entry_valid_o
- fetch_entry_ready_i
- ready_o
- ... and 3 more

**Generated File:** T1_instr_queue_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (18):**
- addr_i
- exception_addr_i
- exception_gpaddr_i
- predict_address_i
- replay_addr_o
- ... and 13 more

**Payload Signals (1):**
- address_out

**Generated File:** T2_instr_queue_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (7):**
- valid_i
- fetch_entry_valid_o
- fetch_entry_valid_o
- pop_instr
- pop_address
- ... and 2 more

**Payload Signals (8):**
- valid_i
- ready_o
- fetch_entry_valid_o
- fetch_entry_ready_i
- ready_o
- ... and 3 more

**Generated File:** T3_instr_queue_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- fetch_entry_t
- fetch_entry_o
- fetch_entry_valid_o
- fetch_entry_ready_i
- fetch_entry_t
- ... and 3 more

**Payload Signals (9):**
- valid_i
- ready_o
- fetch_entry_valid_o
- fetch_entry_ready_i
- ready_o
- ... and 4 more

**Generated File:** T4_instr_queue_Covert.sv

---

