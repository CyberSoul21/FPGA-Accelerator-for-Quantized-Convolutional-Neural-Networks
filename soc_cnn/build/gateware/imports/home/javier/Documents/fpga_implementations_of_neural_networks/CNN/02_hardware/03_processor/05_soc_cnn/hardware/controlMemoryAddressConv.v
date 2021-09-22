`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08/17/2021 10:15:22 PM
// Design Name: 
// Module Name: controlMemoryAddressConv
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


module controlMemoryAddressConv
#(
    //counter for read memory 
    parameter counterWidth= 10   
)
(
    input clk, en, rst, 
    output stop_count,
    output[counterWidth-1:0] i,j    
);
    wire sig_ok_1;
    wire sig_ok_2;
    reg sig_en;

    counter_col_max counter_j(
        .clk(clk),
        .rst(rst),
        .en(sig_en),
        .blk(~en),
        .counter(j),
        .sig_ok(sig_ok_1)
    );
    counter_row_max counter_i(
        .clk(sig_ok_1),
        .rst(rst),
        .en(sig_en),
        .blk(~en),
        .counter(i),
        .sig_ok(sig_ok_2)
    );

    always @(sig_ok_2) //always @(*)
    begin    
        if(sig_ok_2)
        begin
            sig_en <= 0;
        end
        else if(!sig_ok_2)
            sig_en <= 1;
        begin
        
        end
    end
    assign stop_count = sig_en;
endmodule


module counter_row_max
#(
    //counter for read memory 
    parameter counterWidth= 10,
    parameter n_c = 5'd26,  //number of column matrix image 
    parameter n_r = 5'd26  //number of rows matrix image 
     
)
(
    input clk, rst, en, blk, 
    output[counterWidth-1:0] counter, 
    output sig_ok
);
                        
   reg [counterWidth-1:0] counter_2;
   reg ok;
    
    initial
    begin
        ok = 0;
    end
    
    // up counter
    always @(posedge clk or posedge rst)
    begin
        if(rst | blk)
        begin
            counter_2 <= 4'd0;
            ok <= 0;
        end
        else if(en)
        begin
            counter_2 <= counter_2 + 4'd1;
            ok <= 0;
            if(counter_2 == (n_r/4'd2 - 1))
            begin
                counter_2 <= 0;
                ok <= 1; 
            end
        end
    end 
    assign counter = counter_2;
    assign sig_ok = ok;
endmodule


module counter_col_max
#(
    //counter for read memory 
    parameter counterWidth= 10,
    parameter n_c = 5'd26,  //number of column matrix image 
    parameter n_r = 5'd26  //number of rows matrix image 
)
(
    input clk, rst, en, blk, 
    output[counterWidth-1:0] counter, 
    output sig_ok
);

    
    reg [counterWidth-1:0] counter_2;
    reg [counterWidth-1:0] aux_counter_2;

    reg ok;
    
    initial
    begin
        ok = 0;
    end
    
    // up counter
    always @(posedge clk or posedge rst)
    begin
        if(rst | blk)
        begin
            counter_2 <= 4'd0;
            aux_counter_2 <= 4'd0;
            ok <= 0;
        end
        else if(en)
        begin
            counter_2 <= counter_2 + 4'd2;
            aux_counter_2 <= aux_counter_2 + 4'd2;
            ok <= 0;
            if(aux_counter_2 == (n_c - 4'd2))
            begin
                aux_counter_2 <= 0;
                ok <= 1; 
            end
        end
        else if(!en)
        begin
            counter_2 <= 4'd0;
            aux_counter_2 <= 4'd0;
            ok <= 0;
        end
    end 
    assign counter = counter_2;
    assign sig_ok = ok;
endmodule