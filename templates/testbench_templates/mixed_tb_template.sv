`timescale 1ns/1ps

/**
 * Mixed Logic Module Testbench Template
 * Pattern-based stimulus for trojan validation
 * Handles modules with both sequential and combinational logic
 * 
 * Template Variables:
 * {{MODULE_NAME}} - Name of the module under test
 * {{VARIANT}} - 'original' or 'trojan_DoS' or 'trojan_Integrity' etc.
 * {{INPUT_DECLARATIONS}} - Input signal declarations
 * {{OUTPUT_DECLARATIONS}} - Output signal declarations
 * {{PORT_CONNECTIONS}} - Port connection list
 * {{CLOCK_SIGNAL}} - Clock signal name (if present)
 * {{RESET_SIGNAL}} - Reset signal name (if present)
 * {{HAS_CLOCK}} - true/false
 * {{HAS_RESET}} - true/false
 * {{STIMULUS_PATTERN}} - Test stimulus code
 */

module tb_{{MODULE_NAME}}_{{VARIANT}};

  // ============================================================
  // Signal Declarations
  // ============================================================
  
  // Clock and reset (if present)
{{CLOCK_RESET_DECLARATIONS}}
  
  // Input signals (driven by testbench)
{{INPUT_DECLARATIONS}}
  
  // Output signals (from DUT)
{{OUTPUT_DECLARATIONS}}

  // ============================================================
  // Clock Generation (if needed)
  // ============================================================
  
{{CLOCK_GENERATION}}

  // ============================================================
  // Device Under Test
  // ============================================================
  
  {{MODULE_NAME}}_{{VARIANT}} dut (
{{PORT_CONNECTIONS}}
  );

  // ============================================================
  // Test Sequence
  // ============================================================
  
  initial begin
    // VCD dump for waveform analysis
    $dumpfile("{{MODULE_NAME}}_{{VARIANT}}.vcd");
    $dumpvars(0, tb_{{MODULE_NAME}}_{{VARIANT}});
    
    $display("Starting {{VARIANT}} simulation...");
    
    // ========================================
    // Reset Sequence (if applicable)
    // ========================================
{{RESET_SEQUENCE}}
    
    // ========================================
    // Pattern-Based Test Stimulus
    // ========================================
    
{{STIMULUS_PATTERN}}
    
    // ========================================
    // Observation Period
    // ========================================
{{OBSERVATION_PERIOD}}
    
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
