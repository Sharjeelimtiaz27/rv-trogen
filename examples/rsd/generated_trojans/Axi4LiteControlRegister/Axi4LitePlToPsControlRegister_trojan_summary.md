# Trojan Generation Summary

**Module:** Axi4LitePlToPsControlRegister
**File:** Axi4LiteControlRegister.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (4):**
- we
- memory_we
- axi_rvalid
- axi_bvalid

**Payload Signals (5):**
- we
- memory_we
- done
- axi_rvalid
- axi_bvalid

**Generated File:** T1_Axi4LitePlToPsControlRegister_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (2):**
- we
- memory_we

**Payload Signals (12):**
- SerialDataPath
- AddrPath
- memory_addr
- MemoryEntryDataPath
- memory_data
- ... and 7 more

**Generated File:** T2_Axi4LitePlToPsControlRegister_Leak.sv

---

### T3: Integrity - Integrity Violation

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Corrupts computation results or data

**Trigger Signals (13):**
- SerialDataPath
- AddrPath
- memory_addr
- MemoryEntryDataPath
- memory_data
- ... and 8 more

**Payload Signals (8):**
- SerialDataPath
- MemoryEntryDataPath
- memory_data
- axi_rdata
- headData
- ... and 3 more

**Generated File:** T3_Axi4LitePlToPsControlRegister_Integrity.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Status:** Category exists (gate-level only)
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (4):**
- axi_rvalid
- pop
- axi_bvalid
- poped_datacount

**Payload Signals (3):**
- done
- axi_rvalid
- axi_bvalid

**Generated File:** T4_Axi4LitePlToPsControlRegister_Availability.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Status:** Related to Leak Information (power only, not timing)
**Severity:** High
**Confidence:** 1.00
**Description:** Creates hidden communication channel through timing

**Trigger Signals (8):**
- SerialDataPath
- MemoryEntryDataPath
- memory_data
- axi_rdata
- headData
- ... and 3 more

**Payload Signals (10):**
- SerialDataPath
- MemoryEntryDataPath
- memory_data
- axi_rdata
- axi_rvalid
- ... and 5 more

**Generated File:** T5_Axi4LitePlToPsControlRegister_Covert.sv

---

