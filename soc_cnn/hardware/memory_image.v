`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 12:43:12 PM
// Design Name: 
// Module Name: memory_image
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


module memory_image
#(
    //memory image
    parameter numWeightImg = 784, 
    parameter addressWidthPos = 11,
    parameter addressWidthImg=10, dataWidthImg= 16,
    parameter weightFileImg="/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/05_CNN_IP_core_z20/05_CNN_IP_core_z20.srcs/sources_1/new/image.mem",
    parameter n_c = 5'd28,  //number of column matrix image 
    parameter n_r = 5'd28,  //number of rows matrix image 
    //quantization
    parameter q = 64'd2014687024, //q = 31'b1111000000101011010111100110000
    parameter mask = 8'd255,
    parameter zero = 1'd0,
    parameter one = 1'd1,
    parameter offset_ent = 6,
    parameter offset_sor = -1
)
( 
    input clk,
    input wen,
    input ren,
    input [addressWidthImg-1:0] addr1,
    input [addressWidthImg-1:0] addr2,
    
    input [addressWidthImg-1:0] wadd,  //test soc
    input [dataWidthImg-1:0] wdata,    //test soc
    
    input ren2,                        //test soc   
    input [addressWidthImg-1:0] radd, //test soc
    output signed [dataWidthImg-1:0] rdata, //test soc   
    output reg mem_full,   //test soc
    
    output reg [dataWidthImg-1:0] rdata0,
    output reg [dataWidthImg-1:0] rdata1,
    output reg [dataWidthImg-1:0] rdata2,
    output reg [dataWidthImg-1:0] rdata3,
    output reg [dataWidthImg-1:0] rdata4,
    output reg [dataWidthImg-1:0] rdata5,
    output reg [dataWidthImg-1:0] rdata6,
    output reg [dataWidthImg-1:0] rdata7,
    output reg [dataWidthImg-1:0] rdata8     
    
);
    
    reg [dataWidthImg-1:0] register[numWeightImg-1:0];

    
    wire [addressWidthPos-1:0] p_img_0;
    wire [addressWidthPos-1:0] p_img_1;
    wire [addressWidthPos-1:0] p_img_2;
    wire [addressWidthPos-1:0] p_img_3;
    wire [addressWidthPos-1:0] p_img_4;
    wire [addressWidthPos-1:0] p_img_5;
    wire [addressWidthPos-1:0] p_img_6;
    wire [addressWidthPos-1:0] p_img_7;
    wire [addressWidthPos-1:0] p_img_8;

    initial
	   begin
	        $readmemb(weightFileImg, register);
	    end

    assign p_img_0 = (0+addr1)*(n_c) + (0+addr2);
    assign p_img_1 = (0+addr1)*(n_c) + (1+addr2);
    assign p_img_2 = (0+addr1)*(n_c) + (2+addr2);
    assign p_img_3 = (1+addr1)*(n_c) + (0+addr2);    
    assign p_img_4 = (1+addr1)*(n_c) + (1+addr2);
    assign p_img_5 = (1+addr1)*(n_c) + (2+addr2);
    assign p_img_6 = (2+addr1)*(n_c) + (0+addr2);
    assign p_img_7 = (2+addr1)*(n_c) + (1+addr2);
    assign p_img_8 = (2+addr1)*(n_c) + (2+addr2);      

    
    always @(posedge clk)
    begin
        if (ren)
        begin
            rdata0 <= register[p_img_0] + offset_ent;
            rdata1 <= register[p_img_1] + offset_ent;
            rdata2 <= register[p_img_2] + offset_ent;
            rdata3 <= register[p_img_3] + offset_ent;
            rdata4 <= register[p_img_4] + offset_ent;
            rdata5 <= register[p_img_5] + offset_ent;
            rdata6 <= register[p_img_6] + offset_ent;
            rdata7 <= register[p_img_7] + offset_ent;
            rdata8 <= register[p_img_8] + offset_ent;                                                                                    
          
        end
    end 
    
    
    always @(posedge clk)
	begin
	   if (wen)
	   begin
	       register[wadd] <= wdata;
	       //$display("wadd1, %d",wadd,data_in); 

	   end
	   if(wadd >= (numWeightImg -1) )
	   begin
	       mem_full <= 1;
	   end
	   else
	   begin
	       mem_full <= 0;
	   end
	end 


    assign rdata = register[radd];  //test soc



    
endmodule

