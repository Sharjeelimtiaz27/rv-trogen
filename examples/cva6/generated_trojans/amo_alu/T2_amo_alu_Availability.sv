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

module amo_alu_trojan (
    input  logic amo_operand_a_i,
    input  logic {{NORMAL_VALID}},
    output logic {{DEGRADED_VALID}}
);

    assign {{DEGRADED_VALID}} = amo_operand_a_i ? 
                                1'b0 : 
                                {{NORMAL_VALID}};

endmodule