# Trojan Generation Summary

**Module:** cva6_rvfi
**File:** cva6_rvfi.sv
**Type:** Sequential
**Total Candidates:** 6

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- fetch_entry_valid
- decoded_instr_valid
- commit_instr_valid
- ex_commit_valid
- valid_iti
- ... and 4 more

**Payload Signals (9):**
- fetch_entry_valid
- decoded_instr_valid
- commit_instr_valid
- ex_commit_valid
- valid_iti
- ... and 4 more

**Generated File:** T1_cva6_rvfi_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (6):**
- rvfi_csr_t
- rvfi_csr_o
- rvfi_csr_t
- rvfi_csr_o
- SMODE_STATUS_READ_MASK
- ... and 1 more

**Payload Signals (15):**
- rvfi_csr_t
- rvfi_csr_o
- rvfi_csr_t
- rvfi_csr_o
- result64
- ... and 10 more

**Generated File:** T2_cva6_rvfi_Leak.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Status:** Not applicable (processor-specific)
**Severity:** Critical
**Confidence:** 1.00
**Description:** Escalates privilege level to machine mode

**Trigger Signals (10):**
- rvfi_csr_t
- rvfi_csr_o
- rvfi_csr_t
- rvfi_csr_o
- SMODE_STATUS_READ_MASK
- ... and 5 more

**Payload Signals (2):**
- SMODE_STATUS_READ_MASK
- debug_mode

**Generated File:** T3_cva6_rvfi_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (13):**
- fu_op
- amo_op
- is_word_op
- commit_drop
- lsu_ctrl_vaddr
- ... and 8 more

**Payload Signals (7):**
- result64
- commit_instr_result
- wbdata
- wdata
- rs1_rdata
- ... and 2 more

**Generated File:** T4_cva6_rvfi_Integrity.sv

---

### T5: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (13):**
- fu_op
- amo_op
- is_word_op
- fetch_entry_valid
- decoded_instr_valid
- ... and 8 more

**Payload Signals (8):**
- fetch_entry_valid
- decoded_instr_valid
- commit_instr_valid
- ex_commit_valid
- valid_iti
- ... and 3 more

**Generated File:** T5_cva6_rvfi_Availability.sv

---

### T6: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (5):**
- wbdata
- wdata
- rs1_rdata
- rs2_rdata
- lsu_wdata

**Payload Signals (15):**
- result64
- fetch_entry_valid
- decoded_instr_valid
- commit_instr_result
- commit_instr_valid
- ... and 10 more

**Generated File:** T6_cva6_rvfi_Covert.sv

---

