// Auto-generated minimal testbench for TestMain_trojan_Leak
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_TestMain_trojan_Leak;
    logic clk;
    logic rst;

    TestMain_trojan_Leak dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("TestMain_trojan_Leak.vcd"); $dumpvars(0, tb_TestMain_trojan_Leak); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
