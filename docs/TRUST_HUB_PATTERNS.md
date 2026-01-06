# Trust-Hub Pattern Library

## Overview

RV-TroGen implements 6 hardware Trojan categories based on Trust-Hub taxonomy and RISC-V security literature. Each pattern targets specific signal types in RISC-V processors.

---

## Pattern 1: Denial of Service (DoS)

**Trust-Hub Source:** AES-T1400

**Description:** Disables functionality by forcing control signals to 0

**Target Signals:**
- `enable`, `en`, `valid`, `ready`, `start`

**Trigger Mechanism:**
- Counter-based: Activates after N operations
- Condition-based: Specific input pattern

**Payload:**
```systemverilog
assign ready_o = trojan_active ? 1'b0 : normal_ready;
```

**Example in Ibex:**
- Target: `ibex_decoder` module
- Signal: `instr_valid_o`
- Effect: Prevents instruction execution

**References:**
- [1] Trust-Hub Benchmark AES-T1400
- [2] Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF 2021

---

## Pattern 2: Information Leakage

**Trust-Hub Source:** RSA-T600

**Description:** Leaks sensitive data to attacker-accessible location

**Target Signals:**
- `key`, `secret`, `data`, `addr`, `address`, `priv`

**Trigger Mechanism:**
- Debug mode activation
- External pin signal

**Payload:**
```systemverilog
assign debug_output = trojan_trigger ? secret_register : normal_output;
```

**Example in Ibex:**
- Target: `ibex_csr` module
- Signal: `csr_rdata_o`
- Effect: Leaks CSR contents to unused port

**References:**
- [3] Trust-Hub Benchmark RSA-T600
- [2] Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF 2021

---

## Pattern 3: Privilege Escalation

**Literature Source:** Bailey (2017), Nashimoto et al. (2020)

**Description:** Escalates RISC-V privilege level from User/Supervisor to Machine mode

**Why Important for RISC-V:**
RISC-V's three-tier privilege architecture (M/S/U modes) is fundamental to its security model. Compromising privilege escalation breaks the entire security boundary, allowing:
- Bypass of memory protection (PMP)
- Access to all CSRs and system resources
- Subversion of TEE (Trusted Execution Environment)
- Complete system compromise

**Target Signals:** RISC-V-specific privilege CSRs
- `priv_lvl_q`, `priv_mode_id` - Privilege level registers
- `mstatus` - Machine status register (CSR 0x300)
- `mtvec` - Machine trap vector (CSR 0x305)
- `mepc` - Machine exception PC (CSR 0x341)
- `mode`, `priv`, `privilege`, `level`, `lvl`

**Trigger Mechanism:**
- Specific CSR write pattern
- Magic value in instruction
- Exploit timing window during mode transitions

**Payload:**
```systemverilog
always_ff @(posedge clk) begin
  if (trojan_trigger) begin
    priv_lvl_q <= PRIV_LVL_M;  // Force M-mode (2'b11)
  end
end
```

**Example in Ibex:**
- Target: `ibex_cs_registers` module
- Signal: `priv_lvl_q`
- Effect: User mode gains machine privileges

**Our Contribution:**
First automated systematic generation of privilege escalation Trojans for RISC-V processors. Previous work (Bailey 2017) demonstrated manual exploitation; we provide automated generation across multiple RISC-V cores.

**References:**
- [4] D. A. Bailey, "The RISC-V Files: Supervisor→Machine Privilege Escalation Exploit," Security Mouse Blog, 2017
- [5] S. Nashimoto et al., "Bypassing Isolated Execution on RISC-V with Fault Injection," IACR ePrint 2020/1193, 2020
- [6] Carre et al., "Return-Oriented Programming on RISC-V," arXiv:2103.08229, 2021

---

## Pattern 4: Integrity Violation

**Trust-Hub Source:** AES-T800

**Description:** Corrupts computation results

**Target Signals:**
- `data`, `result`, `output`, `computation`

**Trigger Mechanism:**
- Specific input pattern
- Address-based trigger

**Payload:**
```systemverilog
assign data_out = trojan_trigger ? (data_in ^ CORRUPTION) : data_in;
```

**Example in Ibex:**
- Target: `ibex_alu` module
- Signal: `result_o`
- Effect: Corrupts ALU output

**References:**
- [7] Trust-Hub Benchmark AES-T800

---

## Pattern 5: Performance Degradation (Availability Attack)

**Literature Source:** Boraten & Kodi (2016), Hoque et al. (2020), Mukherjee et al. (2023)

**Description:** Degrades RISC-V processor performance through artificial delays in Load/Store Unit

**Why Important for RISC-V:**
RISC-V's simple in-order pipeline makes it particularly vulnerable to LSU stalling:
- Single-cycle memory operations become multi-cycle
- Pipeline bubbles propagate through entire processor
- Real-time systems miss deadlines
- Covert degradation (5-30% slowdown) hard to detect
- Appears as normal timing variation

**Target Signals:** RISC-V Load/Store Unit timing-critical paths
- `lsu_req_valid_o` - LSU request valid signal
- `lsu_resp_valid_o` - LSU response valid signal
- `data_rvalid_i` - Data memory response valid
- `data_gnt_i` - Data memory grant signal
- `ready`, `valid`, `stall`, `busy`, `delay`

**Trigger Mechanism:**
- Secret data bit embedded in instruction
- Probabilistic activation (e.g., every Nth memory access)
- Address-based trigger (specific memory regions)

**Payload:**
```systemverilog
logic [3:0] delay_counter;

always_ff @(posedge clk) begin
  if (trojan_trigger) begin
    delay_counter <= 4'd15;  // 15 cycle artificial delay
  end else if (delay_counter > 0) begin
    delay_counter <= delay_counter - 1;
  end
end

// Inject wait states
assign lsu_resp_valid_o = (delay_counter == 0) ? normal_valid : 1'b0;
```

**Example in Ibex:**
- Target: `ibex_load_store_unit` module
- Signal: `lsu_resp_valid_o`
- Effect: Slows memory operations by 5-30%

**Our Contribution:**
First systematic LSU-targeted performance degradation implementation for RISC-V. Previous work focused on cache policies and NoC; we target RISC-V pipeline stalls.

**References:**
- [8] T. Boraten and A. K. Kodi, "Mitigation of denial of service attack with hardware trojans in noc architectures," IEEE IPDPS, 2016
- [9] T. Hoque et al., "Hardware trojan attacks in embedded memory," ACM JETC, vol. 16, no. 4, 2020
- [10] S. Mukherjee et al., "Design, threat analysis and countermeasures for cache replacement policy-affecting Hardware Trojans," Microelectronics Reliability, vol. 149, 2023

---

## Pattern 6: Covert Channel (Timing-Based)

**Literature Source:** Lipp et al. (2021), Weisse et al. (2021), Lin et al. (2009)

**Description:** Creates hidden timing-based communication channel for information exfiltration

**Why Important for RISC-V:**
Open-source nature makes timing channels particularly dangerous:
- Known microarchitectural implementation details
- Predictable timing behavior for encoding
- Observable through debug interfaces
- Difficult to detect without specialized tools
- Can leak cryptographic keys, privilege bits, or sensitive data

**Target Signals:** Any observable timing-sensitive path
- Cache access latencies
- Memory response delays
- Pipeline stall cycles
- Debug interface timing
- `debug`, `test`, `unused` ports

**Trigger Mechanism:**
- Secret data bit to transmit
- Encoding mechanism (long delay = '1', short = '0')
- Modulation through cache access patterns

**Payload:**
```systemverilog
// Encode secret bit through timing modulation
logic [7:0] delay_counter;

always_ff @(posedge clk) begin
  if (secret_data_bit) begin
    delay_counter <= 8'd255;  // Long delay = bit '1'
  end else begin
    delay_counter <= 8'd1;    // Short delay = bit '0'
  end
end

assign ready_o = (delay_counter == 0);
```

**Example in Ibex:**
- Target: Any module with observable timing
- Signal: Response delays, cache timing
- Effect: Leaks data through timing variations
- Bandwidth: ~1-10 bits/second (typical for timing channels)

**Detection Difficulty:** 
High - appears as normal timing variation, requires statistical analysis or formal verification to detect.

**Our Contribution:**
First automated systematic generation of timing-based covert channels for RISC-V processors. Previous work (Lipp 2021) manually implemented channels; we automate generation and provide validation framework.

**References:**
- [2] M. Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF, DOI: 10.1145/3457388.3458869, 2021
- [11] O. Weisse et al., "Prevention of Microarchitectural Covert Channels on an Open-Source 64-bit RISC-V Core," IEEE CSF, 2021
- [12] L. Lin et al., "Trojan Side-Channels: Lightweight Hardware Trojans through Side-Channel Engineering," CHES, pp. 382-395, 2009

---

## Signal Keyword Mapping

| Pattern | Trigger Keywords | Payload Keywords |
|---------|------------------|------------------|
| **DoS** | enable, valid, ready, start | enable, valid, ready |
| **Leak** | debug, test, mode | key, secret, data, addr |
| **Privilege** | csr, write, mode, priv, mstatus | mode, priv, level, lvl, mtvec, mepc |
| **Integrity** | data, input, addr | data, output, result |
| **Availability** | data, valid, request, lsu | ready, stall, busy, delay, gnt |
| **Covert** | data, input, secret | debug, test, unused, timing |

---

## Pattern Detection in Modules

### Sequential Modules (with always_ff)
- Use **counter-based triggers**
- State machine injection
- Register modification
- Suitable for: Privilege Escalation, Performance Degradation, Covert Channel

### Combinational Modules (always_comb/assign)
- Use **condition-based triggers**
- Direct signal manipulation
- No state required
- Suitable for: DoS, Information Leak, Integrity Violation

---

## Pattern Source Summary

| Pattern | Source Type | Primary Reference | Adaptation |
|---------|-------------|-------------------|------------|
| DoS | Trust-Hub Benchmark | AES-T1400 [1] | RISC-V control signals |
| Information Leak | Trust-Hub Benchmark | RSA-T600 [3] | CSR leakage vectors |
| Privilege Escalation | RISC-V Literature | Bailey 2017 [4], Nashimoto 2020 [5] | **Automated generation** |
| Integrity | Trust-Hub Benchmark | AES-T800 [7] | RISC-V ALU targeting |
| Performance Degradation | General Literature | Boraten 2016 [8], Hoque 2020 [9] | **RISC-V LSU targeting** |
| Covert Channel | Side-Channel Literature | Lipp 2021 [2], Lin 2009 [12] | **Automated generation** |

**Key:** 
- **Bold** = Our novel contribution (first automated implementation for RISC-V)
- Regular = Adaptation from existing work

---

## References

### Trust-Hub Benchmarks
[1] Trust-Hub, "AES-T1400: Denial of Service Trojan," https://trust-hub.org/benchmarks/AES-T1400

[3] Trust-Hub, "RSA-T600: Information Leakage Trojan," https://trust-hub.org/benchmarks/RSA-T600

[7] Trust-Hub, "AES-T800: Data Integrity Trojan," https://trust-hub.org/benchmarks/AES-T800

### RISC-V Specific Work
[2] M. Lipp, T. Zahur, M. Schwarz, S. Gneißl, P. Kogler, D. Gruss, S. Mangard, and M. Werner, "Tapeout of a RISC-V crypto chip with hardware trojans: A case-study on trojan design and pre-silicon detectability," in Proc. 18th ACM International Conference on Computing Frontiers (CF '21), 2021, DOI: 10.1145/3457388.3458869

[4] D. A. Bailey, "The RISC-V Files: Supervisor → Machine Privilege Escalation Exploit," Security Mouse Blog, April 2017. [Online]. Available: http://blog.securitymouse.com/2017/04/the-risc-v-files-supervisor-machine.html

[5] S. Nashimoto, D. Suzuki, R. Ueno, and N. Homma, "Bypassing Isolated Execution on RISC-V with Fault Injection," IACR ePrint Archive, Report 2020/1193, 2020. [Online]. Available: https://eprint.iacr.org/2020/1193.pdf

[6] H. Carre, M. Debbabi, L. Lebel, and B. Bossuet, "Return-Oriented Programming on RISC-V," arXiv preprint arXiv:2103.08229, March 2021.

### Performance Degradation & Side Channels
[8] T. Boraten and A. K. Kodi, "Mitigation of denial of service attack with hardware trojans in noc architectures," in Proc. IEEE International Parallel and Distributed Processing Symposium (IPDPS), 2016, pp. 1091-1100.

[9] T. Hoque, X. Wang, A. Basak, R. Karam, and S. Bhunia, "Hardware trojan attacks in embedded memory," ACM Journal on Emerging Technologies in Computing Systems (JETC), vol. 16, no. 4, Article 39, Oct. 2020, DOI: 10.1145/3422353

[10] S. Mukherjee, S. Mondal, and P. P. Chakrabarti, "Design, threat analysis and countermeasures for cache replacement policy-affecting Hardware Trojans in the context of a many-core system," Microelectronics Reliability, vol. 149, Article 115151, Oct. 2023, DOI: 10.1016/j.microrel.2023.115151

[11] O. Weisse, I. Neal, K. Loughlin, T. F. Wenisch, and B. Kasikci, "Prevention of Microarchitectural Covert Channels on an Open-Source 64-bit RISC-V Core," in Proc. IEEE 34th Computer Security Foundations Symposium (CSF), 2021, DOI: 10.1109/CSF51468.2021.00045

[12] L. Lin, M. Kasper, T. Güneysu, C. Paar, and W. Burleson, "Trojan Side-Channels: Lightweight Hardware Trojans through Side-Channel Engineering," in Proc. Cryptographic Hardware and Embedded Systems (CHES), 2009, pp. 382-395.

### General Hardware Trojan Literature
[13] M. Tehranipoor and F. Koushanfar, "A survey of hardware trojan taxonomy and detection," IEEE Design & Test of Computers, vol. 27, no. 1, pp. 10-25, Jan.-Feb. 2010.

[14] S. Bhasin, J.-L. Danger, S. Guilley, and X. T. Ngo, "Hardware Trojan horses in cryptographic IP cores," in Proc. Workshop on Fault Diagnosis and Tolerance in Cryptography (FDTC), 2013, pp. 15-29.

[15] K. Xiao, D. Forte, Y. Jin, R. Karri, S. Bhunia, and M. Tehranipoor, "Hardware Trojans: Lessons Learned after One Decade of Research," ACM Transactions on Design Automation of Electronic Systems, vol. 22, no. 1, Article 6, May 2016, DOI: 10.1145/2906147

### RISC-V Documentation
[16] RISC-V International, "The RISC-V Instruction Set Manual, Volume II: Privileged Architecture, Version 1.12," 2021. [Online]. Available: https://riscv.org/technical/specifications/

[17] lowRISC Contributors, "Ibex RISC-V Core Documentation," 2024. [Online]. Available: https://ibex-core.readthedocs.io

---

## Our Contributions Summary

**RV-TroGen provides:**

1. **Automated Generation** - First tool to automatically generate Trojans for RISC-V
2. **Multi-Core Support** - Works across Ibex, CVA6, and NaxRiscv
3. **Systematic Validation** - Automated simulation and behavioral verification
4. **Open-Source Tool** - Publicly available for security research

**Novel Implementations:**
- ✅ Privilege Escalation: First automated generation for RISC-V M/S/U modes
- ✅ Performance Degradation: First RISC-V LSU-targeted implementation
- ✅ Covert Channel: First automated timing channel generation for RISC-V

**Adaptations from Trust-Hub:**
- ✅ DoS, Information Leak, Integrity: Adapted to RISC-V signal patterns

---

## Adding New Patterns

To add a new pattern:

1. Create `src/patterns/your_pattern.py`
2. Define trigger and payload keywords based on literature
3. Add to `pattern_library.py`
4. Create template in `templates/trojan_templates/`
5. Add citations to this documentation
6. Run validation tests across target cores

---

## Citation for This Work

If you use RV-TroGen in your research, please cite:
```bibtex
@misc{rvtrogen2025,
  author = {Imtiaz, Sharjeel},
  title = {RV-TroGen: Automated Hardware Trojan Generation for RISC-V Processors},
  year = {2025},
  institution = {Tallinn University of Technology},
  url = {https://github.com/sharjeelimtiaz27/rv-trogen}
}
```

---

**Last Updated:** January 2025  
**Version:** 1.0.0  
**Maintainer:** Sharjeel Imtiaz (sharjeel.imtiaz@taltech.ee)
