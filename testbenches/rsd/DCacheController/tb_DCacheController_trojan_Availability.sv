// Auto-generated minimal testbench for DCacheController_trojan_Availability
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_DCacheController_trojan_Availability;
    logic clk;
    logic first;

    DCacheController_trojan_Availability dut ( .clk(clk), .first(first) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("DCacheController_trojan_Availability.vcd"); $dumpvars(0, tb_DCacheController_trojan_Availability); end
    initial begin
        first = 1'b0; #100; first = 1'b1;
        #300000; $finish;
    end
endmodule
