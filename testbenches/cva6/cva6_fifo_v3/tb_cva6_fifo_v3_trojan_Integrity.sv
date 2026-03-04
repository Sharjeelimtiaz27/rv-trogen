// Auto-generated minimal testbench for cva6_fifo_v3_trojan_Integrity
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_cva6_fifo_v3_trojan_Integrity;
    logic clk_i;
    logic rst_ni;

    cva6_fifo_v3_trojan_Integrity dut ( .clk_i(clk_i), .rst_ni(rst_ni) );

    initial begin clk_i = 1'b0; forever #5 clk_i = ~clk_i; end
    initial begin $dumpfile("cva6_fifo_v3_trojan_Integrity.vcd"); $dumpvars(0, tb_cva6_fifo_v3_trojan_Integrity); end
    initial begin
        rst_ni = 1'b0; #100; rst_ni = 1'b1;
        #300000; $finish;
    end
endmodule
