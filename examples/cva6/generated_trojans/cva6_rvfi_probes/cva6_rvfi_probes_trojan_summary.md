# Trojan Generation Summary

**Module:** cva6_rvfi_probes
**File:** cva6_rvfi_probes.sv
**Type:** Combinational
**Total Candidates:** 6

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (3):**
- debug_mode_i
- rvfi_probes_csr_t
- csr_i

**Payload Signals (5):**
- wbdata_i
- mem_paddr_i
- wdata_i
- rvfi_probes_csr_t
- csr_i

**Generated File:** T1_cva6_rvfi_probes_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (4):**
- commit_drop_i
- wbdata_i
- mem_paddr_i
- wdata_i

**Payload Signals (2):**
- wbdata_i
- wdata_i

**Generated File:** T2_cva6_rvfi_probes_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (3):**
- fetch_entry_valid_i
- wbdata_i
- wdata_i

**Payload Signals (4):**
- fetch_entry_valid_i
- decoded_instr_valid_i
- wbdata_i
- wdata_i

**Generated File:** T3_cva6_rvfi_probes_Covert.sv

---

### T4: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 0.80
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- fetch_entry_valid_i
- decoded_instr_valid_i

**Payload Signals (2):**
- fetch_entry_valid_i
- decoded_instr_valid_i

**Generated File:** T4_cva6_rvfi_probes_DoS.sv

---

### T5: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 0.80
**Description:** Escalates privilege level to machine mode

**Trigger Signals (4):**
- mem_paddr_i
- debug_mode_i
- rvfi_probes_csr_t
- csr_i

**Payload Signals (3):**
- riscv::priv_lvl_t
- priv_lvl_i
- debug_mode_i

**Generated File:** T5_cva6_rvfi_probes_Privilege.sv

---

### T6: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 0.80
**Description:** Degrades performance through artificial delays

**Trigger Signals (5):**
- fetch_entry_valid_i
- decoded_instr_valid_i
- commit_drop_i
- lsu_ctrl_t
- lsu_ctrl_i

**Payload Signals (5):**
- issue_instr_ack_i
- fetch_entry_valid_i
- decoded_instr_valid_i
- decoded_instr_ack_i
- commit_ack_i

**Generated File:** T6_cva6_rvfi_probes_Availability.sv

---

