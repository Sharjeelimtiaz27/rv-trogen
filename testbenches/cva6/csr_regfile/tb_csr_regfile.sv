// Testbench for csr_regfile
`timescale 1ns/1ps

module tb_csr_regfile;

    logic        clk_i;
    logic        rst_ni;
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    csr_regfile dut (
        .clk_i(clk_i),
        .rst_ni(rst_ni),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin clk_i = 1'b0; forever #5 clk_i = ~clk_i; end
    initial begin $dumpfile("csr_regfile.vcd"); $dumpvars(0, tb_csr_regfile); end
    
    initial begin
        rst_ni = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 rst_ni = 1'b1;
        repeat(30000) begin
            @(posedge clk_i); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge clk_i); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
