// Auto-generated minimal testbench for RMT
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_RMT;
    logic clk;
    logic rstWriteLogRegNum;

    RMT dut ( .clk(clk), .rstWriteLogRegNum(rstWriteLogRegNum) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("RMT.vcd"); $dumpvars(0, tb_RMT); end
    initial begin
        rstWriteLogRegNum = 1'b0; #100; rstWriteLogRegNum = 1'b1;
        #300000; $finish;
    end
endmodule
