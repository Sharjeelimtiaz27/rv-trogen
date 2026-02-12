# RV-TroGen

**Automated Hardware Trojan Generation for RISC-V Processors**

[![License: Academic](https://img.shields.io/badge/License-Academic-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Beta](https://img.shields.io/badge/status-beta-orange.svg)]()

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

### **Complete Simulation Workflow**
End-to-end trojan validation with:
- Simple parser handling parameterized modules
- Dynamic testbench generation (any module)
- Automatic trojan integration with payload
- VCD waveform analysis with time filtering
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
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv
```

**Output:**
```
Parsing: ibex_cs_registers.sv

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

### Step 4: Integrate Trojan & Generate Testbenches
```bash
# Complete integration: trojan insertion + testbench generation
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv

# Creates:
#   - examples/ibex/trojaned_rtl/ibex_csr_trojan.sv  (with payload!)
#   - testbenches/ibex/tb_ibex_csr.sv                (original)
#   - testbenches/ibex/tb_ibex_csr_trojan.sv         (trojan)
```

### Step 5: Simulate & Validate
```bash
# Upload to server, compile, simulate (see docs/SIMULATION_SETUP.md)
# Then download VCD files and analyze:

python scripts/analyze_vcd.py --start 9000 --end 12000

# Generates:
#   - comparison_report.txt
#   - waveform_comparison.png (differences highlighted!)
```

---

## Command-Line Tools

```bash
# 1. Parse single module
python -m src/parser/rtl_parser.py <module.sv>

# 2. Batch parse directory
python -m scripts/batch_parse.py --dir <directory>

# 3. Find security-critical modules
python -m scripts/batch_parse.py --dir <directory> --security-only

# 4. Rank by security importance
python scripts/parse_and_rank.py <directory> --top 5

# 5. Generate Trojans for single module
python scripts/generate_trojans.py <module.sv>

# 6. Batch generate for all processors
python scripts/batch_generate.py                    # All 3 processors
python scripts/batch_generate.py --processor ibex   # Single processor

# 7. Integrate trojan + generate testbenches
python scripts/prepare_simulation.py <module.sv>

# 8. Analyze VCD files
python scripts/analyze_vcd.py --start 9000 --end 12000

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
| **Validation** | ✅ QuestaSim (100%) | ⚠️ Evasion | ⚠️ Detection | ⚠️ Not reported | ✅ FPGA+GNN | ✅ Benchmarks |
| **Simulation** | ✅ Complete workflow | ❌ N/A | ❌ Not reported | ❌ Manual | ✅ Behavioral | ❌ N/A |
| **Detection Focus** | ⚠️ Secondary | ⚠️ Primary | ⚠️ Primary | ❌ No | ✅ Primary | ✅ Benchmarks |
| **Open-Source** | ✅ Full (MIT) | ❌ No | ❌ No | ✅ Yes | ✅ 3 HTs | ❌ Registration |
| **Generated HTs** | ✅ 707 | ⚠️ Unknown | ⚠️ 4 | ⚠️ 3 | ⚠️ 3 | ✅ 90+ |
| **Performance** | ✅ 4.1s | ⚠️ Hours | ⚠️ Slow | ❌ N/A | ❌ Manual | ❌ N/A |
| **Cost** | ✅ Free | ❌ Unknown | ⚠️ API costs | ✅ Free | ✅ Free | ❌ Paid |
| **Year** | 2026 | 2024 | 2024 | 2020 | 2023 | 2008-now |

**Key Innovation:** First automated, template-based, open-source framework for RISC-V Trojan generation with complete simulation and validation workflow.

**Note:** Trust-Hub includes performance degradation in their taxonomy, but examples are primarily gate-level. Our template provides RTL-level implementation specifically for RISC-V based on Boraten & Kodi (IPDPS 2016).

**References:**
- [1] K. Hui et al., "TrojanForge: Generating Adversarial Hardware Trojan Examples Using Reinforcement Learning," arXiv:2405.15184, 2024. https://arxiv.org/abs/2405.15184
- [2] J. Bhandari et al., "SENTAUR: Security EnhaNced Trojan Assessment Using LLMs Against Undesirable Revisions," arXiv:2407.12352, 2024. https://arxiv.org/pdf/2407.12352
- [3] A. Moschos, "Towards Practical Fabrication Stage Attacks Using Interrupt-Resilient Hardware Trojans," GitHub, 2020. https://github.com/0ena/riscv-hw-trojans
- [4] S. Deb, "A RISC-V SoC with Hardware Trojans: Case Study on Trojan-ing the On-Chip Protocol Conversion," IEEE, 2023. https://ieeexplore.ieee.org/abstract/document/10321883
- [5] Trust-Hub, "Hardware Trojan Benchmarks," https://trust-hub.org

---

## Use Cases

### **1. Security Researcher**
Test your Trojan detection algorithms:
```bash
# Generate diverse Trojan variants
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Integrate and simulate
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv

# Validate trojan behavior
python scripts/analyze_vcd.py --start 9000 --end 12000
```

### **2. Processor Designer**
Validate security assertions in your RISC-V design:
```bash
# Find most critical modules
python scripts/parse_and_rank.py my_processor/rtl --top 5

# Generate test cases for formal verification
python scripts/generate_trojans.py <critical_module.sv>

# Validate with simulation
python scripts/prepare_simulation.py <critical_module.sv>
```

### **3. Educator/Student**
Learn about hardware security:
```bash
# Start with parsing
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv

# Generate and study Trojan examples
python scripts/generate_trojans.py examples/ibex/original/ibex_alu.sv

# See how they work in simulation
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv
python scripts/analyze_vcd.py
```

---

## Documentation

### **Getting Started:**
- [Quick Start Guide](docs/QUICK_START.md) - 15-minute tutorial
- [Commands Reference](docs/COMMANDS_REFERENCE.md) - All commands explained
- [Step-by-Step Progress](docs/STEP_GUIDE.md) - Development roadmap

### **Technical Details:**
- [Template Library](docs/TEMPLATES.md) - Template documentation
- [Simulation Setup](docs/SIMULATION_SETUP.md) - Complete workflow guide
- [Trust-Hub Patterns](docs/TRUST_HUB_PATTERNS.md) - Pattern library with citations

---

## Testing & Validation

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src/parser tests/

# Validate trojan integration and simulation
python scripts/prepare_simulation.py examples/ibex/original/ibex_csr.sv
```

**Test Coverage:** 74% (19/19 tests passing)

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

**Generated 929 Trojans across 3 RISC-V processors in 4.1 seconds:**

| Processor | Modules | Trojans | Avg per Module |
|-----------|---------|---------|----------------|
| Ibex | 28 | 154 | 5.5 |
| CVA6 | 85 | 376 | 4.4 |
| RSD | 152 | 399 | 2.6 |
| **Total** | **265** | **929** | **3.5** |

**Validation Results:**
- ✅ Compilation: 100% success (QuestaSim 2024.3)
- ✅ Simulation: Both original and trojan modules run to completion
- ✅ VCD Analysis: 3000+ time points with differences detected
- ✅ Payload Verification: XOR corruption confirmed (0xDEADBEEF)

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
  note = {Open-source template-based framework with complete simulation workflow}
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

**Current Version:** 1.6.0  
**Last Updated:** January 19, 2026

---

**Star this repo if you find it useful!**