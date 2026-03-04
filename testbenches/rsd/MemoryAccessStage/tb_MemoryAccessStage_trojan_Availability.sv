// Auto-generated minimal testbench for MemoryAccessStage_trojan_Availability
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_MemoryAccessStage_trojan_Availability;
    logic clk;
    logic rst;

    MemoryAccessStage_trojan_Availability dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("MemoryAccessStage_trojan_Availability.vcd"); $dumpvars(0, tb_MemoryAccessStage_trojan_Availability); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
