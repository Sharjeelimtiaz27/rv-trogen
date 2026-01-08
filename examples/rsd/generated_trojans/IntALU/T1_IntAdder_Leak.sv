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

module IntAdder_trojan (
    input  logic DataPath,
    input  logic [{{WIDTH}}-1:0] {{SECRET_DATA}},
    output logic [{{WIDTH}}-1:0] {{LEAK_PORT}}
);

    assign {{LEAK_PORT}} = DataPath ? 
                           {{SECRET_DATA}} : 
                           '0;

endmodule