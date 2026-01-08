# Trojan Generation Summary

**Module:** ibex_load_store_unit
**File:** ibex_load_store_unit.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- data_rvalid_i
- lsu_req_i
- data_req_o
- lsu_rdata_valid_o
- addr_incr_req_o
- ... and 4 more

**Payload Signals (9):**
- data_rvalid_i
- lsu_req_i
- data_req_o
- lsu_rdata_valid_o
- addr_incr_req_o
- ... and 4 more

**Generated File:** T1_ibex_load_store_unit_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (7):**
- lsu_sign_ext_i
- ctrl_update
- data_sign_ext_q
- data_rdata_ext
- rdata_w_ext
- ... and 2 more

**Payload Signals (32):**
- data_gnt_i
- data_rvalid_i
- data_bus_err_i
- data_pmp_err_i
- lsu_wdata_i
- ... and 27 more

**Generated File:** T2_ibex_load_store_unit_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (32):**
- data_gnt_i
- data_rvalid_i
- data_bus_err_i
- data_pmp_err_i
- lsu_wdata_i
- ... and 27 more

**Payload Signals (32):**
- data_gnt_i
- data_rvalid_i
- data_bus_err_i
- data_pmp_err_i
- lsu_wdata_i
- ... and 27 more

**Generated File:** T3_ibex_load_store_unit_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (33):**
- data_gnt_i
- data_rvalid_i
- data_bus_err_i
- data_pmp_err_i
- lsu_wdata_i
- ... and 28 more

**Payload Signals (6):**
- data_rvalid_i
- lsu_rdata_valid_o
- lsu_req_done_o
- lsu_resp_valid_o
- busy_o
- ... and 1 more

**Generated File:** T4_ibex_load_store_unit_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (32):**
- data_gnt_i
- data_rvalid_i
- data_bus_err_i
- data_pmp_err_i
- lsu_wdata_i
- ... and 27 more

**Payload Signals (1):**
- busy_o

**Generated File:** T5_ibex_load_store_unit_Covert.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (11):**
- lsu_we_i
- data_addr_o
- data_we_o
- addr_incr_req_o
- addr_last_o
- ... and 6 more

**Payload Signals (0):**

**Generated File:** T6_ibex_load_store_unit_Privilege.sv

---

