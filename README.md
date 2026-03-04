# RV-TroGen

**Automated Hardware Trojan Generation and Validation for RISC-V Processors**

[![License: Academic](https://img.shields.io/badge/License-Academic-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Production](https://img.shields.io/badge/status-production-green.svg)]()

---

## Overview

**RV-TroGen** is an automated framework for systematic hardware Trojan generation, integration, simulation, and validation specifically designed for RISC-V processors. It enables security researchers and processor designers to:

- **Test security assertions** — Validate formal verification tools against real Trojan implementations
- **Evaluate detection methods** — Generate diverse, reproducible Trojan variants at scale
- **Research hardware security** — Systematic coverage of RISC-V-specific attack surfaces
- **Education** — Study hardware Trojan behavior through simulation-validated examples

RV-TroGen operates in two phases. Phase 1 covers RTL parsing, module classification, security ranking, pattern matching, and SystemVerilog code generation. Phase 2 covers RTL integration, dynamic testbench generation, QuestaSim simulation, VCD capture, and time-aligned behavioral comparison.

---

## Key Features

### Automated Generation
Template-based generation of hardware Trojans for RISC-V processors, reducing insertion time from days (manual) to seconds (automated). Six Trojan patterns are generated per module using 12 reusable SystemVerilog templates (6 sequential, 6 combinational).

### Multi-Core Support
Validated across three open-source RISC-V implementations:
- **lowRISC Ibex** (RV32IMC) — in-order, 32-bit
- **OpenHW CVA6** (RV64GC) — application-class, 64-bit
- **RSD** — out-of-order superscalar

### Six Trojan Categories
Based on the Trust-Hub taxonomy [5] and RISC-V security literature, each targeting a distinct signal and mechanism:

| # | Category | Trust-Hub Basis | Target Signal | Mechanism |
|---|----------|-----------------|---------------|-----------|
| 1 | Denial of Service | AES-T1800, T1900 | `csr_we_int` | Permanently blocks CSR writes |
| 2 | Availability Degradation | MEMCTRL-T100, S35932-T300 | `csr_we_int` | 50% duty-cycle stall (8/16 cycles) |
| 3 | Data Integrity | AES-T2300, T2400 | `csr_rdata_o` | XOR all reads with `0xDEADBEEF` |
| 4 | Covert Channel | AES-T800 (extended) | `csr_rdata_o[0]` | Pulse-width encoding (10 cycles=1, 5=0) |
| 5 | Information Leakage | AES-T600, T1000, T1400 | `csr_mepc_o` | Routes secret write data to stable port |
| 6 | Privilege Escalation | RISC-V specific [6] | `priv_mode_id_o` | Forces `PRIV_LVL_M` (2'b11) |

### Template-Based Generation
12 SystemVerilog templates (6 sequential, 6 combinational) providing:
- Reproducible pattern encoding
- Independent compilation verification
- Easy extensibility to new patterns
- Direct structural comparison with Trust-Hub benchmarks

### Complete Multi-Trojan Simulation Workflow
End-to-end validation pipeline:
- RTL parser with full support for parameterized modules and package-typed ports
- Dynamic testbench generation per Trojan with CSR-aware stimulus
- Batch integration of all 6 Trojans in a single command
- Time-aligned VCD comparison using last-value semantics and binary search
- Auto-zoom waveform plots focused on the Trojan activation region (v3 analyzer)

### Open Source
MIT license for the academic research community.

---

## Repository Structure

```
rv-trogen/
|
|-- src/                                    Phase 1: RTL analysis and generation
|   |-- parser/
|   |   |-- rtl_parser.py                  Top-level parser entry point
|   |   |-- parse_module.py                Module structure extraction
|   |   |-- signal_extractor.py            Signal classification (input/output/internal)
|   |   |-- simple_parser.py               Lightweight fallback parser
|   |   `-- module_classifier.py           Sequential vs combinational classification
|   |-- patterns/
|   |   |-- pattern_library.py             Pattern registry and dispatch
|   |   |-- dos_pattern.py                 Denial of Service
|   |   |-- availability_pattern.py        Availability Degradation
|   |   |-- integrity_pattern.py           Data Integrity
|   |   |-- covert_pattern.py              Covert Channel
|   |   |-- leak_pattern.py                Information Leakage
|   |   `-- privilege_pattern.py           Privilege Escalation
|   `-- generator/
|       |-- trojan_generator.py            Core generation logic
|       |-- combinational_gen.py           Combinational module generator
|       |-- sequential_gen.py              Sequential module generator
|       |-- template_loader.py             Template loading and placeholder resolution
|       `-- placeholder_handler.py         Signal-to-placeholder mapping
|
|-- scripts/                               Phase 2: Integration, simulation, analysis
|   |-- prepare_multi_trojan_simulation.py Trojan RTL integration + testbench generation
|   |-- analyze_vcd.py                     VCD comparison, auto-zoom plots, diff reports
|   |-- batch_parse.py                     Batch RTL parsing
|   |-- batch_generate.py                  Batch Trojan generation
|   |-- batch_full_pipeline.py             End-to-end pipeline (parse to integrate)
|   |-- parse_and_rank.py                  Security ranking of modules
|   |-- generate_trojans.py                Single-module Trojan generation
|   |-- classify_signals.py                Signal classification utility
|   `-- extract_signals_helper.py          Signal extraction helper
|
|-- templates/
|   |-- trojan_templates/
|   |   |-- sequential/                    6 templates for clocked (FF-based) modules
|   |   `-- combinational/                 6 templates for combinational logic modules
|   `-- testbench_templates/
|       |-- sequential_tb_template.sv
|       |-- combinational_tb_template.sv
|       `-- mixed_tb_template.sv
|
|-- examples/
|   |-- ibex/
|   |   |-- original/                      Original Ibex RTL (ibex_cs_registers.sv, ibex_pkg.sv, ...)
|   |   |-- generated_trojans/             Phase 1 output: per-pattern Trojan snippets
|   |   `-- trojaned_rtl/                  Phase 2 output: integrated trojaned modules
|   |-- cva6/
|   `-- rsd/
|
|-- testbenches/
|   |-- ibex/
|   |   `-- ibex_cs_registers/             7 testbenches (1 original + 6 trojaned)
|   |-- cva6/
|   `-- rsd/
|
|-- simulation_results/
|   |-- vcd/
|   |   `-- ibex/ibex_cs_registers/        VCD files from QuestaSim (7 files)
|   `-- analysis/
|       `-- ibex/ibex_cs_registers/        Waveform plots and comparison reports
|
|-- tests/                                 Unit and integration tests
|-- docs/                                  Documentation
`-- README.md
```

---

## Quick Start

### Step 1: Install
```bash
git clone https://github.com/sharjeelimtiaz27/rv-trogen.git
cd rv-trogen
python install.py
python -c "from src.parser import RTLParser; print('Installation successful')"
```

### Step 2: Parse a Module
```bash
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv
```

```
============================================================
Module: ibex_cs_registers
Type: Sequential
Inputs:    15
Outputs:   8
Has Clock: True (clk_i)
Has Reset: True (rst_ni)
============================================================
```

### Step 3: Generate All 6 Trojans
```bash
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

Output in `examples/ibex/generated_trojans/ibex_cs_registers/`:
```
T1_ibex_cs_registers_DoS.sv
T2_ibex_cs_registers_Availability.sv
T3_ibex_cs_registers_Integrity.sv
T4_ibex_cs_registers_Covert.sv
T5_ibex_cs_registers_Leak.sv
T6_ibex_cs_registers_Privilege.sv
ibex_cs_registers_trojan_summary.md
```

### Step 4: Integrate All Trojans and Generate Testbenches
```bash
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers
```

Creates 6 trojaned RTL files and 7 testbenches under
`examples/ibex/trojaned_rtl/ibex_cs_registers/` and
`testbenches/ibex/ibex_cs_registers/`.

### Step 5: Simulate on Server (QuestaSim)
```bash
# Upload all files to simulation server (ibex_pkg.sv required for enum types)
scp examples/ibex/original/ibex_pkg.sv \
    examples/ibex/original/ibex_cs_registers.sv \
    examples/ibex/trojaned_rtl/ibex_cs_registers/*.sv \
    testbenches/ibex/ibex_cs_registers/*.sv \
    user@server:/workdir/

# On server: compile and simulate each pair (see docs/SIMULATION_SETUP.md)
vlog +acc ibex_pkg.sv ibex_cs_registers.sv tb_ibex_cs_registers.sv
vsim -c work.tb_ibex_cs_registers -do "run -all; quit -f"
# Repeat for each of the 6 trojaned variants
```

### Step 6: Analyze VCD Files
```bash
# Download all 7 VCD files, then analyze all 6 trojans vs original in one command
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

# Analyze a single trojan (auto-finds original in same directory)
python scripts/analyze_vcd.py \
    --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_DoS.vcd
```

Outputs land in `simulation_results/analysis/ibex/ibex_cs_registers/`:
one auto-zoomed waveform PNG and one text report per Trojan.

---

## Command-Line Reference

```bash
# Parse single module
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv

# Batch parse directory
python scripts/batch_parse.py --dir examples/ibex/original

# Find security-critical modules
python scripts/batch_parse.py --dir examples/ibex/original --security-only

# Rank modules by security importance
python scripts/parse_and_rank.py examples/ibex/original --top 5

# Generate 6 Trojans for a single module
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Run full pipeline for all processors
python scripts/batch_full_pipeline.py
python scripts/batch_full_pipeline.py --processor ibex

# Integrate all Trojans and generate testbenches
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers

# Analyze all Trojan VCDs (batch, auto-zoom)
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

# Analyze single Trojan with manual time window (ns)
python scripts/analyze_vcd.py \
    --trojan simulation_results/vcd/ibex/ibex_cs_registers/ibex_cs_registers_trojan_DoS.vcd \
    --start 140 --end 350

# Run tests
python -m pytest tests/ -v
```

---

## Comparison with Related Work

| Feature | RV-TroGen (Ours) | TrojanForge [1] | SENTAUR [2] | 0ena [3] | SoC-HTs [4] | Trust-Hub [5] |
|---------|-----------------|-----------------|-------------|----------|-------------|---------------|
| Target | RISC-V (3 cores) | Generic | Generic | RISC-V | Ariane SoC | AES/RSA |
| Approach | Template-based | RL-based | LLM (GPT-4) | Manual | Manual | Manual |
| Automation | Full | Automated | Semi | None | None | None |
| Multi-Core | 3 cores, 265 mod | Single | Untested | Generic | Single SoC | Single |
| RTL-Level | Yes (SystemVerilog) | Gate-focused | Yes | Yes | SoC/AXI | Mixed |
| Attack Surface | Processor (CSR/LSU) | Generic | Generic | Generic | AXI protocol | Crypto ops |
| Patterns | 6 categories | Black-box | 4 types | 3 examples | 3 types | Multiple |
| Templates | 12 (.sv files) | RL policy | LLM prompts | None | None | None |
| Multi-Trojan workflow | Yes | No | No | No | No | No |
| Validation | QuestaSim, 100% | Evasion rate | Detection rate | Not reported | FPGA + GNN | Benchmarks |
| Full simulation workflow | Yes | No | No | No | Behavioral | No |
| Open-Source | Yes (MIT) | No | No | Yes | Partial | Registration |
| Generated HTs | 707 | Unknown | 4 | 3 | 3 | 90+ |
| Generation time | 4.1 seconds | Hours | Slow | N/A | N/A | N/A |
| Cost | Free | Unknown | API cost | Free | Free | Paid |
| Year | 2026 | 2024 | 2024 | 2020 | 2023 | 2008–present |

**Key innovation:** First automated, template-based, open-source framework for RISC-V Trojan generation with a complete multi-Trojan simulation and validation workflow.

---

## Results

**707 Trojans generated across 3 RISC-V processors in 4.1 seconds:**

| Processor | Modules | Trojans | Avg per Module |
|-----------|---------|---------|----------------|
| Ibex      | 28      | 136     | 4.9            |
| CVA6      | 85      | 331     | 3.9            |
| RSD       | 152     | 240     | 1.6            |
| **Total** | **265** | **707** | **3.5**        |

**Simulation and validation results — ibex_cs_registers, QuestaSim 2024.3:**

| Trojan | Target Signal | Observed Behavior | Status |
|--------|--------------|-------------------|--------|
| Denial of Service | `csr_we_int` | Signal permanently blocked after activation | Confirmed |
| Availability | `csr_we_int` | Periodic gaps at 8/16-cycle duty cycle | Confirmed |
| Data Integrity | `csr_rdata_o` | XOR deviation of exactly `0xDEADBEEF` on all reads | Confirmed |
| Covert Channel | `csr_rdata_o[0]` | Variable-width pulses encoding secret bits | Confirmed |
| Information Leakage | `csr_mepc_o` | Stable port changes with each secret CSR write | Confirmed |
| Privilege Escalation | `priv_mode_id_o` | Transition from `2'b00` (user) to `2'b11` (machine) | Confirmed |

---

## Use Cases

### Security Researcher
```bash
# Generate diverse Trojan variants
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv

# Integrate all Trojans and prepare simulation
python scripts/prepare_multi_trojan_simulation.py \
    examples/ibex/original/ibex_cs_registers.sv \
    --trojans examples/ibex/generated_trojans/ibex_cs_registers

# After simulation: validate all Trojan behaviors
python scripts/analyze_vcd.py \
    --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers
```

### Processor Designer
```bash
# Identify the highest-risk modules in your design
python scripts/parse_and_rank.py my_processor/rtl --top 5

# Generate Trojans for formal verification testing
python scripts/generate_trojans.py <critical_module.sv>
```

### Educator / Student
```bash
# Parse and inspect a security-critical module
python -m src.parser.rtl_parser examples/ibex/original/ibex_cs_registers.sv

# Generate Trojans and examine the generated SystemVerilog
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
```

---

## Documentation

- [Quick Start Guide](docs/QUICK_START.md) — 15-minute tutorial
- [Commands Reference](docs/COMMANDS_REFERENCE.md) — All CLI commands with expected output
- [Simulation Setup](docs/SIMULATION_SETUP.md) — Complete server simulation workflow
- [Template Library](docs/TEMPLATES.md) — Template system documentation
- [Trust-Hub Patterns](docs/TRUST_HUB_PATTERNS.md) — Pattern taxonomy and citations
- [Step Guide](docs/STEP_GUIDE.md) — Development roadmap

---

## Testing

```bash
python -m pytest tests/ -v
python -m pytest --cov=src tests/
```

Test coverage: 85% (24/24 tests passing).

---

## Dependencies

```
pytest>=7.0.0
pytest-cov>=3.0.0
matplotlib>=3.5.0
```

```bash
python -m pip install -e .
python -m pip install matplotlib
```

Simulation requires QuestaSim 2024.3 (or compatible). GTKWave is recommended for manual waveform inspection.

---

## Acknowledgments and Processor Credits

RV-TroGen targets the following open-source RISC-V processor implementations. We gratefully acknowledge their authors and communities.

**lowRISC Ibex (RV32IMC)**
A small, efficient, 32-bit RISC-V processor core.
Repository: https://github.com/lowRISC/ibex
License: Apache 2.0

**OpenHW CVA6 (RV64GC)**
An application-class, Linux-capable 64-bit RISC-V processor.
Repository: https://github.com/openhwgroup/cva6
License: Solderpad Hardware License 0.51

**RSD (Out-of-Order RISC-V Processor)**
An out-of-order superscalar RISC-V processor.
Repository: https://github.com/rsd-devel/rsd
License: Apache 2.0

All three processor codebases are used solely for academic security research. No modifications are made to the original processor RTL; Trojans are generated as separate files that instrument the original modules.

This work also builds on the **Trust-Hub** Hardware Trojan benchmark suite [5] and the **RISC-V Privileged Architecture Specification** (RISC-V International).

---

## References

**Related work (comparison table):**

- [1] K. Hui et al., "TrojanForge: Generating Adversarial Hardware Trojan Examples Using Reinforcement Learning," arXiv:2405.15184, 2024. https://arxiv.org/abs/2405.15184
- [2] J. Bhandari et al., "SENTAUR: Security EnhaNced Trojan Assessment Using LLMs Against Undesirable Revisions," arXiv:2407.12352, 2024. https://arxiv.org/pdf/2407.12352
- [3] A. Moschos, "Towards Practical Fabrication Stage Attacks Using Interrupt-Resilient Hardware Trojans," GitHub, 2020. https://github.com/0ena/riscv-hw-trojans
- [4] S. Deb, "A RISC-V SoC with Hardware Trojans: Case Study on Trojan-ing the On-Chip Protocol Conversion," IEEE, 2023. https://ieeexplore.ieee.org/abstract/document/10321883
- [5] Trust-Hub, "Hardware Trojan Benchmarks," https://trust-hub.org

**Trojan pattern foundations:**

- [6] D. A. Bailey, "The RISC-V Files: Supervisor to Machine Privilege Escalation," MIT CSAIL, 2017.
- [7] T. Boraten and A. K. Kodi, "Mitigation of Denial of Service Attack with Hardware Trojans in NoC Architectures," IEEE IPDPS, pp. 1091–1100, 2016. https://doi.org/10.1109/IPDPS.2016.112
- [8] L. Lin, M. Kasper, T. Guneysu, C. Paar, and W. Burleson, "Trojan Side-Channels: Lightweight Hardware Trojans through Side-Channel Engineering," CHES, LNCS vol. 5747, pp. 382–395, 2009. https://doi.org/10.1007/978-3-642-04138-9_27

---

## Citation

```bibtex
@misc{rvtrogen2026,
  author      = {Imtiaz, Sharjeel},
  title       = {{RV-TroGen}: Automated Hardware Trojan Generation and Validation
                 for {RISC-V} Processors},
  year        = {2026},
  institution = {Tallinn University of Technology},
  url         = {https://github.com/sharjeelimtiaz27/rv-trogen},
  note        = {Open-source template-based framework with complete multi-Trojan
                 simulation and validation workflow}
}
```

---

## License

Academic and Research Use Only.

This is a PhD research project from Tallinn University of Technology (TalTech), Estonia.
Free for academic research and education. Cite this work if you use it.
Commercial use requires prior written permission.

Contact: sharjeel.imtiaz@taltech.ee — See [LICENSE](LICENSE) for full terms.

---

## Ethical Use

This tool is intended for security research, validation of Trojan detection methods, formal verification testing, and education. It must not be used to insert Trojans into production hardware, compromise real systems, or facilitate any illegal activity. Users bear full responsibility for ensuring ethical and lawful use.

---

## Contact

- **Author:** Sharjeel Imtiaz, PhD Candidate
- **Institution:** Tallinn University of Technology (TalTech), Estonia
- **Email:** sharjeel.imtiaz@taltech.ee
- **Repository:** https://github.com/sharjeelimtiaz27/rv-trogen
- **Issues:** https://github.com/sharjeelimtiaz27/rv-trogen/issues

---

**Version:** 3.0.0 | **Last Updated:** March 2026