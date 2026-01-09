# Simulation Setup Guide

Complete guide for setting up local or remote simulation with RV-TroGen.

---

## Overview

RV-TroGen supports flexible simulation configurations:
- **Local Simulation** - If tools installed on your machine
- **Remote Simulation** - If tools on university/company server (via SSH)
- **Auto Mode** - Try local first, fallback to remote

---

## Quick Start

### Step 1: Run Setup Wizard
```bash
python scripts/setup_simulation.py
```

This interactive wizard will:
1. Detect local simulators (Verilator, QuestaSim, Icarus)
2. Configure remote server access (if needed)
3. Handle CAD environment managers
4. Generate `config/simulation_config.py`

### Step 2: Validate Compilation
```bash
python scripts/validate_compilation.py
```

Tests that generated Trojans compile successfully.

---

## Scenario 1: Local Simulation

**Requirements:**
- Verilator, QuestaSim, or Icarus Verilog installed locally

**Install Verilator (Recommended - Free):**
```bash
# Windows (via MSYS2)
pacman -S mingw-w64-x86_64-verilator

# Ubuntu/Linux
sudo apt install verilator

# macOS
brew install verilator
```

**Setup:**
```bash
python scripts/setup_simulation.py

# Answer:
# Local simulator found? yes
# Remote server? no
# Mode: local
```

---

## Scenario 2: Remote Simulation (University Server)

**Common Setup:** QuestaSim on shared university HPC cluster

**Our Example:**
- Server: ekleer.pld.ttu.ee (Tallinn University of Technology)
- Tools: Siemens QuestaSim 2024.3
- Access: SSH with password authentication
- Environment: CAD module manager

**Setup:**
```bash
python scripts/setup_simulation.py

# Answer:
# Remote server? yes
#   Hostname: ekleer.pld.ttu.ee
#   Username: sharjeel
#   CAD environment? yes
#   Setup command: cad
#   CAD option: 2.4
#   QuestaSim command: vsim
#   Working dir: /home/sharjeel/rv-trogen-sims
# Mode: remote
```

**What Happens Behind the Scenes:**
1. SSH connects to server (password prompted)
2. Transfers files via SFTP
3. Runs: `echo '2.4' | cad` (loads CAD tools)
4. Runs: `vsim -c -do "vlog file.sv; quit"`
5. Fetches results back to laptop

---

## CAD Environment Managers

Many universities use environment managers like:

**Examples:**
```bash
# Menu-based (common at universities)
cad
# Then select option: 2.4

# Module-based (HPC clusters)
module load questasim

# Script-based
source /opt/tools/setup.sh
```

**RV-TroGen handles these automatically!**

---

## Configuration File

After setup, `config/simulation_config.py` contains:
```python
SIMULATION_MODE = 'remote'  # or 'local' or 'auto'

REMOTE_SIMULATOR = {
    'enabled': True,
    'host': 'ekleer.pld.ttu.ee',
    'username': 'sharjeel',
    'port': 22,
    
    # CAD environment loading
    'cad_setup_command': "echo '2.4' | cad",
    
    # Simulator
    'tool': 'questasim',
    'questasim_path': 'vsim',
    'remote_work_dir': '/home/sharjeel/rv-trogen-sims',
    
    # Authentication
    'use_ssh_key': False,  # Password authentication
    'ssh_key_path': None,
}
```

**Edit this file to reconfigure manually.**

---

## Dependencies

**Required for Remote Simulation:**
```bash
python -m pip install paramiko --break-system-packages
```

**Paramiko:** Pure-Python SSH library (cross-platform)

---

## Validation Results

**Example output from our setup:**
```
🔧 RV-TROGEN COMPILATION VALIDATION

🔐 Connecting to sharjeel@ekleer.pld.ttu.ee...
Password: ********
✅ Connected successfully!

📂 Finding generated Trojans...
Found 929 Trojan files

🧪 Testing compilation (first 10 files)...
📤 Transferring T1_ibex_alu_Integrity.sv... ✓
🔧 Compiling T1_ibex_alu_Integrity.sv... ✅
📤 Transferring T2_ibex_alu_DoS.sv... ✓
🔧 Compiling T2_ibex_alu_DoS.sv... ✅
...

======================================================================
📊 COMPILATION VALIDATION RESULTS
======================================================================

✅ Passed: 10/10
❌ Failed: 0/10

🎉 All tested Trojans compile successfully!
```

---

## Troubleshooting

### Issue: "No module named 'paramiko'"
```bash
python -m pip install paramiko --break-system-packages
```

### Issue: "Connection timeout"

- Check server hostname/IP
- Ensure you're on university network (VPN if remote)
- Verify username
- Check firewall rules

### Issue: "Authentication failed"

- Double-check password
- Try SSH manually first: `ssh username@server`
- Consider setting up SSH key

### Issue: "vsim: Command not found"

- CAD environment not loading correctly
- Check `cad_setup_command` in config
- Test manually on server: `cad` then `which vsim`

---

## SSH Key Setup (Optional - Recommended)

For password-free authentication:
```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t rsa -b 4096

# Copy to server
ssh-copy-id username@server

# Update config to use SSH key
# Edit config/simulation_config.py:
# 'use_ssh_key': True
# 'ssh_key_path': '~/.ssh/id_rsa'
```

---

## For Researchers

**Why Remote Simulation?**
- University HPC clusters have expensive tools (QuestaSim, VCS)
- Centralized license management
- More compute power
- Standard practice in academia

**Our Implementation:**
- Uses Paramiko (pure Python, no system SSH dependencies)
- Cross-platform (Windows, Linux, macOS)
- Secure (password not stored, prompted at runtime)
- Flexible (handles various CAD environment systems)

---

## Next Steps

After setup and validation:
```bash
# Step 16: Full simulation with testbenches (coming soon)
python scripts/run_simulations.py

# Step 17: VCD analysis (coming soon)
python scripts/analyze_waveforms.py
```

---

**Last Updated:** January 9, 2026  
**Step:** 15/30 (50%)  
**Status:** Remote simulation framework complete
```

---

## ✅ **SUMMARY OF ALL UPDATES:**
```
Files to Update:
1. ✅ requirements.txt - Add paramiko>=3.0.0
2. ✅ docs/STEP_GUIDE.md - Add Step 15 complete section
3. ✅ docs/COMMANDS_REFERENCE.md - Add validation commands
4. ✅ docs/QUICK_START.md - Update status line
5. ✅ Root README.md - Multiple updates (5 sections)
6. ✅ docs/SIMULATION_SETUP.md - NEW complete guide

Total: 6 files (5 updates + 1 new file)