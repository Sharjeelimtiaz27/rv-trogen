# 🚀 Quick Start Guide

**Get RV-TroGen Running in 15 Minutes**

This guide will walk you through installing RV-TroGen and generating your first hardware Trojans.

---

## 📋 What You'll Learn

By the end of this guide (15 minutes), you'll know how to:

1. **Install RV-TroGen** (2 min)
2. **Parse RISC-V modules** (3 min)
3. **Extract and analyze signals** (3 min)
4. **Classify modules** (2 min)
5. **Generate hardware Trojans** (5 min) ⭐ Uses template library!

**Total Time:** ~15 minutes

---

## Prerequisites

- Python 3.8 or higher
- Git (for cloning)
- Basic command-line knowledge
- (Optional) Verilator for verification

---

## Part 1: Installation (2 Minutes)

### Step 1: Clone Repository
```bash
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git
cd rv-trogen
```

### Step 2: Install Package

**Option 1: Automated (Recommended)**
```bash
python install.py
```
This shows a welcome banner with quick commands!

**Option 2: Traditional**
```bash
python -m pip install -e .
```

### Step 3: Verify Installation
```bash
python -c "from src.parser import RTLParser; print('✅ Installation successful!')"
```

**Expected Output:**
```
✅ Installation successful!
```

---

## Part 2: Parse Your First Module (3 Minutes)

### Step 1: Parse a RISC-V Module
```bash
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv
```

**Expected Output:**
```
🔍 Parsing: ibex_cs_registers.sv

============================================================
Module: ibex_cs_registers
Type: Sequential
Inputs:    15
Outputs:   8
Internal:  42
Has Clock: True (clk_i)
Has Reset: True (rst_ni)
============================================================
```

### Step 2: Understanding the Output

- **Module Name:** The name extracted from `module` declaration
- **Type:** Sequential (has clock) or Combinational (no clock)
- **Signals:** Count of inputs, outputs, and internal signals
- **Clock/Reset:** Detected clock and reset signals

### Step 3: Try Another Module
```bash
python -m src.parser.rtl_parser examples/ibex/original/ibex_alu.sv
```

Notice this one might be **Combinational** (no clock signal).

---

## Part 3: Signal Extraction (3 Minutes)

### Step 1: Extract Detailed Signal Information
```python
# Create file: test_signals.py
from src.parser import RTLParser

parser = RTLParser('examples/ibex/original/ibex_cs_registers.sv')
module = parser.parse()

print(f"📊 Module: {module.name}\n")

print("📥 Inputs:")
for signal in module.inputs[:5]:  # Show first 5
    print(f"  - {signal}")

print("\n📤 Outputs:")
for signal in module.outputs[:5]:
    print(f"  - {signal}")

print(f"\n🔧 Internal Signals: {len(module.internals)} total")
print(f"⏰ Clock: {module.clock_signal}")
print(f"🔄 Reset: {module.reset_signal}")
```

### Step 2: Run It
```bash
python test_signals.py
```

**Expected Output:**
```
📊 Module: ibex_cs_registers

📥 Inputs:
  - clk_i
  - rst_ni
  - csr_we_int
  - csr_addr
  - csr_wdata_int

📤 Outputs:
  - csr_rdata_o
  - priv_lvl_q
  - ...

🔧 Internal Signals: 42 total
⏰ Clock: clk_i
🔄 Reset: rst_ni
```

---

## Part 4: Module Classification (2 Minutes)

### Understanding Sequential vs Combinational

**Sequential modules** have:
- Clock signal (`clk`, `clk_i`)
- `always_ff` blocks
- Registers/state

**Combinational modules** have:
- No clock
- `always_comb` or `assign` statements
- Pure logic, no state

### Step 1: Classify Multiple Modules
```bash
python -m scripts.batch_parse --dir examples/ibex/original
```

**Expected Output:**
```
Processing: examples/ibex/original/

Module: ibex_cs_registers    [Sequential]  ⏰
Module: ibex_alu             [Combinational]
Module: ibex_decoder         [Sequential]  ⏰
Module: ibex_controller      [Sequential]  ⏰

Summary:
  Sequential: 15 modules
  Combinational: 8 modules
  Total: 23 modules
```

### Step 2: Filter Security-Critical Modules
```bash
python -m scripts.batch_parse --dir examples/ibex/original --security-only
```

This shows only modules with security-relevant keywords like:
- `csr`, `priv`, `pmp`, `mstatus`
- `privilege`, `mode`, `secure`

---

## Part 5: Rank Modules by Security (2 Minutes)

### Step 1: Security Ranking
```bash
python -m scripts.parse_and_rank examples/ibex/original --top 5
```

**Expected Output:**
```
🔒 Top 5 Security-Critical Modules:

1. ibex_cs_registers (Score: 95/100)
   - CSR management, privilege control
   - Signals: mstatus, priv_lvl_q, mtvec

2. ibex_pmp (Score: 90/100)
   - Physical memory protection
   - Signals: pmp_cfg, pmp_addr

3. ibex_controller (Score: 85/100)
   - Core control logic
   - Signals: ctrl_fsm_cs, debug_mode

4. ibex_decoder (Score: 75/100)
   - Instruction decoding
   - Signals: instr_valid, illegal_insn

5. ibex_load_store_unit (Score: 70/100)
   - Memory access control
   - Signals: lsu_req, lsu_we
```

### Understanding the Score

The ranking system considers:
- Signal name keywords (e.g., `priv`, `csr`, `secure`)
- Module name keywords
- Number of security-relevant signals
- Sequential vs combinational (sequential ranked higher)

---

## Part 6: Generate Hardware Trojans (5 Minutes) ⭐ NEW!

### Step 1: Generate Trojans for a Module
```bash
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

**Expected Output:**
```
📊 Module type: Sequential
🎯 Generating Trojans for: ibex_cs_registers

✅ DoS: Found 5 triggers, 8 payloads
✅ Leak: Found 3 triggers, 6 payloads
✅ Privilege: Found 4 triggers, 2 payloads
✅ Integrity: Found 7 triggers, 10 payloads
✅ Availability: Found 5 triggers, 8 payloads
✅ Covert: Found 4 triggers, 6 payloads

📄 Summary saved to: examples/ibex/generated_trojans/ibex_cs_registers/ibex_cs_registers_trojan_summary.md

✅ Generated 6 Trojan variants!
```

### Step 2: Explore Generated Files
```bash
# Windows
dir examples\ibex\generated_trojans\ibex_cs_registers

# Linux/Mac
ls -la examples/ibex/generated_trojans/ibex_cs_registers/
```

**You should see:**
```
T1_ibex_cs_registers_DoS.sv           # Denial of Service
T2_ibex_cs_registers_Leak.sv          # Information Leakage
T3_ibex_cs_registers_Privilege.sv     # Privilege Escalation
T4_ibex_cs_registers_Integrity.sv     # Data Integrity Violation
T5_ibex_cs_registers_Availability.sv  # Performance Degradation
T6_ibex_cs_registers_Covert.sv        # Covert Channel
ibex_cs_registers_trojan_summary.md   # Summary report
```

### Step 3: View the Summary
```bash
# Windows
type examples\ibex\generated_trojans\ibex_cs_registers\ibex_cs_registers_trojan_summary.md

# Linux/Mac
cat examples/ibex/generated_trojans/ibex_cs_registers/ibex_cs_registers_trojan_summary.md
```

**Summary includes:**
- Module statistics
- Generated Trojan descriptions
- Usage instructions
- File locations

### Step 4: Examine a Generated Trojan
```bash
# View the DoS Trojan
type examples\ibex\generated_trojans\ibex_cs_registers\T1_ibex_cs_registers_DoS.sv
```

**Look for:**
- `// TROJAN TRIGGER LOGIC` section
- `// TROJAN PAYLOAD LOGIC` section
- Counter-based or condition-based triggers
- Signal manipulation in payload

### Step 5: Understanding Trojan Types

**T1 - Denial of Service (DoS):**
- Disables functionality by forcing control signals to 0
- Example: Forces `instr_valid_o` to 0, preventing execution

**T2 - Information Leakage:**
- Leaks sensitive data (CSR contents, keys) to unused ports
- Example: Copies `mstatus` to debug output port

**T3 - Privilege Escalation:**
- Escalates privilege level to Machine mode
- Example: Forces `priv_lvl_q` to 2'b11 (M-mode)

**T4 - Integrity Violation:**
- Corrupts computation results
- Example: XORs ALU output with corruption pattern

**T5 - Performance Degradation:**
- Slows operations through artificial delays
- Example: Adds 15 cycles to memory operations

**T6 - Covert Channel:**
- Creates timing-based communication channel
- Example: Modulates delays to encode secret bits

### Step 6: Generate Trojans for Other Modules
```bash
# Try different security-critical modules
python scripts/generate_trojans.py examples/ibex/original/ibex_pmp.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_controller.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_alu.sv
```

---

## 📚 Understanding Template-Based Generation

RV-TroGen uses **template-based generation** for reproducibility:

### What Are Templates?

Templates are pre-defined SystemVerilog files with placeholders:
```systemverilog
module {{MODULE_NAME}}_trojan (
    input logic {{CLOCK_SIGNAL}},
    input logic {{TRIGGER_SIGNAL}},
    output logic {{PAYLOAD_SIGNAL}}
);
    // Trojan logic with placeholders
endmodule
```

The generator:
1. Loads appropriate template (sequential or combinational)
2. Matches signals from your module to placeholders
3. Replaces placeholders with actual signal names
4. Generates working SystemVerilog code

### Benefits of Templates:

- ✅ **Reproducible**: Same template → same structure
- ✅ **Verifiable**: Templates can be compiled independently
- ✅ **Extensible**: Add new patterns by creating new templates
- ✅ **Educational**: Templates show Trojan structure clearly

**Location:** `templates/trojan_templates/`
- `sequential/` - 6 templates for sequential logic
- `combinational/` - 6 templates for combinational logic

**See:** [docs/TEMPLATES.md](TEMPLATES.md) for detailed documentation.

---

## 🎯 What Can You Do Now?

After completing this guide, you can:

✅ Parse any RISC-V module  
✅ Extract and analyze signals  
✅ Classify sequential vs combinational modules  
✅ Rank modules by security importance  
✅ Generate 6 types of hardware Trojans automatically  
✅ Understand template-based generation  

---

## 🔍 Next Steps

### Week 2: Advanced Features (Steps 10-13)
- Validate templates with Verilator
- Batch generation for multiple modules
- Custom template creation
- Performance analysis

### Week 3: Validation (Steps 14-19)
- Simulate Trojans vs original modules
- Compare behaviors
- Analyze waveforms
- Generate HTML reports

### Week 4-5: Research & Publication
- Compare with Trust-Hub benchmarks
- Measure detection difficulty
- Write paper
- Publish tool

---

## 📖 Learn More

### Documentation
- [Commands Reference](COMMANDS_REFERENCE.md) - All CLI commands
- [Template Documentation](TEMPLATES.md) - Template system explained
- [Trust-Hub Patterns](TRUST_HUB_PATTERNS.md) - Pattern library with citations
- [Step Guide](STEP_GUIDE.md) - Detailed progress tracking

### Examples
- `examples/parser_usage.py` - Parser examples
- `examples/ibex/generated_trojans/` - Generated Trojan examples

### Code
- `src/parser/` - RTL parsing logic
- `src/patterns/` - Trojan pattern definitions
- `src/generator/` - Trojan generation logic
- `templates/trojan_templates/` - SystemVerilog templates

---

## 🐛 Troubleshooting

### Issue: "Module not found"
**Solution:**
```bash
python -m pip install -e .
```

### Issue: "No such file: ibex_cs_registers.sv"
**Solution:** Check you're in the `rv-trogen/` directory:
```bash
cd path/to/rv-trogen
ls examples/ibex/original/
```

### Issue: "No Trojans generated"
**Possible causes:**
1. Module is too simple (no suitable signals)
2. No clock signal detected (for sequential patterns)
3. Pattern matching failed

**Solution:** Try a different module, like `ibex_cs_registers.sv`

### Issue: Import errors
**Solution:** Reinstall package:
```bash
python -m pip uninstall rv-trogen
python -m pip install -e .
```

---

## 💡 Tips & Tricks

### Tip 1: Start with Security-Critical Modules
```bash
python -m scripts.parse_and_rank examples/ibex/original --top 3
# Focus on top 3 for best Trojan generation
```

### Tip 2: View Generated Code
Open generated `.sv` files in a text editor to learn Trojan structure.

### Tip 3: Compare with Original
Keep original and Trojan side-by-side to see differences:
```bash
code examples/ibex/original/ibex_cs_registers.sv
code examples/ibex/generated_trojans/ibex_cs_registers/T1_ibex_cs_registers_DoS.sv
```

### Tip 4: Customize Templates
Want to create your own Trojan pattern?
1. Copy existing template from `templates/trojan_templates/`
2. Modify trigger/payload logic
3. Add to pattern library
4. Regenerate Trojans

See [TEMPLATES.md](TEMPLATES.md) for details.

---

## 🎓 For Researchers

### Using RV-TroGen in Your Research

1. **Generate benchmark set:**
```bash
   python -m scripts.batch_parse --dir my_processor/ --security-only
   # Generates Trojans for all security-critical modules
```

2. **Test detection algorithms:**
   - Use generated Trojans as test cases
   - Measure detection rates
   - Compare with Trust-Hub benchmarks

3. **Validate formal verification:**
   - Generate Trojans for modules with assertions
   - Check if assertions catch Trojans
   - Measure false positive/negative rates

4. **Cite the tool:**
```bibtex
   @misc{rvtrogen2026,
     author = {Imtiaz, Sharjeel},
     title = {RV-TroGen: Automated Hardware Trojan Generation for RISC-V},
     year = {2026},
     url = {https://github.com/sharjeelimtiaz27/rv-trogen}
   }
```

---

## ✅ Quick Reference Card
```
📦 Installation:
   python install.py

🔍 Parse single module:
   python -m src.parser.rtl_parser <file.sv>

📁 Parse directory:
   python -m scripts.batch_parse --dir <dir>

🔒 Security ranking:
   python -m scripts.parse_and_rank <dir> --top 5

⚡ Generate Trojans:
   python scripts/generate_trojans.py <file.sv>

🧪 Run tests:
   python -m pytest tests/ -v

📚 Documentation:
   docs/QUICK_START.md (this file)
   docs/COMMANDS_REFERENCE.md
   docs/TEMPLATES.md
```

---

## 🎉 Congratulations!

You've completed the Quick Start guide! You now know how to:

✅ Install and verify RV-TroGen  
✅ Parse RISC-V modules and extract signals  
✅ Classify and rank modules by security  
✅ Generate hardware Trojans using templates  
✅ Understand template-based generation  

**Progress:** You've completed Week 1-2 features (30% of project)!

---

## 📧 Need Help?

- **Documentation:** See `docs/` folder
- **Issues:** https://github.com/sharjeelimtiaz27/rv-trogen/issues
- **Email:** sharjeel.imtiaz@taltech.ee

---

````
**Last Updated:** January 9, 2026  
**Version:** 1.0.0-beta  
**Status:** Step 15 Complete (15/30 steps, 50%) - Remote simulation working!
````