// Auto-generated minimal testbench for TestCacheSystem_trojan_DoS
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_TestCacheSystem_trojan_DoS;
    logic clk;
    logic rst;

    TestCacheSystem_trojan_DoS dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("TestCacheSystem_trojan_DoS.vcd"); $dumpvars(0, tb_TestCacheSystem_trojan_DoS); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
