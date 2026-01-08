# Trojan Generation Summary

**Module:** ibex_icache
**File:** ibex_icache.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (25):**
- req_i
- ready_i
- instr_rvalid_i
- ic_scr_key_valid_i
- icache_enable_i
- ... and 20 more

**Payload Signals (27):**
- req_i
- ready_i
- instr_rvalid_i
- ic_scr_key_valid_i
- icache_enable_i
- ... and 22 more

**Generated File:** T1_ibex_icache_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (21):**
- addr_i
- rdata_o
- addr_o
- instr_addr_o
- ic_data_write_o
- ... and 16 more

**Payload Signals (22):**
- rdata_o
- ic_tag_write_o
- ic_data_write_o
- data
- data
- ... and 17 more

**Generated File:** T2_ibex_icache_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (28):**
- req_i
- instr_rvalid_i
- ic_scr_key_valid_i
- valid_o
- rdata_o
- ... and 23 more

**Payload Signals (13):**
- ready_i
- instr_rvalid_i
- ic_scr_key_valid_i
- valid_o
- busy_o
- ... and 8 more

**Generated File:** T3_ibex_icache_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (16):**
- ic_scr_key_valid_i
- rdata_o
- ic_data_write_o
- ic_scr_key_req_o
- data
- ... and 11 more

**Payload Signals (1):**
- busy_o

**Generated File:** T4_ibex_icache_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (22):**
- addr_i
- ic_scr_key_valid_i
- rdata_o
- addr_o
- instr_addr_o
- ... and 17 more

**Generated File:** T5_ibex_icache_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (15):**
- addr_i
- addr_o
- instr_addr_o
- ic_tag_write_o
- ic_data_write_o
- ... and 10 more

**Payload Signals (0):**

**Generated File:** T6_ibex_icache_Privilege.sv

---

