// Auto-generated minimal testbench for StoreQueue_trojan_Covert
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_StoreQueue_trojan_Covert;
    logic clk;
    logic rst;

    StoreQueue_trojan_Covert dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("StoreQueue_trojan_Covert.vcd"); $dumpvars(0, tb_StoreQueue_trojan_Covert); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
