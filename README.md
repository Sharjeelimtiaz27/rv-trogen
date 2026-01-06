# 🔧 RV-TroGen

**Automated Hardware Trojan Generation for RISC-V Processors**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Beta](https://img.shields.io/badge/status-beta-orange.svg)]()

---

## 📖 What is RV-TroGen?

**RV-TroGen** is the first automated framework for systematic hardware Trojan generation specifically designed for RISC-V processors. It helps security researchers and processor designers:

- ✅ **Test security assertions** - Validate formal verification tools with real Trojans
- ✅ **Evaluate detection methods** - Generate diverse Trojan variants for testing
- ✅ **Research hardware security** - Systematic exploration of RISC-V vulnerabilities
- ✅ **Education** - Learn about hardware Trojans through hands-on examples

---

## 🌟 Key Features

### **Automated Generation**
First tool to automatically generate hardware Trojans for RISC-V processors - from manual insertion (days) to automated generation (minutes).

### **Multi-Core Support**
Works across multiple open-source RISC-V implementations:
- ✅ lowRISC Ibex (RV32IMC)
- ✅ OpenHW CVA6 (RV64GC)
- ✅ RSD (Out-of-order processor)

### **Six Trojan Categories**
Based on Trust-Hub taxonomy and RISC-V security literature:
1. **Denial of Service** (DoS) - Based on Trust-Hub AES-T1400
2. **Information Leakage** - Based on Trust-Hub RSA-T600
3. **Privilege Escalation** - RISC-V M/S/U mode attacks
4. **Data Integrity** - Based on Trust-Hub AES-T800
5. **Performance Degradation** - LSU stalling attacks
6. **Covert Channels** - Timing-based information exfiltration

### **Template-Based Generation**
12 SystemVerilog templates (6 sequential + 6 combinational) providing:
- ✅ Reproducible pattern encoding
- ✅ Independent verification
- ✅ Easy extensibility
- ✅ Direct comparison with Trust-Hub

### **Open Source**
Fully open-source tool for the security research community.

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install
```bash
# Clone repository
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git
cd rv-trogen

# Install package (shows welcome banner)
python install.py

# Alternative: Manual install
python -m pip install -e .

# Verify installation
python -c "from src.parser import RTLParser; print('✅ Installed successfully!')"
```

### Step 2: Parse Your First Module
```bash
# Parse a RISC-V module
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv
```

**Output:**
```
🔍 Parsing: ibex_cs_registers.sv

============================================================
Module: ibex_cs_registers
Type: Sequential
Inputs:    15
Outputs:   8
Has Clock: True
Has Reset: True
============================================================
```

### Step 3: Generate Trojans ⭐ NEW!
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

### Step 4: Find Security-Critical Modules
```bash
# Rank modules by security importance
python scripts/parse_and_rank.py examples/ibex/original --top 5
```

---

## 📦 What's Currently Working

### ✅ **Parser Module (Week 1 - COMPLETE)**

**Parse any Verilog/SystemVerilog file:**
```python
from src.parser import RTLParser

parser = RTLParser('your_module.sv')
module = parser.parse()

print(f"Module: {module.name}")
print(f"Type: {'Sequential' if module.is_sequential else 'Combinational'}")
print(f"Inputs: {len(module.inputs)}")
```

**Features:**
- ✅ Extracts all signals (inputs, outputs, internals)
- ✅ Classifies sequential vs combinational
- ✅ Detects clock and reset signals
- ✅ Batch processing for multiple files
- ✅ Security-critical module identification

**Test Coverage:** 74% (19/19 tests passing)

### ✅ **Generator Module (Week 2 Steps 7-9 - COMPLETE)**

- ✅ Pattern library (6 categories)
- ✅ Sequential/Combinational generators
- ✅ Smart output organization
- ✅ Trojan summary reports
- ✅ **Template library (12 templates)** ← NEW!

### **✅ Template Library (Step 9 - COMPLETE)**

**12 SystemVerilog Templates:**
- 6 Sequential patterns (always_ff based)
- 6 Combinational patterns (assign/always_comb based)

**Why Templates?**
- ✅ **Reproducible**: Fixed .sv files, not black-box code generation
- ✅ **Verifiable**: Each template can be compiled independently
- ✅ **Extensible**: Add new patterns by creating new templates
- ✅ **Comparable**: Direct structural comparison with Trust-Hub

**Template Library:**
```
Sequential:                      Combinational:
✅ dos_template.sv              ✅ dos_template.sv
✅ leak_template.sv             ✅ leak_template.sv
✅ privilege_template.sv        ✅ privilege_template.sv
✅ integrity_template.sv        ✅ integrity_template.sv
✅ availability_template.sv     ✅ availability_template.sv
✅ covert_template.sv           ✅ covert_template.sv
```

**See:** [docs/TEMPLATES.md](docs/TEMPLATES.md) for detailed documentation.

### ⏸️ **Validator Module (Week 3 - PLANNED)**

- Simulation integration
- Signal comparison
- Behavioral analysis
- HTML reports with waveforms

---

## 🛠️ Command-Line Tools
```bash
# 1. Parse single module
python -m src/parser/rtl_parser.py <module.sv>

# 2. Batch parse directory
python -m scripts/batch_parse.py --dir <directory>

# 3. Find security-critical modules
python -m scripts/batch_parse.py --dir <directory> --security-only

# 4. Rank by security importance
python -m scripts/parse_and_rank.py <directory> --top 10

# 5. Generate Trojans ⭐
python scripts/generate_trojans.py <module.sv>

# 6. Save results to JSON
python -m scripts/batch_parse.py --dir <directory> --save-json

# 7. Run tests
python -m pytest tests/ -v
```

---

## 📊 Project Status
```
✅ Week 1: Parser Implementation (Steps 1-6) - COMPLETE
   ├── ✅ RTL parser core
   ├── ✅ Signal extraction
   ├── ✅ Module classification
   ├── ✅ Batch processing
   ├── ✅ Security ranking
   └── ✅ 19 unit tests (100% passing, 74% coverage)

✅ Week 2: Generator & Templates (Steps 7-9) - COMPLETE
   ├── ✅ Pattern library split (6 modules)
   ├── ✅ Generator split (sequential/combinational)
   ├── ✅ Wrapper script (generate_trojans.py)
   ├── ✅ Smart output organization
   └── ✅ Template library (12 templates)

⏸️ Week 2: Template Integration (Steps 10-13) - IN PROGRESS
   ├── ⏸️ Template testing (Step 10)
   ├── ⏸️ Generator updates (Step 11)
   ├── ⏸️ Batch generation (Step 12)
   └── ⏸️ Examples reorganization (Step 13)

⏸️ Week 3: Validation Framework (Steps 14-19) - PLANNED
   └── Simulation, comparison, reporting

⏸️ Week 4-5: Polish & Release (Steps 20-30) - PLANNED
   └── Examples, CI/CD, documentation
```

**Progress:** 9/30 steps (30%)

---

## 📁 Project Structure
```
rv-trogen/
├── src/
│   ├── parser/              ✅ COMPLETE (Week 1)
│   │   ├── rtl_parser.py
│   │   ├── signal_extractor.py
│   │   └── module_classifier.py
│   ├── patterns/            ✅ COMPLETE (Week 2)
│   │   ├── dos_pattern.py
│   │   ├── leak_pattern.py
│   │   ├── privilege_pattern.py
│   │   ├── integrity_pattern.py
│   │   ├── availability_pattern.py
│   │   └── covert_pattern.py
│   ├── generator/           ✅ COMPLETE (Week 2)
│   │   ├── trojan_generator.py
│   │   ├── sequential_gen.py
│   │   └── combinational_gen.py
│   └── validator/           ⏸️ PLANNED (Week 3)
├── templates/               ✅ NEW! (Step 9)
│   └── trojan_templates/
│       ├── sequential/ (6 templates)
│       └── combinational/ (6 templates)
├── scripts/
│   ├── batch_parse.py       ✅ Parser wrapper
│   ├── parse_and_rank.py    ✅ Security ranking
│   └── generate_trojans.py  ✅ Generator wrapper
├── docs/
│   ├── QUICK_START.md       ✅ Beginner tutorial
│   ├── COMMANDS_REFERENCE.md ✅ Command guide
│   ├── TEMPLATES.md         ✅ Template documentation
│   ├── TRUST_HUB_PATTERNS.md ✅ Pattern library
│   └── STEP_GUIDE.md        ✅ Progress tracking
├── tests/
│   └── test_parser.py       ✅ 19 tests
└── examples/
    └── ibex/
        ├── original/        ✅ Test modules
        └── generated_trojans/ ✅ Generated Trojans
```

---

## 🆚 Comparison with Related Work

| Feature | RV-TroGen (Ours) | Lipp et al. [1] | Trust-Hub [2] | TrojanForge [3] |
|---------|------------------|-----------------|---------------|-----------------|
| **Target** | RISC-V (Ibex/CVA6/RSD) | RISC-V (PULPino) | AES/RSA | Generic |
| **Approach** | Template-based | Manual insertion | Manual benchmarks | ML/RL-based |
| **Automation** | ✅ Fully automated | ❌ Manual | ❌ Manual | ✅ Automated |
| **Multi-Core** | ✅ 3 cores | ❌ Single | ❌ Single design | ❌ Generic |
| **Patterns** | 6 categories | 4 types | Various | Black-box |
| **Templates** | ✅ 12 templates | ❌ | ❌ | ❌ |
| **Validation** | ✅ Planned | ✅ Silicon | ✅ Benchmarks | ❌ Evasion-focused |
| **Open-Source** | ✅ Yes | ⚠️ Partial | ❌ No | ❌ No |
| **Documentation** | ✅ Comprehensive | ⚠️ Paper only | ⚠️ Limited | ⚠️ Paper only |

**Key Innovation:** First automated, template-based, open-source framework for RISC-V Trojan generation.

**References:**
- [1] Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF 2021
- [2] Trust-Hub: https://trust-hub.org
- [3] TrojanForge: "Adversarial Hardware Trojan Examples with Reinforcement Learning," arXiv 2024

---

## 🎯 Use Cases

### **1. Security Researcher**
Test your Trojan detection algorithms:
```bash
# Generate diverse Trojan variants
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Use generated Trojans to validate your detection tool
```

### **2. Processor Designer**
Validate security assertions in your RISC-V design:
```bash
# Find most critical modules
python scripts/parse_and_rank.py my_processor/rtl --top 5

# Generate test cases for formal verification
python scripts/generate_trojans.py <critical_module.sv>
```

### **3. Educator/Student**
Learn about hardware security:
```bash
# Start with parsing
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv

# Generate and study Trojan examples
python scripts/generate_trojans.py examples/ibex/original/ibex_alu.sv
```

---

## 📚 Documentation

### **Getting Started:**
- [Quick Start Guide](docs/QUICK_START.md) - 15-minute tutorial
- [Commands Reference](docs/COMMANDS_REFERENCE.md) - All commands explained
- [Step-by-Step Progress](docs/STEP_GUIDE.md) - Development roadmap

### **Technical Details:**
- [Template Library](docs/TEMPLATES.md) - Template documentation ⭐ NEW!
- [Trust-Hub Patterns](docs/TRUST_HUB_PATTERNS.md) - Pattern library with citations
- [Parser Architecture](docs/parser/PARSER_ARCHITECTURE.md) - Implementation details

---

## 🧪 Testing & Validation
```bash
# Run all tests
python -m pytest tests/ -v

# Expected: 19 passed

# Run with coverage
python -m pytest --cov=src/parser tests/

# Expected: 74% coverage
```

---

## 🤝 Contributing

We welcome contributions! Current needs:

**High Priority:**
- Testing on CVA6 and RSD cores
- Template validation (Step 10)
- Generator template integration (Step 11)

**Medium Priority:**
- Additional Trojan patterns
- Validation framework (Week 3)
- Documentation improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file

---

## 📧 Contact & Support

- **Author:** Sharjeel Imtiaz
- **Email:** sharjeel.imtiaz@taltech.ee
- **Institution:** Tallinn University of Technology (TalTech)
- **Repository:** https://github.com/sharjeelimtiaz27/rv-trogen
- **Issues:** https://github.com/sharjeelimtiaz27/rv-trogen/issues

---

## 🙏 Acknowledgments

This work builds upon:
- **Trust-Hub** - Hardware Trojan benchmarks and taxonomy
- **lowRISC Ibex** - Open-source RISC-V core for testing
- **OpenHW CVA6** - Application-class RISC-V processor
- **RISC-V International** - ISA specifications and privilege architecture

Key papers that informed our work:
- Bailey (2017) - RISC-V privilege escalation exploits
- Lipp et al. (2021) - RISC-V Trojan tapeout case study
- Lin et al. (2009) - Trojan side-channel engineering
- Boraten & Kodi (2016) - Performance degradation attacks

See [docs/TRUST_HUB_PATTERNS.md](docs/TRUST_HUB_PATTERNS.md) for complete references.

---

## 📝 Citation

If you use RV-TroGen in your research, please cite:
```bibtex
@misc{rvtrogen2026,
  author = {Imtiaz, Sharjeel},
  title = {RV-TroGen: Automated Hardware Trojan Generation for RISC-V Processors},
  year = {2026},
  institution = {Tallinn University of Technology},
  url = {https://github.com/sharjeelimtiaz27/rv-trogen},
  note = {Open-source template-based framework for hardware security research}
}
```

---

## ⚖️ Ethical Use

**Important:** This tool is designed for:
- ✅ Security research and testing
- ✅ Educational purposes
- ✅ Validating detection methods
- ✅ Improving processor security

**Not intended for:**
- ❌ Malicious hardware insertion
- ❌ Compromising production systems
- ❌ Any illegal activities

Users are responsible for ethical and legal use of this software.

---

**Current Version:** 1.0.0-beta  
**Last Updated:** January 2026  
**Status:** Active Development (30% Complete - Step 9 Done)

---

**⭐ Star this repo if you find it useful!**