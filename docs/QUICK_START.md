\# Quick Start Guide



\## Installation

```bash

\# Clone repository

git clone https://github.com/sharjeelimtiaz27/RV-TroGen.git

cd RV-TroGen



\# Install package

pip install -e .



\# Verify installation

python -c "import src; print(src.\_\_version\_\_)"

```



\## Basic Usage



\### Step 1: Parse a RISC-V Module

```bash

python src/parser/parse\_module.py examples/ibex/original/ibex\_csr.sv

```



\*\*Output:\*\*

```

🔍 Parsing: ibex\_csr.sv

============================================================

Module: ibex\_csr

Type: Sequential

Inputs: 15

Outputs: 8

Internals: 47

============================================================

```



\### Step 2: Find Trojan Candidates

```bash

python src/generator/signal\_matcher.py examples/ibex/original/ibex\_csr.sv

```



\*\*Output:\*\*

```

🎯 Found 4 Trojan candidates:



\[1] Privilege: Privilege Escalation

&nbsp;   Confidence: 1.00

&nbsp;   Triggers: csr\_addr, csr\_we\_int

&nbsp;   Payloads: priv\_lvl\_q, priv\_mode\_id\_o

```



\### Step 3: Generate Trojan Code

```bash

python src/generator/trojan\_generator.py examples/ibex/original/ibex\_csr.sv

```



\*\*Output:\*\*

```

⚙️  Generating Trojan code...

&nbsp; ✓ T1: Privilege → T1\_ibex\_csr\_Privilege.sv

&nbsp; ✓ T2: DoS → T2\_ibex\_csr\_DoS.sv

&nbsp; ✓ T3: Leak → T3\_ibex\_csr\_Leak.sv



✅ Complete! Generated 3 Trojans

📁 Output: generated\_trojans/

```



\### Step 4: Manual Insertion



1\. Copy original module:

```bash

&nbsp;  copy examples\\ibex\\original\\ibex\_csr.sv examples\\ibex\\trojaned\_rtl\\ibex\_csr\_T1.sv

```



2\. Open `generated\_trojans/T1\_ibex\_csr\_Privilege.sv`



3\. Copy Trojan code



4\. Paste BEFORE `endmodule` in `ibex\_csr\_T1.sv`



5\. Save file



\### Step 5: Validate (Coming Soon)

```bash

\# Compile original

vlog examples/ibex/original/ibex\_csr.sv



\# Compile trojaned

vlog examples/ibex/trojaned\_rtl/ibex\_csr\_T1.sv



\# Run simulation

vsim -c -do "run 1us; quit" tb\_ibex\_csr

```



\## Next Steps



\- See \[Trust-Hub Patterns](TRUST\_HUB\_PATTERNS.md) for Trojan details

\- See \[Architecture](ARCHITECTURE.md) for system design

\- See \[Ibex Tutorial](examples/ibex\_tutorial.md) for complete example



\## Troubleshooting



\*\*Problem:\*\* `ModuleNotFoundError: No module named 'src'`



\*\*Solution:\*\* Make sure you installed with `pip install -e .`



---



\*\*Problem:\*\* Parser fails on module



\*\*Solution:\*\* Check if file is valid SystemVerilog. Try simpler module first.



---



\*\*Problem:\*\* No Trojans generated



\*\*Solution:\*\* Module may not have security-critical signals. Try CSR or PMP modules.

