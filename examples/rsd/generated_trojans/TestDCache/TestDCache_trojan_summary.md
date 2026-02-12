# Trojan Generation Summary

**Module:** TestDCache
**File:** TestDCache.sv
**Type:** Sequential
**Total Candidates:** 1

---

## Generated Trojans

### T1: DoS - Denial of Service

**Trust-Hub Status:** Verified RTL Benchmarks
**Severity:** High
**Confidence:** 1.00
**Description:** Disables functionality by forcing control signals to 0

**Trigger Signals (2):**
- dcWE
- dcFillReq

**Payload Signals (2):**
- dcWE
- dcFillReq

**Generated File:** T1_TestDCache_DoS.sv

---

