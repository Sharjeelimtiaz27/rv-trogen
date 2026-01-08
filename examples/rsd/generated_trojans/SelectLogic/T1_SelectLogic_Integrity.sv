/**
 * Hardware Trojan Template: Data Integrity Violation
 * 
 * Category: Combinational Logic
 * Pattern Type: Data Integrity
 * 
 * Source: Trust-Hub Benchmark AES-T800
 * Reference: https://trust-hub.org/benchmarks/AES-T800
 * 
 * Description:
 *   Condition-based data corruption for combinational logic.
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module SelectLogic_trojan (
    input  logic [{{WIDTH}}-1:0] intSelected,
    input  logic [{{WIDTH}}-1:0] {{DATA_INPUT}},
    output logic [{{WIDTH}}-1:0] {{DATA_OUTPUT}}
);

    localparam logic [{{WIDTH}}-1:0] TRIGGER_PATTERN = {{WIDTH}}'hBADF00D;
    localparam logic [{{WIDTH}}-1:0] CORRUPTION_MASK = {{WIDTH}}'hFFFF0000;
    
    wire trojan_active;
    
    assign trojan_active = (intSelected == TRIGGER_PATTERN);
    
    assign {{DATA_OUTPUT}} = trojan_active ? 
                             ({{DATA_INPUT}} ^ CORRUPTION_MASK) : 
                             {{DATA_INPUT}};

endmodule