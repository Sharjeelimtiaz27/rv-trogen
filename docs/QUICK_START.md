# 🚀 Quick Start Guide

**Get RV-TroGen Running in 15 Minutes**

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
- matplotlib (`pip install matplotlib`) — for VCD analysis plots

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

**Option 2: Traditional**
```bash
python -m pip install -e .
```

### Step 3: Verify Installation
```bash
python -c "from src.parser import RTLParser; print('✅ Installation successful!')"
```

---

## Part 2: Parse Your First Module (3 Minutes)

### Step 1: Parse the Primary Target Module
```bash
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv
```

**Expected Output:**
```
🔍 Parsing: ibex_cs_registers.sv

============================================================
Module: ibex_cs_registers
Type: Sequential
Inputs:    15+
Outputs:   8+
Internal:  42+
Has Clock: True (clk_i)
Has Reset: True (rst_ni)
============================================================
```

> `ibex_cs_registers` is the primary target — it is the most security-critical
> module in the Ibex core, controlling CSR registers, privilege modes, interrupts,
> and memory protection.

### Step 2: Understanding the Output

- **Module Name:** Extracted from `module` declaration
- **Type:** Sequential (has clock/FFs) or Combinational (pure logic)
- **Signals:** Count of inputs, outputs, and internal signals
- **Clock/Reset:** Detected clock and reset signals

### Step 3: Try Another Module
```bash
python -m src.parser.rtl_parser examples/ibex/original/ibex_alu.sv
```
This one is **Combinational** (no clock signal).

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
for signal in module.inputs[:5]:
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

---

## Part 4: Module Classification (2 Minutes)

### Classify Multiple Modules
```bash
python -m scripts.batch_parse --dir examples/ibex/original
```

### Filter Security-Critical Modules
```bash
python -m scripts.batch_parse --dir examples/ibex/original --security-only
```

---

## Part 5: Rank Modules by Security (2 Minutes)

```bash
python scripts/parse_and_rank.py examples/ibex/original --top 5
```

**Expected Output:**
```
🔒 Top 5 Security-Critical Modules:

1. ibex_cs_registers (Score: 95/100)
   - CSR management, privilege control, interrupt handling
   - Signals: mstatus, priv_lvl_q, mtvec, csr_we_int

2. ibex_pmp (Score: 90/100)
   - Physical memory protection
   - Signals: pmp_cfg, pmp_addr

3. ibex_controller (Score: 85/100)
   - Core control logic
   - Signals: ctrl_fsm_cs, debug_mode
```

---

## Part 6: Generate Hardware Trojans (5 Minutes) ⭐

### Step 1: Generate All 6 Trojans for ibex_cs_registers
```bash
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

**Expected Output:**
```
📊 Module type: Sequential
🎯 Generating Trojans for: ibex_cs_registers

✅ DoS:          Found triggers and payload signals
✅ Availability: Found triggers and payload signals
✅ Integrity:    Found triggers and payload signals
✅ Covert:       Found triggers and payload signals
✅ Leak:         Found triggers and payload signals
✅ Privilege:    Found triggers and payload signals

✅ Generated 6 Trojan variants!
```

### Step 2: Explore Generated Files
```bash
# Linux/Mac
ls -la examples/ibex/generated_trojans/ibex_cs_registers/

# Windows
dir examples\ibex\generated_trojans\ibex_cs_registers
```

**You should see:**
```
T1_ibex_cs_registers_DoS.sv           # Denial of Service
T2_ibex_cs_registers_Availability.sv  # Availability Degradation
T3_ibex_cs_registers_Integrity.sv     # Data Integrity Corruption
T4_ibex_cs_registers_Covert.sv        # Covert Channel
T5_ibex_cs_registers_Leak.sv          # Information Leakage
T6_ibex_cs_registers_Privilege.sv     # Privilege Escalation
ibex_cs_registers_trojan_summary.md   # Summary report
```

### Step 3: Understanding the 6 Trojan Types

**T1 - Denial of Service (DoS):**
- Permanently disables `csr_we_int` (CSR write enable) after trigger fires
- Effect: no more CSR writes possible → processor security state frozen

**T2 - Availability Degradation:**
- Blocks `csr_we_int` on a 50% duty cycle (8 stall / 16 period)
- Effect: intermittent CSR write failures, harder to detect than full DoS

**T3 - Integrity Corruption:**
- XORs all `csr_rdata_o` reads with `0xDEADBEEF`
- Effect: CPU receives systematically corrupted CSR values

**T4 - Covert Channel:**
- Encodes secret data in pulse width of `csr_rdata_o[0]`
  (10 clock cycles = bit '1', 5 clock cycles = bit '0')
- Effect: exfiltrates data via timing — attacker must count pulse durations

**T5 - Information Leakage:**
- Routes CSR write data (`csr_wdata_i`) to normally-stable `csr_mepc_o` port
- Effect: secret write data readable as a value on the exception PC output

**T6 - Privilege Escalation:**
- Forces `priv_mode_id_o` and internal `priv_lvl_q` register to `PRIV_LVL_M` (2'b11)
- Effect: any user-mode code gets full machine-mode access

---

## 📚 Understanding Template-Based Generation

RV-TroGen uses **template-based generation** for reproducibility:

### What Are Templates?

Templates are pre-defined SystemVerilog files with placeholders:
```systemverilog
// TROJAN TRIGGER LOGIC
logic [15:0] trojan_counter;
logic        trojan_active;
always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    if (!{{RESET_SIGNAL}}) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else if ({{TRIGGER_SIGNAL}} && !trojan_active) begin
        if (trojan_counter >= TRIGGER_THRESHOLD)
            trojan_active <= 1'b1;
        else
            trojan_counter <= trojan_counter + 1;
    end
end
```

### Benefits of Templates:
- ✅ **Reproducible**: Same template → same structure
- ✅ **Verifiable**: Templates compile independently in QuestaSim
- ✅ **Extensible**: Add new patterns by creating new templates
- ✅ **Educational**: Templates show Trojan structure clearly

**Location:** `templates/trojan_templates/`
- `sequential/` — 6 templates for sequential logic (with clock/FF)
- `combinational/` — 6 templates for combinational logic

---

## 🎯 What Can You Do Now?

After completing this guide:

✅ Parse any RISC-V module
✅ Extract and analyze signals
✅ Classify sequential vs combinational modules
✅ Rank modules by security importance
✅ Generate 6 types of hardware Trojans automatically
✅ Understand template-based generation

---

## 🔮 Next Steps

### Simulation & Validation
- Integrate trojans into RTL: `prepare_multi_trojan_simulation.py`
- Upload to QuestaSim server, simulate all 6 trojans
- Download VCDs and analyze: `analyze_vcd.py`
- See [SIMULATION_SETUP.md](SIMULATION_SETUP.md) for full workflow

### Paper Writing
- See [SIX_PATTERN_DEFENSE_UPDATED.docx] for copy-paste defense paragraphs
- See [QUICK_REFERENCE_CARD.md](QUICK_REFERENCE_CARD.md) for Trust-Hub mapping

---

## 📖 Learn More

- [Commands Reference](COMMANDS_REFERENCE.md) — All CLI commands
- [Simulation Setup](SIMULATION_SETUP.md) — Server simulation workflow
- [Quick Reference Card](QUICK_REFERENCE_CARD.md) — Pattern defense guide

---

## 🐛 Troubleshooting

### Issue: "Module not found"
```bash
python -m pip install -e .
```

### Issue: "No such file: ibex_cs_registers.sv"
```bash
cd path/to/rv-trogen
ls examples/ibex/original/
```

### Issue: "No Trojans generated"
Try the primary target: `ibex_cs_registers.sv` — it has all required signal types.

### Issue: "VCD analysis shows no differences"
- Check `trojan_active` went HIGH in GTKWave
- Ensure simulation ran enough cycles (>25,000)
- Verify `csr_op_i` was driven to `CSR_OP_WRITE` in testbench

---

## ✅ Quick Reference
```
📦 Installation:
   python install.py

🔍 Parse single module:
   python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv

📊 Batch parse directory:
   python scripts/batch_parse.py --dir examples/ibex/original

🔒 Security ranking:
   python scripts/parse_and_rank.py examples/ibex/original --top 5

⚡ Generate 6 Trojans:
   python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

🔧 Prepare simulation files:
   python scripts/prepare_multi_trojan_simulation.py \
       examples/ibex/original/ibex_cs_registers.sv \
       --trojans examples/ibex/generated_trojans/ibex_cs_registers

📊 Analyze VCDs (batch):
   python scripts/analyze_vcd.py \
       --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

📊 Analyze single trojan:
   python scripts/analyze_vcd.py \
       --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_DoS.vcd

🧪 Run tests:
   python -m pytest tests/ -v
```

---

**Last Updated:** March 2026
**Version:** 4.0.0
**Status:** Six-pattern validation complete ✅