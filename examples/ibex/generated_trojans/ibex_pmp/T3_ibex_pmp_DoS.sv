/**
 * Hardware Trojan Template: Denial of Service (DoS)
 * 
 * Category: Combinational Logic
 * Pattern Type: Denial of Service
 * 
 * Source: Trust-Hub Benchmark AES-T1400
 * Reference: https://trust-hub.org/benchmarks/AES-T1400
 * 
 * Description:
 *   Condition-based signal disabling for combinational logic.
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module ibex_pmp_trojan (
    input  logic pmp_req_err_o,
    input  logic [{{WIDTH}}-1:0] {{TRIGGER_CONDITION}},
    input  logic {{NORMAL_OUTPUT}},
    output logic {{TROJAN_OUTPUT}}
);

    localparam logic [{{WIDTH}}-1:0] TRIGGER_PATTERN = {{WIDTH}}'hDEAD;
    
    wire trojan_active;
    
    assign trojan_active = ({{TRIGGER_CONDITION}} == TRIGGER_PATTERN);
    
    assign {{TROJAN_OUTPUT}} = trojan_active ? 
                               1'b0 : 
                               {{NORMAL_OUTPUT}};

endmodule