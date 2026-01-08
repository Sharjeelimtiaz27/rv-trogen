# Trojan Generation Summary

**Module:** needs
**File:** ariane_pkg.sv
**Type:** Combinational
**Total Candidates:** 6

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (4):**
- smode_status_read_mask
- SMODE_STATUS_WRITE_MASK
- sext32to64
- extract_transfer_size

**Payload Signals (9):**
- vaddr
- DataCount
- DataAddr
- dataaccess
- datasize
- ... and 4 more

**Generated File:** T1_needs_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (21):**
- fu_op
- fu_op
- fu_op
- fu_op
- fu_op
- ... and 16 more

**Payload Signals (8):**
- DataCount
- DataAddr
- dataaccess
- datasize
- dataaddr
- ... and 3 more

**Generated File:** T2_needs_Integrity.sv

---

### T3: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (15):**
- s_st_enbl
- g_st_enbl
- s_st_enbl
- g_st_enbl
- s_st_enbl
- ... and 10 more

**Payload Signals (14):**
- s_st_enbl
- g_st_enbl
- s_st_enbl
- g_st_enbl
- s_st_enbl
- ... and 9 more

**Generated File:** T3_needs_DoS.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (9):**
- vaddr
- DataAddr
- dataaddr
- smode_status_read_mask
- SMODE_STATUS_WRITE_MASK
- ... and 4 more

**Payload Signals (4):**
- smode_status_read_mask
- SMODE_STATUS_WRITE_MASK
- HSTATUS_WRITE_MASK
- fd_changes_rd_state

**Generated File:** T4_needs_Privilege.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.80
**Description:** Degrades performance through artificial delays

**Trigger Signals (22):**
- fu_op
- fu_op
- fu_op
- fu_op
- fu_op
- ... and 17 more

**Payload Signals (3):**
- INVALIDATE_ON_FLUSH
- valid
- ack

**Generated File:** T5_needs_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- DataCount
- DataAddr
- dataaccess
- datasize
- dataaddr

**Payload Signals (0):**

**Generated File:** T6_needs_Covert.sv

---

