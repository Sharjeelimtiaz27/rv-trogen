// Auto-generated minimal testbench for needs_trojan_DoS
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_needs_trojan_DoS;
    logic clk_i;
    logic first;

    needs_trojan_DoS dut ( .clk_i(clk_i), .first(first) );

    initial begin clk_i = 1'b0; forever #5 clk_i = ~clk_i; end
    initial begin $dumpfile("needs_trojan_DoS.vcd"); $dumpvars(0, tb_needs_trojan_DoS); end
    initial begin
        first = 1'b0; #100; first = 1'b1;
        #300000; $finish;
    end
endmodule
