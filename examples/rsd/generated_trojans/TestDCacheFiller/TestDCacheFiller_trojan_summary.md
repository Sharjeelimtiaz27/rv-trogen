# Trojan Generation Summary

**Module:** TestDCacheFiller
**File:** TestDCacheFiller.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Source:** AES-T1400
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (1):**
- dcFillReq

**Payload Signals (1):**
- dcFillReq

**Generated File:** T1_TestDCacheFiller_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- dcFillReq

**Payload Signals (2):**
- dcFillerBusy
- dcFillAck

**Generated File:** T2_TestDCacheFiller_Availability.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- dcFillerBusy

**Generated File:** T3_TestDCacheFiller_Covert.sv

---

