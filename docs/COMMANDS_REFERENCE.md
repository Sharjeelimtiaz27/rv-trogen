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

## Generator Commands (STRICT MODE - Phase 2 ✅)

### Single Module Trojan Generation
```bash
# Generate Trojans for one module (STRICT MODE)
python scripts/generate_trojans.py <file.sv>

# Examples
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_pmp.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_controller.sv
```

**STRICT MODE:** Generator only creates trojans when REAL matching signals are found in the RTL. No hardcoded fallback signal names!

**Expected Output:**
```
📄 Parsing: ibex_csr.sv
   Module: ibex_csr
   Type: Sequential
   Signals: 6

🎯 Finding Trojan candidates (STRICT MODE)...
   ⊘ Skipped Leak: No payload signals (need: data, secret, key...)
   ⊘ Skipped Privilege: No trigger signals (need: csr, write, mode...)
   ✓ Found 1 valid candidates

   [1] DoS: Denial of Service
       Confidence: 1.00
       Triggers: 1 signals → ['wr_en_i']  ← Real signal! ✅
       Payloads: 1 signals → ['wr_en_i']  ← Real signal! ✅

⚙️  Generating Trojan code...
   ✓ T1: DoS → T1_ibex_csr_DoS.sv
      DoS trojan: disables wr_en_i after wr_en_i activates 1000 times

✅ Complete! Generated 1 Trojans
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
│   ├── ibex_csr/
│   │   ├── T1_ibex_csr_DoS.sv         ← Uses REAL signals!
│   │   └── ibex_csr_trojan_summary.md
│   └── ... (other modules)
├── cva6/generated_trojans/
│   └── ...
└── rsd/generated_trojans/
    └── ...
```

---

## 🆕 Trojan Integration & Simulation Commands (Phase 3 ✅)

### Step 1: Prepare Simulation Files
```bash
# UPDATED: Smart integration with trojan reading
python .\scripts\prepare_multi_trojan_simulation.py examples\ibex\original\ibex_csr.sv --trojans examples\ibex\generated_trojans\ibex_csr

# What it does (NEW in Phase 3):
# 1. Parses original module
# 2. READS generated trojan code snippet
# 3. EXTRACTS trigger logic and signal names
# 4. Inserts trojan logic with CORRECT payload type
# 5. Generates testbenches dynamically
# 6. Creates:
#    - examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
#    - testbenches/ibex/tb_ibex_csr.sv
#    - testbenches/ibex/tb_ibex_csr_trojan.sv
```

**Expected Output (Updated):**
```
======================================================================
TROJAN INTEGRATION: ibex_csr
======================================================================

[1/6] Parsing original module...
   ✅ Module: ibex_csr
   Clock: clk_i
   Reset: rst_ni
   Signals: 6

[2/6] Finding generated trojan code...
   ✅ Found: T1_ibex_csr_DoS.sv

[3/6] Reading trojan code snippet...
   ✅ Trojan type: DoS
   ✅ Trigger code: 450 chars
   ✅ Trigger signal: wr_en_i    ← Extracted from trojan!
   ✅ Payload signal: wr_en_i    ← Extracted from trojan!

[4/6] Injecting trojan payload...
   ✅ Added trojan_active declaration
   ✅ Modified assign wr_en_i (DoS payload)  ← Correct payload type!

[5/6] Inserting trojan trigger logic...
   ✅ Inserted trigger logic before endmodule

[6/6] Saving files...
   ✅ Trojaned RTL: examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
   
[Bonus] Generating testbenches...
   ✅ Original TB: tb_ibex_csr.sv
   ✅ Trojan TB: tb_ibex_csr_trojan.sv

======================================================================
✅ TROJAN INTEGRATION COMPLETE!
======================================================================
```

### Step 2: Manual Simulation Workflow

#### 2a. Upload to Server
```bash
# Upload original files
scp examples/ibex/original/ibex_csr.sv USERNAME@SERVER:/path/to/workdir/
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv USERNAME@SERVER:/path/to/workdir/

# Upload testbenches
scp testbenches/ibex/tb_ibex_csr.sv USERNAME@SERVER:/path/to/workdir/
scp testbenches/ibex/tb_ibex_csr_trojan.sv USERNAME@SERVER:/path/to/workdir/
```

#### 2b. SSH and Simulate
```bash
# Connect to server
ssh USERNAME@SERVER
cd /path/to/workdir

# Load CAD environment (if needed)
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh

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
Errors: 0, Warnings: 0  ← No compilation errors! ✅
```

#### 2c. Download VCD Files
```bash
# Create local directory
mkdir -p simulation_results/vcd

# Download VCD files
scp USERNAME@SERVER:/path/to/workdir/ibex_csr_original.vcd simulation_results/vcd/
scp USERNAME@SERVER:/path/to/workdir/ibex_csr_trojan.vcd simulation_results/vcd/
```

---

### Step 3: VCD Analysis
```bash
# Full waveform analysis
python scripts/analyze_vcd.py

# Zoom to specific time range
python scripts/analyze_vcd.py --start 9000 --end 12000

# Analyze from specific time to end
python scripts/analyze_vcd.py --start 10000
```

**Expected Output:**
```
======================================================================
RV-TROGEN VCD ANALYZER
======================================================================

Found 2 VCD files:
  - ibex_csr_original.vcd (645,120 bytes)
  - ibex_csr_trojan.vcd (682,240 bytes)

Parsing simulation_results/vcd/ibex_csr_original.vcd...
  Found 47 signals
  Time range: 0 - 20000 ns

Parsing simulation_results/vcd/ibex_csr_trojan.vcd...
  Found 51 signals (4 more = trojan signals) ← trojan_counter, trojan_active
  Time range: 0 - 20000 ns

======================================================================
SIGNAL COMPARISON
======================================================================

Signal: wr_en_i
  Differences found: 1500 time points (after trojan activation)
    Time 10000: Original=1, Trojan=0  ← DoS payload active!
    Time 10010: Original=1, Trojan=0
    ... and 1495 more differences

🎯 Total signals with differences: 1

📄 Saved: simulation_results/analysis/comparison_report.txt
📊 Saved: simulation_results/analysis/waveform_comparison.png
```

---

## Complete End-to-End Workflow (Updated)

### Full Workflow with Phase 1-3 Improvements
```bash
# STEP 1: Parse and rank modules
python scripts/parse_and_rank.py examples/ibex/original --top 5

# STEP 2: Generate trojans (STRICT MODE - Phase 2)
python scripts/generate_trojans.py examples/ibex/original/ibex_csr.sv
# ✅ Only generates if REAL signals found
# ✅ No hardcoded fallback names

# STEP 3: Integrate trojan (SMART INTEGRATION - Phase 3)
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv
# ✅ Reads generated trojan code
# ✅ Extracts signal names
# ✅ Adapts payload to trojan type
# ✅ Generates testbenches

# STEP 4: Upload to server (manual)
scp examples/ibex/original/ibex_csr.sv SERVER:/workdir/
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv SERVER:/workdir/
scp testbenches/ibex/tb_ibex_csr.sv SERVER:/workdir/
scp testbenches/ibex/tb_ibex_csr_trojan.sv SERVER:/workdir/

# STEP 5: SSH and simulate (manual)
ssh SERVER
cd /workdir
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
python scripts/analyze_vcd.py
```

---

## Python API

### Trojan Generation (Phase 2 - STRICT MODE)
```python
from src.generator.trojan_generator import TrojanGenerator

gen = TrojanGenerator('ibex_csr.sv')
gen.parse_module()
gen.find_candidates()  # STRICT: Only adds if BOTH trigger AND payload found

if gen.candidates:
    gen.generate_trojans()  # Uses REAL signals only!
```

### Trojan Integration (Phase 3 - SMART INTEGRATION)
```python
from scripts.prepare_simulation import insert_trojan_properly

# Complete integration workflow
success = insert_trojan_properly('examples/ibex/original/ibex_csr.sv')

# Reads generated trojan, extracts signals, integrates properly
# Creates:
# - examples/ibex/trojaned_rtl/ibex_csr_trojan.sv (with REAL signals!)
# - testbenches/ibex/tb_ibex_csr.sv
# - testbenches/ibex/tb_ibex_csr_trojan.sv
```

---

## Testing Commands
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src tests/

# Test trojan generation (STRICT MODE)
python -m pytest tests/test_generator.py -v

# Test integration
python -m pytest tests/test_integration.py -v
```

---

## Troubleshooting Commands

### Issue: "DoS requires trigger signal"
**Cause:** STRICT MODE - No matching signals found
**Solution:** Module doesn't have suitable signals for this pattern
```bash
# Try different module or check signal names
python scripts/parse_and_rank.py examples/ibex/original --top 5
# Use top-ranked modules (better signal matches)
```

### Issue: "Compilation error: signal not declared"
**OLD PROBLEM:** Hardcoded fallback signals don't exist
**FIXED IN PHASE 2:** Now uses only REAL signals from RTL

### Issue: "Wrong payload type"
**OLD PROBLEM:** Integration always did XOR corruption
**FIXED IN PHASE 3:** Now adapts to trojan type (DoS, Leak, etc.)

---

## Quick Reference Card

```
📦 Installation:
   python -m pip install -e .

🔍 Parse module:
   python -m src.parser.rtl_parser <file.sv>

🎯 Generate Trojans (STRICT):
   python scripts/generate_trojans.py <file.sv>
   ✅ Uses only REAL signals
   ✅ No hardcoded fallbacks

🔧 Integrate Trojan (SMART):
   python scripts/prepare_simulation.py <file.sv>
   ✅ Reads generated trojan
   ✅ Correct payload type

🖥️ Simulate (manual workflow):
   1. Upload files to server
   2. SSH and run simulation
   3. Download VCD files

📊 Analyze VCD:
   python scripts/analyze_vcd.py --start 9000 --end 12000

🧪 Test:
   python -m pytest tests/ -v

📚 Documentation:
   docs/TEMPLATES.md (Updated - Phase 1)
   docs/COMMANDS_REFERENCE.md (this file)
   docs/COMPLETE_FIX_SUMMARY.md (Phase 1-3)
```

---

**Last Updated:** January 2026  
**Version:** 2.0.0 (Phase 1-3 Complete)  
**Status:** STRICT generation + SMART integration working! ✅
