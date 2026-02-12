`timescale 1ns/1ps

/**
 * Combinational Module Testbench Template
 * Pattern-based stimulus for trojan validation
 * 
 * Template Variables:
 * {{MODULE_NAME}} - Name of the module under test
 * {{VARIANT}} - 'original' or 'trojan_DoS' or 'trojan_Integrity' etc.
 * {{INPUT_DECLARATIONS}} - Input signal declarations
 * {{OUTPUT_DECLARATIONS}} - Output signal declarations
 * {{PORT_CONNECTIONS}} - Port connection list
 * {{STIMULUS_PATTERN}} - Test stimulus code
 */

module tb_{{MODULE_NAME}}_{{VARIANT}};

  // ============================================================
  // Signal Declarations
  // ============================================================
  
  // Input signals (driven by testbench)
{{INPUT_DECLARATIONS}}
  
  // Output signals (from DUT)
{{OUTPUT_DECLARATIONS}}

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
    // Pattern-Based Test Stimulus
    // ========================================
    // Combinational modules respond immediately
    // Test with incrementing/pattern-based inputs
    
{{STIMULUS_PATTERN}}
    
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
