`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/25/2021 01:29:58 AM
// Design Name: 
// Module Name: printBinary
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


module printBinary
(

    input clk

);
    
    
    
//Para imprimir en consola
///////////////////////////////////////////
///////////////////////////////////////////
reg [15:0]print[0:9];
reg [15:0]data[0:506];
reg [9:0]i;
reg flag;

//con_f1 = \
//[[  46,  -9,-127],
// [  70, -23, -93],
// [ -20, -88, -86]]; con_f0 = np.asarray(con_f0);           # filtre 0 conv2d
//con_b0 = -843;                                            # bias   0 conv2d 

//con_f2 = \
//[[ -79, -63,  51],
// [  78,  58,  61],
// [-127,  91, -72]]; con_f1 = np.asarray(con_f1);           # filtre 1 conv2d
//con_b1 = -1235;  

//con_f3 = \
//[[ -33,-111,-115],
// [-127,  28,  14],
// [ -40,  68,  47]]; con_f2 = np.asarray(con_f2);           # filtre 2 conv2d
//con_b2 = -696;

//initial
//begin
//i =0;
//flag=0;
//print[0] =  16'd46;
//print[1] = -16'd9;
//print[2] = -16'd127;
//print[3] =  16'd70;
//print[4] = -16'd23;
//print[5] = -16'd93;
//print[6] = -16'd20;
//print[7] = -16'd88;
//print[8] = -16'd86;
//print[9] = -16'd843;
//end




//fc_b = \
//[ -48, 1081, -146,  -256, -109, 976, 31, 466, -905, 33];

initial
begin
i =0;
flag=0;

data[0] = -16'd48;
data[1] =  16'd1081;
data[2] = -16'd146;
data[3] = -16'd256;
data[4] = -16'd109;
data[5] =  16'd976;
data[6] =  16'd31;
data[7] =  16'd466;
data[8] = -16'd905;
data[9] =  16'd33;




end














always @(clk)
begin
    if(i< 9'd10 && flag == 0)
    begin
        $display("%b",data[i]);
        i = i + 1;
    end
    if(i==9'd10)
    begin
        flag = 1;
    end
end    
    
    
endmodule
