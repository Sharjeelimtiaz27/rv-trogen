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

### Control & Security ⭐ High Priority
- \csr_regfile.sv\ - CSR registers
- \controller.sv\ - Main controller
- \decoder.sv\ - Instruction decoder
- \commit_stage.sv\ - Commit logic

### Execution Units
- \lu.sv\ - ALU
- \mult.sv\ - Multiplier
- \load_store_unit.sv\ - LSU
- \ranch_unit.sv\ - Branch execution

### Memory & Cache
- \cache_subsystem.sv\ - Cache system
- \mmu.sv\ - Memory Management Unit
- \ptw.sv\ - Page Table Walker
- \	lb.sv\ - Translation Lookaside Buffer

---

## 🔒 Security-Critical Modules

**Priority 1:**
1. \csr_regfile.sv\ - Privilege and mode control
2. \mmu.sv\ / \ptw.sv\ - Memory protection bypass
3. \commit_stage.sv\ - Integrity control

**Priority 2:**
4. \cache_subsystem.sv\ - Side-channel targets
5. \load_store_unit.sv\ - Memory integrity
6. \	lb.sv\ - Address translation attacks

---

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

- ⏸️ RTL modules not yet downloaded (Step 13)
- ⏸️ Trojan generation pending
- ⏸️ Validation pending

---

## 📚 References

- CVA6 Docs: https://docs.openhwgroup.org/projects/cva6-user-manual
- OpenHW GitHub: https://github.com/openhwgroup/cva6
- Paper: "Ariane: An Open-Source 64-bit RISC-V Application Processor"
