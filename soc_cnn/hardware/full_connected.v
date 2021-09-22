`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/12/2021 09:58:17 AM
// Design Name: 
// Module Name: full_connected
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module full_connected#(
    //full connected
    parameter addressWidthConv=10, dataWidthMax=8, dataWidthWeight=16, dataWidthAux=16,
    parameter s0 = 4'b0000, s1 = 4'b0001, s2 = 4'b0010, s3 = 4'b0011, s4 = 4'b0100,
    parameter s5 = 4'b0101, s6 = 4'b0110, s7 = 4'b0111, s8 = 4'b1000, s9 = 4'b1001,
    parameter s10 = 4'b1010, s11 = 4'b1011, s12 = 4'b1100, s13 = 4'b1101, s14 = 4'b1110,
    
    parameter dataWidthCount= 10,
    parameter numWeightRstlMax = 507,
    
    parameter q = 63'd1841896888, //q = 31'b1111000000101011010111100110000
    parameter mask = 32'd511,
    parameter exponent = 8'd9,
//    parameter zero = 1'd0,
//    parameter one = 1'd1,
    parameter offset_ent =  1,
    parameter offset_sor = -1,
    parameter offset_fil =  0, 
     
     
     parameter bias = -16'd48
    
    
  
    
    
)
(
    input clk,
    input clk_div,
    input en,
    input rst,
    input[dataWidthCount-1:0] pos_memory,
    input [dataWidthMax-1:0] idata_max,
    input [dataWidthMax-1:0] idata_weight,
    output [dataWidthMax-1:0] num_dens,
    output reg den_ok,
    output quant_ok
);


    

    //FSM
    reg [3:0] present_state, next_state; //ok
    reg  [dataWidthWeight-1:0] rstl_mult;
    reg  [dataWidthWeight-1:0] rstl_sum;
    reg  [dataWidthAux-1:0] aux_max;
    reg  [dataWidthAux-1:0] aux_weight;
    
    //reg den_ok;
    //reg rst_quant;
    reg  [63:0] num;
    wire [8:0] num_quant;
    wire quant_ok_wire;
    


    quantization #(.q(q),.mask(mask),.exponent(exponent)) quant 
    (
        .clk(clk),
        .rst(~den_ok),
        .a(num),
        .num_quant(num_quant),
        .sig_ok(quant_ok_wire)
    );


    
    initial
    begin
        rstl_sum <= 0;
        rstl_mult <= 0;
        den_ok <= 0;
        num <= 0;
        //rst_quant <= 0;

    end
  
    
    always @(posedge clk) //Present estate 
    begin
        if(rst)
        begin
            present_state = 0; 
        end
        else if(en)
        begin
            if(clk_div == 1)
            begin
                present_state <= s0;
                
            end
            else
            begin
                present_state <= next_state;
            end     
        end            
    end    

    always @(negedge clk) //negedge
    begin
        case(present_state)
                s0:
                    next_state <= s1;                
                s1:
                    next_state <= s2;
                s2:
                    next_state <= s3;
                                                                          
            endcase 
    end


    always @ (negedge clk) begin //always @ (posedge clk) begin
        if(rst)
        begin
           den_ok <= 0;
           rstl_sum <= 0;
        end    
      case (present_state)
        s0: begin
                aux_weight <= $signed(idata_weight);
                aux_max <= $signed(idata_max);
     
            end          
        s1: begin
                rstl_mult <= $signed(aux_weight*aux_max);

            end
        s2: begin
                rstl_sum <= $signed(rstl_sum + rstl_mult);                
            end
        s3: begin
            if(pos_memory == (numWeightRstlMax - 1 + 1 +1))
            begin
                den_ok <= 1;
                num <= $signed(rstl_sum + bias);               
            end                
            end
                                     
      endcase
    end
    
  
    
    assign quant_ok = quant_ok_wire;   
    assign num_dens = $signed(num_quant + offset_sor);  

    
endmodule



