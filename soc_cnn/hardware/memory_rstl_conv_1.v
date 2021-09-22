`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/24/2021 08:05:23 PM
// Design Name: 
// Module Name: memory_rstl_conv_1
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


module memory_rstl_conv_1
#(
    //memory_rstl_conv
    parameter n_c = 5'd26,  //number of column matrix image 
    parameter n_r = 5'd26,  //number of rows matrix image 
    parameter dataWidthImg= 16,
    parameter numWeightRstlConv = 676,
    parameter addressWidthRstlConv = 10, 
    parameter dataWidthRstlConv = 8
)
( 
    input clk,
    input wen,
    input ren,
    input [addressWidthRstlConv-1:0] wadd,
    input [addressWidthRstlConv-1:0] radd1,
    input [addressWidthRstlConv-1:0] radd2,
    input signed [dataWidthRstlConv-1:0] data_in,

    output reg [dataWidthRstlConv-1:0] rdata0,
    output reg [dataWidthRstlConv-1:0] rdata1,
    output reg [dataWidthRstlConv-1:0] rdata2,
    output reg [dataWidthRstlConv-1:0] rdata3 

);
    
    reg [dataWidthRstlConv-1:0] mem_rstl_conv1 [numWeightRstlConv-1:0];

    wire [11-1:0] p_img_0;
    wire [11-1:0] p_img_1;
    wire [11-1:0] p_img_2;
    wire [11-1:0] p_img_3;
    
//    assign p_img_0 = (0+radd1)*(n_c) + (0+radd2);
//    assign p_img_1 = (0+radd1)*(n_c) + (1+radd2);
//    assign p_img_2 = (1+radd1)*(n_c) + (0+radd2);
//    assign p_img_3 = (1+radd1)*(n_c) + (1+radd2);  
    
    assign p_img_0 = (radd2 + 0) + (radd1*n_c);
    assign p_img_1 = (radd2 + 1) + (radd1*n_c);
    assign p_img_2 = (radd2 + 26) + (radd1*n_c);
    assign p_img_3 = (radd2 + 27) + (radd1*n_c);        


    always @(posedge clk)
    begin
       if (wen & (wadd < numWeightRstlConv))
       begin
           mem_rstl_conv1[wadd] <= data_in;
           //$display("conv1, %d",wadd,data_in); 
           //$display("%d",data_in);
       end
    end 
    
    always @(posedge clk)
    begin
        if (ren)
        begin
            rdata0 <= mem_rstl_conv1[p_img_0];
            rdata1 <= mem_rstl_conv1[p_img_1];
            rdata2 <= mem_rstl_conv1[p_img_2];
            rdata3 <= mem_rstl_conv1[p_img_3];
        end
    end 
endmodule







//module memory_rstl_conv_1 //test soc
//#(
//    //memory_rstl_conv
//    parameter n_c = 5'd26,  //number of column matrix image 
//    parameter n_r = 5'd26,  //number of rows matrix image 
//    parameter dataWidthImg= 16,
//    parameter numWeightRstlConv = 676,
//    parameter addressWidthRstlConv = 10, 
//    parameter dataWidthRstlConv = 8
//)
//( 
//    input clk,
//    input wen,
//    input ren,
//    input [addressWidthRstlConv-1:0] wadd,
//    input [addressWidthRstlConv-1:0] radd,
//    input signed [dataWidthRstlConv-1:0] data_in,

//    output reg [dataWidthRstlConv-1:0] rdata

//);
    
//    reg [dataWidthRstlConv-1:0] mem_rstl_conv1 [numWeightRstlConv-1:0];



//    always @(posedge clk)
//  begin
//     if (wen & (wadd < numWeightRstlConv))
//     begin
//         mem_rstl_conv1[wadd] <= data_in;
//         //$display("conv1, %d",wadd,data_in);
//         $display("%d",data_in); 

//     end
//  end 
    
//    always @(posedge clk)
//    begin
//        if (ren)
//        begin
//            rdata <= mem_rstl_conv1[radd];

//        end
//    end 
//endmodule

















