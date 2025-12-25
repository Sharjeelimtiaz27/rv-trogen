\# Parser Architecture



\## Overview



The RV-TroGen parser is a modular RTL parser designed for Verilog and SystemVerilog files. It consists of three main components working together.



---



\## Architecture Diagram

```

┌────────────────────────────────────────────────────────────┐

│                        RTLParser                           │

│                   (Main Orchestrator)                      │

└────────────────┬──────────────────────┬────────────────────┘

&nbsp;                │                      │

&nbsp;                ▼                      ▼

&nbsp;   ┌────────────────────┐  ┌──────────────────────┐

&nbsp;   │ SignalExtractor    │  │ ModuleClassifier     │

&nbsp;   │ - Extract inputs   │  │ - Sequential/Comb    │

&nbsp;   │ - Extract outputs  │  │ - Detect clock/reset │

&nbsp;   │ - Extract internals│  │ - Get classification │

&nbsp;   └────────────────────┘  └──────────────────────┘

```



---



\## Components



\### 1. SignalExtractor (`signal\_extractor.py`)



\*\*Purpose:\*\* Extract signals from RTL content



\*\*Methods:\*\*

\- `extract\_inputs()` - Find all input ports

\- `extract\_outputs()` - Find all output ports

\- `extract\_internals(exclude\_names)` - Find internal signals



\*\*Example:\*\*

```python

extractor = SignalExtractor(rtl\_content)

inputs = extractor.extract\_inputs()

outputs = extractor.extract\_outputs()

internals = extractor.extract\_internals(exclude\_names=\['clk\_i'])

```



\*\*Signal Data Structure:\*\*

```python

Signal(

&nbsp;   name='data\_i',

&nbsp;   signal\_type='input',

&nbsp;   width=32,

&nbsp;   is\_vector=True

)

```



---



\### 2. ModuleClassifier (`module\_classifier.py`)



\*\*Purpose:\*\* Classify module type and detect special signals



\*\*Methods:\*\*

\- `is\_sequential()` - Check if module has state

\- `has\_clock()` - Detect clock signal

\- `has\_reset()` - Detect reset signal

\- `get\_clock\_signal()` - Get clock signal name

\- `get\_reset\_signal()` - Get reset signal name

\- `get\_classification\_report()` - Full report



\*\*Classification Logic:\*\*

```

Sequential if:

&nbsp; - Contains always\_ff block

&nbsp; - Contains @(posedge clk)

&nbsp; - Has clock signal



Otherwise:

&nbsp; - Combinational

```



\*\*Example:\*\*

```python

classifier = ModuleClassifier(content, all\_signals)

is\_seq = classifier.is\_sequential()

report = classifier.get\_classification\_report()

```



---



\### 3. RTLParser (`rtl\_parser.py`)



\*\*Purpose:\*\* Main orchestrator that combines SignalExtractor and ModuleClassifier



\*\*Methods:\*\*

\- `parse()` - Main entry point

\- `\_extract\_module\_name()` - Get module name

\- `\_extract\_signals()` - Extract all signals

\- `\_classify\_module()` - Classify module type



\*\*Module Data Structure:\*\*

```python

Module(

&nbsp;   name='ibex\_csr',

&nbsp;   file\_path=Path('ibex\_csr.sv'),

&nbsp;   inputs=\[...],

&nbsp;   outputs=\[...],

&nbsp;   internals=\[...],

&nbsp;   is\_sequential=True,

&nbsp;   has\_clock=True,

&nbsp;   has\_reset=True,

&nbsp;   clock\_signal='clk\_i',

&nbsp;   reset\_signal='rst\_ni'

)

```



\*\*Example:\*\*

```python

parser = RTLParser('ibex\_csr.sv')

module = parser.parse()

module.print\_summary()

```



---



\## Usage Examples



\### Basic Parsing

```python

from src.parser import RTLParser



\# Parse a file

parser = RTLParser('path/to/module.sv')

module = parser.parse()



\# Access module info

print(f"Module: {module.name}")

print(f"Type: {'Sequential' if module.is\_sequential else 'Combinational'}")

print(f"Inputs: {len(module.inputs)}")

print(f"Outputs: {len(module.outputs)}")

```



\### Signal Filtering

```python

\# Get all clock signals

clocks = \[s for s in module.get\_all\_signals() if 'clk' in s.name.lower()]



\# Get all vector signals

vectors = \[s for s in module.get\_all\_signals() if s.is\_vector]



\# Get signals by type

inputs\_only = module.inputs

```



\### Classification

```python

from src.parser import ModuleClassifier



classifier = ModuleClassifier(content, signals)



if classifier.is\_sequential():

&nbsp;   print(f"Sequential module with clock: {classifier.get\_clock\_signal()}")

else:

&nbsp;   print("Combinational module")

```



---



\## Limitations



\### Known Issues



1\. \*\*Multi-line Declarations:\*\*

&nbsp;  - Current parser may not handle multi-line port declarations

&nbsp;  - Example: `input logic\\n\[31:0]\\ndata\_i;`

&nbsp;  - Workaround: Use single-line declarations



2\. \*\*Parameterized Widths:\*\*

&nbsp;  - Parser extracts signal names but may not compute parameter-based widths

&nbsp;  - Example: `input \[WIDTH-1:0] data;`

&nbsp;  - Signal width will be set to 1 (default)



3\. \*\*Generate Blocks:\*\*

&nbsp;  - Signals inside generate blocks may not be extracted

&nbsp;  - Future improvement planned



4\. \*\*Preprocessor Directives:\*\*

&nbsp;  - `ifdef`, `ifndef` not evaluated

&nbsp;  - All code is parsed as-is



---



\## Extension Guide



\### Adding New Signal Types



1\. Edit `signal\_extractor.py`:

```python

def extract\_your\_type(self) -> List\[Signal]:

&nbsp;   pattern = r'your\_type\\s+(?:\\\[(\\d+):(\\d+)\\]\\s+)?(\\w+)'

&nbsp;   return self.\_extract\_signals(pattern, 'your\_type')

```



2\. Update `extract\_internals()` to include new type



\### Adding New Classification Rules



1\. Edit `module\_classifier.py`:

```python

def is\_your\_condition(self) -> bool:

&nbsp;   # Your logic here

&nbsp;   return True/False

```



2\. Update `get\_classification\_report()` to include new field



---



\## Testing



\### Unit Tests

```bash

\# Run parser tests

pytest tests/test\_parser.py



\# Run with coverage

pytest --cov=src/parser tests/test\_parser.py



\# Run specific test

pytest tests/test\_parser.py::TestRTLParser::test\_parse\_simple\_module

```



\### Integration Tests

```bash

\# Test on real Ibex module

python src/parser/rtl\_parser.py examples/ibex/original/ibex\_csr.sv

```



---



\## Performance



\*\*Typical Performance:\*\*

\- Small module (< 1000 lines): < 0.1s

\- Medium module (1000-5000 lines): 0.1-0.5s

\- Large module (> 5000 lines): 0.5-2s



\*\*Memory Usage:\*\*

\- ~10MB per module

\- Scales linearly with file size



---



\## References



\- SystemVerilog LRM IEEE 1800-2017

\- Verilog LRM IEEE 1364-2005

