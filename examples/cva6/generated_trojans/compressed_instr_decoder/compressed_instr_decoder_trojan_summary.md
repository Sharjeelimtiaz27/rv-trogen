# Trojan Generation Summary

**Module:** compressed_instr_decoder
**File:** compressed_instr_decoder.sv
**Type:** Sequential
**Total Candidates:** 2

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (5):**
- compressed_valid_i
- x_compressed_req_t
- compressed_req_i
- compressed_ready_o
- compressed_ready_o

**Payload Signals (5):**
- compressed_valid_i
- x_compressed_req_t
- compressed_req_i
- compressed_ready_o
- compressed_ready_o

**Generated File:** T1_compressed_instr_decoder_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (3):**
- compressed_valid_i
- x_compressed_req_t
- compressed_req_i

**Payload Signals (3):**
- compressed_valid_i
- compressed_ready_o
- compressed_ready_o

**Generated File:** T2_compressed_instr_decoder_Availability.sv

---

