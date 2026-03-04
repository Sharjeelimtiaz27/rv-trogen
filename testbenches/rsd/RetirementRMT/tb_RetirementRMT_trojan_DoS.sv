// Auto-generated minimal testbench for RetirementRMT_trojan_DoS
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_RetirementRMT_trojan_DoS;
    logic clk;
    logic rstWriteLogRegNum;

    RetirementRMT_trojan_DoS dut ( .clk(clk), .rstWriteLogRegNum(rstWriteLogRegNum) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("RetirementRMT_trojan_DoS.vcd"); $dumpvars(0, tb_RetirementRMT_trojan_DoS); end
    initial begin
        rstWriteLogRegNum = 1'b0; #100; rstWriteLogRegNum = 1'b1;
        #300000; $finish;
    end
endmodule
