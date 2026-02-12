`timescale 1ns/1ps

/**
 * Sequential Module Testbench Template
 * Pattern-based stimulus for trojan validation
 * 
 * Template Variables:
 * {{MODULE_NAME}} - Name of the module under test
 * {{VARIANT}} - 'original' or 'trojan_DoS' or 'trojan_Integrity' etc.
 * {{INPUT_DECLARATIONS}} - Input signal declarations
 * {{OUTPUT_DECLARATIONS}} - Output signal declarations
 * {{PORT_CONNECTIONS}} - Port connection list
 * {{CLOCK_SIGNAL}} - Clock signal name
 * {{RESET_SIGNAL}} - Reset signal name
 * {{RESET_ACTIVE_LOW}} - true/false
 * {{STIMULUS_PATTERN}} - Test stimulus code
 */

module tb_{{MODULE_NAME}}_{{VARIANT}};

  // ============================================================
  // Signal Declarations
  // ============================================================
  
  // Clock and reset
  logic {{CLOCK_SIGNAL}} = 1'b0;
  logic {{RESET_SIGNAL}} = {{RESET_INITIAL_VALUE}};
  
  // Input signals (driven by testbench)
{{INPUT_DECLARATIONS}}
  
  // Output signals (from DUT)
{{OUTPUT_DECLARATIONS}}

  // ============================================================
  // Clock Generation
  // ============================================================
  
  // 10ns period = 100MHz clock
  always #5 {{CLOCK_SIGNAL}} = ~{{CLOCK_SIGNAL}};

  // ============================================================
  // Device Under Test
  // ============================================================
  
  {{MODULE_NAME}}_{{VARIANT}} dut (
    .{{CLOCK_SIGNAL}}({{CLOCK_SIGNAL}}),
    .{{RESET_SIGNAL}}({{RESET_SIGNAL}}),
{{PORT_CONNECTIONS}}
  );

  // ============================================================
  // Test Sequence
  // ============================================================
  
  initial begin
    // VCD dump for waveform analysis
    $dumpfile("{{MODULE_NAME}}_{{VARIANT}}.vcd");
    $dumpvars(0, tb_{{MODULE_NAME}}_{{VARIANT}});
    
    // ========================================
    // Reset Sequence
    // ========================================
    $display("Starting {{VARIANT}} simulation...");
    
    {{RESET_SIGNAL}} = {{RESET_ASSERT_VALUE}};  // Assert reset
    repeat(10) @(posedge {{CLOCK_SIGNAL}});
    {{RESET_SIGNAL}} = {{RESET_DEASSERT_VALUE}};  // Deassert reset
    repeat(5) @(posedge {{CLOCK_SIGNAL}});
    
    $display("Reset complete. Starting test stimulus...");
    
    // ========================================
    // Pattern-Based Test Stimulus
    // ========================================
    // This pattern runs long enough to trigger ALL trojans:
    // - DoS trojan: ~1000 cycles
    // - Integrity trojan: ~1500 cycles
    // - Covert trojan: ~2000 cycles
    // - Leak trojan: ~2500 cycles
    // Total: 3000 cycles for observation
    
{{STIMULUS_PATTERN}}
    
    // ========================================
    // Observation Period
    // ========================================
    $display("Test stimulus complete. Observing for 100 cycles...");
    repeat(100) @(posedge {{CLOCK_SIGNAL}});
    
    // ========================================
    // Finish
    // ========================================
    $display("{{VARIANT}} simulation done");
    $display("VCD file: {{MODULE_NAME}}_{{VARIANT}}.vcd");
    $finish;
  end

  // ============================================================
  // Timeout Watchdog
  // ============================================================
  
  initial begin
    #100000000;  // 100ms timeout
    $display("ERROR: Simulation timeout!");
    $finish;
  end

endmodule
