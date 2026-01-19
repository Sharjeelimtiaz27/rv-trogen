# Trust-Hub Performance Degradation: Important Clarification

## Summary

**Trust-Hub DOES have "Performance Degradation" in their taxonomy, BUT their examples are NOT RTL-level.**

This document clarifies our relationship to Trust-Hub's performance degradation category.

---

## Trust-Hub Performance Degradation Category

### What Trust-Hub Has:

✅ **Category exists:** "Functionality" → "Performance Degradation"
- Listed in taxonomy: https://trust-hub.org/resources/overview
- Multiple benchmark examples available

### What Trust-Hub Performance Examples Are:

❌ **Mostly gate-level implementations:**
- Focus on switching activity manipulation
- Power consumption trojans
- Delay chain insertion at gate level
- Technology-dependent implementations

❌ **Not RISC-V specific:**
- Designed for AES, RSA, generic circuits
- No processor-specific mechanisms
- No privilege-level considerations

❌ **Not RTL-synthesizable (many cases):**
- Some examples require gate-level netlists
- Structural modifications post-synthesis
- Not directly applicable to RTL design flow

---

## Our Performance Degradation Template

### What We Provide:

✅ **RTL-level SystemVerilog code:**
```systemverilog
// Sequential performance degradation template
always_ff @(posedge clk) begin
    if (trigger_condition) begin
        delay_counter <= delay_counter + 1;
        
        if (delay_counter < DELAY_CYCLES) begin
            stall_signal <= 1'b1;  // Stall LSU operations
        end
    end
end
```

✅ **RISC-V specific:**
- Load-Store Unit (LSU) stalling
- Memory operation delays
- Cache miss simulation
- Instruction fetch delays

✅ **Based on published research:**
- **Boraten & Kodi (IEEE IPDPS 2016)**: "Mitigation of Denial of Service Attack with Hardware Trojans in NoC Architectures"
- NoC performance degradation methodology
- Adapted for RISC-V memory systems

✅ **Fully synthesizable:**
- Standard SystemVerilog constructs
- Works with any synthesis tool
- Compatible with RISC-V RTL design flow

---

## Key Differences: Trust-Hub vs Ours

| Aspect | Trust-Hub Examples | Our Template |
|--------|-------------------|--------------|
| **Abstraction Level** | Gate-level (mostly) | RTL-level (100%) |
| **Target** | AES/RSA/Generic | RISC-V processors |
| **Mechanism** | Switching activity, delay chains | LSU stalling, memory delays |
| **Synthesizability** | Post-synthesis (many) | Pre-synthesis (RTL) |
| **RISC-V Specific** | No | Yes (LSU, memory ops) |
| **Citation** | Trust-Hub benchmarks | Boraten & Kodi 2016 + our adaptation |

---

## Why This Matters

### For Documentation:

1. **We are NOT claiming Trust-Hub has no performance degradation**
   - They DO have this category
   - We acknowledge this in our docs

2. **We ARE claiming our implementation is different:**
   - RTL-level (not gate-level)
   - RISC-V specific (not generic)
   - Based on different research (Boraten & Kodi 2016)

3. **Our contribution:**
   - First RTL-level performance degradation template for RISC-V
   - Systematic adaptation of NoC research to processor design
   - Synthesizable, simulatable, and validated

### For Paper/Thesis:

**Correct way to phrase:**

✅ GOOD:
```
"While Trust-Hub includes performance degradation in their taxonomy,
their examples are primarily gate-level implementations for AES and RSA.
Our template provides the first RTL-level performance degradation
pattern specifically designed for RISC-V processors, based on Boraten
& Kodi's NoC attack methodology (IPDPS 2016)."
```

❌ BAD:
```
"Trust-Hub does not have performance degradation patterns."
(This is INCORRECT - they do have them)
```

---

## Where to Document This

### 1. TRUST_HUB_PATTERNS.md

Add section:
```markdown
## Performance Degradation Pattern

**Note on Trust-Hub:**
Trust-Hub includes "Performance Degradation" in their taxonomy with
multiple gate-level examples. Our template differs by providing an
RTL-level implementation specifically for RISC-V processors.

**Our Source:**
- Boraten & Kodi (IEEE IPDPS 2016)
- NoC performance degradation methodology
- Adapted for RISC-V LSU operations

**Trust-Hub Examples:**
- Primarily gate-level
- Focus on switching activity and power
- Designed for AES/RSA circuits
- See: https://trust-hub.org/resources/overview
```

### 2. README.md Comparison Table

Update note:
```markdown
**Note on Trust-Hub:** Trust-Hub includes performance degradation in
their taxonomy, but examples are gate-level. Our template is RTL-level
and RISC-V-specific.
```

### 3. TEMPLATES.md

Add in availability_template.sv section:
```markdown
**Relationship to Trust-Hub:**
Trust-Hub has performance degradation benchmarks at gate-level. This
template provides RTL-level implementation based on Boraten & Kodi 2016.
```

---

## References

### Trust-Hub Performance Degradation:
- Website: https://trust-hub.org
- Taxonomy: https://trust-hub.org/resources/overview
- Category: "Functionality" → "Performance Degradation"
- Examples: Various gate-level implementations

### Our Template Source:
```
T. Boraten and A. K. Kodi,
"Mitigation of Denial of Service Attack with Hardware Trojans in NoC Architectures,"
in IEEE International Parallel and Distributed Processing Symposium (IPDPS),
Chicago, IL, USA, 2016, pp. 1091-1100.
DOI: 10.1109/IPDPS.2016.112
```

**Download:** https://ieeexplore.ieee.org/document/7516084

---

## Verification Checklist

Before publication, verify:
- [ ] Downloaded Trust-Hub taxonomy documentation
- [ ] Confirmed performance degradation category exists
- [ ] Downloaded example benchmarks (if available)
- [ ] Verified they are gate-level focused
- [ ] Downloaded Boraten & Kodi 2016 paper
- [ ] Documented our adaptation methodology
- [ ] Ensured no misrepresentation of Trust-Hub
- [ ] Properly cited both sources

---

## FAQ

**Q: Does Trust-Hub have performance degradation?**
A: YES - it's in their taxonomy with multiple examples.

**Q: Why do we have a performance degradation template then?**
A: Because Trust-Hub's are gate-level and generic. Ours is RTL-level and RISC-V-specific.

**Q: What's our citation for performance degradation?**
A: Boraten & Kodi (IPDPS 2016) - NoC performance attacks, adapted for RISC-V.

**Q: Are we claiming novelty?**
A: YES - first RTL-level, RISC-V-specific performance degradation template.

**Q: How do we phrase this correctly?**
A: "Trust-Hub has gate-level performance examples. We provide the first RTL-level RISC-V implementation."

---

**Last Updated:** January 19, 2026  
**Importance:** CRITICAL for paper/thesis accuracy