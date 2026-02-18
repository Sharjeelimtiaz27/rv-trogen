// Testbench for Axi4LitePlToPsControlRegister_trojan_Leak
`timescale 1ns/1ps

module tb_Axi4LitePlToPsControlRegister_trojan_Leak;

    logic        S_AXI_ACLK;
    logic        rst_ni;
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    Axi4LitePlToPsControlRegister_trojan_Leak dut (
        .S_AXI_ACLK(S_AXI_ACLK),
        .rst_ni(rst_ni),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin S_AXI_ACLK = 1'b0; forever #5 S_AXI_ACLK = ~S_AXI_ACLK; end
    initial begin $dumpfile("Axi4LitePlToPsControlRegister_trojan_Leak.vcd"); $dumpvars(0, tb_Axi4LitePlToPsControlRegister_trojan_Leak); end
    
    initial begin
        rst_ni = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 rst_ni = 1'b1;
        repeat(30000) begin
            @(posedge S_AXI_ACLK); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge S_AXI_ACLK); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
