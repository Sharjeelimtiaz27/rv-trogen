module tb_ibex_csr;

  // Input signals (driven by testbench)
  logic clk_i = 1'b0;
  logic rst_ni = 1'b0;
  logic [31:0] wr_data_i = 32'b0;
  logic wr_en_i = 1'b0;

  // Output signals (from DUT)
  logic [31:0] rd_data_o;
  logic rd_error_o;

  // Clock generation (10ns period = 100MHz)
  always #5 clk_i = ~clk_i;

  // Device Under Test
  ibex_csr dut (
    .clk_i(clk_i),
    .rst_ni(rst_ni),
    .wr_data_i(wr_data_i),
    .wr_en_i(wr_en_i),
    .rd_data_o(rd_data_o),
    .rd_error_o(rd_error_o)
  );

  initial begin
    // VCD dump for waveform analysis
    $dumpfile("ibex_csr_original.vcd");
    $dumpvars(0, tb_ibex_csr);

    // Reset sequence
    rst_ni = 0;  // Assert reset (active low)
    repeat(10) @(posedge clk_i);
    rst_ni = 1;  // Deassert reset
    @(posedge clk_i);

    // Test stimulus - Write operations to trigger trojan
    // Trojan threshold = 1000, so we do 2000+ operations
    repeat(2000) begin
      @(posedge clk_i);
      wr_data_i = $random;
      wr_en_i = 1;
      @(posedge clk_i);
      wr_en_i = 0;
      @(posedge clk_i);
    end

    // Additional cycles for observation
    repeat(100) @(posedge clk_i);

    $display("Original simulation done");
    $finish;
  end

  // Timeout watchdog (prevents infinite simulation)
  initial begin
    #200000000;  // 200ms timeout
    $display("ERROR: Simulation timeout!");
    $finish;
  end

endmodule