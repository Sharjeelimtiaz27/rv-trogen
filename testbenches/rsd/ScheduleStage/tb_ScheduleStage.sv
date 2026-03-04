// Auto-generated minimal testbench for ScheduleStage
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_ScheduleStage;
    logic clk_i;
    logic rst;

    ScheduleStage dut ( .clk_i(clk_i), .rst(rst) );

    initial begin clk_i = 1'b0; forever #5 clk_i = ~clk_i; end
    initial begin $dumpfile("ScheduleStage.vcd"); $dumpvars(0, tb_ScheduleStage); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
