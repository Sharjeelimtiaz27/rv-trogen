# RV-TroGen Development Step Guide

**30-Step Development Plan Tracking Document**

This document tracks progress through the complete 30-step development plan for RV-TroGen, organized into 5 weeks.

**Current Status:** 10/30 steps complete (33%)

---

## 📊 Progress Overview
```
✅ Week 1: Parser Implementation (Steps 1-6)       - COMPLETE
✅ Week 2: Generator & Templates (Steps 7-10)      - COMPLETE
⏸️ Week 2: Template Integration (Steps 11-13)      - IN PROGRESS
⏸️ Week 3: Validation Framework (Steps 14-19)     - PLANNED
⏸️ Week 4-5: Polish & Release (Steps 20-30)        - PLANNED
```

---

## Week 1: Parser & Foundation (Steps 1-6)

### ✅ Step 1: Directory Structure (COMPLETE)

**Date Completed:** December 2024

**Goal:** Create professional directory structure

**What We Built:**
```
rv-trogen/
├── src/
│   ├── parser/
│   ├── patterns/
│   ├── generator/
│   └── validator/
├── docs/
├── scripts/
├── templates/
├── tests/
└── examples/
```

**Deliverables:**
- ✅ Complete folder hierarchy
- ✅ All `__init__.py` files for Python packages
- ✅ `.gitignore` with Python rules
- ✅ `requirements.txt` with dependencies

**Time Spent:** 30 minutes

---

### ✅ Step 2: Python Package Setup (COMPLETE)

**Date Completed:** December 2024

**Goal:** Make RV-TroGen installable as a Python package

**What We Built:**
- `setup.py` - Package metadata and installation
- `pyproject.toml` - Modern Python packaging
- `MANIFEST.in` - File inclusion rules

**Installation:**
```bash
python -m pip install -e .
```

**Console Scripts:**
- `rv-trojangen` - Generate Trojans
- `rv-validate` - Validate Trojans

**Deliverables:**
- ✅ Package installable with pip
- ✅ Console entry points configured
- ✅ Dependencies specified

**Time Spent:** 1 hour

---

### ✅ Step 3: Documentation Framework (COMPLETE)

**Date Completed:** December 2024

**Goal:** Create comprehensive documentation structure

**What We Built:**
- `docs/QUICK_START.md` - Beginner guide
- `docs/TRUST_HUB_PATTERNS.md` - Pattern library documentation
- `docs/ARCHITECTURE.md` - System architecture
- `docs/COMMANDS_REFERENCE.md` - CLI reference

**Deliverables:**
- ✅ Documentation structure
- ✅ Quick start tutorial
- ✅ Pattern library documented
- ✅ Architecture overview

**Time Spent:** 2 hours

---

### ✅ Step 4: Parser Refactor (COMPLETE)

**Date Completed:** December 2024

**Goal:** Split monolithic parser into clean modules

**What We Built:**
- `src/parser/rtl_parser.py` - Main parser orchestrator (103 lines)
- `src/parser/signal_extractor.py` - Signal parsing logic (54 lines)
- `src/parser/module_classifier.py` - Sequential/Comb detection (39 lines)

**Key Features:**
- Clean separation of concerns
- Maintained backward compatibility
- Dataclass-based module representation
- Clock/reset signal detection

**Deliverables:**
- ✅ Parser split into 3 modules
- ✅ Backward compatible with old code
- ✅ Improved code organization

**Time Spent:** 3 hours

---

### ✅ Step 5: Parser Unit Tests (COMPLETE)

**Date Completed:** December 2024

**Goal:** Comprehensive test coverage for parser

**What We Built:**
- `tests/test_parser.py` - 15 comprehensive tests
- `tests/test_signal_extraction.py` - 4 edge case tests
- `pytest.ini` - Pytest configuration

**Test Results:**
```
Total Tests: 19
Passing: 19 (100%)
Coverage: 74%
```

**Test Coverage:**
- Signal extraction (all types)
- Module classification (sequential/combinational)
- Clock/reset detection
- Edge cases (empty modules, complex signals)

**Deliverables:**
- ✅ 19 tests all passing
- ✅ 74% code coverage
- ✅ Publication-quality testing

**Time Spent:** 2 hours

---

### ✅ Step 6: Parser Documentation (COMPLETE)

**Date Completed:** December 2024

**Goal:** Document parser architecture and usage

**What We Built:**
- `docs/parser/PARSER_ARCHITECTURE.md` - Technical documentation
- `examples/parser_usage.py` - Working code examples
- Updated `README.md` with parser section
- Inline code comments throughout

**Deliverables:**
- ✅ Architecture documented
- ✅ Usage examples provided
- ✅ README updated
- ✅ Code well-commented

**Time Spent:** 2 hours

---

### 🎉 Week 1 Summary

**Total Time:** ~10 hours  
**Tests Passing:** 19/19 (100%)  
**Coverage:** 74%  
**Files Created:** 20+  
**Lines of Code:** ~1000

**Key Achievements:**
- Professional project structure
- Installable Python package
- Modular parser implementation
- Comprehensive testing
- Complete documentation

---

## Week 2: Generator, Patterns & Templates (Steps 7-10)

### ✅ Step 7: Pattern Library Refactor (COMPLETE)

**Date Completed:** January 2026

**Goal:** Split pattern library into individual modules

**What We Built:**
- `src/patterns/dos_pattern.py` - Denial of Service
- `src/patterns/leak_pattern.py` - Information Leakage
- `src/patterns/privilege_pattern.py` - Privilege Escalation (Novel)
- `src/patterns/integrity_pattern.py` - Data Integrity Violation
- `src/patterns/availability_pattern.py` - Performance Degradation
- `src/patterns/covert_pattern.py` - Covert Channel

**Pattern Structure (Dataclass):**
```python
@dataclass
class Pattern:
    name: str
    category: str
    trust_hub_source: str
    severity: str
    description: str
    trigger_keywords: List[str]
    payload_keywords: List[str]
    preferred_module_type: str
```

**Deliverables:**
- ✅ 6 pattern modules created
- ✅ Trust-Hub sources cited
- ✅ Keyword lists populated
- ✅ Pattern library aggregator

**Time Spent:** 3 hours

---

### ✅ Step 8: Generator Refactor (COMPLETE)

**Date Completed:** January 2026

**Goal:** Split generator into sequential and combinational

**What We Built:**
- `src/generator/trojan_generator.py` - Main orchestrator
- `src/generator/sequential_gen.py` - Sequential Trojan generation
- `src/generator/combinational_gen.py` - Combinational Trojan generation
- `scripts/generate_trojans.py` - Command-line wrapper

**Key Features:**
- Smart output organization
- Pattern-based generation
- Trojan summary reports
- Automatic directory creation

**Deliverables:**
- ✅ Generator split into 3 modules
- ✅ CLI wrapper script
- ✅ Output organization
- ✅ Summary generation

**Time Spent:** 3 hours

---

### ✅ Step 9: Template Library (COMPLETE)

**Date Completed:** January 6, 2026

**Goal:** Create SystemVerilog templates for all Trojan patterns

**What We Built:**
- Created `templates/trojan_templates/` directory
- **12 SystemVerilog templates:**
  - **Sequential (6):** dos, leak, privilege, integrity, availability, covert
  - **Combinational (6):** dos, leak, privilege, integrity, availability, covert

**Template Structure:**
```systemverilog
module {{MODULE_NAME}}_trojan (
    input logic {{CLOCK_SIGNAL}},
    input logic {{TRIGGER_SIGNAL}},
    output logic {{PAYLOAD_SIGNAL}}
);
    // Trojan trigger logic
    // Trojan payload logic
endmodule
```

**Template Features:**
- ✅ Placeholder syntax (`{{VARIABLE}}`)
- ✅ Source citations in headers
- ✅ Clear trigger/payload sections
- ✅ Usage examples
- ✅ Detection difficulty notes
- ✅ RISC-V adaptations documented

**Trust-Hub Mapping:**
| Template | Trust-Hub Source | Novel Adaptation |
|----------|------------------|------------------|
| dos_template.sv | AES-T1400 | ✅ RISC-V control signals |
| leak_template.sv | RSA-T600 | ✅ CSR leakage |
| privilege_template.sv | Bailey (2017) | ⭐ Novel - RISC-V M/S/U modes |
| integrity_template.sv | AES-T800 | ✅ ALU corruption |
| availability_template.sv | Boraten (2016) | ⭐ Novel - LSU stalling |
| covert_template.sv | Lipp et al. (2021) | ⭐ Novel - Timing channel |

**Why Templates Matter:**
1. **Reproducibility** - Fixed .sv files anyone can verify
2. **Extensibility** - Easy to add new patterns
3. **Validation** - Can compile/verify independently
4. **Comparison** - Direct structural comparison with Trust-Hub
5. **Research Artifact** - Citable, shareable template library

**Documentation Created:**
- `docs/TEMPLATES.md` - Comprehensive template documentation
- `templates/README.md` - Template library overview
- Updated `README.md` with template section

**Deliverables:**
- ✅ 12 template files created
- ✅ All templates have source citations
- ✅ Placeholder syntax standardized
- ✅ Documentation complete

**Time Spent:** 4 hours

---

### ✅ Step 10: Generator Unit Tests (COMPLETE)

**Date Completed:** January 6, 2026

**Goal:** Create comprehensive tests for generator and patterns

**What We Built:**
- `tests/test_generator.py` - 20 comprehensive tests

**Test Classes:**
```
├── TestPatternLibrary       - 3 tests   ✅
├── TestPatternAttributes    - 6 tests   ✅ (one per pattern)
├── TestPatternMethods       - 2 tests   ✅
├── TestSequentialGenerator  - 2 tests   ✅
├── TestCombinationalGen     - 2 tests   ✅
├── TestEdgeCases            - 2 tests   ✅
└── TestRealIbexModule       - 3 tests   ✅
```

**Test Results:**
```
Total Tests: 20
Passing: 20 (100%)
Time: 0.26 seconds
```

**What We Tested:**

1. **Pattern Library:**
   - Initialization
   - Getting all 6 patterns
   - Getting patterns by name

2. **Pattern Attributes (All 6):**
   - Correct name, category, severity
   - Trust-Hub sources present
   - Trigger/payload keywords non-empty
   - Pattern-specific keywords verified

3. **Pattern Methods:**
   - `get_info()` returns dictionary
   - `get_template_params()` returns parameters

4. **Generators:**
   - Sequential generator initialization
   - Combinational generator initialization
   - Required methods present

5. **Edge Cases:**
   - Empty modules handled
   - Simple modules handled
   - No crashes on edge cases

6. **Real Ibex Module:**
   - Parses ibex_cs_registers.sv
   - Can create generator
   - Patterns have relevant keywords

**Key Insights:**
- Patterns are dataclasses with keyword lists
- Generators receive module in `__init__()`
- Pattern matching happens in generator (not pattern classes)
- All patterns properly configured with Trust-Hub sources

**Deliverables:**
- ✅ 20 tests all passing
- ✅ 100% pass rate
- ✅ Patterns validated
- ✅ Generators validated
- ✅ Edge cases covered

**Time Spent:** 1.5 hours

---

### 🎉 Week 2 (Steps 7-10) Summary

**Total Time:** ~11.5 hours  
**Tests Passing:** 39/39 (Parser: 19, Generator: 20)  
**Files Created:** 
- 6 pattern modules
- 3 generator modules
- 12 template files
- 1 test file (20 tests)
- 2 documentation files

**Key Achievements:**
- Pattern library modularized
- Generator refactored
- Template library created (research artifact!)
- Comprehensive testing
- Template documentation

---

## Week 2: Template Integration (Steps 11-13)

### ⏸️ Step 11: Update Generator to Use Templates (IN PROGRESS)

**Goal:** Integrate template library with generator

**What to Do:**
- Modify generators to load templates
- Implement placeholder replacement
- Test template-based generation
- Compare with old generation

**Deliverables:**
- [ ] Template loading in generators
- [ ] Placeholder replacement system
- [ ] Generated code uses templates
- [ ] Tests updated

**Estimated Time:** 3 hours

---

### ⏸️ Step 12: Batch Generation Script (PLANNED)

**Goal:** Generate Trojans for multiple modules at once

**What to Do:**
- Create `scripts/batch_generate.py`
- Process entire directories
- Organize outputs
- Summary reports

**Deliverables:**
- [ ] Batch generation script
- [ ] Progress indicators
- [ ] Error handling
- [ ] Summary reports

**Estimated Time:** 2 hours

---

### ⏸️ Step 13: Examples Reorganization (PLANNED)

**Goal:** Create comprehensive examples

**What to Do:**
- Generate Trojans for all Ibex modules
- Create example documentation
- Add usage tutorials
- Organize generated outputs

**Deliverables:**
- [ ] Ibex examples complete
- [ ] Example documentation
- [ ] Usage tutorials

**Estimated Time:** 2 hours

---

## Week 3: Validation Framework (Steps 14-19)

### ⏸️ Step 14: Simulation Setup (PLANNED)

**Goal:** QuestaSim/Verilator integration

**Estimated Time:** 3 hours

---

### ⏸️ Step 15: Signal Comparison (PLANNED)

**Goal:** Compare original vs Trojan behavior

**Estimated Time:** 3 hours

---

### ⏸️ Step 16: VCD Analysis (PLANNED)

**Goal:** Waveform analysis and comparison

**Estimated Time:** 2 hours

---

### ⏸️ Step 17: Validation Tests (PLANNED)

**Goal:** Unit tests for validator

**Estimated Time:** 2 hours

---

### ⏸️ Step 18: HTML Reports (PLANNED)

**Goal:** Generate validation reports

**Estimated Time:** 2 hours

---

### ⏸️ Step 19: Validation Documentation (PLANNED)

**Goal:** Document validation process

**Estimated Time:** 2 hours

---

## Week 4: Polish & Examples (Steps 20-25)

### ⏸️ Step 20-25: TBD (PLANNED)

**Topics:**
- CVA6 support
- RSD support
- Performance benchmarks
- Detection difficulty analysis
- Advanced examples

**Estimated Time:** 15 hours

---

## Week 5: Release (Steps 26-30)

### ⏸️ Step 26-30: TBD (PLANNED)

**Topics:**
- CI/CD setup
- GitHub Actions
- README polish
- Release preparation
- Paper writing support

**Estimated Time:** 10 hours

---

## 📊 Overall Progress
```
✅ Completed: 10/30 steps (33%)
⏸️ In Progress: Steps 11-13
⏸️ Planned: Steps 14-30

Week 1: ████████████████████ 100% (6/6 steps)
Week 2: ██████████░░░░░░░░░░  57% (4/7 steps)
Week 3: ░░░░░░░░░░░░░░░░░░░░   0% (0/6 steps)
Week 4: ░░░░░░░░░░░░░░░░░░░░   0% (0/6 steps)
Week 5: ░░░░░░░░░░░░░░░░░░░░   0% (0/5 steps)
```

---

## 📈 Metrics

**Code:**
- Python files: 25+
- SystemVerilog templates: 12
- Total lines of code: ~3000

**Testing:**
- Total tests: 39
- Pass rate: 100%
- Coverage: 70%+

**Documentation:**
- Markdown files: 10+
- README: Comprehensive
- Quick start: Complete
- API docs: In progress

---

## 🎯 Next Milestone

**Current Focus:** Step 11 - Template Integration

**Immediate Goal:** Get generators using template library

**ETA:** January 7, 2026

---

## 📝 Notes

**Key Decisions:**
- Chose template-based over pure programmatic generation
- 12 templates (6 seq + 6 comb) for completeness
- Dataclass-based patterns for simplicity
- Generator does matching, patterns provide keywords

**Challenges Overcome:**
- Parser test compatibility
- Generator API design
- Template structure design
- Test strategy for new architecture

**Lessons Learned:**
- Start with tests to understand API
- Templates add value for reproducibility
- Documentation alongside development works well
- Regular commits help track progress

---

**Last Updated:** January 6, 2026  
**Current Step:** 10/30 (33%)  
**Status:** Week 2 in progress