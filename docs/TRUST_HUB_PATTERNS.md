\# Trust-Hub Pattern Library



\## Overview



RV-TroGen implements 6 hardware Trojan categories based on Trust-Hub taxonomy. Each pattern targets specific signal types in RISC-V processors.



---



\## Pattern 1: Denial of Service (DoS)



\*\*Trust-Hub Source:\*\* AES-T1400



\*\*Description:\*\* Disables functionality by forcing control signals to 0



\*\*Target Signals:\*\*

\- `enable`, `en`, `valid`, `ready`, `start`



\*\*Trigger Mechanism:\*\*

\- Counter-based: Activates after N operations

\- Condition-based: Specific input pattern



\*\*Payload:\*\*

```systemverilog

assign ready\_o = trojan\_active ? 1'b0 : normal\_ready;

```



\*\*Example in Ibex:\*\*

\- Target: `ibex\_decoder` module

\- Signal: `instr\_valid\_o`

\- Effect: Prevents instruction execution



---



\## Pattern 2: Information Leakage



\*\*Trust-Hub Source:\*\* RSA-T600



\*\*Description:\*\* Leaks sensitive data to attacker-accessible location



\*\*Target Signals:\*\*

\- `key`, `secret`, `data`, `addr`, `address`, `priv`



\*\*Trigger Mechanism:\*\*

\- Debug mode activation

\- External pin signal



\*\*Payload:\*\*

```systemverilog

assign debug\_output = trojan\_trigger ? secret\_register : normal\_output;

```



\*\*Example in Ibex:\*\*

\- Target: `ibex\_csr` module

\- Signal: `csr\_rdata\_o`

\- Effect: Leaks CSR contents to unused port



---



\## Pattern 3: Privilege Escalation



\*\*Trust-Hub Source:\*\* Custom RISC-V



\*\*Description:\*\* Escalates privilege level to machine mode



\*\*Target Signals:\*\*

\- `mode`, `priv`, `privilege`, `level`, `lvl`



\*\*Trigger Mechanism:\*\*

\- Specific CSR write pattern

\- Magic value in instruction



\*\*Payload:\*\*

```systemverilog

always\_ff @(posedge clk) begin

&nbsp; if (trojan\_trigger) begin

&nbsp;   priv\_lvl\_q <= PRIV\_LVL\_M;  // Force M-mode

&nbsp; end

end

```



\*\*Example in Ibex:\*\*

\- Target: `ibex\_csr` module

\- Signal: `priv\_lvl\_q`

\- Effect: User mode gains machine privileges



---



\## Pattern 4: Integrity Violation



\*\*Trust-Hub Source:\*\* AES-T800



\*\*Description:\*\* Corrupts computation results



\*\*Target Signals:\*\*

\- `data`, `result`, `output`, `computation`



\*\*Trigger Mechanism:\*\*

\- Specific input pattern

\- Address-based trigger



\*\*Payload:\*\*

```systemverilog

assign data\_out = trojan\_trigger ? (data\_in ^ CORRUPTION) : data\_in;

```



\*\*Example in Ibex:\*\*

\- Target: `ibex\_alu` module

\- Signal: `result\_o`

\- Effect: Corrupts ALU output



---



\## Pattern 5: Availability (Performance Degradation)



\*\*Trust-Hub Source:\*\* Custom



\*\*Description:\*\* Degrades performance through artificial delays



\*\*Target Signals:\*\*

\- `ready`, `valid`, `stall`, `busy`, `delay`



\*\*Trigger Mechanism:\*\*

\- Secret data bit

\- Probabilistic activation



\*\*Payload:\*\*

```systemverilog

logic \[3:0] delay\_counter;

assign ready = (delay\_counter == 0);  // Adds cycles

```



\*\*Example in Ibex:\*\*

\- Target: `ibex\_load\_store\_unit`

\- Signal: `lsu\_resp\_valid\_o`

\- Effect: Slows memory operations



---



\## Pattern 6: Covert Channel



\*\*Trust-Hub Source:\*\* Custom



\*\*Description:\*\* Creates hidden communication channel through timing



\*\*Target Signals:\*\*

\- `debug`, `test`, `unused`, timing-sensitive signals



\*\*Trigger Mechanism:\*\*

\- Secret data to transmit

\- Encoding mechanism



\*\*Payload:\*\*

```systemverilog

// Encode 1 bit = long delay, 0 bit = short delay

assign delay = secret\_bit ? 4'b1111 : 4'b0001;

```



\*\*Example in Ibex:\*\*

\- Target: Any module with observable timing

\- Signal: Response delays

\- Effect: Leaks data through timing channel



---



\## Signal Keyword Mapping



| Pattern | Trigger Keywords | Payload Keywords |

|---------|------------------|------------------|

| \*\*DoS\*\* | enable, valid, ready, start | enable, valid, ready |

| \*\*Leak\*\* | debug, test, mode | key, secret, data, addr |

| \*\*Privilege\*\* | csr, write, mode | mode, priv, level, lvl |

| \*\*Integrity\*\* | data, input, addr | data, output, result |

| \*\*Availability\*\* | data, valid, request | ready, stall, busy |

| \*\*Covert\*\* | data, input | debug, test, unused |



---



\## Pattern Detection in Modules



\### Sequential Modules (with always\_ff)

\- Use \*\*counter-based triggers\*\*

\- State machine injection

\- Register modification



\### Combinational Modules (always\_comb/assign)

\- Use \*\*condition-based triggers\*\*

\- Direct signal manipulation

\- No state required



---



\## References



1\. Trust-Hub Benchmarks: https://trust-hub.org

2\. "Hardware Trojan Attacks: Threat Analysis and Countermeasures" (IEEE 2014)

3\. RISC-V Privileged Specification v1.12

4\. Ibex Core Documentation: https://ibex-core.readthedocs.io



---



\## Adding New Patterns



To add a new pattern:



1\. Create `src/patterns/your\_pattern.py`

2\. Define trigger and payload keywords

3\. Add to `pattern\_library.py`

4\. Create template in `templates/trojan\_templates/`

5\. Update this documentation

