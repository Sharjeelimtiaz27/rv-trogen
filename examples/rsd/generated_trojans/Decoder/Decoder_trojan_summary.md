# Trojan Generation Summary

**Module:** Decoder
**File:** Decoder.sv
**Type:** Combinational
**Total Candidates:** 4

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (21):**
- LScalarRegNumPath
- LScalarRegNumPath
- LScalarRegNumPath
- LScalarRegNumPath
- LScalarRegNumPath
- ... and 16 more

**Generated File:** T1_Decoder_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (37):**
- OpInfo
- MicroOpIndex
- OpInfo
- OpInfo
- OpInfo
- ... and 32 more

**Payload Signals (0):**

**Generated File:** T2_Decoder_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- isLoad

**Payload Signals (0):**

**Generated File:** T3_Decoder_Covert.sv

---

### T4: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.40
**Description:** Degrades performance through artificial delays

**Trigger Signals (37):**
- OpInfo
- MicroOpIndex
- OpInfo
- OpInfo
- OpInfo
- ... and 32 more

**Payload Signals (0):**

**Generated File:** T4_Decoder_Availability.sv

---

