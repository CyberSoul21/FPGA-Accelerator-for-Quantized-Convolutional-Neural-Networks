`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/12/2021 02:08:55 PM
// Design Name: 
// Module Name: counterPositionMemMax
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


module counterPositionMemMax#(
    //full connected
    parameter dataWidthMax=8, dataWidthWeight=16,
    parameter dataWidthCount= 10,
    parameter numWeightRstlMax = 507
  
    
    
  
    
    
)
(
    input clk,
    input en,
    input rst,
    //input [dataWidthMax-1:0] rdata_max,
    //input [dataWidthWeight-1:0] rdata_weight,
    
    output[dataWidthCount-1:0] pos_memory
    

);


    reg [dataWidthCount-1:0] count;
    reg once;
    
    initial
    begin
        count <= 4'd0;
        once <= 0;
    end
    
    always @(posedge clk)
    begin
        if(rst)
        begin
            count <= 4'd0;
            once <= 0;
        end
        if(once)
        begin
            count <= 4'd0;
            once <= 0;
        end        
        if(en && !once)
        begin
            count <= count + 4'd1;
            if(count == (numWeightRstlMax - 1 + 1 + 1))
            begin
                count <= 4'd0;
                once <= 1;                
            end
        end
        else if(!en && !once)
        begin
            count<= 4'd0;
            once <= 0;        
        end        
    end 
    
    assign pos_memory = count;

    
    
    
    
    
endmodule
