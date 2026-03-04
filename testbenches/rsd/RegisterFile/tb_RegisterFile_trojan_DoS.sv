// Auto-generated minimal testbench for RegisterFile_trojan_DoS
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_RegisterFile_trojan_DoS;
    logic clk;
    logic regRstIndex;

    RegisterFile_trojan_DoS dut ( .clk(clk), .regRstIndex(regRstIndex) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("RegisterFile_trojan_DoS.vcd"); $dumpvars(0, tb_RegisterFile_trojan_DoS); end
    initial begin
        regRstIndex = 1'b0; #100; regRstIndex = 1'b1;
        #300000; $finish;
    end
endmodule
