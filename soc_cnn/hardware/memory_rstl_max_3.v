`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/30/2021 04:22:21 AM
// Design Name: 
// Module Name: memory_rstl_max_3
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


module memory_rstl_max_3
#(
    //memory_rstl_max
    parameter n_c = 5'd26,  //number of column matrix image 
    parameter n_r = 5'd26,  //number of rows matrix image 
    parameter dataWidthImg= 16,
    parameter numWeightRstlConv = 507,
    parameter addressWidthRstlConv = 10, 
    parameter dataWidthRstlConv = 8
)
( 
    input clk,
    input wen,
//    input ren,
    input [addressWidthRstlConv-1:0] wadd,
//    input [addressWidthRstlConv-1:0] radd1,
//    input [addressWidthRstlConv-1:0] radd2,
    input signed [dataWidthRstlConv-1:0] data_in

//    output reg [dataWidthImg-1:0] rdata0,
//    output reg [dataWidthImg-1:0] rdata1,
//    output reg [dataWidthImg-1:0] rdata2,
//    output reg [dataWidthImg-1:0] rdata3 

);
    
    reg [dataWidthRstlConv-1:0] mem [numWeightRstlConv-1:0];

//    wire [11-1:0] p_img_0;
//    wire [11-1:0] p_img_1;
//    wire [11-1:0] p_img_2;
//    wire [11-1:0] p_img_3;
    
   
//    assign p_img_0 = (radd2 + 0) + (radd1*n_c);
//    assign p_img_1 = (radd2 + 1) + (radd1*n_c);
//    assign p_img_2 = (radd2 + 26) + (radd1*n_c);
//    assign p_img_3 = (radd2 + 27) + (radd1*n_c);        


    always @(posedge clk)
	begin
	   if (wen & (wadd < numWeightRstlConv))
	   begin
	       mem[wadd] <= data_in;
	       $display("wadd1_max3, %d",wadd,data_in); 

	   end
	end 
    
//    always @(posedge clk)
//    begin
//        if (ren)
//        begin
//            rdata0 <= mem[p_img_0];
//            rdata1 <= mem[p_img_1];
//            rdata2 <= mem[p_img_2];
//            rdata3 <= mem[p_img_3];
//        end
//    end 
    
endmodule
