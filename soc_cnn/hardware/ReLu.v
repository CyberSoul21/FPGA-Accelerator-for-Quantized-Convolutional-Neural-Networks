`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/24/2021 07:47:40 PM
// Design Name: 
// Module Name: ReLu
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


module ReLu
#(
    parameter s0 = 4'b0000, s1 = 4'b0001, s2 = 4'b0010, s3 = 4'b0011, s4 = 4'b0100,
    parameter s5 = 4'b0101, s6 = 4'b0110, s7 = 4'b0111, s8 = 4'b1000, s9 = 4'b1001,
    parameter s10 = 4'b1010, s11 = 4'b1011, s12 = 4'b1100, s13 = 4'b1101, s14 = 4'b1110,
    
    //quantization
    parameter q = 64'd2014687024, //q = 31'b1111000000101011010111100110000
    parameter mask = 8'd255,
    parameter zero = 1'd0,
    parameter one = 1'd1,
    parameter offset_ent = 6,
    parameter offset_sor = -1
)
(
    input clk, rst, 
    input [8:0] num_quant, 
    output [7:0] num, 
    output sig_ok
);

    reg [8:0] aux_num;
    reg [8:0] aux_num2;
    reg [8:0] aux_num3;
    reg [8:0] aux_num4;
    reg       aux_ok;
    reg [3:0] present_state, next_state;   

    always @(posedge clk or posedge rst) //Present estate // always @(clk) //Present estate 
    begin
        if(rst)
        begin
            present_state <= s0;
    
        end
        else
        begin
            present_state <= next_state;
        end    
    end    

    always @(posedge clk) //always @(*)
    begin
        case(present_state)
            s0:
                next_state <= s1;                
            s1:
                next_state <= s2;
            s2:
                next_state <= s3;
            s3:
                next_state <= s4;                                
                                
        endcase                
    end


    always @ (posedge clk) begin //always @ (*) begin
      case (present_state)
        s0: begin
                if($signed(num_quant) <= $signed(-8'd1))
                    aux_num <= 0;
                else    
                    aux_num <= num_quant;
                aux_ok <= 0;    
            end          
        s1: begin
                if(aux_num >= 8'd255)
                   aux_num <= 8'd255; //+ offset_sor;
            end
        s2: begin
                aux_num2 <= $signed(aux_num + offset_sor);
            end 
        s3: begin
                if($signed(aux_num2) <= $signed(-8'd128))
                    aux_num3 <= -8'd128;
                else
                    aux_num3 <=  aux_num2;    
            end           
        s4: begin
                if($signed(aux_num3) >= $signed(8'd127))
                    aux_num4 <= 8'd127;
                else
                    aux_num4 <= aux_num3;     
                aux_ok <= 1;    
            end             
      endcase 
    end 

    assign num = aux_num4;
    assign sig_ok = aux_ok;  


endmodule

