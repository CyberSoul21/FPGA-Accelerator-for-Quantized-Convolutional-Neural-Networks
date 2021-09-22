`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/29/2021 01:12:04 AM
// Design Name: 
// Module Name: display
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


module display(
     clk,
     bcd,
     number
    );
     
     input clk;
     input [3:0] bcd;
     output reg [6:0] number;


    always @(posedge clk)
    begin
        case (bcd) 
                         
            4'd0 : number <= 7'b1111110;
            4'd1 : number <= 7'b0110000;
            4'd2 : number <= 7'b1101101;
            4'd3 : number <= 7'b1111001;
            4'd4 : number <= 7'b0110011;
            4'd5 : number <= 7'b1011011;
            4'd6 : number <= 7'b1011111;
            4'd7 : number <= 7'b1110000;
            4'd8 : number <= 7'b1111111;
            4'd9 : number <= 7'b1111011;            
            
            default : number <= 7'b0000000; 
        endcase
    end
    
    
endmodule