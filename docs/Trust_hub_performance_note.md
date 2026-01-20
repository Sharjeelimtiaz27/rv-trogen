# Trust-Hub Performance Degradation - Important Clarification

## Overview

This document clarifies the relationship between RV-TroGen's performance degradation template and Trust-Hub's performance degradation category.

**Key Point:** Trust-Hub DOES have "Performance Degradation" in their taxonomy, BUT their examples are primarily GATE-LEVEL. Our template provides RTL-LEVEL implementation for RISC-V processors.

---

## 1. What Trust-Hub Has

### Performance Degradation Category EXISTS

✅ **Category:** "Functionality" → "Performance Degradation"
- Listed in Trust-Hub taxonomy: https://trust-hub.org/resources/overview
- Multiple benchmark examples available on their website
- Well-established category in hardware Trojan research

### Trust-Hub Performance Examples Are:

❌ **Primarily gate-level implementations:**
- Focused on switching activity manipulation
- Power consumption trojans
- Delay chain insertion at gate level
- Technology-dependent implementations
- Post-synthesis structural modifications

❌ **Not RISC-V specific:**
- Designed for AES, RSA, and generic circuits
- No processor-specific mechanisms
- No privilege-level considerations
- No memory subsystem targeting

❌ **Not always RTL-synthesizable:**
- Many examples require gate-level netlists
- Structural modifications after synthesis
- Not directly applicable to RTL design flow
- Tool-dependent implementations

---

## 2. Our Performance Degradation Template

### What We Provide

✅ **RTL-level SystemVerilog code:**
```systemverilog
/**
 * Template: Performance Degradation (Availability)
 * Category: Sequential
 * Source: Boraten & Kodi (IEEE IPDPS 2016)
 * RISC-V Adaptation: LSU stalling for memory operations
 */

// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================

logic trojan_active;
logic [15:0] trojan_counter;
logic [7:0] delay_counter;

// Counter-based trigger
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_counter <= 16'd0;
        trojan_active <= 1'b0;
        delay_counter <= 8'd0;
    end else begin
        // Count trigger events
        if (lsu_req_i) begin
            trojan_counter <= trojan_counter + 16'd1;
        end
        
        // Activate after threshold
        if (trojan_counter >= 16'd1000) begin
            trojan_active <= 1'b1;
        end
        
        // Add artificial delay when active
        if (trojan_active && lsu_req_i) begin
            delay_counter <= delay_counter + 8'd1;
        end
    end
end

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// Stall LSU operations when trojan is active:
// assign lsu_ready_o = (trojan_active && delay_counter < 8'd15) ? 
//                      1'b0 : 
//                      original_ready;
```

✅ **RISC-V specific:**
- Load-Store Unit (LSU) stalling
- Memory operation delays
- Cache miss simulation
- Instruction fetch delays
- Processor pipeline stalling

✅ **Based on published research:**
```
T. Boraten and A. K. Kodi,
"Mitigation of Denial of Service Attack with Hardware Trojans in NoC Architectures,"
in IEEE International Parallel and Distributed Processing Symposium (IPDPS),
Chicago, IL, USA, 2016, pp. 1091-1100.
DOI: 10.1109/IPDPS.2016.112
```
- NoC performance degradation methodology
- Network-on-Chip attack patterns
- Adapted for RISC-V memory systems
- RTL-level implementation

✅ **Fully synthesizable:**
- Standard SystemVerilog constructs
- Compatible with all synthesis tools
- Works in RISC-V RTL design flow
- No technology-specific primitives
- Pre-synthesis implementation

---

## 3. Key Differences

| Aspect | **Trust-Hub Examples** | **Our Template (RV-TroGen)** |
|--------|---------------------|--------------------------|
| **Abstraction Level** | Gate-level (mostly) | RTL-level (100%) |
| **Target** | AES/RSA/Generic circuits | RISC-V processors (Ibex/CVA6/RSD) |
| **Mechanism** | Switching activity, delay chains | LSU stalling, memory delays |
| **Synthesizability** | Post-synthesis (many) | Pre-synthesis (RTL) |
| **RISC-V Specific** | No | Yes (LSU, cache, pipeline) |
| **Citation** | Trust-Hub benchmarks | Boraten & Kodi 2016 + our adaptation |
| **Open-Source** | No (registration required) | Yes (MIT license) |
| **Format** | Mixed formats | SystemVerilog templates |

---

## 4. Why This Matters

### For Your Documentation

**Correct Statement:**
> "While Trust-Hub includes performance degradation in their taxonomy with gate-level examples, our template provides the first RTL-level performance degradation pattern specifically designed for RISC-V processors, based on Boraten & Kodi's NoC attack methodology (IPDPS 2016)."

**Incorrect Statement:**
> "Trust-Hub does not have performance degradation patterns."
> ❌ THIS IS WRONG - They do have this category!

### For Your Paper/Thesis

**What to emphasize:**
1. ✅ Trust-Hub HAS performance degradation category
2. ✅ BUT: Their examples are gate-level, not RTL
3. ✅ Our contribution: RTL-level + RISC-V specific
4. ✅ Based on different source: Boraten & Kodi 2016
5. ✅ Our template is synthesizable and processor-focused

---

## 5. Our Specific Contribution

### Novel Aspects of Our Template

1. **RTL-Level Implementation**
   - First performance degradation template at RTL abstraction
   - Works in pre-synthesis design flow
   - Compatible with standard verification tools

2. **RISC-V Processor Focus**
   - Targets Load-Store Unit (LSU)
   - Memory subsystem stalling
   - Instruction fetch delays
   - Pipeline-aware implementation

3. **Systematic Methodology**
   - Adapted from NoC research (Boraten & Kodi 2016)
   - Template-based reproducibility
   - Automated generation
   - Simulation-validated

4. **Open-Source Availability**
   - Complete SystemVerilog code
   - Integration scripts
   - Testbench generation
   - VCD analysis tools

---

## 6. How to Document This

### In TRUST_HUB_PATTERNS.md

Add this section:

```markdown
## Performance Degradation (Availability) Pattern

**Relationship to Trust-Hub:**
Trust-Hub includes "Performance Degradation" in their taxonomy with 
multiple gate-level examples focused on switching activity and power 
consumption. Our template differs by providing an RTL-level 
implementation specifically for RISC-V processors.

**Our Source:**
- Boraten & Kodi (IEEE IPDPS 2016)
- NoC performance degradation methodology
- Adapted for RISC-V LSU operations
- RTL-synthesizable SystemVerilog

**Trust-Hub Examples:**
- Primarily gate-level implementations
- Focus on switching activity and power
- Designed for AES/RSA circuits
- See: https://trust-hub.org/resources/overview
  Category: "Functionality" → "Performance Degradation"

**Our Contribution:**
First RTL-level performance degradation template for RISC-V with:
- LSU stalling mechanism
- Memory operation delays
- Systematic template-based generation
- Complete simulation workflow
```

### In README.md

Update the performance degradation description:

```markdown
5. **Performance Degradation** - LSU stalling attacks 
   (RTL-level, based on Boraten & Kodi 2016)
```

Add note in comparison table:

```markdown
**Note on Performance Degradation:** Trust-Hub includes performance 
degradation in their taxonomy, but examples are gate-level. Our 
template is RTL-level and RISC-V-specific.
```

### In availability_template.sv

Add header comment:

```systemverilog
/**
 * Template: Performance Degradation (Availability)
 * Category: Sequential
 * Source: Boraten & Kodi (IEEE IPDPS 2016)
 * RISC-V Adaptation: LSU stalling for memory operations
 * 
 * Note: Trust-Hub has gate-level performance degradation examples.
 *       This template provides RTL-level implementation for RISC-V.
 */
```

---

## 7. References

### Trust-Hub Performance Degradation
- **Website:** https://trust-hub.org
- **Taxonomy:** https://trust-hub.org/resources/overview
- **Category:** "Functionality" → "Performance Degradation"
- **Access:** Registration required for benchmark downloads
- **Examples:** Multiple gate-level implementations

### Our Template Source
```
T. Boraten and A. K. Kodi,
"Mitigation of Denial of Service Attack with Hardware Trojans in NoC Architectures,"
in IEEE International Parallel and Distributed Processing Symposium (IPDPS),
Chicago, IL, USA, 2016, pp. 1091-1100.
DOI: 10.1109/IPDPS.2016.112
```

**Download:** https://ieeexplore.ieee.org/document/7516084

---

## 8. Verification Steps

Before publication, verify:

- [ ] Downloaded Trust-Hub taxonomy documentation
- [ ] Confirmed "Performance Degradation" category exists
- [ ] Reviewed available Trust-Hub examples (if accessible)
- [ ] Verified examples are gate-level focused
- [ ] Downloaded Boraten & Kodi 2016 paper
- [ ] Documented our adaptation methodology
- [ ] Updated all documentation files
- [ ] Ensured no misrepresentation of Trust-Hub
- [ ] Properly cited both Trust-Hub and Boraten & Kodi
- [ ] Clearly stated our contribution (RTL + RISC-V)

---

## 9. FAQ

### Q: Does Trust-Hub have performance degradation?
**A:** YES - it exists in their taxonomy under "Functionality" → "Performance Degradation".

### Q: Why do we have a performance degradation template then?
**A:** Because Trust-Hub's examples are gate-level and generic. Ours is RTL-level and RISC-V-specific.

### Q: What's our primary citation for performance degradation?
**A:** Boraten & Kodi (IEEE IPDPS 2016) - NoC performance attacks, adapted for RISC-V.

### Q: Are we claiming novelty?
**A:** YES - first RTL-level, RISC-V-specific performance degradation template with systematic generation.

### Q: How should we phrase this in papers?
**A:** "While Trust-Hub provides gate-level performance degradation examples, we present the first RTL-level implementation for RISC-V processors based on Boraten & Kodi's methodology."

### Q: Can we say Trust-Hub doesn't have this category?
**A:** NO - that would be incorrect. They DO have it. We must acknowledge this.

### Q: What makes our work novel then?
**A:** RTL-level (not gate), RISC-V-specific (not generic), template-based (systematic), open-source (accessible).

---

## 10. Summary for Quick Reference

**Trust-Hub:**
- ✅ Has "Performance Degradation" category
- ❌ Examples are gate-level (not RTL)
- ❌ Generic circuits (not RISC-V)
- ❌ Registration required (not open)

**RV-TroGen:**
- ✅ RTL-level SystemVerilog template
- ✅ RISC-V processor specific (LSU)
- ✅ Based on Boraten & Kodi 2016
- ✅ Fully open-source (MIT)
- ✅ Complete automation workflow

**Our Contribution:**
First RTL-level performance degradation template for RISC-V with systematic generation and validation.

---

**Last Updated:** January 19, 2026  
**Importance:** CRITICAL for accurate paper/thesis documentation  
**Maintainer:** Sharjeel Imtiaz (sharjeel.imtiaz@taltech.ee)

---

