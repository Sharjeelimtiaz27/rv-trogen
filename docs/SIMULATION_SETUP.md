# Simulation Setup Guide

**Complete guide for trojan simulation and validation with RV-TroGen**

---

## Overview

RV-TroGen uses a **manual simulation workflow** that has been tested and proven to work on university HPC servers with expensive EDA tools like QuestaSim.

**Why Manual?** 
- ✅ Works reliably with any server setup
- ✅ No complex SSH automation
- ✅ Handles CAD environment managers
- ✅ Full control over simulation
- ✅ Easy debugging

---

## Prerequisites

### On Your Local Machine
- Python 3.8+
- RV-TroGen installed
- SSH client (built-in on Windows 10+, Linux, macOS)
- SCP for file transfer

### On Simulation Server
- QuestaSim, ModelSim, Verilator, or similar
- SSH access
- Sufficient disk space (~10MB per simulation)

---

## Complete Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                 RV-TROGEN SIMULATION FLOW                   │
└─────────────────────────────────────────────────────────────┘

LOCAL PC:                          SERVER:
┌──────────────────┐               ┌──────────────────┐
│ 1. Generate      │               │                  │
│    Trojans       │               │                  │
└────────┬─────────┘               │                  │
         │                         │                  │
         ▼                         │                  │
┌──────────────────┐               │                  │
│ 2. Integrate     │               │                  │
│    Trojan        │               │                  │
│    + Testbenches │               │                  │
└────────┬─────────┘               │                  │
         │                         │                  │
         │      SCP Upload         │                  │
         ├────────────────────────►│ 3. Receive Files│
         │                         └────────┬─────────┘
         │                                  │
         │                                  ▼
         │                         ┌──────────────────┐
         │                         │ 4. Compile       │
         │                         │    (vlog)        │
         │                         └────────┬─────────┘
         │                                  │
         │                                  ▼
         │                         ┌──────────────────┐
         │                         │ 5. Simulate      │
         │                         │    (vsim)        │
         │                         └────────┬─────────┘
         │                                  │
         │       SCP Download               │
         │◄─────────────────────────────────┤ 6. VCD Files
         │                                  │
         ▼                                  │
┌──────────────────┐                       │
│ 7. Analyze VCD   │                       │
│    + Compare     │                       │
│    + Plot        │                       │
└──────────────────┘                       │
```

---

## Step-by-Step Guide

### STEP 1: Generate Trojans (Local)

```bash
# Parse and rank modules
python scripts/parse_and_rank.py examples/ibex/original --top 5

# Generate trojans for top module
python scripts/generate_trojans.py examples/ibex/original/ibex_csr.sv
```

**Output:**
- `examples/ibex/generated_trojans/ibex_csr/T1_ibex_csr_DoS.sv`
- `examples/ibex/generated_trojans/ibex_csr/T2_ibex_csr_Leak.sv`
- ... (6 trojan variants)

---

### STEP 2: Integrate Trojan + Generate Testbenches (Local)

```bash
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv
```

**What it does:**
1. ✅ Parses original module (handles parameters correctly)
2. ✅ Finds generated trojan
3. ✅ Inserts trojan trigger logic (counter-based, threshold=1000)
4. ✅ Modifies signal assignments to add payload
5. ✅ Generates dynamic testbenches (2000 cycles)

**Output:**
```
examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
testbenches/ibex/tb_ibex_csr.sv
testbenches/ibex/tb_ibex_csr_trojan.sv
```

**Verification:**
```bash
# Check files were created
ls -lh examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
ls -lh testbenches/ibex/tb_ibex_csr.sv
ls -lh testbenches/ibex/tb_ibex_csr_trojan.sv
```

---

### STEP 3: Upload Files to Server

```bash
# Example for Tallinn University of Technology server
SERVER="sharjeel@ekleer.pld.ttu.ee"
WORKDIR="/home/sharjeel/sharjeelphd/Research/rv_trogen"

# Upload original module
scp examples/ibex/original/ibex_csr.sv $SERVER:$WORKDIR/

# Upload trojaned module
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv $SERVER:$WORKDIR/

# Upload testbenches
scp testbenches/ibex/tb_ibex_csr.sv $SERVER:$WORKDIR/
scp testbenches/ibex/tb_ibex_csr_trojan.sv $SERVER:$WORKDIR/
```

**Generic format:**
```bash
scp <local_file> username@server:/path/to/workdir/
```

**Tips:**
- Create workdir on server first: `ssh username@server "mkdir -p /path/to/workdir"`
- Use `-r` for directories: `scp -r testbenches/ username@server:/path/`
- Use compression for large files: `scp -C file.sv username@server:/path/`

---

### STEP 4: SSH to Server and Compile

```bash
# Connect
ssh username@server

# Navigate to work directory
cd /path/to/workdir

# Load CAD environment (server-specific)
# Option 1: Environment manager with menu
cad
# Then select option (e.g., 2.4 for QuestaSim 2024.3)

# Option 2: Source script
source /cad/eda/Siemens/2024-25/scripts/QUESTA-CORE-PRIME_2024.3_RHELx86.csh

# Option 3: Module system
module load questasim/2024.3

# Verify tools loaded
which vlog
which vsim

# Compile ORIGINAL module + testbench
echo "=== Compiling Original ==="
vlog +acc ibex_csr.sv tb_ibex_csr.sv

# Compile TROJAN module + testbench
echo "=== Compiling Trojan ==="
vlog +acc ibex_csr_trojan.sv tb_ibex_csr_trojan.sv
```

**Expected Output:**
```
=== Compiling Original ===
QuestaSim-64 vlog 2024.3 Compiler 2024.09 Sep 10 2024
-- Compiling module ibex_csr
-- Compiling module tb_ibex_csr
Top level modules:
        tb_ibex_csr
Errors: 0, Warnings: 0

=== Compiling Trojan ===
QuestaSim-64 vlog 2024.3 Compiler 2024.09 Sep 10 2024
-- Compiling module ibex_csr_trojan
-- Compiling module tb_ibex_csr_trojan
Top level modules:
        tb_ibex_csr_trojan
Errors: 0, Warnings: 0
```

**If compilation fails:**
- Check signal widths match
- Verify parameter evaluation
- Regenerate files with updated `prepare_simulation.py`

---

### STEP 5: Run Simulations

```bash
# Still on server...

# Simulate ORIGINAL (command-line mode)
echo "=== Simulating Original ==="
vsim -c work.tb_ibex_csr -do "run -all; quit -f"

# Simulate TROJAN
echo "=== Simulating Trojan ==="
vsim -c work.tb_ibex_csr_trojan -do "run -all; quit -f"

# Check VCD files were generated
ls -lh *.vcd
```

**Expected Output:**
```
# Original simulation done
# Trojan simulation done

-rw-r--r-- 1 username users 645K Jan 13 19:40 ibex_csr_original.vcd
-rw-r--r-- 1 username users 682K Jan 13 19:40 ibex_csr_trojan.vcd
```

**VCD File Size Guidelines:**
- 2000 cycles: ~600-700KB
- 15000 cycles: ~4-5MB
- Trojan VCD slightly larger (extra signals)

**Alternative: GUI Mode (if X11 forwarding enabled)**
```bash
vsim work.tb_ibex_csr
# Click Run -> Run -All
# View waveforms
```

---

### STEP 6: Download VCD Files

```bash
# Back on local machine...

# Create directory
mkdir -p simulation_results/vcd

# Download original VCD
scp username@server:/path/to/workdir/ibex_csr_original.vcd simulation_results/vcd/

# Download trojan VCD
scp username@server:/path/to/workdir/ibex_csr_trojan.vcd simulation_results/vcd/

# Example:
scp sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex_csr_original.vcd simulation_results/vcd/
scp sharjeel@ekleer.pld.ttu.ee:/home/sharjeel/sharjeelphd/Research/rv_trogen/ibex_csr_trojan.vcd simulation_results/vcd/
```

**Verification:**
```bash
ls -lh simulation_results/vcd/
# Should see both VCD files
```

---

### STEP 7: Analyze VCD Files

```bash
# Full waveform analysis
python scripts/analyze_vcd.py

# Zoom to trigger region (cycle 900-1200 = 9000-12000 ns)
python scripts/analyze_vcd.py --start 9000 --end 12000

# Very tight zoom (10ns window)
python scripts/analyze_vcd.py --start 10000 --end 10010
```

**Expected Output:**
```
======================================================================
RV-TROGEN VCD ANALYZER
======================================================================

Found 2 VCD files:
  - ibex_csr_original.vcd (645,120 bytes)
  - ibex_csr_trojan.vcd (682,240 bytes)

Comparing:
  Original: ibex_csr_original.vcd
  Trojan:   ibex_csr_trojan.vcd

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

Common signals: 47

Signal: rd_data_o
  Differences found: 3000 time points
    Time 10000: Original=0x12345678, Trojan=0xCDEF3397
    Time 10010: Original=0xABCDEF01, Trojan=0x7602100E
    Time 10020: Original=0x98765432, Trojan=0x478BAB2D
    Time 10030: Original=0xFEDCBA98, Trojan=0x21370467
    Time 10040: Original=0x11111111, Trojan=0xCEBCBEEE
    ... and 2995 more differences

🎯 Total signals with differences: 1

📄 Saved: simulation_results/analysis/comparison_report_9000_12000.txt
📊 Saved: simulation_results/analysis/waveform_comparison_9000_12000.png

======================================================================
ANALYSIS COMPLETE!
======================================================================

✅ Results saved in: simulation_results/analysis
```

**Key Analysis Points:**
- `rd_data_o` shows MAJOR differences after ~10000ns (cycle 1000)
- Trojan XOR corruption visible (pattern: `original ^ 0xDEADBEEF`)
- Difference count should be high (thousands of time points)
- Waveform plot shows yellow highlighting on differences

---

## Server-Specific Setup Examples

### Example 1: Tallinn University of Technology (TalTech)
```bash
# Server details
Server: ekleer.pld.ttu.ee
Username: sharjeel
Workdir: /home/sharjeel/sharjeelphd/Research/rv_trogen

# CAD environment
echo '2.4' | cad  # Loads QuestaSim 2024.3

# Full workflow
ssh sharjeel@ekleer.pld.ttu.ee
cd /home/sharjeel/sharjeelphd/Research/rv_trogen
echo '2.4' | cad
vlog +acc ibex_csr.sv tb_ibex_csr.sv
vsim -c work.tb_ibex_csr -do "run -all; quit -f"
exit
```

### Example 2: Generic HPC Cluster
```bash
# Module system
module load questasim/2024.2
module load python/3.9

# Batch submission (if required)
cat > sim.sh <<'EOF'
#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --mem=4G

module load questasim
vlog +acc ibex_csr.sv tb_ibex_csr.sv
vsim -c work.tb_ibex_csr -do "run -all; quit -f"
EOF

sbatch sim.sh
```

### Example 3: Local QuestaSim (Windows)
```cmd
REM No SSH needed!
cd C:\Projects\rv-trogen

REM Compile
vlog +acc examples\ibex\original\ibex_csr.sv testbenches\ibex\tb_ibex_csr.sv

REM Simulate (GUI)
vsim work.tb_ibex_csr

REM Or command-line
vsim -c work.tb_ibex_csr -do "run -all; quit -f"

REM Analyze
python scripts\analyze_vcd.py
```

---

## Understanding Test Results

### What to Expect

**Before Trigger (0-10000ns):**
- Original and Trojan: IDENTICAL
- All signals match
- Trojan counter incrementing (if visible)

**At Trigger (10000ns = cycle 1000):**
- `trojan_active` goes 0 → 1
- `trojan_counter` = 1000

**After Trigger (10000ns+):**
- `rd_data_o`: MAJOR DIFFERENCES
- Original: Normal values
- Trojan: Corrupted values (XOR with 0xDEADBEEF)
- Differences persist for all remaining cycles

### Verifying Trojan Works

✅ **Trojan is working if:**
1. VCD files generated successfully
2. Trojan VCD has extra signals (`trojan_counter`, `trojan_active`)
3. `rd_data_o` shows differences after ~10000ns
4. Waveform plot shows yellow highlighting
5. Thousands of time points with differences

❌ **Trojan NOT working if:**
1. No differences found
2. Signals identical throughout
3. VCD files identical size
4. No trojan signals visible

**Debugging:**
- Check trojan logic was inserted: `grep "trojan_active" examples/ibex/trojaned_rtl/ibex_csr_trojan.sv`
- Verify payload modification: `grep "rd_data_o =" examples/ibex/trojaned_rtl/ibex_csr_trojan.sv`
- Check testbench runs 2000+ cycles: `grep "repeat" testbenches/ibex/tb_ibex_csr.sv`

---

## Troubleshooting

### Issue: "vlog: command not found"

**Problem:** CAD tools not loaded

**Solution:**
```bash
# Find setup script
find /cad -name "*questa*" -o -name "*vsim*"

# Source it
source /path/to/setup.sh

# Or use environment manager
cad  # then select option
module load questasim
```

### Issue: Compilation errors

**Problem:** Signal width mismatches, parameter issues

**Solution:**
```bash
# Regenerate with updated tools
cd /path/to/rv-trogen
rm examples/ibex/trojaned_rtl/*
rm testbenches/ibex/*
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv

# Re-upload
scp examples/ibex/trojaned_rtl/ibex_csr_trojan.sv SERVER:/workdir/
scp testbenches/ibex/tb_ibex_csr_trojan.sv SERVER:/workdir/
```

### Issue: VCD files not generated

**Problem:** Simulation didn't complete, $dumpfile missing

**Solution:**
```bash
# Check testbench has VCD dumping
grep -A 5 "initial begin" testbenches/ibex/tb_ibex_csr.sv
# Should see:
#   $dumpfile("ibex_csr_original.vcd");
#   $dumpvars(0, tb_ibex_csr);

# Check simulation completed
# Look for: # Original simulation done
```

### Issue: "No differences found" in analysis

**Problem:** Trojan not triggering or not modifying signals

**Solution:**
```bash
# Verify trojan logic inserted
grep "trojan_active" examples/ibex/trojaned_rtl/ibex_csr_trojan.sv

# Check payload
grep "rd_data_o.*trojan_active" examples/ibex/trojaned_rtl/ibex_csr_trojan.sv
# Should see: assign rd_data_o = trojan_active ? (rdata_q ^ 32'hDEADBEEF) : rdata_q;

# Verify testbench runs long enough
grep "repeat" testbenches/ibex/tb_ibex_csr.sv
# Should see: repeat(2000) begin
```

### Issue: Permission denied on server

**Problem:** File permissions, disk quota

**Solution:**
```bash
# Check disk space
df -h /home/username

# Check permissions
ls -la /path/to/workdir

# Create directory
mkdir -p /path/to/workdir
chmod 755 /path/to/workdir
```

---

## Performance Tips

### Reduce Simulation Time

**Current:** 2000 cycles
```systemverilog
repeat(2000) begin  // Trigger at 1000, observe 1000 more
```

**Faster:** 1500 cycles (still works)
```systemverilog
repeat(1500) begin  // Trigger at 1000, observe 500 more
```

**Minimum:** 1100 cycles
```systemverilog
repeat(1100) begin  // Trigger at 1000, observe 100 more
```

**Trade-off:**
- Fewer cycles = Faster simulation
- More cycles = More observation time

### Reduce VCD File Size

**Option 1:** Selective signal dumping
```systemverilog
$dumpfile("ibex_csr_original.vcd");
$dumpvars(1, tb_ibex_csr);  // Only level 1 signals
```

**Option 2:** Compress VCD files
```bash
gzip *.vcd
scp username@server:/workdir/*.vcd.gz simulation_results/vcd/
gunzip simulation_results/vcd/*.vcd.gz
```

---

## Best Practices

### 1. Organize Simulations

```bash
# Create dated directories
mkdir -p simulations/2026-01-13
cd simulations/2026-01-13

# Run multiple modules
for module in ibex_csr ibex_alu ibex_controller; do
    echo "=== $module ==="
    python scripts/prepare_simulation.py examples/ibex/original/${module}.sv
    # Upload, simulate, download...
done
```

### 2. Automate Uploads (Bash Script)

```bash
#!/bin/bash
# upload_sim.sh

MODULE=$1
SERVER="username@server"
WORKDIR="/path/to/workdir"

scp examples/ibex/original/${MODULE}.sv $SERVER:$WORKDIR/
scp examples/ibex/trojaned_rtl/${MODULE}_trojan.sv $SERVER:$WORKDIR/
scp testbenches/ibex/tb_${MODULE}.sv $SERVER:$WORKDIR/
scp testbenches/ibex/tb_${MODULE}_trojan.sv $SERVER:$WORKDIR/

echo "Uploaded $MODULE files"
```

Usage:
```bash
chmod +x upload_sim.sh
./upload_sim.sh ibex_csr
```

### 3. Batch Analysis

```bash
# Analyze multiple VCD pairs
for module in ibex_csr ibex_alu ibex_controller; do
    echo "=== Analyzing $module ==="
    python scripts/analyze_vcd.py \
        --vcd-dir simulation_results/${module}/vcd \
        --start 9000 --end 12000
done
```

---

## Next Steps

After mastering simulation:

1. **Step 20:** Statistical analysis of trojan behavior
2. **Step 21:** Detectability scoring
3. **Step 22:** Performance impact measurement
4. **Step 23:** Comparison with Trust-Hub benchmarks
5. **Step 24:** HTML report generation

---

## Summary Checklist

✅ **Setup Complete When:**
- [ ] Can upload files to server
- [ ] CAD tools load successfully
- [ ] Compilation works (0 errors)
- [ ] Simulations produce VCD files
- [ ] VCD files download successfully
- [ ] Analysis shows trojan differences
- [ ] Waveform plots generated

---

**Last Updated:** January 13, 2026  
**Version:** 2.0.0 (Manual Workflow)  
**Status:** Steps 16-19 Complete, Tested, Working