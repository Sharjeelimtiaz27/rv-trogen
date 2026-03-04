// Auto-generated minimal testbench for DCacheController
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_DCacheController;
    logic clk;
    logic first;

    DCacheController dut ( .clk(clk), .first(first) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("DCacheController.vcd"); $dumpvars(0, tb_DCacheController); end
    initial begin
        first = 1'b0; #100; first = 1'b1;
        #300000; $finish;
    end
endmodule
