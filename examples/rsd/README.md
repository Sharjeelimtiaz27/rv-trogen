# RSD Core Examples

**Processor:** RSD (RV64GC)  
**Source:** Tokyo Institute of Technology  
**Architecture:** Out-of-order, superscalar  
**Repository:** https://github.com/rsd-devel/rsd

---

## 📁 Folder Structure

\\\
rsd/
├── original/           # Original RSD RTL modules (to be downloaded)
├── generated_trojans/  # Generated Trojan code snippets
├── trojaned_rtl/       # Complete RTL with Trojans inserted
└── results/            # Simulation and validation results
\\\

---

## 🎯 Target Modules (10-15 modules, Step 13)

---

## 📊 Downloaded Modules

**Total:** 152 valid modules (largest processor set!)

**Key Security-Critical Modules Include:**
- `ActiveListManager.sv` - Out-of-order instruction tracking
- `ReorderBuffer.sv` - ROB for OoO execution
- `SchedulerCSR.sv` - CSR scheduler
- `CommitStage.sv` - Commit logic
- `LoadStoreUnit.sv` - Memory operations
- `RecoveryManager.sv` - Exception/speculation recovery
- Plus 146 more modules...

**To see full list:**
```bash
ls examples/rsd/original/*.sv
```

## ⚠️ Out-of-Order Challenges

**Trojan Trigger Complexity:**
- Counter-based triggers harder (non-sequential execution)
- Need to account for speculation and rollback
- Timing attacks easier due to variable execution times

**Pattern Adaptations Needed:**
- DoS: Target commit stage instead of early pipeline
- Leak: Use ROB or speculation windows
- Covert: Exploit timing variability naturally present

---

## 📊 Trojan Generation

**Download Modules First (Step 13):**
\\\ash
# Will download from: https://github.com/rsd-devel/rsd
\\\

**Then Generate:**
\\\ash
python scripts/batch_generate.py examples/rsd/original/ --output examples/rsd/generated_trojans/
\\\

**Expected Output:**
- 6 Trojan variants per module
- ~60-90 total Trojan files
- May require pattern adjustments for OoO

---

## 🧪 Validation

**Simulation:** QuestaSim (OoO complexity requires cycle-accurate sim)  
**Challenge:** Validating speculative execution behavior

**Test Scenarios:**
- Normal execution flow
- Branch misprediction recovery
- Exception handling during speculation
- ROB full/empty edge cases

---

## 📈 Current Status

- ✅ 152 valid RTL modules downloaded (217 files total, 152 parseable)
- ✅ Downloaded from Tokyo Tech RSD repository
- ⏸️ Trojan generation pending (Step 14)
- ⏸️ Pattern adaptation for OoO pending (Step 14)
- ⏸️ Validation pending (Steps 15-19)

**Module Breakdown:**
- 152 parseable SystemVerilog modules
- 65 package/interface files (not modules)
- All modules parse successfully with RV-TroGen parser
- Includes complex OoO control logic

---

## 📚 References

- RSD GitHub: https://github.com/rsd-devel/rsd
- Paper: "RSD: An Open-Source Superscalar RISC-V Processor"
- Spectre/Meltdown: Relevant for OoO attack surfaces
