# CVA6 Core Examples

**Processor:** CVA6 (RV64GC) - formerly Ariane  
**Source:** OpenHW Group  
**Architecture:** In-order, 6-stage pipeline  
**Repository:** https://github.com/openhwgroup/cva6

---

## 📁 Folder Structure

\\\
cva6/
├── original/           # Original CVA6 RTL modules (to be downloaded)
├── generated_trojans/  # Generated Trojan code snippets
├── trojaned_rtl/       # Complete RTL with Trojans inserted
└── results/            # Simulation and validation results
\\\

---

## 🎯 Target Modules (10-15 modules, Step 13)

---

## 📊 Downloaded Modules

**Total:** 85 valid modules

**Key Security-Critical Modules Include:**
- `csr_regfile.sv` - Control and Status Registers
- `controller.sv` - Main pipeline controller
- `load_store_unit.sv` - Load/Store Unit
- `mmu.sv` - Memory Management Unit
- `commit_stage.sv` - Commit logic
- `alu.sv`, `mult.sv`, `branch_unit.sv` - Execution units
- Plus 79 more modules...

**To see full list:**
```bash
ls examples/cva6/original/*.sv
```

## 📊 Trojan Generation

**Download Modules First (Step 13):**
\\\ash
# Will download from: https://github.com/openhwgroup/cva6
\\\

**Then Generate:**
\\\ash
python scripts/batch_generate.py examples/cva6/original/ --output examples/cva6/generated_trojans/
\\\

**Expected Output:**
- 6 Trojan variants per module
- ~60-90 total Trojan files (10-15 modules × 6 patterns)

---

## 🧪 Validation

**Simulation:** QuestaSim or Verilator  
**Note:** CVA6 has 6-stage pipeline, more complex than Ibex

**Challenges:**
- Longer pipeline requires more cycle-accurate testing
- MMU/TLB validation needs virtual memory setup
- Cache testing requires specific access patterns

---

## 📈 Current Status

- ✅ 85 valid RTL modules downloaded (113 files total, 85 parseable)
- ✅ Downloaded from OpenHW Group CVA6 repository
- ⏸️ Trojan generation pending (Step 14)
- ⏸️ Validation pending (Steps 15-19)

**Module Breakdown:**
- 85 parseable SystemVerilog modules
- 28 package/interface files (not modules)
- All modules parse successfully with RV-TroGen parser
---

## 📚 References

- CVA6 Docs: https://docs.openhwgroup.org/projects/cva6-user-manual
- OpenHW GitHub: https://github.com/openhwgroup/cva6
- Paper: "Ariane: An Open-Source 64-bit RISC-V Application Processor"
