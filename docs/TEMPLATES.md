# RV-TroGen Template Library

## Overview

The RV-TroGen template library provides a systematic, reproducible approach to hardware Trojan generation through pre-defined SystemVerilog **code snippets**. This document explains the template structure, usage, and contribution guidelines.

---

## 1. Template Philosophy

### 1.1 Why Templates?

**Problem:** Pure programmatic generation creates a "black box" where:
- Generated code quality is hard to predict
- Structural patterns are implicit in code
- Comparison with literature is indirect
- Community contribution requires Python expertise

**Solution:** Template-based generation where:
- ✅ Patterns are explicit SystemVerilog **code snippets**
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

## 2. Template Structure ⭐ UPDATED

### 2.1 Templates as Code Snippets

**IMPORTANT:** RV-TroGen templates are **code snippets**, NOT standalone modules!

**What this means:**
- Templates contain only the **trigger logic** and **payload logic**
- Templates are **inserted into** the original module (not separate modules)
- Templates use `{{PLACEHOLDER}}` syntax for signal names
- Integration script (`prepare_simulation.py`) handles insertion

**Why code snippets?**
- ✅ Preserves original module structure
- ✅ Maintains module parameters and interfaces
- ✅ Easier to verify correct integration
- ✅ Realistic for security research (stealthy insertion)

### 2.2 Directory Organization
```
templates/trojan_templates/
├── sequential/           # 6 code snippet templates
│   ├── dos_template.sv
│   ├── leak_template.sv
│   ├── privilege_template.sv
│   ├── integrity_template.sv
│   ├── availability_template.sv
│   └── covert_template.sv
└── combinational/        # 6 code snippet templates
    ├── dos_template.sv
    ├── leak_template.sv
    ├── privilege_template.sv
    ├── integrity_template.sv
    ├── availability_template.sv
    └── covert_template.sv
```

### 2.3 Template File Structure

Each template file contains **two main sections**:

```systemverilog
/**
 * Template: DoS Trojan (Denial of Service)
 * Category: Sequential
 * Source: Trust-Hub AES-T1400
 * RISC-V Adaptation: Control signal disabling
 */

// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================
// This section is inserted BEFORE endmodule

// Trojan state
logic trojan_active;
logic [15:0] trojan_counter;

// Trojan trigger: Counter-based activation
always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    if (!{{RESET_SIGNAL}}) begin
        trojan_counter <= 16'd0;
        trojan_active <= 1'b0;
    end else begin
        // Count trigger signal activations
        if ({{TRIGGER_SIGNAL}}) begin
            trojan_counter <= trojan_counter + 16'd1;
        end
        
        // Activate after threshold (e.g., 1000 events)
        if (trojan_counter >= 16'd1000) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// How to modify the original module:

// When trojan is active, disable the payload signal:
// BEFORE: assign {{PAYLOAD_SIGNAL}} = <original_expression>;
// AFTER:  assign {{PAYLOAD_SIGNAL}} = trojan_active ? 1'b0 : <original_expression>;

// This disables the signal, causing denial of service.
```

### 2.4 Placeholder Syntax

Templates use `{{VARIABLE_NAME}}` syntax for signal substitution:

**Standard Placeholders:**
- `{{MODULE_NAME}}` - Original module name (for documentation)
- `{{CLOCK_SIGNAL}}` - Clock signal name (e.g., `clk_i`)
- `{{RESET_SIGNAL}}` - Reset signal name (e.g., `rst_ni`)
- `{{TRIGGER_SIGNAL}}` - Trojan trigger signal (e.g., `wr_en_i`)
- `{{PAYLOAD_SIGNAL}}` - Trojan payload signal (e.g., `rd_data_o`)

**Example Replacement:**
```systemverilog
// Template contains:
if ({{TRIGGER_SIGNAL}}) begin
    trojan_counter <= trojan_counter + 16'd1;
end

// Generator replaces with:
if (wr_en_i) begin
    trojan_counter <= trojan_counter + 16'd1;
end
```

---

## 3. Template Design Patterns

### 3.1 Sequential Template Pattern

**Structure:**
1. **State Declaration**: Trojan registers (counter, active flag)
2. **Trigger Logic**: Counter-based or condition-based activation
3. **Payload Instructions**: Comments explaining signal modifications

**Example (DoS):**
```systemverilog
// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================

// Trojan state
logic trojan_active;
logic [15:0] trojan_counter;

// Counter-based trigger
always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    if (!{{RESET_SIGNAL}}) begin
        trojan_counter <= 16'd0;
        trojan_active <= 1'b0;
    end else begin
        if ({{TRIGGER_SIGNAL}}) begin
            trojan_counter <= trojan_counter + 16'd1;
        end
        
        if (trojan_counter >= 16'd1000) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// Modify signal assignment:
// assign {{PAYLOAD_SIGNAL}} = trojan_active ? 1'b0 : <original>;
```

### 3.2 Combinational Template Pattern

**Structure:**
1. **Trigger Logic**: Condition detection (combinational)
2. **Payload Instructions**: Signal manipulation logic

**Example (Integrity):**
```systemverilog
// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================

// Detect trigger condition
logic trojan_triggered;
assign trojan_triggered = ({{TRIGGER_SIGNAL}} == TRIGGER_VALUE);

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// Corrupt signal when triggered:
// assign {{PAYLOAD_SIGNAL}} = trojan_triggered ? 
//                             (original_value ^ 32'hDEADBEEF) : 
//                             original_value;
```

---

## 4. How Templates Are Used (3-Phase Process)

### Phase 1: Template Creation (Done ✅)
- 12 templates created as code snippets
- Each template has trigger logic + payload instructions
- Trust-Hub citations included
- Stored in `templates/trojan_templates/`

### Phase 2: Code Generation (Automated ✅)
```python
# In sequential_gen.py or combinational_gen.py

# Load template
template_content = loader.load_template('dos', 'sequential')

# Replace placeholders with real signals
replacements = {
    'MODULE_NAME': 'ibex_csr',
    'CLOCK_SIGNAL': 'clk_i',
    'RESET_SIGNAL': 'rst_ni',
    'TRIGGER_SIGNAL': 'wr_en_i',
    'PAYLOAD_SIGNAL': 'wr_en_i'
}

# Generate trojan code snippet
trojan_code = replace_placeholders(template_content, replacements)

# Save to file: T1_ibex_csr_DoS.sv
```

### Phase 3: Integration (Automated ✅)
```python
# In prepare_simulation.py

# Read generated trojan snippet
trojan_code = read_file('T1_ibex_csr_DoS.sv')

# Extract trigger logic section
trigger_logic = extract_trigger_section(trojan_code)

# Insert trigger logic before endmodule
modified_rtl = insert_before_endmodule(original_rtl, trigger_logic)

# Modify signal assignments based on payload instructions
final_rtl = apply_payload_modifications(modified_rtl, payload_instructions)

# Save integrated module: ibex_csr_trojan.sv
```

---

## 5. Template-to-Literature Mapping

### 5.1 Sequential Templates (6 patterns)

| Template | Trust-Hub Source | Key Paper | RISC-V Adaptation |
|----------|-----------------|-----------|-------------------|
| dos_template.sv | AES-T1400 | - | Control signal disabling |
| leak_template.sv | RSA-T600 | - | CSR leakage to debug ports |
| privilege_template.sv | - | Bailey 2017 [1] | M/S/U mode manipulation |
| integrity_template.sv | AES-T800 | - | ALU output corruption |
| availability_template.sv | - | Boraten 2016 [2] | LSU stalling/delays |
| covert_template.sv | - | Lipp 2021 [3] | Timing modulation |

### 5.2 Combinational Templates (6 patterns)

Same patterns as sequential, but using combinational logic:
- `assign` statements instead of `always_ff`
- Condition-based triggers instead of counters
- Immediate payload effects

### 5.3 Adaptation Methodology

For each template:
1. ✅ Downloaded source (Trust-Hub or paper)
2. ✅ Analyzed trigger mechanism
3. ✅ Analyzed payload mechanism
4. ✅ Adapted for RISC-V signal patterns
5. ✅ Created code snippet format
6. ✅ Documented payload instructions
7. ✅ Verified with integration script

---

## 6. Template Validation

### 6.1 Generation Testing
```bash
# Test template instantiation
python src/generator/trojan_generator.py examples/ibex/original/ibex_csr.sv

# Expected output:
# T1_ibex_csr_DoS.sv
# - Uses real signal: wr_en_i ✅
# - NO hardcoded 'valid_signal' ✅
```

### 6.2 Integration Testing
```bash
# Test trojan integration
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv

# Verify integrated file:
# - Trigger logic inserted before endmodule ✅
# - Signal assignments modified ✅
# - Uses real signals from module ✅
```

### 6.3 Compilation Testing
```bash
# Upload to server and compile
scp ibex_csr_trojan.sv server:/workdir/
ssh server
vlog +acc ibex_csr_trojan.sv
# Should compile without errors ✅
```

### 6.4 Structural Validation

Each template must have:
- [ ] Clear trigger mechanism (commented)
- [ ] Clear payload instructions (commented)
- [ ] All placeholders use `{{}}` syntax
- [ ] Source citation in header
- [ ] RISC-V adaptation notes
- [ ] Integration instructions

---

## 7. Example: DoS Template Workflow

### Step 1: Template File (`dos_template.sv`)
```systemverilog
/**
 * Template: DoS Trojan
 * Source: Trust-Hub AES-T1400
 */

// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================

logic trojan_active;
logic [15:0] trojan_counter;

always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    if (!{{RESET_SIGNAL}}) begin
        trojan_counter <= 16'd0;
        trojan_active <= 1'b0;
    end else begin
        if ({{TRIGGER_SIGNAL}}) begin
            trojan_counter <= trojan_counter + 16'd1;
        end
        if (trojan_counter >= 16'd1000) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// assign {{PAYLOAD_SIGNAL}} = trojan_active ? 1'b0 : <original>;
```

### Step 2: Generated File (`T1_ibex_csr_DoS.sv`)
```systemverilog
/**
 * Template: DoS Trojan
 * Source: Trust-Hub AES-T1400
 * Module: ibex_csr
 */

// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================

logic trojan_active;
logic [15:0] trojan_counter;

always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_counter <= 16'd0;
        trojan_active <= 1'b0;
    end else begin
        if (wr_en_i) begin
            trojan_counter <= trojan_counter + 16'd1;
        end
        if (trojan_counter >= 16'd1000) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// assign wr_en_i = trojan_active ? 1'b0 : <original>;
```

### Step 3: Integrated File (`ibex_csr_trojan.sv`)
```systemverilog
module ibex_csr_trojan #(
    parameter int unsigned Width = 32
) (
    input  logic                 clk_i,
    input  logic                 rst_ni,
    input  logic                 wr_en_i,
    output logic [Width-1:0]     rd_data_o
);

    // Forward declaration
    logic trojan_active;
    
    // Original module logic here...
    
    // Modified signal assignment (payload)
    assign wr_en_i_internal = trojan_active ? 1'b0 : wr_en_i;
    
    // ... rest of original logic ...
    
    // ============================================================
    // TROJAN TRIGGER LOGIC (inserted before endmodule)
    // ============================================================
    
    logic [15:0] trojan_counter;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= 16'd0;
            trojan_active <= 1'b0;
        end else begin
            if (wr_en_i) begin
                trojan_counter <= trojan_counter + 16'd1;
            end
            if (trojan_counter >= 16'd1000) begin
                trojan_active <= 1'b1;
            end
        end
    end

endmodule
```

---

## 8. Contributing New Templates

### 8.1 Process

1. **Research**: Find new Trojan pattern in literature
2. **Design**: Create code snippet template
3. **Test Generation**: Verify placeholder replacement works
4. **Test Integration**: Verify insertion into real modules
5. **Document**: Add to this file with citations
6. **Submit**: Pull request with documentation

### 8.2 Template Checklist
```markdown
- [ ] Template is a CODE SNIPPET (not standalone module)
- [ ] Has clear TRIGGER LOGIC section
- [ ] Has clear PAYLOAD INSTRUCTIONS section
- [ ] All placeholders use {{}} syntax
- [ ] Header comment with source citation
- [ ] Works with trojan_generator.py
- [ ] Works with prepare_simulation.py
- [ ] Integration tested on real module
- [ ] Documentation updated (this file)
```

### 8.3 Example New Template
```systemverilog
/**
 * Template: Custom Pattern Name
 * Category: Sequential
 * Source: Your Source (Paper/Trust-Hub)
 * RISC-V Adaptation: Your adaptation notes
 * Author: Your Name
 * Date: YYYY-MM-DD
 */

// ============================================================
// TROJAN TRIGGER LOGIC
// ============================================================

// Your trigger logic here using placeholders
logic trojan_active;

always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    // Your implementation
end

// ============================================================
// PAYLOAD INSTRUCTIONS
// ============================================================
// Detailed instructions on how to modify signals
// Example:
// assign {{PAYLOAD_SIGNAL}} = trojan_active ? <effect> : <original>;
```

---

## 9. Common Template Patterns

### 9.1 Counter-Based Trigger
```systemverilog
logic [15:0] counter;

always_ff @(posedge {{CLOCK_SIGNAL}}) begin
    if ({{TRIGGER_SIGNAL}}) begin
        counter <= counter + 16'd1;
    end
    
    if (counter >= THRESHOLD) begin
        trojan_active <= 1'b1;
    end
end
```

### 9.2 Condition-Based Trigger
```systemverilog
always_ff @(posedge {{CLOCK_SIGNAL}}) begin
    if ({{TRIGGER_SIGNAL}} == SPECIFIC_VALUE) begin
        trojan_active <= 1'b1;
    end
end
```

### 9.3 Signal Disabling Payload
```systemverilog
// PAYLOAD INSTRUCTIONS:
// assign {{PAYLOAD_SIGNAL}} = trojan_active ? 1'b0 : <original>;
```

### 9.4 Signal Corruption Payload
```systemverilog
// PAYLOAD INSTRUCTIONS:
// assign {{PAYLOAD_SIGNAL}} = trojan_active ? 
//                             (<original> ^ CORRUPTION_MASK) : 
//                             <original>;
```

### 9.5 Signal Leakage Payload
```systemverilog
// PAYLOAD INSTRUCTIONS:
// assign {{LEAK_OUTPUT}} = trojan_active ? {{SENSITIVE_SIGNAL}} : 1'b0;
```

---

## 10. References

[1] D. A. Bailey, "The RISC-V Files: Supervisor→Machine Privilege Escalation," 2017  
[2] T. Boraten and A. K. Kodi, "Performance degradation attacks in NoC," IEEE IPDPS, 2016  
[3] M. Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF, 2021

[Full bibliography in TRUST_HUB_PATTERNS.md]

---

## 11. Frequently Asked Questions

### Q: Why code snippets instead of standalone modules?

**A:** Code snippets are more realistic for security research:
- Actual Trojans are inserted into existing modules, not separate
- Easier to maintain original module parameters/interfaces
- More stealthy (preserves module structure)
- Simpler integration testing

### Q: How do I verify templates work?

**A:** Three-step verification:
1. Generate trojan: `python scripts/generate_trojans.py <module.sv>`
2. Integrate trojan: `python scripts/prepare_simulation.py <module.sv>`
3. Compile on server: `vlog <module>_trojan.sv`

### Q: What if my pattern needs custom logic?

**A:** Templates support custom patterns:
- Add new placeholders in template file
- Update generator to provide values
- Document in PAYLOAD INSTRUCTIONS section

### Q: Can templates handle parameterized modules?

**A:** Yes! The integration script (`prepare_simulation.py`) uses `simple_parser.py` which correctly handles parameters like `[Width-1:0]`.

---

## 12. Future Work

**Potential template additions:**
- [ ] Power side-channel templates
- [ ] Fault injection templates  
- [ ] Multi-trigger templates (AND/OR conditions)
- [ ] Distributed Trojan templates (multiple modules)
- [ ] Parametric Trojan templates (analog effects)

**Template improvements:**
- [ ] Formal verification of template correctness
- [ ] Template composition (combine multiple patterns)
- [ ] Template effectiveness metrics
- [ ] Automatic payload strategy selection

---

**Last Updated:** January 19, 2026  
**Version:** 2.0.0 (Updated for code snippet architecture)  
**Maintainer:** Sharjeel Imtiaz (sharjeel.imtiaz@taltech.ee)

---

## Summary of Changes from Version 1.0

**Major Changes:**
1. ✅ Templates are now **code snippets**, not standalone modules
2. ✅ Two-section structure: TRIGGER LOGIC + PAYLOAD INSTRUCTIONS
3. ✅ Integration workflow documented (3-phase process)
4. ✅ Example showing complete workflow from template → integrated module
5. ✅ Updated validation procedures for snippet-based approach

**Why this matters:**
- More realistic Trojan insertion methodology
- Easier verification and testing
- Better alignment with security research practices
- Cleaner integration into existing RTL