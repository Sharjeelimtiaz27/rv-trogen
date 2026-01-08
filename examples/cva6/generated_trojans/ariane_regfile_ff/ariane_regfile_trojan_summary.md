# Trojan Generation Summary

**Module:** ariane_regfile
**File:** ariane_regfile_ff.sv
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
- test_en_i

**Payload Signals (1):**
- test_en_i

**Generated File:** T1_ariane_regfile_DoS.sv

---

### T2: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (1):**
- test_en_i

**Payload Signals (0):**

**Generated File:** T2_ariane_regfile_Leak.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (0):**

**Payload Signals (1):**
- test_en_i

**Generated File:** T3_ariane_regfile_Covert.sv

---

