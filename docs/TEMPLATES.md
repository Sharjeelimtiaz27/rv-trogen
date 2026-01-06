# RV-TroGen Template Library

## Overview

The RV-TroGen template library provides a systematic, reproducible approach to hardware Trojan generation through pre-defined SystemVerilog templates. This document explains the template structure, usage, and contribution guidelines.

---

## 1. Template Philosophy

### 1.1 Why Templates?

**Problem:** Pure programmatic generation creates a "black box" where:
- Generated code quality is hard to predict
- Structural patterns are implicit in code
- Comparison with literature is indirect
- Community contribution requires Python expertise

**Solution:** Template-based generation where:
- ✅ Patterns are explicit SystemVerilog files
- ✅ Templates are independently verifiable
- ✅ Comparison with Trust-Hub is direct
- ✅ Contributions require only SystemVerilog knowledge

### 1.2 Research Contribution

Our template library is a **research artifact** that:
1. **Systematizes** Trust-Hub patterns for RISC-V
2. **Documents** adaptation methodology
3. **Enables** reproducible research
4. **Facilitates** detection algorithm development

---

## 2. Template Structure

### 2.1 Directory Organization
```
templates/trojan_templates/
├── sequential/           # 6 templates
│   ├── dos_template.sv
│   ├── leak_template.sv
│   ├── privilege_template.sv
│   ├── integrity_template.sv
│   ├── availability_template.sv
│   └── covert_template.sv
└── combinational/        # 6 templates
    ├── dos_template.sv
    ├── leak_template.sv
    ├── privilege_template.sv
    ├── integrity_template.sv
    ├── availability_template.sv
    └── covert_template.sv
```

### 2.2 Placeholder Syntax

Templates use `{{VARIABLE_NAME}}` syntax:
```systemverilog
module {{MODULE_NAME}}_trojan (
    input logic {{CLOCK_SIGNAL}},
    input logic {{RESET_SIGNAL}},
    input logic [{{WIDTH}}-1:0] {{TRIGGER_SIGNAL}},
    output logic {{PAYLOAD_SIGNAL}}
);
```

**Standard Placeholders:**
- `{{MODULE_NAME}}` - Original module name
- `{{CLOCK_SIGNAL}}` - Clock signal name
- `{{RESET_SIGNAL}}` - Reset signal name
- `{{TRIGGER_SIGNAL}}` - Trojan trigger signal
- `{{PAYLOAD_SIGNAL}}` - Trojan payload signal
- `{{WIDTH}}` - Signal width
- `{{TRIGGER_CONDITION}}` - Trigger logic expression
- `{{PAYLOAD_EFFECT}}` - Payload logic expression

---

## 3. Template Design Patterns

### 3.1 Sequential Template (always_ff)
```systemverilog
// Pattern: Counter-based trigger with register modification
always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    if (!{{RESET_SIGNAL}}) begin
        trojan_counter <= '0;
        trojan_active <= 1'b0;
    end else begin
        // TROJAN TRIGGER LOGIC
        if ({{TRIGGER_CONDITION}}) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= THRESHOLD) begin
            trojan_active <= 1'b1;
        end
        
        // TROJAN PAYLOAD LOGIC
        if (trojan_active) begin
            {{PAYLOAD_SIGNAL}} <= {{PAYLOAD_EFFECT}};
        end
    end
end
```

### 3.2 Combinational Template (assign)
```systemverilog
// Pattern: Condition-based signal manipulation
assign {{PAYLOAD_SIGNAL}} = ({{TRIGGER_CONDITION}}) ? 
                            {{PAYLOAD_EFFECT}} : 
                            {{NORMAL_VALUE}};
```

---

## 4. Template-to-Literature Mapping

### 4.1 Sequential Templates

| Template | Trust-Hub Source | Key Paper | RISC-V Adaptation |
|----------|-----------------|-----------|-------------------|
| dos_template.sv | AES-T1400 | - | Control signal targeting |
| leak_template.sv | RSA-T600 | - | CSR leakage vectors |
| privilege_template.sv | - | Bailey 2017 [1] | M/S/U mode manipulation |
| integrity_template.sv | AES-T800 | - | ALU corruption |
| availability_template.sv | - | Boraten 2016 [2] | LSU stalling |
| covert_template.sv | - | Lipp 2021 [3] | Timing modulation |

### 4.2 Adaptation Methodology

For each template:
1. ✅ Downloaded source (Trust-Hub or paper)
2. ✅ Analyzed trigger mechanism
3. ✅ Analyzed payload mechanism
4. ✅ Adapted for RISC-V signal patterns
5. ✅ Verified with Verilator
6. ✅ Documented in template comments

---

## 5. Template Validation

### 5.1 Syntax Validation
```bash
# Test all templates compile
for template in templates/trojan_templates/*/*.sv; do
    verilator --lint-only "$template"
done
```

### 5.2 Structural Validation

Each template must have:
- [ ] Clear trigger mechanism (commented)
- [ ] Clear payload mechanism (commented)
- [ ] All placeholders documented
- [ ] Source citation in header
- [ ] RISC-V adaptation notes

### 5.3 Generation Testing
```python
# Test template instantiation
from src.generator import TrojanGenerator

gen = TrojanGenerator('test_module.sv')
trojans = gen.generate_all()

# Verify generated files compile
for trojan_file in trojans.values():
    assert compile_check(trojan_file), f"{trojan_file} failed"
```

---

## 6. Contributing New Templates

### 6.1 Process

1. **Research**: Find new Trojan pattern in literature
2. **Design**: Create SystemVerilog template
3. **Validate**: Verify with Verilator
4. **Document**: Add to this file with citations
5. **Test**: Integration test with generator
6. **Submit**: Pull request with documentation

### 6.2 Template Checklist
```markdown
- [ ] Template compiles standalone
- [ ] All placeholders use {{}} syntax
- [ ] Header comment with source citation
- [ ] Trigger mechanism clearly marked
- [ ] Payload mechanism clearly marked
- [ ] Works with at least 2 test modules
- [ ] Added to pattern library (src/patterns/)
- [ ] Documentation updated (this file)
```

### 6.3 Example Contribution
```systemverilog
/**
 * Template: Timing Side-Channel Trojan
 * Source: Lin et al., "Trojan Side-Channels," CHES 2009
 * Adaptation: RISC-V cache timing modulation
 * Author: Contributor Name
 * Date: YYYY-MM-DD
 */

module {{MODULE_NAME}}_timing_trojan (
    input logic {{CLOCK_SIGNAL}},
    // ... rest of template
);
    // Implementation with clear comments
endmodule
```

---

## 7. References

[1] D. A. Bailey, "The RISC-V Files: Supervisor→Machine Privilege Escalation," 2017  
[2] T. Boraten and A. K. Kodi, "Performance degradation attacks in NoC," IEEE IPDPS, 2016  
[3] M. Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF, 2021

[Full bibliography in TRUST_HUB_PATTERNS.md]

---

## 8. Future Work

**Potential template additions:**
- [ ] Power side-channel templates
- [ ] Fault injection templates
- [ ] Multi-trigger templates (AND/OR conditions)
- [ ] Distributed Trojan templates (multiple modules)
- [ ] Parametric Trojan templates (analog effects)

**Template improvements:**
- [ ] Formal verification of templates
- [ ] Template composition (combine patterns)
- [ ] Machine learning-based template optimization
- [ ] Template effectiveness metrics

---

**Last Updated:** January 2025  
**Version:** 1.0.0  
**Maintainer:** Sharjeel Imtiaz (sharjeel.imtiaz@taltech.ee)