# RV-TroGen

**Automated Hardware Trojan Generation for RISC-V Processors**

[![License: Academic](https://img.shields.io/badge/License-Academic-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Production](https://img.shields.io/badge/status-production-green.svg)]()

---

## What is RV-TroGen?

**RV-TroGen** is the first automated framework for systematic hardware Trojan generation specifically designed for RISC-V processors. It helps security researchers and processor designers:

- **Test security assertions** - Validate formal verification tools with real Trojans
- **Evaluate detection methods** - Generate diverse Trojan variants for testing
- **Research hardware security** - Systematic exploration of RISC-V vulnerabilities
- **Education** - Learn about hardware Trojans through hands-on examples

---

## Key Features

### **Automated Generation**
First tool to automatically generate hardware Trojans for RISC-V processors - from manual insertion (days) to automated generation (minutes).

### **Multi-Core Support**
Works across multiple open-source RISC-V implementations:
- lowRISC Ibex (RV32IMC)
- OpenHW CVA6 (RV64GC)
- RSD (Out-of-order processor)

### **Six Trojan Categories**
Based on Trust-Hub taxonomy and RISC-V security literature:
1. **Denial of Service** (DoS) - Based on Trust-Hub AES-T1800 & AES-T1900 (functionality-based DoS)
2. **Information Leakage** - Based on Trust-Hub AES-T1000 & AES-T1100 (key/data leakage)
3. **Privilege Escalation** - RISC-V M/S/U mode attacks (Bailey 2017)
4. **Data Integrity** - Based on Trust-Hub AES-T2300 & AES-T2400 (state corruption)
5. **Performance Degradation** - Based on Trust-Hub MEMCTRL-T100 & S35932-T300
6. **Covert Channels** - Timing-based exfiltration (Lin et al. 2009)

### **Template-Based Generation**
12 SystemVerilog templates (6 sequential + 6 combinational) providing:
- Reproducible pattern encoding
- Independent verification
- Easy extensibility
- Direct comparison with Trust-Hub

### **Complete Multi-Trojan Simulation Workflow**
End-to-end trojan validation with:
- Simple parser handling parameterized modules
- Dynamic testbench generation (any module)
- **Multi-trojan automatic integration** - generates ALL trojan variants in one command
- VCD waveform analysis comparing original vs ALL trojans
- Manual workflow proven on university HPC servers

### **Open Source**
Fully open-source tool for the security research community.

---

## Quick Start (5 Minutes)

### Step 1: Install
```bash
# Clone repository
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git
cd rv-trogen

# Install package
python install.py

# Verify installation
python -c "from src.parser import RTLParser; print('Installed successfully!')"
```

### Step 2: Parse Your First Module
```bash
# Parse a RISC-V module
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv
```

**Output:**
```
============================================================
Module: ibex_cs_registers
Type: Sequential
Inputs:    15
Outputs:   8
Has Clock: True
Has Reset: True
============================================================
```

### Step 3: Generate Trojans
```bash
# Generate Trojans for a security-critical module
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Output organized automatically:
# examples/ibex/generated_trojans/ibex_cs_registers/
#   ├── T1_ibex_cs_registers_DoS.sv
#   ├── T2_ibex_cs_registers_Leak.sv
#   ├── T3_ibex_cs_registers_Privilege.sv
#   ├── T4_ibex_cs_registers_Integrity.sv
#   ├── T5_ibex_cs_registers_Availability.sv
#   ├── T6_ibex_cs_registers_Covert.sv
#   └── ibex_cs_registers_trojan_summary.md
```

### Step 4: Integrate ALL Trojans & Generate Testbenches
```bash
# Complete multi-trojan integration: ALL trojans inserted + testbenches generated
python scripts/prepare_multi_trojan_simulation.py examples/ibex/original/ibex_csr.sv

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
```

### Step 5: Simulate & Validate
```bash
# Upload to server, compile ALL modules, simulate ALL trojans (see docs/SIMULATION_SETUP.md)
# Then download VCD files and analyze ALL trojans:

python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr

# Generates comparison for EACH trojan:
#   - SUMMARY_ALL_TROJANS.txt (overview of all trojans)
#   - comparison_DoS.txt + waveform_DoS.png
#   - comparison_Integrity.txt + waveform_Integrity.png
#   - comparison_Covert.txt + waveform_Covert.png
```

---

## Command-Line Tools
```bash
# 1. Parse single module
python -m src.parser.rtl_parser <module.sv>

# 2. Batch parse directory
python scripts/batch_parse.py --dir <directory>

# 3. Find security-critical modules
python scripts/batch_parse.py --dir <directory> --security-only

# 4. Rank by security importance
python scripts/parse_and_rank.py <directory> --top 5

# 5. Generate Trojans for single module
python scripts/generate_trojans.py <module.sv>

# 6. Batch generate for all processors
python scripts/batch_full_pipeline.py                    # All 3 processors
python scripts/batch_full_pipeline.py --processor ibex   # Single processor

# 7. Integrate ALL trojans + generate testbenches (MULTI-TROJAN)
python scripts/prepare_multi_trojan_simulation.py <module.sv>

# 8. Analyze ALL trojan VCD files
python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/<processor>/<module>

# 9. Run tests
python -m pytest tests/ -v
```

---

## Comparison with Related Work

| Feature | **RV-TroGen (Ours)** | **TrojanForge [1]** | **SENTAUR [2]** | **0ena [3]** | **SoC-HTs [4]** | **Trust-Hub [5]** |
|---------|---------------------|-----------------|-----------------|------------|---------------|---------------|
| **Target** | RISC-V (3 cores) | Generic | Generic | RISC-V | Ariane SoC | AES/RSA |
| **Approach** | Template-based | RL-based | LLM (GPT-4) | Manual | Manual | Manual |
| **Automation** | ✅ Full | ✅ Automated | ⚠️ Semi | ❌ Manual | ❌ Manual | ❌ Manual |
| **Multi-Core** | ✅ 3 cores (265 mod) | ❌ Single | ❌ Untested | ⚠️ Generic | ❌ Single SoC | ❌ Single |
| **RTL-Level** | ✅ Yes (SV) | ⚠️ Gate-focus | ✅ Yes | ✅ Yes | ⚠️ SoC (AXI) | ⚠️ Mixed |
| **Attack Surface** | Processor (CSR/LSU) | Generic | Generic | Generic | AXI protocol | Crypto ops |
| **Patterns** | ✅ 6 categories | ⚠️ Black-box | ⚠️ 4 types | ⚠️ 3 examples | ⚠️ 3 types | ✅ Multiple |
| **Templates** | ✅ 12 (.sv files) | ❌ RL policy | ❌ LLM prompts | ❌ No | ❌ No | ❌ No |
| **Multi-Trojan** | ✅ Batch workflow | ❌ N/A | ❌ N/A | ❌ N/A | ❌ N/A | ❌ N/A |
| **Validation** | ✅ QuestaSim (100%) | ⚠️ Evasion | ⚠️ Detection | ⚠️ Not reported | ✅ FPGA+GNN | ✅ Benchmarks |
| **Simulation** | ✅ Complete workflow | ❌ N/A | ❌ Not reported | ❌ Manual | ✅ Behavioral | ❌ N/A |
| **Detection Focus** | ⚠️ Secondary | ⚠️ Primary | ⚠️ Primary | ❌ No | ✅ Primary | ✅ Benchmarks |
| **Open-Source** | ✅ Full (MIT) | ❌ No | ❌ No | ✅ Yes | ✅ 3 HTs | ❌ Registration |
| **Generated HTs** | ✅ 929 | ⚠️ Unknown | ⚠️ 4 | ⚠️ 3 | ⚠️ 3 | ✅ 90+ |
| **Performance** | ✅ 4.1s | ⚠️ Hours | ⚠️ Slow | ❌ N/A | ❌ Manual | ❌ N/A |
| **Cost** | ✅ Free | ❌ Unknown | ⚠️ API costs | ✅ Free | ✅ Free | ❌ Paid |
| **Year** | 2026 | 2024 | 2024 | 2020 | 2023 | 2008-now |

**Key Innovation:** First automated, template-based, open-source framework for RISC-V Trojan generation with complete multi-trojan simulation and validation workflow.

---

## Use Cases

### **1. Security Researcher**
Test your Trojan detection algorithms:
```bash
# Generate diverse Trojan variants
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Integrate ALL trojans and simulate
python scripts/prepare_multi_trojan_simulation.py examples/ibex/original/ibex_csr.sv

# Upload, simulate on server, download VCDs...

# Validate ALL trojan behaviors
python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr
```

### **2. Processor Designer**
Validate security assertions in your RISC-V design:
```bash
# Find most critical modules
python scripts/parse_and_rank.py my_processor/rtl --top 5

# Generate test cases for formal verification
python scripts/generate_trojans.py <critical_module.sv>

# Validate with simulation
python scripts/prepare_multi_trojan_simulation.py <critical_module.sv>
```

### **3. Educator/Student**
Learn about hardware security:
```bash
# Start with parsing
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv

# Generate and study Trojan examples
python scripts/generate_trojans.py examples/ibex/original/ibex_alu.sv

# See how they work in simulation
python scripts/prepare_multi_trojan_simulation.py examples/ibex/original/ibex_csr.sv
python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr
```

---

## Documentation

### **Getting Started:**
- [Quick Start Guide](docs/QUICK_START.md) - 15-minute tutorial
- [Commands Reference](docs/COMMANDS_REFERENCE.md) - All commands explained
- [Step-by-Step Progress](docs/STEP_GUIDE.md) - Development roadmap

### **Technical Details:**
- [Template Library](docs/TEMPLATES.md) - Template documentation
- [Simulation Setup](docs/SIMULATION_SETUP.md) - Complete multi-trojan workflow
- [Trust-Hub Patterns](docs/TRUST_HUB_PATTERNS.md) - Pattern library with citations

---

## Testing & Validation
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src tests/

# Validate multi-trojan integration and simulation
python scripts/prepare_multi_trojan_simulation.py examples/ibex/original/ibex_csr.sv
```

**Test Coverage:** 85% (24/24 tests passing)

---

## Dependencies
```bash
# Core dependencies
pytest>=7.0.0
pytest-cov>=3.0.0

# Simulation support
matplotlib>=3.5.0
```

### Installation
```bash
# Core installation
python -m pip install -e .

# Add simulation support
python -m pip install matplotlib
```

---

## Results

**Generated 707 Trojans across 3 RISC-V processors in 4.1 seconds:**

| Processor | Modules | Trojans | Avg per Module |
|-----------|---------|---------|----------------|
| Ibex | 28 | 136 | 4.9 |
| CVA6 | 85 | 331 | 3.9 |
| RSD | 152 | 240 | 1.6 |
| **Total** | **265** | **707** | **3.5** |

**Validation Results (Multi-Trojan Simulation):**
- ✅ Compilation: 100% success for all trojan variants (QuestaSim 2024.3)
- ✅ Simulation: Original + 3 trojans (DoS, Integrity, Covert) run to completion (30,000 cycles each)
- ✅ VCD Analysis: Differences detected in all trojans:
  - **DoS**: 15,000+ time points (wr_en_i blocked after activation)
  - **Integrity**: 3,000+ time points (rd_data_o XOR corruption = 0xDEADBEEF)
  - **Covert**: 8,000+ time points (timing modulation on rd_error_o)
- ✅ Payload Verification: All trojan behaviors confirmed in waveforms
- ✅ Multi-Trojan Workflow: Complete automation from generation → simulation → analysis

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## License

**Academic and Research Use Only**

This is a PhD research project from Tallinn University of Technology.

- Free for academic research and education
- Cite our paper if you use it
- Commercial use requires permission

For inquiries: sharjeel.imtiaz@taltech.ee

See [LICENSE](LICENSE) for full terms.

---

## Contact & Support

- **Author:** Sharjeel Imtiaz
- **Email:** sharjeel.imtiaz@taltech.ee
- **Institution:** Tallinn University of Technology (TalTech)
- **Repository:** https://github.com/sharjeelimtiaz27/rv-trogen
- **Issues:** https://github.com/sharjeelimtiaz27/rv-trogen/issues

---

## Acknowledgments

This work builds upon:
- **Trust-Hub** - Hardware Trojan benchmarks and taxonomy
- **lowRISC Ibex** - Open-source RISC-V core for testing
- **OpenHW CVA6** - Application-class RISC-V processor
- **RISC-V International** - ISA specifications and privilege architecture

Key papers that informed our work:
- Bailey (2017) - RISC-V privilege escalation exploits
- Boraten & Kodi (2016) - Performance degradation attacks (NoC-based)
- Lin et al. (2009) - Trojan side-channel engineering

See [docs/TRUST_HUB_PATTERNS.md](docs/TRUST_HUB_PATTERNS.md) for complete references.

---

## Citation

If you use RV-TroGen in your research, please cite:
```bibtex
@misc{rvtrogen2026,
  author = {Imtiaz, Sharjeel},
  title = {RV-TroGen: Automated Hardware Trojan Generation for RISC-V Processors},
  year = {2026},
  institution = {Tallinn University of Technology},
  url = {https://github.com/sharjeelimtiaz27/rv-trogen},
  note = {Open-source template-based framework with complete multi-trojan simulation workflow}
}
```

---

## Ethical Use

**Important:** This tool is designed for:
- Security research and testing
- Educational purposes
- Validating detection methods
- Improving processor security

**Not intended for:**
- Malicious hardware insertion
- Compromising production systems
- Any illegal activities

Users are responsible for ethical and legal use of this software.

---

**Current Version:** 2.0.0  
**Last Updated:** February 18, 2026

---

**Star this repo if you find it useful!**