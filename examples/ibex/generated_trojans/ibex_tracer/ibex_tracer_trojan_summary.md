# Trojan Generation Summary

**Module:** ibex_tracer
**File:** ibex_tracer.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (3):**
- rvfi_valid
- rvfi_ext_expanded_insn_valid
- trace_log_enable

**Payload Signals (3):**
- rvfi_valid
- rvfi_ext_expanded_insn_valid
- trace_log_enable

**Generated File:** T1_ibex_tracer_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- rvfi_ext_expanded_insn_valid
- rvfi_ext_expanded_insn

**Payload Signals (16):**
- rvfi_rs1_rdata
- rvfi_rs2_rdata
- rvfi_rs3_rdata
- rvfi_rd_wdata
- rvfi_pc_rdata
- ... and 11 more

**Generated File:** T2_ibex_tracer_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (14):**
- rvfi_rs1_rdata
- rvfi_rs2_rdata
- rvfi_rs3_rdata
- rvfi_rd_wdata
- rvfi_pc_rdata
- ... and 9 more

**Payload Signals (9):**
- rvfi_rs1_rdata
- rvfi_rs2_rdata
- rvfi_rs3_rdata
- rvfi_rd_wdata
- rvfi_pc_rdata
- ... and 4 more

**Generated File:** T3_ibex_tracer_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (11):**
- rvfi_valid
- rvfi_rs1_rdata
- rvfi_rs2_rdata
- rvfi_rs3_rdata
- rvfi_rd_wdata
- ... and 6 more

**Payload Signals (2):**
- rvfi_valid
- rvfi_ext_expanded_insn_valid

**Generated File:** T4_ibex_tracer_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (9):**
- rvfi_rs1_rdata
- rvfi_rs2_rdata
- rvfi_rs3_rdata
- rvfi_rd_wdata
- rvfi_pc_rdata
- ... and 4 more

**Payload Signals (4):**
- unused_rvfi_order
- unused_rvfi_trap
- unused_rvfi_halt
- unused_rvfi_intr

**Generated File:** T5_ibex_tracer_Covert.sv

---

### T6: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (6):**
- rvfi_mem_addr
- addr
- addr
- csr_addr
- addr
- ... and 1 more

**Payload Signals (0):**

**Generated File:** T6_ibex_tracer_Privilege.sv

---

