# Quick Start Guide - RV-TroGen

**For Complete Beginners** 👋

This guide assumes you know nothing about the project. We'll go step by step.

---

## What You'll Learn

1. ✅ Install RV-TroGen
2. ✅ Parse your first module
3. ✅ Parse multiple modules
4. ✅ Find security-critical modules
5. ✅ Run tests
6. ✅ Understand the output

**Time:** 15 minutes

---

## Prerequisites

- Python 3.8 or higher
- Git installed
- Windows 11, Linux, or macOS
- Basic command line knowledge

---



## Part 1: Installation (2 minutes)

### **Step 1: Clone Repository**

Open Command Prompt (Windows) or Terminal (Linux/Mac):
```bash
# Navigate to where you want the project
cd Desktop

# Clone the repository
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git

# Enter directory
cd rv-trogen
```

### **Step 2: Install Package**
```bash
# Install RV-TroGen
python -m pip install -e .

# You should see:
# Successfully installed rv-trojangen-1.0.0
```
---

## 💡 Why `python -m pip` Instead of `pip`?

You might notice we use `python -m pip install` instead of just `pip install`.

**Reasons:**
1. **Works on restricted Windows systems** (like university PCs)
2. **Always uses the correct Python** (important if you have multiple versions)
3. **More reliable** - doesn't depend on PATH configuration
4. **Recommended by Python.org** - official best practice

**Both commands do the same thing, but `python -m pip` is more robust!**

--- 
### **Step 3: Verify Installation**
```bash
# Test import
python -c "from src.parser import RTLParser; print('✅ Success!')"

# Should print: ✅ Success!
```

**✅ If you see "Success!" - you're ready!**

---

## Part 2: Parse Your First Module (3 minutes)

### **What is Parsing?**

Parsing means reading a Verilog/SystemVerilog file and extracting information like:
- Module name
- Input/output signals
- Internal signals
- Whether it's sequential or combinational

### **Try It:**
```bash
# Parse an Ibex CSR module
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv
```

### **Expected Output:**
```
🔍 Parsing: ibex_cs_registers.sv

============================================================
Module: ibex_cs_registers
File: ibex_cs_registers.sv
============================================================
Inputs:    15
Outputs:   8
Internals: 47
Has Clock: True
Has Reset: True
Type:      Sequential
Clock:     clk_i
Reset:     rst_ni
============================================================

📥 INPUTS:
  input clk_i
  input rst_ni
  input [31:0] boot_addr_i
  ...

📤 OUTPUTS:
  output [31:0] csr_rdata_o
  output csr_illegal_o
  ...

🔧 INTERNAL SIGNALS: (showing first 10 of 47)
  logic [31:0] mtvec_q
  logic [31:0] mscratch_q
  ...

✅ Parsing complete!
```

### **What Does This Mean?**

- **Module:** `ibex_cs_registers` - The CSR (Control & Status Register) module
- **Type:** Sequential - Has state (uses flip-flops)
- **Inputs:** 15 input signals
- **Outputs:** 8 output signals
- **Clock:** `clk_i` - Clock signal detected
- **Reset:** `rst_ni` - Reset signal detected (active low)

**This module is CRITICAL for security** - it controls privilege levels!

---

## Part 3: Parse Multiple Modules (5 minutes)

### **Batch Parsing**

Instead of parsing one file at a time, parse all files in a directory:
```bash
# Parse all .sv files in Ibex directory
python -m scripts/batch_parse.py --dir examples/ibex/original
```

### **Expected Output:**
```
🔍 Found 15 files to parse

[1/15] Parsing: ibex_alu.sv... ✅
[2/15] Parsing: ibex_cs_registers.sv... ✅
[3/15] Parsing: ibex_compressed_decoder.sv... ✅
[4/15] Parsing: ibex_controller.sv... ✅
[5/15] Parsing: ibex_core.sv... ✅
...
[15/15] Parsing: ibex_wb_stage.sv... ✅

============================================================
✅ Successfully parsed: 15/15
============================================================

============================================================
PARSING SUMMARY
============================================================
Total Modules:    15
Sequential:       10
Combinational:    5
With Clock:       10
With Reset:       10
Total Signals:    804
  - Inputs:       187
  - Outputs:      94
  - Internals:    523
============================================================
```

### **Save Results to JSON**
```bash
# Parse and save to JSON
python -m scripts/batch_parse.py --dir examples/ibex/original --save-json

# Creates: parsed_results/parse_summary.json
```

**You can now open `parse_summary.json` in any text editor to see all the data!**

---

## Part 4: Find Security-Critical Modules (3 minutes)

### **What Are Security-Critical Modules?**

Modules that handle:
- Privilege levels (User mode vs Machine mode)
- Memory protection
- Debug access
- Cryptographic keys
- Control flow

### **Find Them Automatically:**
```bash
# Show only security-critical modules
python -m scripts/batch_parse.py --dir examples/ibex/original --security-only
```

### **Expected Output:**
```
🔐 Security-Critical Modules: 4/15

============================================================
Module: ibex_cs_registers
Type: Sequential
============================================================
Inputs:    15
Outputs:   8
...

============================================================
Module: ibex_pmp
Type: Combinational
============================================================
Inputs:    10
Outputs:   6
...

============================================================
Module: ibex_controller
Type: Sequential
============================================================
...
```

**Why These Are Critical:**
- **ibex_cs_registers** - Controls privilege levels
- **ibex_pmp** - Physical Memory Protection
- **ibex_controller** - Main state machine
- **ibex_core** - Top-level integration

---

## Part 5: Rank Modules by Security Importance (2 minutes)

### **Automatic Ranking**
```bash
# Rank all modules by security score
python -m scripts/parse_and_rank.py examples/ibex/original --top 10
```

### **Expected Output:**
```
================================================================================
SECURITY-CRITICAL MODULE RANKINGS
================================================================================
Rank   Score    Module                         Type            Signals
--------------------------------------------------------------------------------
1      45       ibex_cs_registers              Sequential      70
2      38       ibex_pmp                       Combinational   42
3      32       ibex_controller                Sequential      55
4      24       ibex_core                      Sequential      128
5      18       ibex_load_store_unit           Sequential      45
6      15       ibex_decoder                   Combinational   38
7      12       ibex_alu                       Combinational   25
8      10       ibex_compressed_decoder        Combinational   22
9      8        ibex_fetch_fifo                Sequential      30
10     5        ibex_wb_stage                  Sequential      28
================================================================================

================================================================================
TOP 3 MOST CRITICAL MODULES - DETAILS
================================================================================

============================================================
Module: ibex_cs_registers
...
[Full details shown]
```

**The higher the score, the more security-critical the module is!**

---

## Part 6: Run Tests (1 minute)

### **Verify Everything Works:**
```bash
# Run all tests
python -m pytest tests/ -v
```

### **Expected Output:**
```
=================== test session starts ===================
collected 19 items

tests/test_parser.py::test_extract_simple_input PASSED [ 5%]
tests/test_parser.py::test_extract_vector_input PASSED [10%]
...
tests/test_parser.py::test_parse_real_ibex_csr PASSED [68%]
...

=================== 19 passed in 0.52s ===================
```

**All 19 tests should PASS ✅**

### **Check Coverage:**
```bash
# See how much code is tested
python -m pytest --cov=src/parser tests/
```

**Should show ~74% coverage** ✅

---

## Part 7: Understanding the Parser Output

### **Module Information:**
```
Module: ibex_cs_registers
Type: Sequential
```

- **Module name:** Extracted from `module ibex_cs_registers` declaration
- **Type:** Sequential = has state (flip-flops), Combinational = no state

### **Signals:**
```
Inputs:    15   ← Number of input ports
Outputs:   8    ← Number of output ports
Internals: 47   ← Number of internal signals (logic, wire, reg)
```

### **Special Signals:**
```
Has Clock: True
Clock:     clk_i
Reset:     rst_ni
```

- **Clock detected:** Module is clocked (sequential)
- **Reset detected:** Module has reset logic
- **Signal names:** Actual names found in the code

---

## What Can You Do Now?

✅ **Parse any Verilog/SystemVerilog file**
```bash
python src/parser/rtl_parser.py <your_file.sv>
```

✅ **Parse entire directories**
```bash
python scripts/batch_parse.py --dir <your_directory>
```

✅ **Find security-critical modules**
```bash
python scripts/batch_parse.py --dir <directory> --security-only
```

✅ **Rank modules by importance**
```bash
python scripts/parse_and_rank.py <directory> --top 10
```

✅ **Run tests to verify**
```bash
python -m pytest tests/ -v
```

---

## Next Steps (Week 2)

After mastering the parser, you'll learn to:

1. **Generate Trojans** - Automatically create hardware Trojans
2. **Insert Trojans** - Add them to RTL files
3. **Validate Trojans** - Simulate and verify them

See [STEP_GUIDE.md](STEP_GUIDE.md) for the roadmap!

---

## Troubleshooting

### **Problem: "ModuleNotFoundError"**
```bash
# Make sure you installed the package
pip install -e .
```

### **Problem: "File not found"**
```bash
# Check you're in the right directory
pwd  # (Linux/Mac)
cd   # (Windows)

# Should show: .../rv-trogen
```

### **Problem: Tests failing**
```bash
# Make sure you have pytest
python -m pip install pytest pytest-cov

# Run tests again
python -m pytest tests/ -v
```

---

## Getting Help

- **Issues:** https://github.com/sharjeelimtiaz27/rv-trogen/issues
- **Documentation:** See `docs/` folder
- **Examples:** See `examples/parser_usage.py`

---

**🎉 Congratulations!** You've completed the Quick Start guide!

You can now parse RISC-V modules and identify security-critical components.

---

## 💡 Two Ways to Run Commands

You'll notice we provide two ways to run every command:

### **Method 1: Simple Wrappers (Recommended for Beginners)**
```bash
python parse_module.py <file>
python batch_parse_modules.py --dir <dir>
python rank_modules.py <dir>
python run_tests.py
```

**Advantages:**
- ✅ Easy to remember
- ✅ Short commands
- ✅ No warnings
- ✅ Works from project root

### **Method 2: Python Module Pattern (Recommended for Scripts)**
```bash
python -m src.parser.rtl_parser <file>
python -m scripts.batch_parse --dir <dir>
python -m scripts.parse_and_rank <dir>
python -m pytest tests/ -v
```

**Advantages:**
- ✅ More explicit
- ✅ Better for automation scripts
- ✅ Shows package structure
- ✅ Works with relative imports

**Both methods do exactly the same thing - use whichever you prefer!**

---