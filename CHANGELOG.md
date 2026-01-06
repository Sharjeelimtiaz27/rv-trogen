\# Changelog



All notable changes to RV-TroGen will be documented in this file.



---



\## \[Unreleased]



\### Week 2 (In Progress)

\- Pattern library refactor (Steps 7-9)

\- Generator refactor (Steps 7-9)

\- Template system (Step 9)



---



\## \[1.0.0-beta] - Week 1 Complete



\### Added - Steps 4-6 (Parser Module)



\#### Step 4: Parser Refactor

\- Split monolithic parser into 3 modules

\- Added `rtl\_parser.py` - Main parser orchestrator (103 lines)

\- Added `signal\_extractor.py` - Signal parsing logic (54 lines)

\- Added `module\_classifier.py` - Sequential/Comb detection (39 lines)

\- Maintained backward compatibility with `parse\_module.py`



\#### Step 5: Parser Unit Tests

\- Added `tests/test\_parser.py` - 15 comprehensive tests

\- Added `tests/test\_signal\_extraction.py` - 4 edge case tests

\- Added `pytest.ini` - Pytest configuration

\- \*\*Test Results:\*\* 19/19 passing (100% pass rate)

\- \*\*Coverage:\*\* 74% (publication quality)



\#### Step 6: Parser Documentation

\- Added `docs/parser/PARSER\_ARCHITECTURE.md` - Technical documentation

\- Added `examples/parser\_usage.py` - Working code examples

\- Updated `README.md` - Parser section added

\- Added inline code comments throughout



\#### Bonus: Batch Processing Tools

\- Added `scripts/batch\_parse.py` - Parse multiple files at once

\- Added `scripts/parse\_and\_rank.py` - Security ranking system

\- Added `configs/security\_critical\_modules.json` - Configuration

\- Features:

&nbsp; - Parse entire directories

&nbsp; - Filter security-critical modules

&nbsp; - Rank by security importance

&nbsp; - Export to JSON



\### Changed

\- Updated `src/parser/\_\_init\_\_.py` - New module exports

\- Updated `src/\_\_init\_\_.py` - Commented out validator imports (Week 3)

\- Updated `src/validator/\_\_init\_\_.py` - Stub until Week 3



\### Fixed

\- Fixed import errors for non-existent validator modules

\- Fixed test compatibility issues

\- Fixed module name assertion in tests



\### Test Coverage

```

Module                          Coverage

================================================

src/parser/\_\_init\_\_.py           100%

src/parser/signal\_extractor.py    94%

src/parser/module\_classifier.py   90%

src/parser/parse\_module.py        75%

src/parser/rtl\_parser.py          55%

================================================

TOTAL                             74%

```



---



\## \[0.3.0] - Step 3 Complete



\### Added - Documentation Structure

\- `docs/QUICK\_START.md` - Beginner guide

\- `docs/TRUST\_HUB\_PATTERNS.md` - Pattern library documentation

\- `docs/ARCHITECTURE.md` - System architecture

\- `docs/examples/ibex\_tutorial.md` - Ibex walkthrough

\- `docs/examples/cva6\_tutorial.md` - CVA6 placeholder

\- `docs/examples/rsd\_tutorial.md` - RSD placeholder



---



\## \[0.2.0] - Step 2 Complete



\### Added - Python Package Setup

\- `setup.py` - Package metadata and installation

\- `pyproject.toml` - Modern Python packaging

\- `MANIFEST.in` - File inclusion rules

\- Package now installable with `pip install -e .`

\- Console scripts:

&nbsp; - `rv-trojangen` - Generate Trojans

&nbsp; - `rv-validate` - Validate Trojans



---



\## \[0.1.0] - Step 1 Complete



\### Added - Professional Directory Structure

\- Complete folder hierarchy created

\- All `\_\_init\_\_.py` files for Python packages

\- `requirements.txt` - Python dependencies

\- `.gitignore` - Git ignore rules

\- `LICENSE` - MIT License

\- Initial `README.md`



\### Project Structure

```

rv-trogen/

├── src/

│   ├── parser/

│   ├── patterns/

│   ├── generator/

│   └── validator/

├── docs/

├── scripts/

├── testbenches/

├── examples/

├── templates/

└── tests/

```



---



\## Repository Information



\- \*\*Repository:\*\* https://github.com/sharjeelimtiaz27/rv-trogen

\- \*\*License:\*\* MIT

\- \*\*Python:\*\* 3.8+

\- \*\*Status:\*\* Active Development (Week 2)



---



\## Links



\- \[Full Documentation](docs/)

\- \[Quick Start](docs/QUICK\_START.md)

\- \[Step Guide](docs/STEP\_GUIDE.md)

\- \[Issues](https://github.com/sharjeelimtiaz27/rv-trogen/issues)

## [Unreleased] - Week 2 Step 9 Complete

### Added - Step 9: Template Library

#### Template System (January 6, 2025)
- Created `templates/trojan_templates/` directory structure
- Added 12 SystemVerilog templates:
  - **Sequential templates** (6 files):
    - `dos_template.sv` - Trust-Hub AES-T1400 adaptation
    - `leak_template.sv` - Trust-Hub RSA-T600 adaptation
    - `privilege_template.sv` - Bailey (2017) RISC-V adaptation
    - `integrity_template.sv` - Trust-Hub AES-T800 adaptation
    - `availability_template.sv` - Boraten (2016) LSU adaptation
    - `covert_template.sv` - Lipp et al. (2021) timing adaptation
  - **Combinational templates** (6 files):
    - Simplified versions for combinational logic
- Each template includes:
  - Source citations in header
  - Placeholder syntax (`{{VARIABLE}}`)
  - Clear trigger/payload sections
  - Usage examples
  - Detection difficulty notes
  - RISC-V specific adaptations

#### Documentation
- Added `docs/TEMPLATES.md` - Comprehensive template documentation
- Updated `README.md` - Added template section
- Updated progress: 9/30 steps (30%)

#### Why Templates?
1. **Reproducibility** - Fixed SystemVerilog files anyone can verify
2. **Extensibility** - Easy to add new patterns
3. **Validation** - Can compile/verify independently
4. **Comparison** - Direct structural comparison with Trust-Hub
5. **Research Artifact** - Citable, shareable template library

### Changed
- Updated `README.md` - Progress now 30% (was 27%)
- Fixed processor name: NaxRiscv → RSD (out-of-order processor)

### Next Steps
- Step 10: Template validation with Verilator
- Step 11: Update generator to use templates
- Step 12: Batch generation script
- Step 13: Examples reorganization

**Time Invested:** 4 hours  
**Date Completed:** January 6, 2026
