// Auto-generated minimal testbench for Axi4LiteDualPortBlockRAM_trojan_Covert
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module tb_Axi4LiteDualPortBlockRAM_trojan_Covert;
    logic S_AXI_ACLK;
    logic rst_ni;

    Axi4LiteDualPortBlockRAM_trojan_Covert dut ( .S_AXI_ACLK(S_AXI_ACLK), .rst_ni(rst_ni) );

    initial begin S_AXI_ACLK = 1'b0; forever #5 S_AXI_ACLK = ~S_AXI_ACLK; end
    initial begin $dumpfile("Axi4LiteDualPortBlockRAM_trojan_Covert.vcd"); $dumpvars(0, tb_Axi4LiteDualPortBlockRAM_trojan_Covert); end
    initial begin
        rst_ni = 1'b0; #100; rst_ni = 1'b1;
        #300000; $finish;
    end
endmodule
