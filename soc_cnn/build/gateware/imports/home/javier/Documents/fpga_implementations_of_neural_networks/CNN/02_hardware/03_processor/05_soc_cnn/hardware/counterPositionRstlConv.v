`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 12:41:56 PM
// Design Name: 
// Module Name: counterPositionRstlConv
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


module counterPositionRstlConv
#(
    //counter for memory of result of convolution
    parameter counterWidth= 10,
    //memory_rstl_conv
    parameter numWeightRstlConv = 676
)
(
    input clk, rst, en, 
    output[counterWidth-1:0] counter
);

    reg [counterWidth-1:0] count;
    reg once;
    
    initial
    begin
        once = 1;
        count = 0;
    end
    
    always @(posedge clk)
    begin
        if(rst)
        begin
            count <= 4'd0;
            once = 1;
        end
        else if(once)
        begin
            count <= 4'd0;
            once <= 0;
        end
        else if(en && !once)
        begin
            count <= count + 4'd1;
            if(count == (numWeightRstlConv - 1))
            begin
                once <= 1;
            end
        end
    end 
    assign counter = count;
endmodule

