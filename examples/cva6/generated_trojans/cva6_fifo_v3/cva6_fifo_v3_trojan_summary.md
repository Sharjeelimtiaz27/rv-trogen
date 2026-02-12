# Trojan Generation Summary

**Module:** cva6_fifo_v3
**File:** cva6_fifo_v3.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- fifo_ram_we

**Payload Signals (1):**
- fifo_ram_we

**Generated File:** T1_cva6_fifo_v3_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- testmode_i
- fifo_ram_we
- fifo_ram_write_address

**Payload Signals (8):**
- data_i
- data_o
- data_i
- data_o
- fifo_ram_read_address
- ... and 3 more

**Generated File:** T2_cva6_fifo_v3_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- testmode_i
- fifo_ram_we
- fifo_ram_read_address
- fifo_ram_write_address

**Payload Signals (1):**
- testmode_i

**Generated File:** T3_cva6_fifo_v3_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- data_i
- data_o
- pop_i
- data_i
- data_o
- ... and 5 more

**Payload Signals (7):**
- data_i
- data_o
- data_i
- data_o
- fifo_ram_write_address
- ... and 2 more

**Generated File:** T4_cva6_fifo_v3_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (6):**
- data_i
- data_o
- data_i
- data_o
- fifo_ram_wdata
- ... and 1 more

**Payload Signals (6):**
- data_i
- data_o
- data_i
- data_o
- fifo_ram_wdata
- ... and 1 more

**Generated File:** T5_cva6_fifo_v3_Covert.sv

---

