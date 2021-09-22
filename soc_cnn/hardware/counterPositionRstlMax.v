`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 10:16:14 PM
// Design Name: 
// Module Name: counterPositionRstlMax
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



//module counterPositionRstlMax
//#(
//    //counter for memory of result of convolution
//    parameter counterWidth= 10,
//    //memory_rstl_conv
//    parameter numWeightRstlMax = 169
//)
//(
//    input clk, rst, en, 
//    output[counterWidth-1:0] counter_1
//);

//    reg [counterWidth-1:0] count_1;
//    reg once;
    
//    initial
//    begin
//        once <= 1;
//        count_1 <= 4'd0;
      
//    end
    
//    always @(posedge clk)
//    begin
//        if(rst)
//        begin
//            count_1 <= 4'd0;
//        end
//        if(once)
//        begin
//            count_1 <= 4'd0;
//            once <= 0;
//        end
//        else if(en && !once)
//        begin
//            count_1 <= count_1 + 4'd1;
//            if(count_1 == (numWeightRstlMax - 1))
//            begin
//                once <= 1;
//            end
//        end
//        else if(!en && !once)
//        begin
//            count_1 <= 4'd0;
//            once <= 0;        
//        end
//    end 
//    assign counter_1 = count_1;

//endmodule


module counterPositionRstlMax
#(
    //counter for memory of result of convolution
    parameter counterWidth= 10,
    //memory_rstl_conv
    parameter numWeightRstlMax = 507
)
(
    input clk, rst, en, 
    output[counterWidth-1:0] counter_1,
    output[counterWidth-1:0] counter_2,
    output[counterWidth-1:0] counter_3
);

    reg [counterWidth-1:0] count_1;
    reg [counterWidth-1:0] count_2;
    reg [counterWidth-1:0] count_3;
    reg once;
    
    initial
    begin
        once <= 1;
        count_1 <= 4'd0;
        count_2 <= 4'd1;
        count_3 <= 4'd2;        
    end
    
    always @(posedge clk)
    begin
        if(rst)
        begin
            count_1 <= 4'd0;
            count_2 <= 4'd1;
            count_3 <= 4'd2;
        end
        if(once)
        begin
            count_1 <= 4'd0;
            count_2 <= 4'd1;
            count_3 <= 4'd2;
            once <= 0;
        end
        else if(en && !once)
        begin
            count_1 <= count_1 + 4'd3;
            count_2 <= count_2 + 4'd3;
            count_3 <= count_3 + 4'd3;
            if(count_3 == (numWeightRstlMax - 1))
            begin
                once <= 1;
            end
        end
        else if(!en && !once)
        begin
            count_1 <= 4'd0;
            count_2 <= 4'd1;
            count_3 <= 4'd2;
            once <= 0;        
        end
    end 
    assign counter_1 = count_1;
    assign counter_2 = count_2;
    assign counter_3 = count_3;
endmodule

