`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/24/2021 12:09:57 PM
// Design Name: 
// Module Name: clock_divider_fpga
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


//contador = (reloj_entrante / reloj_nuevo) / 2

module clock_divider_fpga(
   input           clk,     // reloj entrante de 50MHz
   output reg      clk2      // nuevo reloj de 5MHz
    );

reg [3:0] count =0;

initial

begin
 clk2 = 0;

end

// divisor de reloj 50MHz a 5MHz
always@(posedge clk)
    begin
        if(count==4'd2)      // cuenta 5 ciclos (0-4) de reloj    
            begin
              count<=0;      // reinicia cuenta a 0
              clk2 <= ~clk2; // transiciona clk2 a alto o bajo
            end
        else
            begin
            count<=count+1;  //  aumenta contador
            end                  
    end 
    
    
endmodule   
