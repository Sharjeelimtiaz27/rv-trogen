/**
 * Hardware Trojan Template: Performance Degradation
 * 
 * Category: Combinational Logic
 * Pattern Type: Performance Degradation
 * 
 * Description:
 *   Simplified performance degradation for combinational logic.
 *   Note: Sequential version provides better control.
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module decoder_trojan (
    input  logic debug_req_i,
    input  logic {{NORMAL_VALID}},
    output logic {{DEGRADED_VALID}}
);

    assign {{DEGRADED_VALID}} = debug_req_i ? 
                                1'b0 : 
                                {{NORMAL_VALID}};

endmodule