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

# Example (primary target module)
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

**Expected Output:**
```
📄 Parsing: ibex_cs_registers.sv
   Module: ibex_cs_registers
   Type: Sequential
   Signals: 65+

🎯 Finding Trojan candidates...
   ✓ Found 6 valid candidates

   [1] DoS:         Denial of Service
   [2] Availability: Availability Degradation
   [3] Integrity:   Data Integrity Corruption
   [4] Covert:      Covert Channel
   [5] Leak:        Information Leakage
   [6] Privilege:   Privilege Escalation

⚙️ Generating Trojan code...
   ✓ T1: DoS        → T1_ibex_cs_registers_DoS.sv
   ✓ T2: Availability → T2_ibex_cs_registers_Availability.sv
   ✓ T3: Integrity  → T3_ibex_cs_registers_Integrity.sv
   ✓ T4: Covert     → T4_ibex_cs_registers_Covert.sv
   ✓ T5: Leak       → T5_ibex_cs_registers_Leak.sv
   ✓ T6: Privilege  → T6_ibex_cs_registers_Privilege.sv

✅ Complete! Generated 6 Trojans
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

## Multi-Trojan Simulation Workflow

### Step 1: Prepare Simulation Files (All 6 Trojans)
```bash
# Smart integration: reads generated trojan snippets, inserts logic, generates testbenches
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers

# Or run full pipeline (generation + integration in one command)
python scripts/batch_full_pipeline.py
```

**What it does:**
1. Parses original module
2. Reads each generated trojan code snippet
3. Extracts trigger logic and signal names
4. Inserts trojan logic with correct payload type per pattern
5. Generates testbenches dynamically (with pkg_stimulus for CSR_OP_WRITE, MRET only for Privilege)

**Creates:**
```
examples/ibex/trojaned_rtl/ibex_cs_registers/
  ├── ibex_cs_registers_trojan_DoS.sv
  ├── ibex_cs_registers_trojan_Availability.sv
  ├── ibex_cs_registers_trojan_Integrity.sv
  ├── ibex_cs_registers_trojan_Covert.sv
  ├── ibex_cs_registers_trojan_Leak.sv
  └── ibex_cs_registers_trojan_Privilege.sv

testbenches/ibex/ibex_cs_registers/
  ├── tb_ibex_cs_registers.sv              (original)
  ├── tb_ibex_cs_registers_trojan_DoS.sv
  ├── tb_ibex_cs_registers_trojan_Availability.sv
  ├── tb_ibex_cs_registers_trojan_Integrity.sv
  ├── tb_ibex_cs_registers_trojan_Covert.sv
  ├── tb_ibex_cs_registers_trojan_Leak.sv
  └── tb_ibex_cs_registers_trojan_Privilege.sv
```

**What each trojan modifies:**

| Trojan        | Target Signal          | Mechanism                                 |
|---------------|------------------------|-------------------------------------------|
| DoS           | `csr_we_int`           | Permanently blocks CSR writes             |
| Availability  | `csr_we_int`           | 50% duty-cycle stall (8/16 cycles)        |
| Integrity     | `csr_rdata_o`          | XOR all reads with `0xDEADBEEF`           |
| Covert        | `csr_rdata_o[0]`       | Pulse-width encoding (10 cycles=1, 5=0)   |
| Leak          | `csr_mepc_o`           | Routes secret write data to stable port   |
| Privilege     | `priv_mode_id_o` + FF  | Forces `PRIV_LVL_M` (2'b11) escalation    |

---

### Step 2: Upload to Server
```bash
SERVER="sharjeel@ekleer.pld.ttu.ee"
WORKDIR="/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers"

# Create directory on server
ssh $SERVER "mkdir -p $WORKDIR"

# Upload original RTL + package file
scp examples/ibex/original/ibex_cs_registers.sv $SERVER:$WORKDIR/
scp examples/ibex/original/ibex_pkg.sv $SERVER:$WORKDIR/          # required for pkg types

# Upload ALL 6 trojaned RTL files
scp examples/ibex/trojaned_rtl/ibex_cs_registers/* $SERVER:$WORKDIR/

# Upload ALL 7 testbenches (1 original + 6 trojaned)
scp testbenches/ibex/ibex_cs_registers/* $SERVER:$WORKDIR/

# Verify upload
ssh $SERVER "ls -lh $WORKDIR/"
```

---

### Step 3: SSH and Simulate ALL 6 Trojans
```bash
# Connect to server
ssh sharjeel@ekleer.pld.ttu.ee
cd /home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers

# Load QuestaSim environment
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh
# OR: echo '2.4' | cad

# ============================================================
# SIMULATION 1: Original (baseline)
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers.sv tb_ibex_cs_registers.sv
vsim -c work.tb_ibex_cs_registers -do "run -all; quit -f"

# ============================================================
# SIMULATION 2: DoS Trojan
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_DoS.sv tb_ibex_cs_registers_trojan_DoS.sv
vsim -c work.tb_ibex_cs_registers_trojan_DoS -do "run -all; quit -f"

# ============================================================
# SIMULATION 3: Availability Trojan
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Availability.sv tb_ibex_cs_registers_trojan_Availability.sv
vsim -c work.tb_ibex_cs_registers_trojan_Availability -do "run -all; quit -f"

# ============================================================
# SIMULATION 4: Integrity Trojan
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Integrity.sv tb_ibex_cs_registers_trojan_Integrity.sv
vsim -c work.tb_ibex_cs_registers_trojan_Integrity -do "run -all; quit -f"

# ============================================================
# SIMULATION 5: Covert Channel Trojan
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Covert.sv tb_ibex_cs_registers_trojan_Covert.sv
vsim -c work.tb_ibex_cs_registers_trojan_Covert -do "run -all; quit -f"

# ============================================================
# SIMULATION 6: Information Leakage Trojan
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Leak.sv tb_ibex_cs_registers_trojan_Leak.sv
vsim -c work.tb_ibex_cs_registers_trojan_Leak -do "run -all; quit -f"

# ============================================================
# SIMULATION 7: Privilege Escalation Trojan
# ============================================================
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Privilege.sv tb_ibex_cs_registers_trojan_Privilege.sv
vsim -c work.tb_ibex_cs_registers_trojan_Privilege -do "run -all; quit -f"

# ============================================================
# CHECK ALL VCD FILES
# ============================================================
ls -lh *.vcd
echo "Total VCD files: $(ls -1 *.vcd | wc -l)"   # Expected: 7

exit
```

**Expected VCD Files (7 total):**
```
ibex_cs_registers.vcd                      (~8 MB)
ibex_cs_registers_trojan_DoS.vcd           (~8 MB)
ibex_cs_registers_trojan_Availability.vcd  (~8 MB)
ibex_cs_registers_trojan_Integrity.vcd     (~8 MB)
ibex_cs_registers_trojan_Covert.vcd        (~8 MB)
ibex_cs_registers_trojan_Leak.vcd          (~8 MB)
ibex_cs_registers_trojan_Privilege.vcd     (~8 MB)
```

---

### Step 4: Download VCD Files
```bash
# Create local directory
mkdir -p simulation_results/vcd/ibex/ibex_cs_registers

# Download ALL 7 VCD files from server
scp sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers/*.vcd \
    simulation_results/vcd/ibex/ibex_cs_registers/

# Verify download (Windows)
dir simulation_results\vcd\ibex\ibex_cs_registers\*.vcd

# Verify download (Linux)
ls -lh simulation_results/vcd/ibex/ibex_cs_registers/
```

---

### Step 5: Analyze ALL 6 Trojans
```bash
# ── BATCH: compare all 6 trojans vs original in one command ──────────────
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

# ── SINGLE FILE: auto-finds original in same directory ───────────────────
python scripts/analyze_vcd.py \
    --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_Availability.vcd

# ── MANUAL TIME WINDOW (ns): override auto-zoom ──────────────────────────
python scripts/analyze_vcd.py \
    --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_DoS.vcd \
    --start 140 --end 350

# ── FULL WAVEFORM (disable auto-zoom) ────────────────────────────────────
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers \
    --no-zoom
```

**analyze_vcd.py v3 — Key Features:**
- **Auto-zoom**: detects `trojan_active` HIGH edge, zooms plot to ±50ns around payload region
- **Skips flat signals**: only plots signals that actually differ (no empty rows)
- **Single-file mode**: `--trojan FILE` auto-finds original in same directory
- **Auto output path**: `vcd/ibex/ibex_cs_registers/` → `analysis/ibex/ibex_cs_registers/`

**Expected Output:**
```
============================================================
  RV-TroGen VCD Analyzer  v3
============================================================

  Original VCD: ibex_cs_registers.vcd
  Trojaned VCDs found: 6

────────────────────────────────────────────────────────────
  Trojan : Availability
  Orig   : ibex_cs_registers.vcd
  Parsing ibex_cs_registers.vcd …  65 signals, t=[0…600000000] ps
  Parsing ibex_cs_registers_trojan_Availability.vcd …  68 signals
  ⚡ trojan_active ↑ at 150000000 ps  (150000.0 ns)
  Auto-zoom window: 149950 – 600050 ns
  Signals with differences: 2  (csr_we_int, stall_active)
  📊 Saved: waveform_Availability_149950ns_600050ns.png
  📄 Report: report_Availability.txt
...

============================================================
BATCH SUMMARY
============================================================
  DoS                  ✅ differences detected  → csr_we_int
  Availability         ✅ differences detected  → csr_we_int, stall_active
  Integrity            ✅ differences detected  → csr_rdata_o
  Covert               ✅ differences detected  → csr_rdata_o
  Leak                 ✅ differences detected  → csr_mepc_o
  Privilege            ✅ differences detected  → priv_mode_id_o
```

**Generated Files:**
```
simulation_results/
└── analysis/
    └── ibex/
        └── ibex_cs_registers/
            ├── waveform_DoS_<range>.png
            ├── waveform_Availability_<range>.png
            ├── waveform_Integrity_<range>.png
            ├── waveform_Covert_<range>.png
            ├── waveform_Leak_<range>.png
            ├── waveform_Privilege_<range>.png
            ├── report_DoS.txt
            ├── report_Availability.txt
            ├── report_Integrity.txt
            ├── report_Covert.txt
            ├── report_Leak.txt
            └── report_Privilege.txt
```

---

## Complete End-to-End Workflow

```bash
# STEP 1: Parse and rank modules
python scripts/parse_and_rank.py examples/ibex/original --top 5

# STEP 2: Generate trojans (6 patterns)
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# STEP 3: Prepare ALL 6 trojans for simulation
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers

# STEP 4: Upload to server
SERVER="sharjeel@ekleer.pld.ttu.ee"
WORKDIR="/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers"
ssh $SERVER "mkdir -p $WORKDIR"
scp examples/ibex/original/ibex_pkg.sv $SERVER:$WORKDIR/
scp examples/ibex/original/ibex_cs_registers.sv $SERVER:$WORKDIR/
scp examples/ibex/trojaned_rtl/ibex_cs_registers/* $SERVER:$WORKDIR/
scp testbenches/ibex/ibex_cs_registers/* $SERVER:$WORKDIR/

# STEP 5: SSH and simulate (see Step 3 above for full commands)

# STEP 6: Download VCD files
mkdir -p simulation_results/vcd/ibex/ibex_cs_registers
scp $SERVER:$WORKDIR/*.vcd simulation_results/vcd/ibex/ibex_cs_registers/

# STEP 7: Analyze ALL trojans
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers
```

---

## Python API

### Multi-Trojan Integration
```python
from scripts.prepare_multi_trojan_simulation import MultiTrojanIntegrator

integrator = MultiTrojanIntegrator('examples/ibex/original/ibex_cs_registers.sv')
integrator.process_all_trojans()
# Creates 6 trojaned RTL files + 7 testbenches (1 original + 6 trojaned)
```

### VCD Analysis
```python
from scripts.analyze_vcd import VCDParser, find_differences, find_trojan_activation

orig = VCDParser('simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers.vcd').parse()
troj = VCDParser('simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_Integrity.vcd').parse()

activation_t = find_trojan_activation(troj)   # → time in ps
diffs        = find_differences(orig, troj)    # → {sig_name: [(t, orig_val, troj_val)]}
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
   python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv

🎯 Generate Trojans (6 patterns):
   python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

🔧 Prepare Multi-Trojan Simulation:
   python scripts/prepare_multi_trojan_simulation.py \
       examples/ibex/original/ibex_cs_registers.sv \
       --trojans examples/ibex/generated_trojans/ibex_cs_registers

🖥️ Simulate (on server):
   # Upload → SSH → vlog + vsim for each of 7 files → download VCDs

📊 Analyze ALL Trojans (batch):
   python scripts/analyze_vcd.py \
       --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

📊 Analyze single trojan (auto-finds original):
   python scripts/analyze_vcd.py \
       --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_DoS.vcd

🧪 Test:
   python -m pytest tests/ -v
```

---

**Last Updated:** March 2026
**Version:** 4.0.0 (Six-Pattern Validation Complete)
**Status:** All 6 trojans validated on ibex_cs_registers ✅