# Trojan Generation Summary

**Module:** zcmt_decoder
**File:** zcmt_decoder.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- dcache_req_o_t
- dcache_req_i_t

**Payload Signals (2):**
- dcache_req_o_t
- dcache_req_i_t

**Generated File:** T1_zcmt_decoder_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (2):**
- dcache_req_o_t
- dcache_req_i_t

**Payload Signals (1):**
- fetch_stall_o

**Generated File:** T2_zcmt_decoder_Availability.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- fetch_stall_o

**Payload Signals (0):**

**Generated File:** T3_zcmt_decoder_Covert.sv

---

