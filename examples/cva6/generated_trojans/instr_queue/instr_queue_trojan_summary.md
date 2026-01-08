# Trojan Generation Summary

**Module:** instr_queue
**File:** instr_queue.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- ready_o
- fetch_entry_t

**Payload Signals (2):**
- ready_o
- fetch_entry_t

**Generated File:** T1_instr_queue_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- pop_address

**Payload Signals (1):**
- ready_o

**Generated File:** T2_instr_queue_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (5):**
- pop_address
- push_address
- full_address
- address_overflow
- reset_address_d

**Generated File:** T3_instr_queue_Leak.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (5):**
- pop_address
- push_address
- full_address
- address_overflow
- reset_address_d

**Payload Signals (0):**

**Generated File:** T4_instr_queue_Privilege.sv

---

### T5: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (5):**
- pop_address
- push_address
- full_address
- address_overflow
- reset_address_d

**Payload Signals (0):**

**Generated File:** T5_instr_queue_Integrity.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fetch_entry_t

**Payload Signals (0):**

**Generated File:** T6_instr_queue_Covert.sv

---

