module tb_ibex_csr_trojan_DoS;

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
  ibex_csr_trojan_DoS dut (
    .clk_i(clk_i),
    .rst_ni(rst_ni),
    .wr_data_i(wr_data_i),
    .wr_en_i(wr_en_i),
    .rd_data_o(rd_data_o),
    .rd_error_o(rd_error_o)
  );

  initial begin
    $dumpfile("ibex_csr_trojan_DoS.vcd");
    $dumpvars(0, tb_ibex_csr_trojan_DoS);

    // Reset sequence
    rst_ni = 0;
    repeat(10) @(posedge clk_i);
    rst_ni = 1;
    @(posedge clk_i);

    // Test stimulus (30,000 cycles for trojan thresholds: 5000-25000)
    integer i;
    for (i = 0; i < 30000; i = i + 1) begin
      @(posedge clk_i);
      wr_data_i = i;  // Incrementing pattern
      wr_en_i = 1;
      @(posedge clk_i);
      wr_en_i = 0;
      @(posedge clk_i);
    end

    repeat(100) @(posedge clk_i);
    $display("trojan_DoS simulation done");
    $finish;
  end

  // Timeout watchdog
  initial begin
    #3000000000;  // 3 second timeout
    $display("ERROR: Simulation timeout!");
    $finish;
  end

endmodule