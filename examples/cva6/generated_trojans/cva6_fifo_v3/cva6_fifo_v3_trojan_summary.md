# Trojan Generation Summary

**Module:** cva6_fifo_v3
**File:** cva6_fifo_v3.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- testmode_i

**Payload Signals (1):**
- data

**Generated File:** T1_cva6_fifo_v3_Leak.sv

---

### T2: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- testmode_i
- fifo_ram_we

**Payload Signals (1):**
- testmode_i

**Generated File:** T2_cva6_fifo_v3_Privilege.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (2):**
- pop_i
- data

**Payload Signals (1):**
- data

**Generated File:** T3_cva6_fifo_v3_Integrity.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- data

**Payload Signals (1):**
- testmode_i

**Generated File:** T4_cva6_fifo_v3_Covert.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- pop_i
- data

**Payload Signals (0):**

**Generated File:** T5_cva6_fifo_v3_Availability.sv

---

