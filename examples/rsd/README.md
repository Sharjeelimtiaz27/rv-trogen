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

### Core Control ⭐ High Priority
- \ActiveListManager.sv\ - Instruction tracking (OoO)
- \SchedulerCSR.sv\ - CSR scheduler
- \CommitStage.sv\ - Commit logic
- \ReorderBuffer.sv\ - Reorder Buffer (ROB)

### Execution Units
- \IntegerIssueStage.sv\ - Integer issue
- \ComplexIntegerExecutionStage.sv\ - Complex ALU
- \MemoryExecutionStage.sv\ - Memory ops
- \LoadStoreUnit.sv\ - LSU

### Out-of-Order Logic
- \RenameStage.sv\ - Register renaming
- \DispatchStage.sv\ - Instruction dispatch
- \ReplayQueue.sv\ - Replay mechanism
- \RecoveryManager.sv\ - Exception recovery

---

## 🔒 Security-Critical Modules

**Priority 1 (OoO-Specific):**
1. \ActiveListManager.sv\ - Speculative execution control
2. \ReorderBuffer.sv\ - State consistency, rollback
3. \SchedulerCSR.sv\ - Privilege control

**Priority 2 (Execution):**
4. \LoadStoreUnit.sv\ - Memory ordering attacks
5. \CommitStage.sv\ - Integrity control
6. \RecoveryManager.sv\ - Exception manipulation

**Special Attack Surfaces:**
- Speculative execution windows (Spectre-like)
- ROB timing channels (Meltdown-like)
- Replay queue manipulation
- Register renaming confusion

---

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

- ⏸️ RTL modules not yet downloaded (Step 13)
- ⏸️ Trojan generation pending
- ⏸️ Pattern adaptation for OoO pending
- ⏸️ Validation pending

---

## 📚 References

- RSD GitHub: https://github.com/rsd-devel/rsd
- Paper: "RSD: An Open-Source Superscalar RISC-V Processor"
- Spectre/Meltdown: Relevant for OoO attack surfaces
