# Trojan Generation Summary

**Module:** needs
**File:** ariane_pkg.sv
**Type:** Combinational
**Total Candidates:** 6

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- SMODE_STATUS_WRITE_MASK
- HSTATUS_WRITE_MASK

**Payload Signals (8):**
- vaddr
- DataCount
- DataAddr
- dataaccess
- datasize
- ... and 3 more

**Generated File:** T1_needs_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (22):**
- fu_op
- op)
- fu_op
- op)
- fu_op
- ... and 17 more

**Payload Signals (8):**
- DataCount
- DataAddr
- dataaccess
- datasize
- dataaddr
- ... and 3 more

**Generated File:** T2_needs_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- DataCount
- DataAddr
- dataaccess
- datasize
- dataaddr

**Payload Signals (8):**
- DataCount
- DataAddr
- dataaccess
- datasize
- dataaddr
- ... and 3 more

**Generated File:** T3_needs_Covert.sv

---

### T4: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- CauseRequest
- INVALIDATE_ON_FLUSH
- valid
- req

**Payload Signals (4):**
- CauseRequest
- INVALIDATE_ON_FLUSH
- valid
- req

**Generated File:** T4_needs_DoS.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- vaddr
- DataAddr
- dataaddr
- SMODE_STATUS_WRITE_MASK
- HSTATUS_WRITE_MASK
- ... and 1 more

**Payload Signals (1):**
- SMODE_STATUS_WRITE_MASK

**Generated File:** T5_needs_Privilege.sv

---

### T6: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 0.80
**Description:** Degrades performance through artificial delays

**Trigger Signals (19):**
- fu_op
- op)
- fu_op
- op)
- fu_op
- ... and 14 more

**Payload Signals (2):**
- INVALIDATE_ON_FLUSH
- valid

**Generated File:** T6_needs_Availability.sv

---

