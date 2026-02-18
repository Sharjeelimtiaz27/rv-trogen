// Testbench for TestDCacheTop_trojan_DoS
`timescale 1ns/1ps

module tb_TestDCacheTop_trojan_DoS;

    logic        clk_p;
    logic        rstTrigger;
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    TestDCacheTop_trojan_DoS dut (
        .clk_p(clk_p),
        .rstTrigger(rstTrigger),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin clk_p = 1'b0; forever #5 clk_p = ~clk_p; end
    initial begin $dumpfile("TestDCacheTop_trojan_DoS.vcd"); $dumpvars(0, tb_TestDCacheTop_trojan_DoS); end
    
    initial begin
        rstTrigger = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 rstTrigger = 1'b1;
        repeat(30000) begin
            @(posedge clk_p); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge clk_p); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
