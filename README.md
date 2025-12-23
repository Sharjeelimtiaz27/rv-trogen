 🔧 TroGen\_V



\*\*Automated Hardware Trojan Generation and Validation for RISC-V Processors\*\*




---



\## 📖 Overview



TroGen\_V is an automated framework for generating and validating hardware Trojans in RISC-V processor designs. Based on Trust-Hub taxonomy, it systematically identifies insertion points, generates Trojan code, and validates detection through simulation.



\### Key Features



✅ \*\*Automated RTL Parsing\*\* - Supports Verilog and SystemVerilog  

✅ \*\*6 Trust-Hub Trojan Categories\*\* - DoS, Leak, Privilege, Integrity, Availability, Covert  

✅ \*\*Multi-Processor Support\*\* - Ibex, CVA6, RSD, and more  

✅ \*\*Automated Validation\*\* - QuestaSim integration with VCD comparison  

✅ \*\*Professional Reports\*\* - HTML reports with signal visualizations  

✅ \*\*One-Click Workflow\*\* - Complete automation from parsing to validation  



---



\## 🚀 Quick Start



\### Installation

```bash

\# Clone repository

git clone https://github.com/YOUR\_USERNAME/TroGen\_V.git

cd TroGen\_V



\# Install package

pip install -e .

```



\### Basic Usage

```bash

\# Generate Trojans for a module

python scripts/generate\_trojans.py examples/ibex/original/ibex\_csr.sv



\# View generated Trojans

ls examples/ibex/generated\_trojans/

```



See \[Quick Start Guide](docs/QUICK\_START.md) for detailed instructions.



---



\## 📁 Project Structure

```

TroGen\_V/

├── src/                    # Source code

│   ├── parser/            # RTL parser

│   ├── patterns/          # Trust-Hub patterns

│   ├── generator/         # Trojan generator

│   └── validator/         # Validation framework

├── examples/              # Working examples

│   ├── ibex/             # Ibex RISC-V processor

│   ├── cva6/             # CVA6 processor

│   └── rsd/              # RSD out-of-order processor

├── docs/                  # Documentation

├── scripts/               # Automation scripts

└── tests/                 # Unit tests

```



---



\## 🎯 Trust-Hub Trojan Categories



| Category | Description | Trust-Hub Source | Targets |

|----------|-------------|------------------|---------|

| \*\*DoS\*\* | Denial of Service | AES-T1400 | enable, valid, ready signals |

| \*\*Leak\*\* | Information Leakage | RSA-T600 | key, secret, data signals |

| \*\*Privilege\*\* | Privilege Escalation | Custom RISC-V | mode, priv, level signals |

| \*\*Integrity\*\* | Data Corruption | AES-T800 | data, result signals |

| \*\*Availability\*\* | Performance Degradation | Custom | delay, stall signals |

| \*\*Covert\*\* | Covert Channel | Custom | debug, test signals |



See \[Trust-Hub Patterns](docs/TRUST\_HUB\_PATTERNS.md) for details.



---



\## 📊 Example Output

```bash

$ python scripts/generate\_trojans.py examples/ibex/original/ibex\_csr.sv



🔍 Processing: ibex\_csr.sv

📊 Found 4 candidates



⚙️  Generating Trojan code...



&nbsp; ✓ T1: Privilege → T1\_ibex\_csr\_Privilege.sv

&nbsp; ✓ T2: DoS → T2\_ibex\_csr\_DoS.sv

&nbsp; ✓ T3: Leak → T3\_ibex\_csr\_Leak.sv

&nbsp; ✓ T4: Integrity → T4\_ibex\_csr\_Integrity.sv



✅ Complete! Generated 4 Trojans

```



---



\## 🛠️ Workflow

```

Input RTL → Parse Module → Pattern Match → Generate Trojans → 

Manual Insert → Compile → Simulate → VCD Compare → HTML Report

```



See \[Architecture](docs/ARCHITECTURE.md) for detailed workflow.



---



\## 📚 Documentation



\- \[Quick Start Guide](docs/QUICK\_START.md)

\- \[Trust-Hub Patterns](docs/TRUST\_HUB\_PATTERNS.md)

\- \[Architecture](docs/ARCHITECTURE.md)

\- \[Ibex Tutorial](docs/examples/ibex\_tutorial.md)

\- \[CVA6 Tutorial](docs/examples/cva6\_tutorial.md)



---



\## 🧪 Testing

```bash

\# Run all tests

pytest tests/



\# Run specific test

pytest tests/test\_parser.py



\# With coverage

pytest --cov=src tests/

```



---



\## 🤝 Contributing



Contributions are welcome! Please:



1\. Fork the repository

2\. Create a feature branch (`git checkout -b feature/amazing-feature`)

3\. Commit your changes (`git commit -m 'Add amazing feature'`)

4\. Push to branch (`git push origin feature/amazing-feature`)

5\. Open a Pull Request



---



\## 📄 License



This project is licensed under the MIT License - see \[LICENSE](LICENSE) file for details.



---



\## 📧 Contact



\*\*Author:\*\* Sharjeel Imtiaz  

\*\*Email:\*\* sharjeelimtiazprof@gmail.com, Sharjeel.imtia@taltech.ee

\*\*GitHub:\*\* \[@Sharjeelimtiaz27](https://github.com/Sharjeelimtiaz27)



---



\## 🙏 Acknowledgments



\- Trust-Hub for Trojan benchmarks

\- lowRISC for Ibex processor

\- OpenHW Group for CVA6 processor

\- RISC-V community



---



\## 📝 Citation



If you use TroGen\_V in your research, please cite:

```bibtex

@software{TroGen\_V2026,

&nbsp; title = {TroGen\_V: Automated Hardware Trojan Generation for RISC-V},

&nbsp; author = {Sharjeel Imtiaz},

&nbsp; year = {2026},

&nbsp; url = {https://github.com/Sharjeelimtiaz27/TroGen\_V}

}

```



---



\## 🚧 Status



\*\*Current Version:\*\* 1.0.0 (Beta)



\*\*Supported Processors:\*\*

\- ✅ Ibex (fully tested)

\- 🚧 CVA6 (in progress)

\- 🚧 RSD (planned)



\*\*Platform Support:\*\*

\- ✅ Windows 11

\- ✅ Linux

\- ⚠️ macOS (untested)



---





