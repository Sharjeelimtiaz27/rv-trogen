\# RV-TroGen Architecture



\## System Overview

```

┌──────────────────────────────────────────────────────────────┐

│                     RV-TroGen Framework                      │

└──────────────────────────────────────────────────────────────┘

&nbsp;                             │

&nbsp;                             ▼

&nbsp;       ┌────────────────────────────────────────┐

&nbsp;       │  PHASE 1: RTL Parsing \& Analysis       │

&nbsp;       └────────────────────────────────────────┘

&nbsp;                             │

&nbsp;                             ▼

&nbsp;       ┌────────────────────────────────────────┐

&nbsp;       │  PHASE 2: Pattern Matching             │

&nbsp;       └────────────────────────────────────────┘

&nbsp;                             │

&nbsp;                             ▼

&nbsp;       ┌────────────────────────────────────────┐

&nbsp;       │  PHASE 3: Trojan Code Generation       │

&nbsp;       └────────────────────────────────────────┘

&nbsp;                             │

&nbsp;                             ▼

&nbsp;       ┌────────────────────────────────────────┐

&nbsp;       │  PHASE 4: Manual Insertion             │

&nbsp;       └────────────────────────────────────────┘

&nbsp;                             │

&nbsp;                             ▼

&nbsp;       ┌────────────────────────────────────────┐

&nbsp;       │  PHASE 5: Validation \& Comparison      │

&nbsp;       └────────────────────────────────────────┘

```



---



\## Module Architecture



\### 1. Parser Module (`src/parser/`)



\*\*Components:\*\*

\- `rtl\_parser.py` - Main parsing orchestrator

\- `signal\_extractor.py` - Signal identification

\- `module\_classifier.py` - Sequential/Combinational classification



\*\*Input:\*\* Verilog/SystemVerilog files



\*\*Output:\*\* 

```python

Module(

&nbsp;   name="ibex\_csr",

&nbsp;   type="sequential",

&nbsp;   inputs=\[...],

&nbsp;   outputs=\[...],

&nbsp;   internals=\[...]

)

```



---



\### 2. Pattern Library (`src/patterns/`)



\*\*Components:\*\*

\- `dos\_pattern.py` - DoS Trojan pattern

\- `leak\_pattern.py` - Information leakage pattern

\- `privilege\_pattern.py` - Privilege escalation pattern

\- `integrity\_pattern.py` - Integrity violation pattern

\- `availability\_pattern.py` - Performance degradation pattern

\- `covert\_pattern.py` - Covert channel pattern

\- `pattern\_library.py` - Unified interface



\*\*Data Structure:\*\*

```python

TrojanPattern(

&nbsp;   category="Privilege",

&nbsp;   trust\_hub\_source="Custom RISC-V",

&nbsp;   trigger\_keywords=\["csr", "mode"],

&nbsp;   payload\_keywords=\["priv", "level"]

)

```



---



\### 3. Generator Module (`src/generator/`)



\*\*Components:\*\*

\- `trojan\_generator.py` - Main generator

\- `sequential\_gen.py` - Sequential module Trojans

\- `combinational\_gen.py` - Combinational module Trojans



\*\*Process:\*\*

1\. Match module signals to patterns

2\. Calculate confidence score

3\. Select appropriate generator (seq/comb)

4\. Apply template

5\. Generate SystemVerilog code



\*\*Output:\*\* `.sv` files with Trojan code



---



\### 4. Validator Module (`src/validator/`)



\*\*Components:\*\*

\- `simulator.py` - QuestaSim wrapper

\- `vcd\_analyzer.py` - VCD file parser

\- `signal\_comparator.py` - Signal comparison

\- `report\_generator.py` - HTML report generation



\*\*Workflow:\*\*

1\. Compile original RTL

2\. Compile trojaned RTL

3\. Run simulations

4\. Generate VCD dumps

5\. Compare signals

6\. Generate report



---



\## Data Flow

```

RTL File → Parser → Module Object → Pattern Matcher → 

Candidates → Generator → Trojan Code → Manual Insert → 

Trojaned RTL → Simulator → VCD Files → Comparator → Report

```



---



\## Design Decisions



\### Why Pattern-Based (vs ML)?



\*\*Advantages:\*\*

\- ✅ Interpretable

\- ✅ Reproducible

\- ✅ No training data needed

\- ✅ Deterministic

\- ✅ Easy to extend



\*\*Trade-offs:\*\*

\- ⚠️ Less diverse than ML

\- ⚠️ Requires domain knowledge



\### Why RTL-Level (vs Gate-Level)?



\*\*Advantages:\*\*

\- ✅ Designer-friendly

\- ✅ Pre-synthesis

\- ✅ Higher abstraction

\- ✅ Tool-independent



\*\*Trade-offs:\*\*

\- ⚠️ Less stealthy than gate-level



\### Why Manual Insertion?



\*\*Reasons:\*\*

\- Safety: Prevents breaking original logic

\- Flexibility: User controls placement

\- Understanding: Forces examination of code



\*\*Future:\*\* Semi-automated insertion planned



---



\## Extension Points



\### Adding New Processor



1\. Add example folder: `examples/your\_processor/`

2\. Test parser on modules

3\. Document specific features

4\. Create testbench template



\### Adding New Pattern



1\. Create pattern file: `src/patterns/new\_pattern.py`

2\. Add to pattern library

3\. Create generator logic

4\. Add template

5\. Document in TRUST\_HUB\_PATTERNS.md



\### Adding New Validation Method



1\. Create validator: `src/validator/new\_validator.py`

2\. Implement validation logic

3\. Integrate with report generator

4\. Add tests



---



\## Performance Considerations



\*\*Parser:\*\*

\- Time complexity: O(n) where n = file size

\- Memory: ~10MB per module



\*\*Generator:\*\*

\- Time complexity: O(m\*p) where m = modules, p = patterns

\- Memory: Negligible



\*\*Validator:\*\*

\- Time complexity: Depends on simulation time

\- Memory: VCD file size (can be large)



---



\## Security Considerations



\*\*Generated Trojans are for research only!\*\*



\- Never use on production systems

\- Store generated Trojans securely

\- Document all experiments

\- Follow responsible disclosure



---



\## Testing Strategy



\*\*Unit Tests:\*\*

\- Parser: Test on various SV constructs

\- Patterns: Test keyword matching

\- Generator: Test code generation



\*\*Integration Tests:\*\*

\- End-to-end on real modules

\- Multiple processors

\- All patterns



\*\*Validation:\*\*

\- Simulation-based testing

\- VCD verification

\- Manual inspection

