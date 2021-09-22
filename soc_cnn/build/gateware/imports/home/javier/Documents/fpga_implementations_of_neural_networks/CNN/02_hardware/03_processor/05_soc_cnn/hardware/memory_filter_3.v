`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/24/2021 07:22:01 PM
// Design Name: 
// Module Name: memory_filter_3
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


module memory_filter_3
#(
    //memory filter
    parameter numWeightFilter = 10, addressWidthFilter=4, dataWidthFilter=16,
    parameter weightFileFilter="/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_CNN_IP_core/03_CNN_IP_core.srcs/sources_1/new/filter3.mem"
)
( 
    input clk,
    input en,
    input [addressWidthFilter-1:0] addr,
    output reg [dataWidthFilter-1:0] rdata0,
    output reg [dataWidthFilter-1:0] rdata1,
    output reg [dataWidthFilter-1:0] rdata2,
    output reg [dataWidthFilter-1:0] rdata3,
    output reg [dataWidthFilter-1:0] rdata4,
    output reg [dataWidthFilter-1:0] rdata5,
    output reg [dataWidthFilter-1:0] rdata6,
    output reg [dataWidthFilter-1:0] rdata7,
    output reg [dataWidthFilter-1:0] rdata8,    
    output reg [dataWidthFilter-1:0] bias
);
    
    reg [dataWidthFilter-1:0] register[numWeightFilter-1:0];
    wire [addressWidthFilter-1:0] addr_wire;


        initial
		begin
	        $readmemb(weightFileFilter, register);
	    end
	    
    assign addr_wire = addr;	    
    
    always @(posedge clk)
    begin
        if (en)
        begin
            rdata0 <= register[addr_wire + 4'd0];
            rdata1 <= register[addr_wire + 4'd1];
            rdata2 <= register[addr_wire + 4'd2];
            rdata3 <= register[addr_wire + 4'd3];
            rdata4 <= register[addr_wire + 4'd4];
            rdata5 <= register[addr_wire + 4'd5];
            rdata6 <= register[addr_wire + 4'd6];
            rdata7 <= register[addr_wire + 4'd7];
            rdata8 <= register[addr_wire + 4'd8];
            bias <= register[addr_wire + 4'd9];
        end
    end 
endmodule
