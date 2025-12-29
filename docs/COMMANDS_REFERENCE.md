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
python -m src/parser/rtl_parser.py <file.sv>

# Example
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv
```

### Batch Parsing
```bash
# Parse entire directory
python -m scripts/batch_parse.py --dir <directory>

# Parse with specific pattern
python -m scripts/batch_parse.py --dir <directory> --pattern "*.v"

# Security-critical modules only
python -m scripts/batch_parse.py --dir <directory> --security-only

# Save to JSON
python -m scripts/batch_parse.py --dir <directory> --save-json

# Custom output directory
python -m scripts/batch_parse.py --dir <directory> --output-dir results
```

### Security Ranking
```bash
# Rank all modules
python -m scripts/parse_and_rank.py <directory>

# Show top N modules
python -m scripts/parse_and_rank.py <directory> --top 5

# Minimum score threshold
python -m scripts/parse_and_rank.py <directory> --min-score 10
```

---

## Generator Commands ⭐ NEW!

### Single Module Trojan Generation
```bash
# Generate Trojans for one module (recommended)
python scripts/generate_trojans.py <file.sv>

# Alternative: Direct module method
python -m src.generator.trojan_generator <file.sv> --output <output_dir>

# Examples
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_pmp.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_controller.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_alu.sv
```

### Output Organization
```bash
# Default output structure (automatic):
# Input:  examples/ibex/original/ibex_cs_registers.sv
# Output: examples/ibex/generated_trojans/ibex_cs_registers/
#   ├── T1_ibex_cs_registers_DoS.sv
#   ├── T2_ibex_cs_registers_Leak.sv
#   ├── T3_ibex_cs_registers_Privilege.sv
#   ├── T4_ibex_cs_registers_Integrity.sv
#   ├── T5_ibex_cs_registers_Availability.sv
#   ├── T6_ibex_cs_registers_Covert.sv
#   └── ibex_cs_registers_trojan_summary.md
```

### View Generated Files
```bash
# Windows
dir examples\ibex\generated_trojans\ibex_cs_registers

# Linux/Mac
ls -la examples/ibex/generated_trojans/ibex_cs_registers/

# View summary report
cat examples/ibex/generated_trojans/ibex_cs_registers/ibex_cs_registers_trojan_summary.md

# View a specific Trojan
cat examples/ibex/generated_trojans/ibex_cs_registers/T1_ibex_cs_registers_DoS.sv
```

### Batch Generation (Coming Soon - Step 11)
```bash
# Generate for all modules in directory
python scripts/batch_generate.py --dir examples/ibex/original

# Generate for security-critical modules only
python scripts/batch_generate.py --dir examples/ibex/original --security-only

# Generate with specific patterns only
python scripts/batch_generate.py --dir examples/ibex/original --patterns dos,leak
```

---

## Testing Commands
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest --cov=src/parser tests/

# Run specific test file
python -m pytest tests/test_parser.py -v

# Run specific test
python -m pytest tests/test_parser.py::TestRTLParser::test_parse_simple_module -v

# Stop on first failure
python -m pytest tests/ -x

# Show detailed output
python -m pytest tests/ -vv

# Generate coverage HTML report
python -m pytest --cov=src/parser --cov-report=html tests/
```

---

## Python Usage

### Basic Parsing
```python
from src.parser import RTLParser

# Parse a file
parser = RTLParser('module.sv')
module = parser.parse()

# Access information
print(f"Name: {module.name}")
print(f"Type: {module.is_sequential}")
print(f"Inputs: {len(module.inputs)}")
```

### Signal Extraction
```python
from src.parser import SignalExtractor

# Extract signals
with open('module.sv') as f:
    content = f.read()

extractor = SignalExtractor(content)
inputs = extractor.extract_inputs()
outputs = extractor.extract_outputs()
internals = extractor.extract_internals()
```

### Module Classification
```python
from src.parser import ModuleClassifier

classifier = ModuleClassifier(content, all_signals)

if classifier.is_sequential():
    print(f"Clock: {classifier.get_clock_signal()}")
    print(f"Reset: {classifier.get_reset_signal()}")
```

### Trojan Generation ⭐ NEW!
```python
from src.generator.trojan_generator import TrojanGenerator
from pathlib import Path

# Generate Trojans for a module
input_file = Path('examples/ibex/original/ibex_cs_registers.sv')
output_dir = Path('examples/ibex/generated_trojans/ibex_cs_registers')

generator = TrojanGenerator(input_file, output_dir)
trojans = generator.generate_all()

# Access generated Trojans
for trojan in trojans:
    print(f"Generated: {trojan.output_path}")
    print(f"Type: {trojan.trojan_type}")
    print(f"Confidence: {trojan.confidence}")
```

### Pattern Matching
```python
from src.patterns.pattern_library import PatternLibrary
from src.parser import RTLParser

# Parse module
parser = RTLParser('module.sv')
module = parser.parse()

# Match all patterns
library = PatternLibrary()
matches = library.match_all_patterns(module)

for pattern_name, match in matches.items():
    if match.matched:
        print(f"{pattern_name}: {match.confidence:.2f}")
        print(f"  Signals: {match.matched_signals}")
```

### Sequential/Combinational Generation
```python
from src.generator.sequential_gen import SequentialGenerator
from src.generator.combinational_gen import CombinationalGenerator

# For sequential modules
seq_gen = SequentialGenerator(module)
trojan_code = seq_gen.generate_dos_trojan(trigger_signal, payload_signal)

# For combinational modules
comb_gen = CombinationalGenerator(module)
trojan_code = comb_gen.generate_leak_trojan(data_signal, leak_signal)
```

### Batch Processing
```python
from scripts.batch_parse import BatchParser

# Parse directory
batch = BatchParser()
modules = batch.parse_directory('examples/ibex/original')

# Filter security-critical
security_modules = batch.filter_security_critical(modules)

# Generate summary
batch.print_summary()
batch.save_summary_json('results.json')
```

---

## Git Commands
```bash
# Check status
git status

# Add all changes
git add .

# Add specific files
git add src/parser/rtl_parser.py

# Commit
git commit -m "Description of changes"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline
```

---

## Package Management
```bash
# Install in editable mode
python -m pip install -e .

# Install with dev dependencies
python -m pip install -e ".[dev]"

# Install with docs dependencies
python -m pip install -e ".[docs]"

# Update dependencies
python -m pip install -r requirements.txt --upgrade

# List installed packages
pip list

# Uninstall
pip uninstall rv-trojangen
```

---

## Development Commands
```bash
# Format code with black
black src/ tests/ scripts/

# Check code style
flake8 src/ tests/ scripts/

# Run all checks
black src/ && flake8 src/ && pytest tests/
```

---

## Documentation Commands
```bash
# View documentation
start docs/QUICK_START.md          # Windows
open docs/QUICK_START.md           # macOS
xdg-open docs/QUICK_START.md       # Linux

# Generate HTML docs (if Sphinx installed)
cd docs
make html
```

---

## Troubleshooting Commands
```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check installed packages
pip show rv-trojangen

# Reinstall package
pip uninstall rv-trojangen
python -m pip install -e .

# Clear pytest cache
python -m pytest --cache-clear

# Verbose test output
python -m pytest tests/ -vv --tb=long
```

---

## Quick Examples

### Example 1: Parse and Display
```bash
python -m src/parser/rtl_parser.py examples/ibex/original/ibex_cs_registers.sv
```

### Example 2: Batch Parse
```bash
python -m scripts/batch_parse.py --dir examples/ibex/original
```

### Example 3: Find Critical Modules
```bash
python -m scripts/batch_parse.py --dir examples/ibex/original --security-only
```

### Example 4: Rank Modules
```bash
python -m scripts/parse_and_rank.py examples/ibex/original --top 5
```

### Example 5: Export to JSON
```bash
python -m scripts/batch_parse.py --dir examples/ibex/original --save-json
cat parsed_results/parse_summary.json
```

### Example 6: Generate Trojans ⭐ NEW!
```bash
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

### Example 7: View Generated Trojans
```bash
# Windows
dir examples\ibex\generated_trojans\ibex_cs_registers

# Linux/Mac
ls examples/ibex/generated_trojans/ibex_cs_registers/

# Read summary
cat examples/ibex/generated_trojans/ibex_cs_registers/ibex_cs_registers_trojan_summary.md
```

### Example 8: Run Tests
```bash
python -m pytest tests/ -v
```

---

## Complete Workflow Example

### End-to-End: Parse → Rank → Generate
```bash
# Step 1: Parse all modules
python -m scripts/batch_parse.py --dir examples/ibex/original

# Step 2: Find most critical modules
python -m scripts/parse_and_rank.py examples/ibex/original --top 3

# Output shows:
# 1. ibex_cs_registers (score: 45)
# 2. ibex_pmp (score: 38)
# 3. ibex_controller (score: 32)

# Step 3: Generate Trojans for top module
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Step 4: View results
dir examples\ibex\generated_trojans\ibex_cs_registers  # Windows
ls examples/ibex/generated_trojans/ibex_cs_registers/  # Linux/Mac

# You should see:
# - T1_ibex_cs_registers_DoS.sv
# - T2_ibex_cs_registers_Leak.sv
# - T3_ibex_cs_registers_Privilege.sv
# - T4_ibex_cs_registers_Integrity.sv
# - T5_ibex_cs_registers_Availability.sv
# - T6_ibex_cs_registers_Covert.sv
# - ibex_cs_registers_trojan_summary.md

# Step 5: Verify everything works
python -m pytest tests/ -v
```

### Research Workflow: Multiple Modules
```bash
# Generate Trojans for multiple critical modules
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_pmp.sv
python scripts/generate_trojans.py examples/ibex/original/ibex_controller.sv

# View all generated Trojans
dir examples\ibex\generated_trojans  # Windows
ls examples/ibex/generated_trojans/  # Linux/Mac

# You should see:
# ibex_cs_registers/
# ibex_pmp/
# ibex_controller/
```

---

## Environment Setup

### Windows
```cmd
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install
python -m pip install -e .
```

### Linux/macOS
```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Install
python -m pip install -e .
```

---

## Common Issues and Solutions

### Issue: "No Trojans generated"
```bash
# Solution: Check if module is sequential
python -m src/parser/rtl_parser.py <module.sv>

# Look for:
# Has Clock: True
# Has Reset: True
# Type: Sequential

# Note: Combinational modules have fewer patterns available
```

### Issue: "Pattern matching failed"
```bash
# Solution: Module may not have security-critical signals
# Check the pattern matching output for details
# Some modules (like simple ALU) may not match security patterns
```

### Issue: "Output directory error"
```bash
# Solution: Script auto-creates directories
# If error persists, manually create:
mkdir -p examples/ibex/generated_trojans  # Linux/Mac
mkdir examples\ibex\generated_trojans     # Windows
```

---

**For more details, see:**
- [Quick Start Guide](QUICK_START.md)
- [Step Guide](STEP_GUIDE.md)
- [Parser Architecture](parser/PARSER_ARCHITECTURE.md)
- [Trust-Hub Patterns](TRUST_HUB_PATTERNS.md)