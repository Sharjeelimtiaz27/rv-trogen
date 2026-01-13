# Command Reference

Quick reference for all RV-TroGen commands.

---

## Installation Commands
```bash
# Clone repository
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git
cd rv-trogen

# Install package
python -m pip install -e .

# Verify installation
python -c "from src.parser import RTLParser; print('✅ OK')"
```

---

## Parser Commands

### Single Module Parsing
```bash
# Parse one module
python -m src.parser.rtl_parser <file.sv>

# Example
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv
```

### Batch Parsing
```bash
# Parse entire directory
python scripts/batch_parse.py --dir <directory>

# Parse with specific pattern
python scripts/batch_parse.py --dir <directory> --pattern "*.v"

# Security-critical modules only
python scripts/batch_parse.py --dir <directory> --security-only

# Save to JSON
python scripts/batch_parse.py --dir <directory> --save-json

# Custom output directory
python scripts/batch_parse.py --dir <directory> --output-dir results
```

### Security Ranking
```bash
# Rank all modules
python scripts/parse_and_rank.py <directory>

# Show top N modules
python scripts/parse_and_rank.py <directory> --top 5

# Minimum score threshold
python scripts/parse_and_rank.py <directory> --min-score 10
```

---

## Generator Commands

### Single Module Trojan Generation
```bash
# Generate Trojans for one module (recommended)
python scripts/generate_trojans.py <file.sv>

# Examples
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_pmp.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_controller.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_alu.sv
```

### Batch Generation
```bash
# Generate for all processors (Ibex, CVA6, RSD)
python scripts/batch_generate.py

# Generate for specific processor only
python scripts/batch_generate.py --processor ibex
python scripts/batch_generate.py --processor cva6
python scripts/batch_generate.py --processor rsd

# Dry run (validate without generating)
python scripts/batch_generate.py --dry-run
```

**Output Structure:**
```
examples/
├── ibex/generated_trojans/
│   ├── ibex_alu/
│   │   ├── T1_ibex_alu_DoS.sv
│   │   ├── T2_ibex_alu_Leak.sv
│   │   └── ibex_alu_trojan_summary.md
│   └── ... (28 modules)
├── cva6/generated_trojans/
│   └── ... (85 modules)
└── rsd/generated_trojans/
    └── ... (152 modules)
```

---

## 🆕 Trojan Integration & Simulation Commands (Steps 16-19)

### Step 1: Prepare Simulation Files
```bash
# Generate trojaned module + testbenches
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv

# What it does:
# 1. Parses original module (uses simple_parser.py)
# 2. Finds generated trojan
# 3. Inserts trojan logic with proper payload
# 4. Generates testbenches dynamically
# 5. Creates:
#    - examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
#    - testbenches/ibex/tb_ibex_csr.sv
#    - testbenches/ibex/tb_ibex_csr_trojan.sv
```

**Expected Output:**
```
======================================================================
TROJAN INTEGRATION: ibex_csr
======================================================================

[1/5] Parsing original module...
   ✅ Module: ibex_csr
   Clock: clk_i
   Reset: rst_ni
   Signals: 6

[2/5] Finding generated trojan...
   ✅ Found: T1_ibex_csr_DoS.sv

[3/5] Creating trojan trigger logic...
   ✅ Trigger logic created

[4/5] Injecting trojan payload...
   ✅ Added forward declaration of trojan_active
   ✅ Modified: rd_data_o = trojan_active ? CORRUPTED : normal
   ✅ Payload injected

[5/5] Generating testbenches...
   ✅ Original TB: tb_ibex_csr.sv
   ✅ Trojan TB: tb_ibex_csr_trojan.sv

======================================================================
✅ INTEGRATION COMPLETE!
======================================================================
Original Module:  examples/ibex/original/ibex_csr.sv
Trojaned Module:  examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
Original TB:      testbenches/ibex/tb_ibex_csr.sv
Trojan TB:        testbenches/ibex/tb_ibex_csr_trojan.sv
```

---

### Step 2: Manual Simulation Workflow

#### 2a. Upload to Server
```bash
# Upload original files
scp examples/ibex/original/ibex_csr.sv USERNAME@SERVER:/path/to/workdir/
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv USERNAME@SERVER:/path/to/workdir/

# Upload testbenches
scp testbenches/ibex/tb_ibex_csr.sv USERNAME@SERVER:/path/to/workdir/
scp testbenches/ibex/tb_ibex_csr_trojan.sv USERNAME@SERVER:/path/to/workdir/

# Example (Tallinn University of Technology):
scp examples/ibex/original/ibex_csr.sv sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/
scp testbenches/ibex/tb_ibex_csr.sv sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/
scp testbenches/ibex/tb_ibex_csr_trojan.sv sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/
```

#### 2b. SSH and Simulate
```bash
# Connect to server
ssh USERNAME@SERVER
cd /path/to/workdir

# Load CAD environment (if needed)
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh
# or: module load questasim
# or: cad (then select option)

# Simulate ORIGINAL
echo "=== Simulating Original ==="
vlog +acc ibex_csr.sv tb_ibex_csr.sv
vsim -c work.tb_ibex_csr -do "run -all; quit -f"

# Simulate TROJAN
echo "=== Simulating Trojan ==="
vlog +acc ibex_csr_trojan.sv tb_ibex_csr_trojan.sv
vsim -c work.tb_ibex_csr_trojan -do "run -all; quit -f"

# Check VCD files generated
ls -lh *.vcd

# Exit
exit
```

**Expected Compilation Output:**
```
-- Compiling module ibex_csr
-- Compiling module tb_ibex_csr
Top level modules:
        tb_ibex_csr
Errors: 0, Warnings: 0
```

**Expected VCD Files:**
```
-rw-r--r-- 1 username users 645K Jan 13 19:40 ibex_csr_original.vcd
-rw-r--r-- 1 username users 682K Jan 13 19:40 ibex_csr_trojan.vcd
```

#### 2c. Download VCD Files
```bash
# Create local directory
mkdir -p simulation_results/vcd

# Download VCD files
scp USERNAME@SERVER:/path/to/workdir/ibex_csr_original.vcd simulation_results/vcd/
scp USERNAME@SERVER:/path/to/workdir/ibex_csr_trojan.vcd simulation_results/vcd/

# Example:
scp sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex_csr_original.vcd simulation_results/vcd/
scp sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex_csr_trojan.vcd simulation_results/vcd/
```

---

### Step 3: VCD Analysis
```bash
# Full waveform analysis
python scripts/analyze_vcd.py

# Zoom to specific time range (e.g., trigger region)
python scripts/analyze_vcd.py --start 9000 --end 12000

# Zoom to exact time window
python scripts/analyze_vcd.py --start 30120 --end 30130

# Analyze from specific time to end
python scripts/analyze_vcd.py --start 10000

# Analyze from start to specific time
python scripts/analyze_vcd.py --end 15000
```

**Expected Output:**
```
======================================================================
RV-TROGEN VCD ANALYZER
======================================================================

Found 2 VCD files:
  - ibex_csr_original.vcd (645,120 bytes)
  - ibex_csr_trojan.vcd (682,240 bytes)

======================================================================
VCD WAVEFORM COMPARISON
======================================================================
🔍 TIME RANGE FILTER ACTIVE:
   Start: 9000 ns
   End: 12000 ns

Parsing simulation_results/vcd/ibex_csr_original.vcd...
  Found 47 signals
  Time range: 9000 - 12000 1ns

Parsing simulation_results/vcd/ibex_csr_trojan.vcd...
  Found 51 signals
  Time range: 9000 - 12000 1ns

======================================================================
SIGNAL COMPARISON
======================================================================

Signal: rd_data_o
  Differences found: 3000 time points
    Time 10000: Original=0x12345678, Trojan=0xCDEF3397
    Time 10010: Original=0xABCDEF01, Trojan=0x7602100E
    ... and 2995 more differences

🎯 Total signals with differences: 1

📄 Saved: simulation_results/analysis/comparison_report_9000_12000.txt
📊 Saved: simulation_results/analysis/waveform_comparison_9000_12000.png

======================================================================
ANALYSIS COMPLETE!
======================================================================
```

---

## Local Simulation Commands (If QuestaSim/Verilator Installed Locally)

### With QuestaSim
```bash
# Compile
vlog +acc examples/ibex/original/ibex_csr.sv testbenches/ibex/tb_ibex_csr.sv

# Simulate (GUI)
vsim work.tb_ibex_csr

# Simulate (command-line)
vsim -c work.tb_ibex_csr -do "run -all; quit -f"

# Analyze VCD
python scripts/analyze_vcd.py
```

### With Verilator
```bash
# Compile
verilator --cc --exe --build testbenches/ibex/tb_ibex_csr.sv examples/ibex/original/ibex_csr.sv

# Run
./obj_dir/Vtb_ibex_csr

# Analyze VCD
python scripts/analyze_vcd.py
```

---

## Testing Commands
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src/parser tests/

# Run specific test file
python -m pytest tests/test_parser.py -v

# Run specific test
python -m pytest tests/test_parser.py::TestRTLParser::test_parse_simple_module -v
```

---

## Complete End-to-End Workflow

### Full Workflow: Parse → Generate → Integrate → Simulate → Analyze
```bash
# STEP 1: Parse and rank modules
python scripts/parse_and_rank.py examples/ibex/original --top 5

# STEP 2: Generate trojans for top module
python scripts/generate_trojans.py examples/ibex/original/ibex_csr.sv

# STEP 3: Integrate trojan and generate testbenches
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv

# STEP 4: Upload to server (manual)
scp examples/ibex/original/ibex_csr.sv SERVER:/workdir/
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv SERVER:/workdir/
scp testbenches/ibex/tb_ibex_csr.sv SERVER:/workdir/
scp testbenches/ibex/tb_ibex_csr_trojan.sv SERVER:/workdir/

# STEP 5: SSH and simulate (manual)
ssh SERVER
cd /workdir
source /path/to/cad/setup.sh
vlog +acc ibex_csr.sv tb_ibex_csr.sv
vsim -c work.tb_ibex_csr -do "run -all; quit -f"
vlog +acc ibex_csr_trojan.sv tb_ibex_csr_trojan.sv
vsim -c work.tb_ibex_csr_trojan -do "run -all; quit -f"
ls -lh *.vcd
exit

# STEP 6: Download VCD files (manual)
mkdir -p simulation_results/vcd
scp SERVER:/workdir/*.vcd simulation_results/vcd/

# STEP 7: Analyze results
python scripts/analyze_vcd.py --start 9000 --end 12000
```

---

## Git Commands
```bash
# Check status
git status

# Add new files
git add scripts/analyze_vcd.py
git add scripts/dynamic_testbench_generator.py
git add scripts/prepare_simulation.py
git add scripts/simple_parser.py

# Commit
git commit -m "Add trojan integration workflow (Steps 16-19)"

# Push to GitHub
git push origin main
```

---

## Python API

### Simple Parser Usage (NEW - Step 16)
```python
from simple_parser import SimpleModuleParser

# Parse module with parameters
parser = SimpleModuleParser('ibex_csr.sv')
module = parser.parse()

# Access parsed information
print(f"Module: {module.name}")
print(f"Parameters: {module.parameters}")  # {'Width': '32'}
print(f"Inputs: {module.inputs}")           # Correct widths!
print(f"Outputs: {module.outputs}")
```

### Dynamic Testbench Generation (NEW - Step 16)
```python
from dynamic_testbench_generator import DynamicTestbenchGenerator

# Generate testbench for any module
gen = DynamicTestbenchGenerator('ibex_csr.sv')
testbench_code = gen.generate_testbench(is_trojan=False)

# Save testbench
with open('tb_ibex_csr.sv', 'w') as f:
    f.write(testbench_code)
```

### Trojan Integration (NEW - Step 17)
```python
from prepare_simulation import insert_trojan_properly

# Complete integration workflow
success = insert_trojan_properly('examples/ibex/original/ibex_csr.sv')

# Creates:
# - examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
# - testbenches/ibex/tb_ibex_csr.sv
# - testbenches/ibex/tb_ibex_csr_trojan.sv
```

### VCD Analysis (NEW - Step 19)
```python
from analyze_vcd import compare_vcds

# Compare VCD files with time range
compare_vcds(
    'simulation_results/vcd/ibex_csr_original.vcd',
    'simulation_results/vcd/ibex_csr_trojan.vcd',
    start_time=9000,
    end_time=12000
)

# Generates:
# - comparison_report_9000_12000.txt
# - waveform_comparison_9000_12000.png
```

---

## Troubleshooting Commands

### Issue: "Parameter not recognized"
```bash
# Use simple_parser instead of rtl_parser
# Updated in prepare_simulation.py (automatic)
```

### Issue: "Wrong signal widths in testbench"
```bash
# Regenerate with updated dynamic_testbench_generator
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv
```

### Issue: "Compilation error: trojan_active already declared"
```bash
# Updated prepare_simulation.py adds forward declaration
# Regenerate files:
rm examples/ibex/trojaned_rtl/*
rm testbenches/ibex/*
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv
```

### Issue: "VCD files not generated"
```bash
# Check simulation output for errors
# Ensure $dumpfile and $dumpvars in testbench
# Verify simulation ran to completion
```

---

## Quick Reference Card

```
📦 Installation:
   python -m pip install -e .

🔍 Parse module:
   python -m src.parser.rtl_parser <file.sv>

🎯 Generate Trojans:
   python scripts/generate_trojans.py <file.sv>

🔧 Integrate Trojan:
   python scripts/prepare_simulation.py <file.sv>

🖥️ Simulate (manual workflow):
   1. Upload files to server
   2. SSH and run simulation
   3. Download VCD files

📊 Analyze VCD:
   python scripts/analyze_vcd.py --start 9000 --end 12000

🧪 Test:
   python -m pytest tests/ -v

📚 Documentation:
   docs/STEP_GUIDE.md
   docs/SIMULATION_SETUP.md
   docs/COMMANDS_REFERENCE.md (this file)
```

---

**Last Updated:** January 13, 2026  
**Version:** 1.6.0  
**Status:** Steps 1-19 Complete (63%)