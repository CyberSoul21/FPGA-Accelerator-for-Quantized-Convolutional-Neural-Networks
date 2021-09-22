`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/29/2021 12:37:11 AM
// Design Name: 
// Module Name: predictMax
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


module predictMax
#(
    //MaxPooling
    parameter addressWidthConv=10, dataWidthMax=8, dataWidthBCD = 4,
    parameter s0 = 4'b0000, s1 = 4'b0001, s2 = 4'b0010, s3 = 4'b0011, s4 = 4'b0100,
    parameter s5 = 4'b0101, s6 = 4'b0110, s7 = 4'b0111, s8 = 4'b1000, s9 = 4'b1001,
    parameter s10 = 4'b1010, s11 = 4'b1011, s12 = 4'b1100, s13 = 4'b1101, s14 = 4'b1110
)
(
    input clk,
    input clk_div,
    input en,
    input rst,
    input [dataWidthMax-1:0] num_dens_0,
    input [dataWidthMax-1:0] num_dens_1,
    input [dataWidthMax-1:0] num_dens_2,
    input [dataWidthMax-1:0] num_dens_3,
    input [dataWidthMax-1:0] num_dens_4,
    input [dataWidthMax-1:0] num_dens_5,
    input [dataWidthMax-1:0] num_dens_6,
    input [dataWidthMax-1:0] num_dens_7,
    input [dataWidthMax-1:0] num_dens_8,
    input [dataWidthMax-1:0] num_dens_9,
    output signed [dataWidthBCD-1:0]predict,
    output reg predict_ok

);

    //FSM
    reg [3:0] present_state, next_state; //ok
    
    reg [dataWidthBCD-1:0] max1;
    reg [dataWidthBCD-1:0] max2;
    reg [dataWidthBCD-1:0] max3;
    reg [dataWidthBCD-1:0] max4;
    reg [dataWidthBCD-1:0] max5;
    reg [dataWidthMax-1:0] aux_max1;
    reg [dataWidthMax-1:0] aux_max2;
    reg [dataWidthMax-1:0] aux_max3;
    reg [dataWidthMax-1:0] aux_max4;
    reg [dataWidthMax-1:0] aux_max5;
    reg [dataWidthMax-1:0] aux_max6;
    reg [dataWidthMax-1:0] aux_max7;
    reg [dataWidthMax-1:0] aux_max8;    
    reg [dataWidthBCD-1:0] max6;
    reg [dataWidthBCD-1:0] max7;
    reg [dataWidthBCD-1:0] max8;
    reg [dataWidthBCD-1:0] max9;    

    initial
    begin
        predict_ok = 0;
                    max1 <= 0;
                    aux_max1 <= 0;        
                    max2 <= 0;
                    aux_max2 <= 0;
                    max3 <= 0;
                    aux_max3 <= 0;
                    max4 <= 0;
                    aux_max4 <= 0;
                    max5 <= 0;
                    aux_max5 <= 0; 
                    max6 <= 0;
                    aux_max6 <= 0; 
                    max7 <= 0;
                    aux_max7 <= 0; 
                    max8 <= 0;
                    aux_max8 <= 0; 
                    max9 <= 10;
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

    always @(negedge clk)
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

    always @ (negedge clk) begin
      case (present_state)
        s0: begin
                if($signed(num_dens_0) >= $signed(num_dens_1))
                begin
                    max1 <= $signed(4'd0);
                    aux_max1 <= $signed(num_dens_0);
                    max2 <= 0;
                    aux_max2 <= 0;
                    max3 <= 0;
                    aux_max3 <= 0;
                    max4 <= 0;
                    aux_max4 <= 0;
                    max5 <= 0;
                    aux_max5 <= 0; 
                                                                                                                                                              
                end
                else
                begin
                    max1 <= $signed(4'd1);
                    aux_max1 <= $signed(num_dens_1);
                end
                if($signed(num_dens_2) >= $signed(num_dens_3))
                begin
                    max2 <= $signed(4'd2);
                    aux_max2 <= $signed(num_dens_2);
                end
                else
                begin
                    max2 <= $signed(4'd3);
                    aux_max2 <= $signed(num_dens_3);
                end
                if($signed(num_dens_4) >= $signed(num_dens_5))
                begin
                    max3 <= $signed(4'd4);
                    aux_max3 <= $signed(num_dens_4);
                end
                else
                begin
                    max3 <= $signed(4'd5);
                    aux_max3 <= $signed(num_dens_5);
                end
                if($signed(num_dens_6) >= $signed(num_dens_7))
                begin
                    max4 <= $signed(4'd6);
                    aux_max4 <= $signed(num_dens_6);
                end
                else
                begin
                    max4 <= $signed(4'd7);
                    aux_max4 <= $signed(num_dens_7);
                end
                if($signed(num_dens_8) >= $signed(num_dens_9))
                begin
                    max5 <= $signed(4'd8);
                    aux_max5 <= $signed(num_dens_8);
                end
                else
                begin
                    max5 <= $signed(4'd9);
                    aux_max5 <= $signed(num_dens_9);
                end                                                                  
                predict_ok <= 0;
            end          
        s1: begin
                if($signed(aux_max1) >= $signed(aux_max2))
                begin
                    max6 <= $signed(max1);
                    aux_max6 <= $signed(aux_max1);
                end
                else
                begin
                    max6 <= $signed(max2);
                    aux_max6 <= $signed(aux_max2);
                end
                if($signed(aux_max3) >= $signed(aux_max4))
                begin
                    max7 <= $signed(max3);
                    aux_max7 <= $signed(aux_max3);
                end
                else
                begin
                    max7 <= $signed(max4);
                    aux_max7 <= $signed(aux_max4);
                end                
            end
        s2: begin
                if($signed(aux_max6) >= $signed(aux_max7))
                begin
                    max8 <= $signed(max6);
                    aux_max8 <= $signed(aux_max6);
                end
                else
                begin
                    max8 <= $signed(max7);
                    aux_max8 <= $signed(aux_max7);
                end  
            end  
        s3: begin
                if($signed(aux_max8) >= $signed(aux_max5))
                begin
                    max9 <= $signed(max8);
                end
                else
                begin
                    max9 <= $signed(max5);
                end 
            end    
        s4: begin
                predict_ok <= 0;
            end 
      endcase 
    end 

    assign predict = $signed(max9);



endmodule
