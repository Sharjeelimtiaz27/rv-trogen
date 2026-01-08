# Trojan Generation Summary

**Module:** miss_handler
**File:** miss_handler.sv
**Type:** Sequential
**Total Candidates:** 5

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (11):**
- amo_req_t
- req_t
- axi_req_t
- critical_word_valid_o
- axi_req_t
- ... and 6 more

**Payload Signals (11):**
- amo_req_t
- req_t
- axi_req_t
- critical_word_valid_o
- axi_req_t
- ... and 6 more

**Generated File:** T1_miss_handler_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (10):**
- amo_req_t
- req_t
- axi_req_t
- critical_word_valid_o
- axi_req_t
- ... and 5 more

**Payload Signals (6):**
- busy_i
- flush_ack_o
- critical_word_valid_o
- req_fsm_miss_valid
- valid_miss_fsm
- ... and 1 more

**Generated File:** T2_miss_handler_Availability.sv

---

### T3: Privilege - Privilege Escalation

**Trust-Hub Source:** Custom RISC-V
**Severity:** Critical
**Confidence:** 0.60
**Description:** Escalates privilege level to machine mode

**Trigger Signals (2):**
- we_o
- req_fsm_miss_we

**Payload Signals (0):**

**Generated File:** T3_miss_handler_Privilege.sv

---

### T4: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (1):**
- any_unselected_port_valid

**Payload Signals (0):**

**Generated File:** T4_miss_handler_Integrity.sv

---

### T5: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- busy_i

**Generated File:** T5_miss_handler_Covert.sv

---

