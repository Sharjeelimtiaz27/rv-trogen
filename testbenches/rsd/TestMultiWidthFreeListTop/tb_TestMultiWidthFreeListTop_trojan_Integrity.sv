// Testbench for TestMultiWidthFreeListTop_trojan_Integrity
`timescale 1ns/1ps

module tb_TestMultiWidthFreeListTop_trojan_Integrity;

    logic        clk_p;
    logic        rst;
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    TestMultiWidthFreeListTop_trojan_Integrity dut (
        .clk_p(clk_p),
        .rst(rst),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin clk_p = 1'b0; forever #5 clk_p = ~clk_p; end
    initial begin $dumpfile("TestMultiWidthFreeListTop_trojan_Integrity.vcd"); $dumpvars(0, tb_TestMultiWidthFreeListTop_trojan_Integrity); end
    
    initial begin
        rst = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 rst = 1'b1;
        repeat(30000) begin
            @(posedge clk_p); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge clk_p); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
