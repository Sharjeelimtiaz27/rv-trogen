# Command Reference

Complete reference for all RV-TroGen commands with multi-trojan simulation workflow.

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

# Security-critical modules only
python scripts/batch_parse.py --dir <directory> --security-only

# Save to JSON
python scripts/batch_parse.py --dir <directory> --save-json
```

### Security Ranking
```bash
# Rank all modules
python scripts/parse_and_rank.py <directory>

# Show top N modules
python scripts/parse_and_rank.py <directory> --top 5
```

---

## Trojan Generation Commands

### Single Module Generation
```bash
# Generate Trojans for one module
python scripts/generate_trojans.py <file.sv>

# Examples
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_csr.sv
```

**Expected Output:**
```
📄 Parsing: ibex_csr.sv
   Module: ibex_csr
   Type: Sequential
   Signals: 6

🎯 Finding Trojan candidates...
   ✓ Found 3 valid candidates

   [1] DoS: Denial of Service
   [2] Integrity: Data Integrity
   [3] Covert: Covert Channel

⚙️ Generating Trojan code...
   ✓ T1: DoS → T1_ibex_csr_DoS.sv
   ✓ T2: Integrity → T2_ibex_csr_Integrity.sv
   ✓ T3: Covert → T3_ibex_csr_Covert.sv

✅ Complete! Generated 3 Trojans
```

### Batch Generation
```bash
# Full pipeline - all processors, all stages
python scripts/batch_full_pipeline.py

# Single processor only
python scripts/batch_full_pipeline.py --processor ibex

# Stage 1 only (generate snippets)
python scripts/batch_full_pipeline.py --stage1-only

# Stage 2 only (integrate into RTL)
python scripts/batch_full_pipeline.py --stage2-only
```

---

## 🆕 Multi-Trojan Simulation Workflow

### Step 1: Prepare Simulation Files (Multi-Trojan)
```bash
=======
# UPDATED: Smart integration with trojan reading
>>>>>>> origin/main
python .\scripts\prepare_multi_trojan_simulation.py examples\ibex\original\ibex_csr.sv --trojans examples\ibex\generated_trojans\ibex_csr

# What it does (NEW in Phase 3):
# 1. Parses original module
# 2. READS generated trojan code snippet
# 3. EXTRACTS trigger logic and signal names
# 4. Inserts trojan logic with CORRECT payload type
# 5. Generates testbenches dynamically
# Creates:
#   examples/ibex/trojaned_rtl/ibex_csr/
#     ├── ibex_csr_trojan_DoS.sv
#     ├── ibex_csr_trojan_Integrity.sv
#     └── ibex_csr_trojan_Covert.sv
#   
#   testbenches/ibex/ibex_csr/
#     ├── tb_ibex_csr.sv (original)
#     ├── tb_ibex_csr_trojan_DoS.sv
#     ├── tb_ibex_csr_trojan_Integrity.sv
#     └── tb_ibex_csr_trojan_Covert.sv

# OR
python .\scripts\Batch_full_pipeline.py  

#it will also go trojan geenration and after that it will do "prepare_multi_trojan_simulation.py" 
```

**Expected Output:**
```
============================================================
MULTI-TROJAN INTEGRATION
============================================================

📋 Found 3 trojan(s):
   • T1_ibex_csr_DoS.sv
   • T2_ibex_csr_Integrity.sv
   • T3_ibex_csr_Covert.sv

🧪 Generating testbench for original module...
   ✅ tb_ibex_csr.sv

🔧 Integrating: T1_ibex_csr_DoS.sv
   Pattern: DoS
   Trigger: wr_en_i
   Payload: wr_en_i
   ✅ Created: ibex_csr_trojan_DoS.sv
   🧪 Testbench: tb_ibex_csr_trojan_DoS.sv

🔧 Integrating: T2_ibex_csr_Integrity.sv
   Pattern: Integrity
   Trigger: wr_en_i
   Payload: rd_data_o
   ✅ Created: ibex_csr_trojan_Integrity.sv
   🧪 Testbench: tb_ibex_csr_trojan_Integrity.sv

🔧 Integrating: T3_ibex_csr_Covert.sv
   Pattern: Covert
   Trigger: wr_data_i
   Payload: rd_error_o
   ✅ Created: ibex_csr_trojan_Covert.sv
   🧪 Testbench: tb_ibex_csr_trojan_Covert.sv

============================================================
✅ INTEGRATION COMPLETE
============================================================
Integrated:       3
Testbenches:      4 (1 original + 3 trojaned)
```

### Step 2: Upload to Server
```bash
# Create directory on server
ssh USERNAME@SERVERNAME "mkdir -p PATH/TO/DIR"

# Upload original RTL
scp examples/ibex/original/ibex_csr.sv USERNAME@SERVERNAME:PATH/TO/DIR/

# Upload ALL trojaned RTL files
scp examples/ibex/trojaned_rtl/ibex_csr/* USERNAME@SERVERNAME:PATH/TO/DIR/

# Upload ALL testbenches
scp testbenches/ibex/ibex_csr/* USERNAME@SERVERNAME:PATH/TO/DIR/

# Verify upload
ssh USERNAME@SERVERNAME "ls -lh PATH/TO/DIR/"
```

### Step 3: SSH and Simulate ALL Trojans
```bash
# Connect to server
ssh USERNAME@SERVERNAME
cd PATH/TO/DIR

# Load QuestaSim environment
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh

# ============================================================
# SIMULATION 1: Original (baseline)
# ============================================================
echo "========================================="
echo "Simulating ORIGINAL ibex_csr"
echo "========================================="
vlog +acc ibex_csr.sv tb_ibex_csr.sv
vsim -c work.tb_ibex_csr -do "run -all; quit -f"
echo "✓ Original simulation complete"
echo ""

# ============================================================
# SIMULATION 2: DoS Trojan
# ============================================================
echo "========================================="
echo "Simulating DoS TROJAN"
echo "========================================="
vlog +acc ibex_csr_trojan_DoS.sv tb_ibex_csr_trojan_DoS.sv
vsim -c work.tb_ibex_csr_trojan_DoS -do "run -all; quit -f"
echo "✓ DoS trojan simulation complete"
echo ""

# ============================================================
# SIMULATION 3: Integrity Trojan
# ============================================================
echo "========================================="
echo "Simulating INTEGRITY TROJAN"
echo "========================================="
vlog +acc ibex_csr_trojan_Integrity.sv tb_ibex_csr_trojan_Integrity.sv
vsim -c work.tb_ibex_csr_trojan_Integrity -do "run -all; quit -f"
echo "✓ Integrity trojan simulation complete"
echo ""

# ============================================================
# SIMULATION 4: Covert Channel Trojan
# ============================================================
echo "========================================="
echo "Simulating COVERT CHANNEL TROJAN"
echo "========================================="
vlog +acc ibex_csr_trojan_Covert.sv tb_ibex_csr_trojan_Covert.sv
vsim -c work.tb_ibex_csr_trojan_Covert -do "run -all; quit -f"
echo "✓ Covert trojan simulation complete"
echo ""

# ============================================================
# CHECK GENERATED VCD FILES
# ============================================================
echo "========================================="
echo "VCD FILES GENERATED:"
echo "========================================="
ls -lh *.vcd
echo ""
echo "Total VCD files:"
ls -1 *.vcd | wc -l

# Exit server
exit
```

**Expected VCD Files (4 total):**
```
ibex_csr.vcd                      (~4.5 MB)
ibex_csr_trojan_DoS.vcd          (~4.5 MB)
ibex_csr_trojan_Integrity.vcd    (~4.5 MB)
ibex_csr_trojan_Covert.vcd       (~4.5 MB)
```

### Step 4: Download VCD Files
```bash
# Create local directory
mkdir -p simulation_results/vcd/ibex/ibex_csr

# Download ALL VCD files from server
scp USERNAME@SERVERNAME:PATH/TO/DIR/*.vcd simulation_results/vcd/ibex/ibex_csr/

# Verify download
dir simulation_results\vcd\ibex\ibex_csr\*.vcd
```

### Step 5: Analyze ALL Trojans
```bash
# Full waveform analysis - compares original with ALL trojans
python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr

# Zoomed analysis (trigger region)
python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr --start 30100 --end 30200
```

**Expected Output:**
```
======================================================================
  RV-TROGEN VCD ANALYZER - MULTI-TROJAN VERSION
======================================================================

  Processor: IBEX
  Module: ibex_csr

Found 4 VCD files:
  - ibex_csr.vcd (4,567,890 bytes)
  - ibex_csr_trojan_DoS.vcd (4,589,123 bytes)
  - ibex_csr_trojan_Integrity.vcd (4,578,456 bytes)
  - ibex_csr_trojan_Covert.vcd (4,601,789 bytes)

──────────────────────────────────────────────────────────────────────
  Parsing ORIGINAL VCD
──────────────────────────────────────────────────────────────────────
  Parsing ibex_csr.vcd...
    ✓ Found 10 signals
    ✓ Time range: 0 - 600000 ns

──────────────────────────────────────────────────────────────────────
  Comparing: ORIGINAL vs DOS
──────────────────────────────────────────────────────────────────────
  Parsing ibex_csr_trojan_DoS.vcd...
    ✓ Found 12 signals (2 more = trojan signals)
    ✓ Time range: 0 - 600000 ns

    ✓ Found differences in 1 signal(s)
      - wr_en_i: 15000 differences

    📄 Report saved: comparison_DoS.txt
    📊 Plot saved: waveform_DoS.png

──────────────────────────────────────────────────────────────────────
  Comparing: ORIGINAL vs INTEGRITY
──────────────────────────────────────────────────────────────────────
  Parsing ibex_csr_trojan_Integrity.vcd...
    ✓ Found 12 signals
    ✓ Time range: 0 - 600000 ns

    ✓ Found differences in 1 signal(s)
      - rd_data_o: 3000 differences

    📄 Report saved: comparison_Integrity.txt
    📊 Plot saved: waveform_Integrity.png

──────────────────────────────────────────────────────────────────────
  Comparing: ORIGINAL vs COVERT
──────────────────────────────────────────────────────────────────────
  Parsing ibex_csr_trojan_Covert.vcd...
    ✓ Found 16 signals (6 more = covert channel signals)
    ✓ Time range: 0 - 600000 ns

    ✓ Found differences in 1 signal(s)
      - rd_error_o: 8000 differences

    📄 Report saved: comparison_Covert.txt
    📊 Plot saved: waveform_Covert.png

======================================================================
  ANALYSIS COMPLETE!
======================================================================

  📁 Results saved in: simulation_results/analysis/ibex/ibex_csr
  📄 Summary report: SUMMARY_ALL_TROJANS.txt

  Individual reports and plots generated for each trojan:
    ✓ DOS: 1 signal(s) affected
    ✓ INTEGRITY: 1 signal(s) affected
    ✓ COVERT: 1 signal(s) affected
```

**Generated Files:**
```
simulation_results/
└── analysis/
    └── ibex/
        └── ibex_csr/
            ├── SUMMARY_ALL_TROJANS.txt          ← Summary of all trojans
            ├── comparison_DoS.txt
            ├── comparison_Integrity.txt
            ├── comparison_Covert.txt
            ├── waveform_DoS.png
            ├── waveform_Integrity.png
            └── waveform_Covert.png
```

---

## Complete End-to-End Workflow

### Full Multi-Trojan Workflow
```bash
# STEP 1: Parse and rank modules
python scripts/parse_and_rank.py examples/ibex/original --top 5

# STEP 2: Generate trojans
python scripts/generate_trojans.py examples/ibex/original/ibex_csr.sv

# STEP 3: Prepare ALL trojans for simulation
python scripts/prepare_multi_trojan_simulation.py examples/ibex/original/ibex_csr.sv

# STEP 4: Upload to server
ssh USERNAME@SERVERNAME "mkdir -p /path/to/workdir"
scp examples/ibex/original/ibex_csr.sv USERNAME@SERVERNAME:/path/to/workdir/
scp examples/ibex/trojaned_rtl/ibex_csr/* USERNAME@SERVERNAME:/path/to/workdir/
scp testbenches/ibex/ibex_csr/* USERNAME@SERVERNAME:/path/to/workdir/

# STEP 5: SSH and simulate (see Step 3 above for full commands)

# STEP 6: Download VCD files
mkdir -p simulation_results/vcd/ibex/ibex_csr
scp USERNAME@SERVERNAME:/path/to/workdir/*.vcd simulation_results/vcd/ibex/ibex_csr/

# STEP 7: Analyze ALL trojans
python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr
```

---

## Python API

### Multi-Trojan Integration
```python
from scripts.prepare_multi_trojan_simulation import MultiTrojanIntegrator

# Complete integration workflow
integrator = MultiTrojanIntegrator('examples/ibex/original/ibex_csr.sv')
integrator.process_all_trojans()

# Creates:
# - Multiple trojaned RTL files (one per trojan pattern)
# - Multiple testbenches (one per trojan + original)
# - Automatic VCD dump configuration
```

### Multi-Trojan Analysis
```python
from scripts.analyze_vcd import compare_all_vcds

# Compare original with ALL trojans
compare_all_vcds(
    'simulation_results/vcd/ibex/ibex_csr/ibex_csr.vcd',
    [
        {'path': 'ibex_csr_trojan_DoS.vcd', 'name': 'DoS'},
        {'path': 'ibex_csr_trojan_Integrity.vcd', 'name': 'Integrity'},
        {'path': 'ibex_csr_trojan_Covert.vcd', 'name': 'Covert'}
    ],
    processor='ibex',
    module='ibex_csr'
)
```

---

## Testing Commands
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src tests/

# Test specific component
python -m pytest tests/test_generator.py -v
python -m pytest tests/test_parser.py -v
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

🔧 Prepare Multi-Trojan Simulation:
   python scripts/prepare_multi_trojan_simulation.py <file.sv>

🖥️ Simulate (manual workflow):
   1. Upload files to server (see upload commands)
   2. SSH and run simulations (see simulation commands)
   3. Download VCD files

📊 Analyze ALL Trojans:
   python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr

🧪 Test:
   python -m pytest tests/ -v

📚 Documentation:
   docs/README.md
   docs/COMMANDS_REFERENCE.md (this file)
   docs/SIMULATION_SETUP.md
```

---

<<<<<<< HEAD
**Last Updated:** February 18, 2026  
**Version:** 3.0.0 (Multi-Trojan Pipeline Complete)  
**Status:** Full multi-trojan simulation workflow validated! ✅
=======

