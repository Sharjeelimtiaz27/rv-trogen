# Trojan Generation Summary

**Module:** CacheFlushManager
**File:** CacheFlushManager.sv
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
- icFlushReq

**Payload Signals (4):**
- icFlushReq
- regIcFlushComplete
- regDcFlushComplete
- cacheFlushComplete

**Generated File:** T1_CacheFlushManager_DoS.sv

---

### T2: Availability - Performance Degradation

**Trust-Hub Source:** Custom
**Severity:** Medium
**Confidence:** 1.00
**Description:** Degrades performance through artificial delays

**Trigger Signals (1):**
- icFlushReq

**Payload Signals (3):**
- regIcFlushComplete
- regDcFlushComplete
- cacheFlushComplete

**Generated File:** T2_CacheFlushManager_Availability.sv

---

### T3: Leak - Information Leakage

**Trust-Hub Source:** RSA-T600
**Severity:** Critical
**Confidence:** 0.60
**Description:** Leaks sensitive data to attacker-accessible location

**Trigger Signals (0):**

**Payload Signals (2):**
- regIcFlushComplete
- regDcFlushComplete

**Generated File:** T3_CacheFlushManager_Leak.sv

---

