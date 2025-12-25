\# Command Reference



Quick reference for all RV-TroGen commands.



---



\## Installation Commands

```bash

\# Clone repository

git clone https://github.com/sharjeelimtiaz27/rv-trogen.git

cd rv-trogen



\# Install package

python -m pip install -e .



\# Verify installation

python -c "from src.parser import RTLParser; print('✅ OK')"

```



---



\## Parser Commands



\### Single Module Parsing

```bash

\# Parse one module

python -m src/parser/rtl\_parser.py <file.sv>



\# Example

python -m src/parser/rtl\_parser.py examples/ibex/original/ibex\_cs\_registers.sv

```



\### Batch Parsing

```bash

\# Parse entire directory

python -m scripts/batch\_parse.py --dir <directory>



\# Parse with specific pattern

python -m scripts/batch\_parse.py --dir <directory> --pattern "\*.v"



\# Security-critical modules only

python -m scripts/batch\_parse.py --dir <directory> --security-only



\# Save to JSON

python -m scripts/batch\_parse.py --dir <directory> --save-json



\# Custom output directory

python -m scripts/batch\_parse.py --dir <directory> --output-dir results

```



\### Security Ranking

```bash

\# Rank all modules

python -m scripts/parse\_and\_rank.py <directory>



\# Show top N modules

python -m scripts/parse\_and\_rank.py <directory> --top 5



\# Minimum score threshold

python -m scripts/parse\_and\_rank.py <directory> --min-score 10

```



---



\## Testing Commands

```bash

\# Run all tests

python -m pytest tests/ -v



\# Run with coverage

python -m pytest --cov=src/parser tests/



\# Run specific test file

python -m pytest tests/test\_parser.py -v



\# Run specific test

python -m pytest tests/test\_parser.py::TestRTLParser::test\_parse\_simple\_module -v



\# Stop on first failure

python -m pytest tests/ -x



\# Show detailed output

python -m pytest tests/ -vv



\# Generate coverage HTML report

python -m pytest --cov=src/parser --cov-report=html tests/

```



---



\## Python Usage



\### Basic Parsing

```python

from src.parser import RTLParser



\# Parse a file

parser = RTLParser('module.sv')

module = parser.parse()



\# Access information

print(f"Name: {module.name}")

print(f"Type: {module.is\_sequential}")

print(f"Inputs: {len(module.inputs)}")

```



\### Signal Extraction

```python

from src.parser import SignalExtractor



\# Extract signals

with open('module.sv') as f:

&nbsp;   content = f.read()



extractor = SignalExtractor(content)

inputs = extractor.extract\_inputs()

outputs = extractor.extract\_outputs()

internals = extractor.extract\_internals()

```



\### Module Classification

```python

from src.parser import ModuleClassifier



classifier = ModuleClassifier(content, all\_signals)



if classifier.is\_sequential():

&nbsp;   print(f"Clock: {classifier.get\_clock\_signal()}")

&nbsp;   print(f"Reset: {classifier.get\_reset\_signal()}")

```



\### Batch Processing

```python

from scripts.batch\_parse import BatchParser



\# Parse directory

batch = BatchParser()

modules = batch.parse\_directory('examples/ibex/original')



\# Filter security-critical

security\_modules = batch.filter\_security\_critical(modules)



\# Generate summary

batch.print\_summary()

batch.save\_summary\_json('results.json')

```



---



\## Git Commands

```bash

\# Check status

git status



\# Add all changes

git add .



\# Add specific files

git add src/parser/rtl\_parser.py



\# Commit

git commit -m "Description of changes"



\# Push to GitHub

git push origin main



\# Pull latest changes

git pull origin main



\# View commit history

git log --oneline

```



---



\## Package Management

```bash

\# Install in editable mode

pythom -m pip install -e .



\# Install with dev dependencies

pythom -m pip install -e ".\[dev]"



\# Install with docs dependencies

pythom -m pip install -e ".\[docs]"



\# Update dependencies

pythom -m pip install -r requirements.txt --upgrade



\# List installed packages

pip list



\# Uninstall

pip uninstall rv-trojangen

```



---



\## Development Commands

```bash

\# Format code with black

black src/ tests/ scripts/



\# Check code style

flake8 src/ tests/ scripts/



\# Run all checks

black src/ \&\& flake8 src/ \&\& pytest tests/

```



---



\## Documentation Commands

```bash

\# View documentation

start docs/QUICK\_START.md          # Windows

open docs/QUICK\_START.md           # macOS

xdg-open docs/QUICK\_START.md       # Linux



\# Generate HTML docs (if Sphinx installed)

cd docs

make html

```



---



\## Troubleshooting Commands

```bash

\# Check Python version

python --version



\# Check pip version

pip --version



\# Check installed packages

pip show rv-trojangen



\# Reinstall package

pip uninstall rv-trojangen

pythom -m pip install -e .



\# Clear pytest cache

python -m pytest --cache-clear



\# Verbose test output

python -m pytest tests/ -vv --tb=long

```



---



\## Quick Examples



\### Example 1: Parse and Display

```bash

python src/parser/rtl\_parser.py examples/ibex/original/ibex\_cs\_registers.sv

```



\### Example 2: Batch Parse

```bash

python scripts/batch\_parse.py --dir examples/ibex/original

```



\### Example 3: Find Critical Modules

```bash

python scripts/batch\_parse.py --dir examples/ibex/original --security-only

```



\### Example 4: Rank Modules

```bash

python scripts/parse\_and\_rank.py examples/ibex/original --top 5

```



\### Example 5: Export to JSON

```bash

python scripts/batch\_parse.py --dir examples/ibex/original --save-json

cat parsed\_results/parse\_summary.json

```



\### Example 6: Run Tests

```bash

python -m pytest tests/ -v

```



---



\## Environment Setup



\### Windows

```cmd

\# Create virtual environment

python -m venv venv



\# Activate

venv\\Scripts\\activate



\# Install

pythom -m pip install -e .

```



\### Linux/macOS

```bash

\# Create virtual environment

python3 -m venv venv



\# Activate

source venv/bin/activate



\# Install

pythom -m pip install -e .

```



---



\*\*For more details, see:\*\*

\- \[Quick Start Guide](QUICK\_START.md)

\- \[Step Guide](STEP\_GUIDE.md)

\- \[Parser Architecture](parser/PARSER\_ARCHITECTURE.md)

