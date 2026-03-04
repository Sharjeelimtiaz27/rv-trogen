# Simulation Setup Guide

**Complete guide for trojan simulation and validation with RV-TroGen**

---

## Overview

RV-TroGen uses a **manual simulation workflow** tested and validated on TalTech HPC servers with QuestaSim. The primary validation target is the `ibex_cs_registers` module — the most security-critical module in the Ibex RISC-V core.

**Why Manual?**
- ✅ Works reliably with any server setup
- ✅ No complex SSH automation required
- ✅ Handles CAD environment managers
- ✅ Full control over simulation
- ✅ Easy debugging of individual trojans

---

## Prerequisites

### On Your Local Machine
- Python 3.8+
- RV-TroGen installed (`pip install -e .`)
- SSH client (built-in on Windows 10+, Linux, macOS)
- SCP for file transfer
- matplotlib (`pip install matplotlib`)

### On Simulation Server
- QuestaSim 2024.3 (or compatible)
- SSH access
- Sufficient disk space (~100MB for 7 VCDs)

---

## Complete Workflow Diagram

```
LOCAL PC:                              SERVER (ekleer.pld.ttu.ee):
┌──────────────────────┐              ┌──────────────────────────┐
│ 1. generate_trojans  │              │                          │
│    ibex_cs_registers │              │                          │
└──────────┬───────────┘              │                          │
           │                          │                          │
           ▼                          │                          │
┌──────────────────────┐              │                          │
│ 2. prepare_multi_    │              │                          │
│    trojan_simulation │              │                          │
│    → 6 trojaned RTL  │              │                          │
│    → 7 testbenches   │              │                          │
└──────────┬───────────┘              │                          │
           │    SCP upload            │                          │
           ├─────────────────────────►│ 3. Receive 14+ files    │
           │                          └──────────┬───────────────┘
           │                                     │
           │                                     ▼
           │                          ┌──────────────────────────┐
           │                          │ 4. vlog each pair        │
           │                          │    (ibex_pkg + RTL + TB) │
           │                          └──────────┬───────────────┘
           │                                     │
           │                                     ▼
           │                          ┌──────────────────────────┐
           │                          │ 5. vsim × 7              │
           │                          │    (1 original + 6 troj) │
           │                          └──────────┬───────────────┘
           │    SCP download                     │
           │◄────────────────────────────────────┤ 6. 7 × VCD files
           │                                     │
           ▼                                     │
┌──────────────────────┐                        │
│ 7. analyze_vcd.py    │                        │
│    Auto-zoom plots   │                        │
│    + diff reports    │                        │
└──────────────────────┘
```

---

## Step-by-Step Guide

### STEP 1: Generate Trojans (Local)

```bash
# Security ranking (optional — ibex_cs_registers is already top)
python scripts/parse_and_rank.py examples/ibex/original --top 5

# Generate all 6 trojan snippets
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

**Output:**
```
examples/ibex/generated_trojans/ibex_cs_registers/
  ├── T1_ibex_cs_registers_DoS.sv
  ├── T2_ibex_cs_registers_Availability.sv
  ├── T3_ibex_cs_registers_Integrity.sv
  ├── T4_ibex_cs_registers_Covert.sv
  ├── T5_ibex_cs_registers_Leak.sv
  └── T6_ibex_cs_registers_Privilege.sv
```

---

### STEP 2: Integrate Trojans + Generate Testbenches (Local)

```bash
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers
```

**What it does:**
1. ✅ Parses original module (handles ibex_pkg enum types)
2. ✅ Reads each trojan snippet and extracts trigger/payload signals
3. ✅ Inserts trojan logic with correct payload per pattern
4. ✅ Generates dynamic testbenches with `pkg_stimulus` (drives `CSR_OP_WRITE` + `CSR_MSCRATCH`)
5. ✅ Adds MRET sequence only to Privilege testbench (drops to user mode first)
6. ✅ Configures VCD dump for each simulation

**Output (13 files):**
```
examples/ibex/trojaned_rtl/ibex_cs_registers/
  ├── ibex_cs_registers_trojan_DoS.sv
  ├── ibex_cs_registers_trojan_Availability.sv
  ├── ibex_cs_registers_trojan_Integrity.sv
  ├── ibex_cs_registers_trojan_Covert.sv
  ├── ibex_cs_registers_trojan_Leak.sv
  └── ibex_cs_registers_trojan_Privilege.sv

testbenches/ibex/ibex_cs_registers/
  ├── tb_ibex_cs_registers.sv              ← original baseline
  ├── tb_ibex_cs_registers_trojan_DoS.sv
  ├── tb_ibex_cs_registers_trojan_Availability.sv
  ├── tb_ibex_cs_registers_trojan_Integrity.sv
  ├── tb_ibex_cs_registers_trojan_Covert.sv
  ├── tb_ibex_cs_registers_trojan_Leak.sv
  └── tb_ibex_cs_registers_trojan_Privilege.sv
```

**Verification:**
```bash
ls examples/ibex/trojaned_rtl/ibex_cs_registers/
ls testbenches/ibex/ibex_cs_registers/
```

---

### STEP 3: Upload Files to Server

```bash
SERVER="sharjeel@ekleer.pld.ttu.ee"
WORKDIR="/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers"

# Create directory
ssh $SERVER "mkdir -p $WORKDIR"

# Upload ibex_pkg (required — contains CSR_OP_WRITE, PRIV_LVL_M enum types)
scp examples/ibex/original/ibex_pkg.sv $SERVER:$WORKDIR/

# Upload original RTL
scp examples/ibex/original/ibex_cs_registers.sv $SERVER:$WORKDIR/

# Upload all 6 trojaned RTL files
scp examples/ibex/trojaned_rtl/ibex_cs_registers/*.sv $SERVER:$WORKDIR/

# Upload all 7 testbenches
scp testbenches/ibex/ibex_cs_registers/*.sv $SERVER:$WORKDIR/

# Verify (should see 15 .sv files)
ssh $SERVER "ls -lh $WORKDIR/*.sv | wc -l"
```

---

### STEP 4: SSH to Server and Compile + Simulate

```bash
ssh sharjeel@ekleer.pld.ttu.ee
cd /home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers

# Load QuestaSim
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh
# OR: echo '2.4' | cad

# ── Original (baseline) ──────────────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers.sv tb_ibex_cs_registers.sv
vsim -c work.tb_ibex_cs_registers -do "run -all; quit -f"

# ── DoS Trojan ───────────────────────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_DoS.sv tb_ibex_cs_registers_trojan_DoS.sv
vsim -c work.tb_ibex_cs_registers_trojan_DoS -do "run -all; quit -f"

# ── Availability Trojan ──────────────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Availability.sv tb_ibex_cs_registers_trojan_Availability.sv
vsim -c work.tb_ibex_cs_registers_trojan_Availability -do "run -all; quit -f"

# ── Integrity Trojan ─────────────────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Integrity.sv tb_ibex_cs_registers_trojan_Integrity.sv
vsim -c work.tb_ibex_cs_registers_trojan_Integrity -do "run -all; quit -f"

# ── Covert Channel Trojan ────────────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Covert.sv tb_ibex_cs_registers_trojan_Covert.sv
vsim -c work.tb_ibex_cs_registers_trojan_Covert -do "run -all; quit -f"

# ── Information Leakage Trojan ───────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Leak.sv tb_ibex_cs_registers_trojan_Leak.sv
vsim -c work.tb_ibex_cs_registers_trojan_Leak -do "run -all; quit -f"

# ── Privilege Escalation Trojan ──────────────────────────────────────────
vlog +acc ibex_pkg.sv ibex_cs_registers_trojan_Privilege.sv tb_ibex_cs_registers_trojan_Privilege.sv
vsim -c work.tb_ibex_cs_registers_trojan_Privilege -do "run -all; quit -f"

# ── Verify all VCDs generated ────────────────────────────────────────────
ls -lh *.vcd
echo "Total: $(ls -1 *.vcd | wc -l) VCD files (expected: 7)"

exit
```

**Expected compilation output (per simulation):**
```
QuestaSim-64 vlog 2024.3 Compiler
-- Compiling module ibex_pkg
-- Compiling module ibex_cs_registers_trojan_Availability
-- Compiling module tb_ibex_cs_registers_trojan_Availability
Top level modules: tb_ibex_cs_registers_trojan_Availability
Errors: 0, Warnings: 0
```

**If compilation fails:**
```bash
# Most common fix: regenerate on local machine and re-upload
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers \
    --pattern DoS          # regenerate specific pattern only

scp examples/ibex/trojaned_rtl/ibex_cs_registers/ibex_cs_registers_trojan_DoS.sv \
    $SERVER:$WORKDIR/
```

---

### STEP 5: Download VCD Files

```bash
# Create local directory structure
mkdir -p simulation_results/vcd/ibex/ibex_cs_registers

# Download all 7 VCD files
scp sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers/*.vcd \
    simulation_results/vcd/ibex/ibex_cs_registers/

# Verify (Linux)
ls -lh simulation_results/vcd/ibex/ibex_cs_registers/

# Verify (Windows PowerShell)
dir simulation_results\vcd\ibex\ibex_cs_registers\*.vcd
```

---

### STEP 6: Analyze VCD Files

```bash
# ── Batch: analyze all 6 trojans vs original ─────────────────────────────
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

# ── Single trojan: auto-finds original in same directory ─────────────────
python scripts/analyze_vcd.py \
    --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_Availability.vcd

# ── Manual time window (ns) — override auto-zoom ─────────────────────────
python scripts/analyze_vcd.py \
    --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_DoS.vcd \
    --start 140 --end 350

# ── Full waveform (no zoom) ───────────────────────────────────────────────
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers \
    --no-zoom
```

**Results land in:**
```
simulation_results/analysis/ibex/ibex_cs_registers/
  ├── waveform_DoS_140ns_350ns.png         ← zoomed, only differing signals
  ├── waveform_Availability_<range>.png
  ├── waveform_Integrity_<range>.png
  ├── waveform_Covert_<range>.png
  ├── waveform_Leak_<range>.png
  ├── waveform_Privilege_<range>.png
  ├── report_DoS.txt
  ├── report_Availability.txt
  ...
```

---

## Trojan Validation — What to Expect

### Trigger Timing

All trojans use counter-based triggers (range 5,000–25,000 cycles of `csr_op_en_i`). With the testbench running 30,000 cycles at 1ns clock, activation typically occurs at **~150,000 ns** (150µs).

### Expected Signal Changes Per Trojan

| Trojan        | Signal Changed      | Before Activation   | After Activation                      |
|---------------|---------------------|---------------------|---------------------------------------|
| DoS           | `csr_we_int`        | Toggles 0/1         | Stuck at 0 permanently                |
| Availability  | `csr_we_int`        | Toggles 0/1         | Gaps every 8/16 cycles (50% duty)     |
| Integrity     | `csr_rdata_o`       | = `csr_rdata_int`   | = `csr_rdata_int` XOR `0xDEADBEEF`   |
| Covert        | `csr_rdata_o[0]`    | = `csr_rdata_int[0]`| Pulses: 10 cycles or 5 cycles wide    |
| Leak          | `csr_mepc_o`        | = `mepc_q` (stable) | Changes every cycle with write data   |
| Privilege     | `priv_mode_id_o`    | = `2'b00` (user)    | = `2'b11` (machine mode)              |

> **Note for Privilege:** The testbench executes an MRET sequence to drop to user mode first. Without this, `priv_mode_id_o` stays at `2'b11` (M-mode) before AND after activation — making the trojan invisible. Only the Privilege testbench includes MRET; all others stay in M-mode to keep CSR writes legal.

### Verifying Trojan Works

✅ **Trojan is working if:**
1. 7 VCD files generated (all similar size ~8MB)
2. Analyzer reports differences in the expected signal
3. Auto-zoom plot shows clear divergence between blue (original) and red (trojaned) lines
4. Report shows activation timestamp

❌ **Trojan NOT working if:**
1. No differences found in the report
2. `trojan_active` never goes HIGH in GTKWave

**Quick debug on server:**
```bash
# Check trojan logic was inserted
grep "trojan_active" ibex_cs_registers_trojan_DoS.sv | head -5

# Check testbench runs enough cycles
grep "repeat" tb_ibex_cs_registers_trojan_DoS.sv

# Check csr_we_int is actually being driven
grep "csr_op_i\|CSR_OP_WRITE\|csr_addr_i\|CSR_MSCRATCH" tb_ibex_cs_registers_trojan_DoS.sv
```

---

## Server-Specific Setup

### TalTech (ekleer.pld.ttu.ee)
```bash
Server    : ekleer.pld.ttu.ee
Username  : sharjeel
Workdir   : /home/sharjeel/sharjeelphd/Research/rv_trogen/ibex/ibex_cs_registers

# Load QuestaSim (two methods)
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh
# OR
echo '2.4' | cad
```

### Local QuestaSim (Windows)
```cmd
cd C:\Projects\rv-trogen

REM Compile
vlog +acc examples\ibex\original\ibex_pkg.sv ^
          examples\ibex\trojaned_rtl\ibex_cs_registers\ibex_cs_registers_trojan_DoS.sv ^
          testbenches\ibex\ibex_cs_registers\tb_ibex_cs_registers_trojan_DoS.sv

REM Simulate
vsim -c work.tb_ibex_cs_registers_trojan_DoS -do "run -all; quit -f"
```

---

## Summary Checklist

```
□ generate_trojans.py produced 6 .sv snippet files
□ prepare_multi_trojan_simulation.py produced 6 trojaned RTL + 7 testbenches
□ ibex_pkg.sv uploaded to server (required for enum types)
□ All 14 .sv files uploaded to server
□ All 7 simulations compile with 0 errors
□ All 7 VCD files generated (~8MB each)
□ All 7 VCDs downloaded to simulation_results/vcd/ibex/ibex_cs_registers/
□ analyze_vcd.py reports differences for all 6 trojans
□ Waveform plots show clear divergence in zoomed region
```

---

**Last Updated:** March 2026
**Version:** 4.0.0 (Six-Pattern Validation Complete)
**Status:** All 6 trojans validated on ibex_cs_registers ✅