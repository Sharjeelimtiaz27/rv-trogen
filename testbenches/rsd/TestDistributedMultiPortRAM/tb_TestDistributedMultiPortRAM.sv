// Auto-generated minimal testbench for TestDistributedMultiPortRAM
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_TestDistributedMultiPortRAM;
    logic clk;
    logic rst;

    TestDistributedMultiPortRAM dut ( .clk(clk), .rst(rst) );

    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("TestDistributedMultiPortRAM.vcd"); $dumpvars(0, tb_TestDistributedMultiPortRAM); end
    initial begin
        rst = 1'b0; #100; rst = 1'b1;
        #300000; $finish;
    end
endmodule
