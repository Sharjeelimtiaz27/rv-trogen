// Auto-generated minimal testbench for ScheduleStage_trojan_Availability
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_ScheduleStage_trojan_Availability;
    logic clk_i;
    logic rst;

    ScheduleStage_trojan_Availability dut ( .clk_i(clk_i), .rst(rst) );

    initial begin clk_i = 1'b0; forever #5 clk_i = ~clk_i; end
    initial begin $dumpfile("ScheduleStage_trojan_Availability.vcd"); $dumpvars(0, tb_ScheduleStage_trojan_Availability); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
