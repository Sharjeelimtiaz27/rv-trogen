// Auto-generated minimal testbench for ComplexIntegerExecutionStage
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_ComplexIntegerExecutionStage;
    logic clk;
    logic rst;

    ComplexIntegerExecutionStage dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("ComplexIntegerExecutionStage.vcd"); $dumpvars(0, tb_ComplexIntegerExecutionStage); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
