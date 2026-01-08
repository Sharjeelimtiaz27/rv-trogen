/**
 * Hardware Trojan Template: Information Leakage
 * 
 * Category: Combinational Logic
 * Pattern Type: Information Leakage
 * 
 * Source: Trust-Hub Benchmark RSA-T600
 * Reference: https://trust-hub.org/benchmarks/RSA-T600
 * 
 * Description:
 *   Condition-based data leakage for combinational logic.
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module cva6_accel_first_pass_decoder_trojan (
    input  logic is_control_flow_instr_o,
    input  logic [{{WIDTH}}-1:0] {{SECRET_DATA}},
    output logic [{{WIDTH}}-1:0] {{LEAK_PORT}}
);

    assign {{LEAK_PORT}} = is_control_flow_instr_o ? 
                           {{SECRET_DATA}} : 
                           '0;

endmodule