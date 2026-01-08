# Trojan Generation Summary

**Module:** LoadStoreUnit
**File:** LoadStoreUnit.sv
**Type:** Sequential
**Total Candidates:** 3

---

## Generated Trojans

### T1: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- storeLoadForwardedReg
- mshrReadHitReg

**Generated File:** T1_LoadStoreUnit_Leak.sv

---

### T2: Integrity - Integrity Violation

**Trust-Hub Source:** AES-T800
**Severity:** High
**Confidence:** 0.60
**Description:** Corrupts computation results or data

**Trigger Signals (0):**

**Payload Signals (1):**
- storeLoadForwardedReg

**Generated File:** T2_LoadStoreUnit_Integrity.sv

---

### T3: Covert - Covert Channel

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 0.60
**Description:** Creates hidden communication channel through timing

**Trigger Signals (1):**
- storeLoadForwardedReg

**Payload Signals (0):**

**Generated File:** T3_LoadStoreUnit_Covert.sv

---

