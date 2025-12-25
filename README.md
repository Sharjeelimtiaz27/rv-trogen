# 🔧 RV-TroGen

**RTL-Level Hardware Trojan Generation for RISC-V Processors**



## 📖 What is RV-TroGen?

RV-TroGen automatically generates hardware Trojans for RISC-V processors to help you:
- **Test security assertions** in your processor designs
- **Validate detection tools** with real Trojan examples
- **Research hardware security** with systematic Trojan generation

**Key Difference from TrojanForge:** We work at RTL-level (not gate-level) using pattern-based generation (not ML) for assertion validation (not detector evasion).

---

## 🚀 Quick Start (5 Minutes)

### **Step 1: Install**
```bash
# Clone repository
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git
cd rv-trogen

# Install package
python -m pip install -e .

# Verify installation
python -c "from src.parser import RTLParser; print('✅ Installed successfully!')"
```

### **Step 2: Parse Your First Module**
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

### **Step 3: Parse Multiple Modules**
```bash
# Parse all modules in a directory
python -m scripts/batch_parse.py --dir examples/ibex/original

# Parse security-critical modules only
python -m scripts/batch_parse.py --dir examples/ibex/original --security-only

# Rank modules by security importance
python -m scripts/parse_and_rank.py examples/ibex/original --top 5
```

### **Step 4: Generate Trojans** (Coming in Week 2)
```bash
# Generate Trojans for a module (Week 2)
python -m src/generator/trojan_generator.py examples/ibex/original/ibex_cs_registers.sv
```

---

## 📦 What's Currently Working

### ✅ **Parser Module (Week 1 - COMPLETE)**

**Parse any Verilog/SystemVerilog file:**
```python
from src.parser import RTLParser

# Parse a module
parser = RTLParser('your_module.sv')
module = parser.parse()

# Access information
print(f"Module: {module.name}")
print(f"Type: {'Sequential' if module.is_sequential else 'Combinational'}")
print(f"Inputs: {len(module.inputs)}")
print(f"Clock: {module.clock_signal}")
```

**Features:**
- ✅ Extracts all signals (inputs, outputs, internals)
- ✅ Classifies sequential vs combinational
- ✅ Detects clock and reset signals
- ✅ Handles vectors and multi-bit signals
- ✅ Batch processing for multiple files
- ✅ Security-critical module identification

**Test Coverage:** 74% (19/19 tests passing)

### 🚧 **Generator Module (Week 2 - IN PROGRESS)**

- Pattern library (6 Trust-Hub patterns)
- Signal matching
- Trojan code generation
- **Being refactored in Steps 7-9**

### ⏸️ **Validator Module (Week 3 - PLANNED)**

- QuestaSim integration
- VCD comparison
- Signal analysis
- HTML reports

---

## 📚 Documentation

### **For Beginners:**
- [Quick Start Guide](docs/QUICK_START.md) - Step-by-step tutorial
- [Step-by-Step Progress Guide](docs/STEP_GUIDE.md) - What we've done so far
- [Usage Examples](examples/parser_usage.py) - Working code examples

### **For Advanced Users:**
- [Parser Architecture](docs/parser/PARSER_ARCHITECTURE.md) - Technical details
- [Trust-Hub Patterns](docs/TRUST_HUB_PATTERNS.md) - Trojan taxonomy
- [System Architecture](docs/ARCHITECTURE.md) - Overall design

---

## 🛠️ Current Capabilities

### **Command-Line Tools:**
```bash
# 1. Parse single module
python src/parser/rtl_parser.py <module.sv>

# 2. Batch parse directory
python scripts/batch_parse.py --dir <directory>

# 3. Find security-critical modules
python scripts/batch_parse.py --dir <directory> --security-only

# 4. Rank by security importance
python scripts/parse_and_rank.py <directory> --top 10

# 5. Save results to JSON
python scripts/batch_parse.py --dir <directory> --save-json

# 6. Run tests
python -m pytest tests/ -v

# 7. Check coverage
python -m pytest --cov=src/parser tests/
```

---

## 📊 Project Status

**Current Phase:** Week 1 Complete, Week 2 Starting
```
✅ Week 1: Parser Refactor (Steps 1-6) - COMPLETE
   ├── ✅ Directory structure
   ├── ✅ Python package setup
   ├── ✅ Documentation framework
   ├── ✅ Parser refactored (3 modules)
   ├── ✅ 19 unit tests (100% passing)
   └── ✅ Batch processing tools

🚧 Week 2: Generator Refactor (Steps 7-13) - IN PROGRESS
   ├── ⏸️ Pattern library split (6 files)
   ├── ⏸️ Generator split (seq/comb)
   ├── ⏸️ Trojan templates (12 files)
   └── ⏸️ Examples reorganization

⏸️ Week 3: Validator (Steps 14-19) - PLANNED

⏸️ Week 4: Polish & Release (Steps 20-30) - PLANNED
```

**Progress:** 6/30 steps (20%)

---

## 🧪 Testing
```bash
# Run all tests
python -m pytest tests/ -v

# Expected output:
# =================== 19 passed in 0.52s ===================

# Run with coverage
python -m pytest --cov=src/parser tests/

# Expected coverage:
# TOTAL: 74%
```

---

## 📁 Project Structure
```
rv-trogen/
├── src/
│   ├── parser/              ✅ COMPLETE (Week 1)
│   │   ├── rtl_parser.py    # Main parser
│   │   ├── signal_extractor.py
│   │   └── module_classifier.py
│   ├── patterns/            🚧 IN PROGRESS (Week 2)
│   ├── generator/           🚧 IN PROGRESS (Week 2)
│   └── validator/           ⏸️ PLANNED (Week 3)
├── docs/
│   ├── QUICK_START.md       ✅ Beginner guide
│   ├── STEP_GUIDE.md        ✅ Progress tracking
│   └── parser/              ✅ Technical docs
├── scripts/
│   ├── batch_parse.py       ✅ Batch processing
│   └── parse_and_rank.py    ✅ Security ranking
├── tests/
│   ├── test_parser.py       ✅ 19 tests
│   └── test_signal_extraction.py
└── examples/
    ├── parser_usage.py      ✅ Code examples
    └── ibex/original/       ✅ Test modules
```

---

## 🎯 Use Cases

### **1. Security Researcher**
Generate Trojans to test your detection tool:
```bash
python scripts/batch_parse.py --dir my_processor/rtl --security-only
python src/generator/trojan_generator.py <critical_module.sv>
```

### **2. Processor Designer**
Validate security assertions in your design:
```bash
python scripts/parse_and_rank.py my_processor/rtl --top 5
# Focus on top 5 critical modules
```

### **3. Student/Learner**
Understand hardware Trojans systematically:
```bash
# Start with parser
python src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv

# Run example code
python examples/parser_usage.py
```

---

## 🆚 Comparison with Related Work

| Feature | RV-TroGen (Ours) | TrojanForge | Trust-Hub |
|---------|------------------|-------------|-----------|
| **Level** | RTL | Gate-level | Various |
| **Approach** | Pattern-based | ML/RL | Manual |
| **Target** | RISC-V processors | Generic circuits | Benchmarks |
| **Goal** | Assertion validation | Detector evasion | Benchmark suite |
| **Automation** | High | Very High | Low |
| **Interpretability** | High | Low (black box) | High |
| **Customization** | Easy | Hard | Manual |

**Key Innovation:** First systematic RTL-level Trojan generator specifically for RISC-V processors.

---

## 📖 Learn More

- **Tutorial:** See [QUICK_START.md](docs/QUICK_START.md)
- **Progress:** See [STEP_GUIDE.md](docs/STEP_GUIDE.md)
- **Architecture:** See [docs/parser/PARSER_ARCHITECTURE.md](docs/parser/PARSER_ARCHITECTURE.md)
- **Trust-Hub Patterns:** See [TRUST_HUB_PATTERNS.md](docs/TRUST_HUB_PATTERNS.md)

---

## 🤝 Contributing

We welcome contributions!

**Current needs:**
- Testing on more RISC-V processors (CVA6, RSD)
- Additional Trust-Hub patterns
- Improved template generation
- Documentation improvements

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file

---

## 📧 Contact

- **Repository:** https://github.com/sharjeelimtiaz27/rv-trogen
- **Issues:** https://github.com/sharjeelimtiaz27/rv-trogen/issues

---

## 🙏 Acknowledgments

- [TrojanForge](https://arxiv.org/abs/2405.15184) for ML-based generation inspiration
- [Trust-Hub](https://trust-hub.org) for Trojan taxonomy
- [lowRISC Ibex](https://github.com/lowRISC/ibex) for test modules
- RISC-V community for processor specifications

---

## 📝 Citation

If you use RV-TroGen in your research:
```bibtex
@software{rv_trojangen2024,
  title = {RV-TroGen: RTL-Level Hardware Trojan Generation for RISC-V},
  author = {Sharjeel Imtiaz},
  year = {2024},
  url = {https://github.com/sharjeelimtiaz27/rv-trogen}
}
```

---



**Current Version:** 1.0.0-beta  
**Last Updated:** December 2026  
**Status:** Active Development (Week 2)