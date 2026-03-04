// Auto-generated minimal testbench for TestDCacheFiller
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_TestDCacheFiller;
    logic clk;
    logic rst;

    TestDCacheFiller dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("TestDCacheFiller.vcd"); $dumpvars(0, tb_TestDCacheFiller); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
