// Testbench for ibex_alu_trojan_Covert
`timescale 1ns/1ps

module tb_ibex_alu_trojan_Covert;

    logic        clk_i;
    logic        instr_first_cycle_i;
    logic        wr_en_i;
    logic [31:0] wr_data_i;
    logic [31:0] rd_data_o;
    logic        rd_error_o;
    
    ibex_alu_trojan_Covert dut (
        .clk_i(clk_i),
        .instr_first_cycle_i(instr_first_cycle_i),
        .wr_en_i(wr_en_i),
        .wr_data_i(wr_data_i),
        .rd_data_o(rd_data_o),
        .rd_error_o(rd_error_o)
    );
    
    initial begin clk_i = 1'b0; forever #5 clk_i = ~clk_i; end
    initial begin $dumpfile("ibex_alu_trojan_Covert.vcd"); $dumpvars(0, tb_ibex_alu_trojan_Covert); end
    
    initial begin
        instr_first_cycle_i = 1'b0; wr_en_i = 1'b0; wr_data_i = 32'h0;
        #100 instr_first_cycle_i = 1'b1;
        repeat(30000) begin
            @(posedge clk_i); wr_data_i = wr_data_i + 32'd1; wr_en_i = 1'b1;
            @(posedge clk_i); wr_en_i = 1'b0;
        end
        $display("Simulation complete: 30,000 cycles"); $finish;
    end
endmodule
