// Testbench for PipelinedRefDivider
`timescale 1ns/1ps

module tb_PipelinedRefDivider;

    logic        clk;
    logic        rst_ni;
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    PipelinedRefDivider dut (
        .clk(clk),
        .rst_ni(rst_ni),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin clk = 1'b0; forever #5 clk = ~clk; end
    initial begin $dumpfile("PipelinedRefDivider.vcd"); $dumpvars(0, tb_PipelinedRefDivider); end
    
    initial begin
        rst_ni = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 rst_ni = 1'b1;
        repeat(30000) begin
            @(posedge clk); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge clk); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
