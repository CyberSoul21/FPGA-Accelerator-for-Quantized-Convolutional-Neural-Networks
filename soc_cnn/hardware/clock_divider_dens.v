`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 10:26:40 PM
// Design Name: 
// Module Name: clock_divider_dens
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


module clock_divider_dens(clock_in,en,rst,clock_out);

    input clock_in; // input clock on FPGA
    input en,rst;
    output reg clock_out; // output clock after dividing the input clock by divisor
    reg[27:0] counter=28'd0;
    parameter DIVISOR = 28'd4; //parameter DIVISOR = 28'd12;
    // The frequency of the output clk_out
    //  = The frequency of the input clk_in divided by DIVISOR
    // For example: Fclk_in = 50Mhz, if you want to get 1Hz signal to blink LEDs
    // You will modify the DIVISOR parameter value to 28'd50.000.000
    // Then the frequency of the output clk_out = 50Mhz/50.000.000 = 1Hz
    
    initial
    begin
        clock_out=0;
    end
    
    always @(posedge clock_in)
    begin
        if(rst)
        begin
            counter <= 28'd0;
        end
        if(en)
        begin
            counter <= counter + 28'd1;
            if(counter>=(DIVISOR-1))
            begin
                counter <= 28'd0;
            end
            clock_out <= (counter<DIVISOR/4)?1'b1:1'b0; // clock_out <= (counter<DIVISOR/12)?1'b1:1'b0;
        end
    end
endmodule


