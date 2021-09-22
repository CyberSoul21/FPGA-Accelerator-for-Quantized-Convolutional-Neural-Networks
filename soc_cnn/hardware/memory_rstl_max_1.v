`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 10:17:44 PM
// Design Name: 
// Module Name: memory_rstl_max_1
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



module memory_rstl_max_1
#(
    //memory_rstl_max
    parameter n_c = 5'd26,  //number of column matrix image 
    parameter n_r = 5'd26,  //number of rows matrix image 
    parameter dataWidthImg= 16,
    parameter numWeightRstlConv = 507,
    //parameter numWeightRstlConv = 169,
    parameter addressWidthRstlConv = 10, 
    parameter dataWidthRstlConv = 8,
    
    //quantization
//    parameter q = 64'd2014687024, //q = 31'b1111000000101011010111100110000
//    parameter mask = 8'd255,
//    parameter zero = 1'd0,
//    parameter one = 1'd1,
    parameter offset_ent =  1,
    parameter offset_sor = -1,
    parameter offset_fil =  0    
)
( 
    input clk,
    input clk_div,
    input wen,
    input ren,
    input [addressWidthRstlConv-1:0] wadd1,
    input [addressWidthRstlConv-1:0] wadd2,
    input [addressWidthRstlConv-1:0] wadd3,
    input [addressWidthRstlConv-1:0] radd,

    input signed [dataWidthRstlConv-1:0] data_in1,
    input signed [dataWidthRstlConv-1:0] data_in2,
    input signed [dataWidthRstlConv-1:0] data_in3,

    output reg [dataWidthRstlConv-1:0] rdata

);
   
    reg [dataWidthRstlConv-1:0] mem_rstl_max[numWeightRstlConv-1:0];
      


    always @(posedge clk)
    begin
       if (wen & (wadd1 < numWeightRstlConv))
       begin
           mem_rstl_max[wadd1] <= data_in1;
           mem_rstl_max[wadd2] <= data_in2;
           mem_rstl_max[wadd3] <= data_in3;
//         $display("max1, %d",wadd1,data_in1);
//         $display("max1, %d",wadd2,data_in2);
//         $display("max1, %d",wadd3,data_in3);
           $display("%d",data_in1);
           $display("%d",data_in2);
           $display("%d",data_in3); 

       end
    end 

    
    always @(posedge clk_div)
    begin
        if (ren)
        begin
            rdata <= mem_rstl_max[radd] + offset_ent;
        end
    end 

    
endmodule