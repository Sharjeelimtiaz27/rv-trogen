# RV-TroGen Examples

This folder contains example RISC-V processor modules for Trojan generation and validation.

---

## 📂 Processors Included

| Processor | Architecture | ISA | Complexity | Status |
|-----------|--------------|-----|------------|--------|
| **Ibex** | In-order, 2-stage | RV32IMC | Simple | ✅ 30 modules |
| **CVA6** | In-order, 6-stage | RV64GC | Medium | ✅ 85 modules |
| **RSD** | Out-of-order | RV64GC | Complex | ✅ 152 modules |

---

## 🗂️ Folder Structure

Each processor has the same structure:

\\\
processor_name/
├── original/           # Original RTL from upstream
├── generated_trojans/  # Generated Trojan code snippets
├── trojaned_rtl/       # Complete modules with Trojans inserted
├── results/            # Simulation and validation results
└── README.md           # Processor-specific documentation
\\\

---

## 🎯 Quick Start

**1. Generate Trojans for a module:**
\\\ash
python scripts/generate_trojans.py examples/ibex/original/ibex_cs_registers.sv
\\\

**2. Generate for all modules in a processor:**
\\\ash
python scripts/batch_generate.py examples/ibex/original/
\\\

**3. Validate generated Trojans:**
\\\ash
python scripts/validate_trojans.py examples/ibex/generated_trojans/
\\\

---

## 📊 Generation Statistics (Current)

| Processor | Modules | Trojans per Module | Total Trojans | Status |
|-----------|---------|-------------------|---------------|--------|
| Ibex | 28 | 5.5 avg | 154 generated | ✅ Complete |
| CVA6 | 85 | 4.4 avg | 376 generated | ✅ Complete |
| RSD | 152 | 2.6 avg | 399 generated | ✅ Complete |
| **Total** | **265** | **3.5 avg** | **929** | **✅ Complete** |

**Note:** Intelligent pattern matching generates 3-5 Trojans per module (out of 6 possible patterns) based on signal availability and compatibility. This ensures high-quality, targeted Trojan generation rather than blind enumeration.

---

## 🔒 Trojan Patterns

All processors use the same 6 Trust-Hub based patterns:

1. **DoS** - Denial of Service (AES-T1400)
2. **Leak** - Information Leakage (RSA-T600)
3. **Privilege** - Privilege Escalation (Custom RISC-V)
4. **Integrity** - Data Corruption (AES-T800)
5. **Availability** - Performance Degradation (Custom)
6. **Covert** - Covert Channel (Spectre-inspired)

---

## 📚 Additional Files

- \parser_usage.py\ - Example of using the RTL parser
- \parse_example.py\ - Parser demonstration

---

## 🚀 Next Steps (Development)

- [x] Download CVA6 modules (Step 13) ✅
- [x] Download RSD modules (Step 13) ✅
- [ ] Generate Trojans for all Ibex modules (Step 14)
- [ ] Generate Trojans for CVA6 modules (Step 14)
- [ ] Generate Trojans for RSD modules (Step 14)
- [ ] Validate all Trojans (Steps 15-19)

---

## 📖 Documentation

See individual processor READMEs for detailed information:
- [Ibex README](ibex/README.md)
- [CVA6 README](cva6/README.md)
- [RSD README](rsd/README.md)
