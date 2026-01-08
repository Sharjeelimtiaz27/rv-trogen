/**
 * Hardware Trojan Template: Covert Channel
 * 
 * Category: Combinational Logic
 * Pattern Type: Covert Channel
 * 
 * Description:
 *   Simplified covert channel for combinational logic.
 *   Note: Sequential version provides timing modulation.
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module IntAdder_trojan (
    input  logic {{SECRET_BIT}},
    input  logic {{NORMAL_SIGNAL}},
    output logic {{OBSERVABLE_SIGNAL}}
);

    assign {{OBSERVABLE_SIGNAL}} = {{SECRET_BIT}} ? 
                                   ~{{NORMAL_SIGNAL}} : 
                                   {{NORMAL_SIGNAL}};

endmodule