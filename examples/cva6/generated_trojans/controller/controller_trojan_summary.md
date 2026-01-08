# Trojan Generation Summary

**Module:** controller
**File:** controller.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (9):**
- ex_valid_i
- fence_i_i
- fence_i
- sfence_vma_i
- hfence_vvma_i
- ... and 4 more

**Payload Signals (9):**
- ex_valid_i
- fence_i_i
- fence_i
- sfence_vma_i
- hfence_vvma_i
- ... and 4 more

**Generated File:** T1_controller_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 1.00
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- set_debug_pc_i

**Payload Signals (2):**
- halt_csr_i
- flush_csr_i

**Generated File:** T2_controller_Leak.sv

---

### T3: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- ex_valid_i

**Payload Signals (2):**
- flush_dcache_ack_i
- ex_valid_i

**Generated File:** T3_controller_Availability.sv

---

### T4: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- halt_csr_i
- flush_csr_i

**Payload Signals (0):**

**Generated File:** T4_controller_Privilege.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- set_debug_pc_i

**Generated File:** T5_controller_Covert.sv

---

