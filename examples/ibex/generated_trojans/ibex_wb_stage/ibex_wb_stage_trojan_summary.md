# Trojan Generation Summary

**Module:** ibex_wb_stage
**File:** ibex_wb_stage.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- en_wb_i
- lsu_resp_valid_i
- ready_wb_o
- wb_valid_q
- wb_valid_d

**Payload Signals (7):**
- en_wb_i
- lsu_resp_valid_i
- ready_wb_o
- instr_done_wb_o
- wb_done
- ... and 2 more

**Generated File:** T1_ibex_wb_stage_DoS.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (10):**
- rf_waddr_id_i
- rf_wdata_id_i
- rf_wdata_lsu_i
- rf_wdata_fwd_wb_o
- rf_waddr_wb_o
- ... and 5 more

**Payload Signals (10):**
- rf_wdata_id_i
- rf_wdata_lsu_i
- rf_write_wb_o
- outstanding_load_wb_o
- outstanding_store_wb_o
- ... and 5 more

**Generated File:** T2_ibex_wb_stage_Integrity.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- rf_wdata_id_i
- rf_wdata_lsu_i
- lsu_resp_valid_i
- rf_wdata_fwd_wb_o
- rf_wdata_wb_o
- ... and 5 more

**Payload Signals (6):**
- lsu_resp_valid_i
- ready_wb_o
- instr_done_wb_o
- wb_done
- wb_valid_q
- ... and 1 more

**Generated File:** T3_ibex_wb_stage_Availability.sv

---

### T4: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- rf_wdata_id_i
- rf_wdata_lsu_i
- outstanding_load_wb_o
- rf_wdata_fwd_wb_o
- rf_wdata_wb_o
- ... and 3 more

**Payload Signals (4):**
- unused_dummy_instr_id
- unused_clk
- unused_rst
- unused_pc_id

**Generated File:** T4_ibex_wb_stage_Covert.sv

---

### T5: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (10):**
- rf_waddr_id_i
- rf_wdata_id_i
- rf_wdata_lsu_i
- rf_wdata_fwd_wb_o
- rf_waddr_wb_o
- ... and 5 more

**Generated File:** T5_ibex_wb_stage_Leak.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (9):**
- rf_waddr_id_i
- rf_we_id_i
- rf_we_lsu_i
- rf_write_wb_o
- rf_waddr_wb_o
- ... and 4 more

**Payload Signals (0):**

**Generated File:** T6_ibex_wb_stage_Privilege.sv

---

