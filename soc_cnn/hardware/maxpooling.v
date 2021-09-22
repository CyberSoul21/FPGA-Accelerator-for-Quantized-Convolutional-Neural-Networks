`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 10:17:06 PM
// Design Name: 
// Module Name: maxpooling
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


module maxpooling
#(
    //MaxPooling
    parameter addressWidthConv=10, dataWidthMax=8,
    parameter s0 = 4'b0000, s1 = 4'b0001, s2 = 4'b0010, s3 = 4'b0011, s4 = 4'b0100,
    parameter s5 = 4'b0101, s6 = 4'b0110, s7 = 4'b0111, s8 = 4'b1000, s9 = 4'b1001,
    parameter s10 = 4'b1010, s11 = 4'b1011, s12 = 4'b1100, s13 = 4'b1101, s14 = 4'b1110
)
(
    input clk,
    input clk_div,
    input en,
    input rst,
    input [dataWidthMax-1:0] rdata_conv0,
    input [dataWidthMax-1:0] rdata_conv1,
    input [dataWidthMax-1:0] rdata_conv2,
    input [dataWidthMax-1:0] rdata_conv3,
    output signed [dataWidthMax-1:0]max,
    output reg save_rstl

);

    //FSM
    reg [3:0] present_state, next_state; //ok
    
    reg [dataWidthMax-1:0] max1;
    reg [dataWidthMax-1:0] max2;
    reg [dataWidthMax-1:0] max3;

    initial
    begin
        save_rstl = 0;
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
                if($signed(rdata_conv0) >= $signed(rdata_conv1))
                begin
                    max1 <= $signed(rdata_conv0);
                end
                else
                begin
                    max1 <= $signed(rdata_conv1);
                end
                save_rstl <= 0;
            end          
        s1: begin
                if($signed(rdata_conv2) >= $signed(rdata_conv3))
                begin
                    max2 <= $signed(rdata_conv2);
                end
                else
                begin
                    max2 <= $signed(rdata_conv3);
                end
            end
        s2: begin
                if($signed(max1) >= $signed(max2))
                begin
                    max3 <= $signed(max1);
                end
                else
                begin
                    max3 <= $signed(max2);
                end  
            end  
        s3: begin
                save_rstl <= 1;
            end    
        s4: begin
                save_rstl <= 0;
            end 
      endcase 
    end 

    assign max = $signed(max3);



endmodule

