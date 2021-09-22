`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07/24/2021 07:28:03 PM
// Design Name: 
// Module Name: convolution
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


module convolution
#(
    //Convolution
    parameter dataWidthConv=16,                       
    parameter s0 = 4'b0000, s1 = 4'b0001, s2 = 4'b0010, s3 = 4'b0011, s4 = 4'b0100,
    parameter s5 = 4'b0101, s6 = 4'b0110, s7 = 4'b0111, s8 = 4'b1000, s9 = 4'b1001,
    parameter s10 = 4'b1010, s11 = 4'b1011, s12 = 4'b1100, s13 = 4'b1101, s14 = 4'b1110,
    
    //quantization
    parameter q = 64'd2014687024 //q = 31'b1111000000101011010111100110000
    
)


(
    input clk,
    input en,
    input rst,
    input clk_div,
    
    input [dataWidthConv-1:0] rdata_img0,
    input [dataWidthConv-1:0] rdata_img1,
    input [dataWidthConv-1:0] rdata_img2,
    input [dataWidthConv-1:0] rdata_img3,
    input [dataWidthConv-1:0] rdata_img4,
    input [dataWidthConv-1:0] rdata_img5,
    input [dataWidthConv-1:0] rdata_img6,
    input [dataWidthConv-1:0] rdata_img7,
    input [dataWidthConv-1:0] rdata_img8,
    
    input [dataWidthConv-1:0] rdata_filt0,
    input [dataWidthConv-1:0] rdata_filt1,
    input [dataWidthConv-1:0] rdata_filt2,
    input [dataWidthConv-1:0] rdata_filt3,
    input [dataWidthConv-1:0] rdata_filt4,
    input [dataWidthConv-1:0] rdata_filt5,
    input [dataWidthConv-1:0] rdata_filt6,
    input [dataWidthConv-1:0] rdata_filt7,
    input [dataWidthConv-1:0] rdata_filt8,
    input [dataWidthConv-1:0] bias_filt, 
    
    output reg save_rstl,
    output [7:0] out_quant,
    output conv_ready       
);
    //FSM
    reg [3:0] present_state, next_state; //ok
    
    reg [17-1:0] rstl_mult [8:0];//ok
    reg [17-1:0] rstl_sum;
    
    reg rst_quant;
    reg [17-1:0] aux_bias;
    reg  [63:0] num;
    reg rst_relu;
    reg conv_ok;

    wire quant_ok;
    wire relu_ok;
    //wire [7:0] num_quant;
    wire [8:0] num_quant;
    wire signed [7:0] num_final;//ojo
        
    initial
    begin
        $display("***********************************************************************");
        conv_ok = 1'd0;
        //present_state = 3'd0;
        //next_state = 3'd0;
    end

    quantization #(.q(q)) quant 
    (
        .clk(clk),
        .rst(rst_quant),
        .a(num),
        .num_quant(num_quant),
        .sig_ok(quant_ok)
    );
    
    ReLu activation
    (
        .clk(clk),
        .rst(rst_relu),
        .num_quant(num_quant),
        .num(num_final),
        .sig_ok(relu_ok)
    );    

    always @(posedge clk) //Present estate  // always @(clk) //Present estate 
    begin
        if(clk_div == 1)
        begin
            present_state <= s0;    
        end
        else
        begin
            present_state <= next_state;
        end    
    end    

    always @(negedge clk) //always @(*)
    begin
        case(present_state)
            s0:
                next_state <= s1;                
            s1:
                next_state <= s2;
            s2:
                if(quant_ok)
                begin
                    next_state <= s3;
                end
                else
                begin
                    next_state <= s2;
                end
            s3:
                if(relu_ok)
                begin
                    next_state <= s4;
                end
                else
                begin
                    next_state <= s3;
                end
            s4:
                next_state <= s5;
                                                                                                  
        endcase                
    end

    always @ (negedge clk) begin //always @ (posedge clk) begin   
      case (present_state)
        s0: begin
            rstl_mult[0] <= $signed(rdata_img0*rdata_filt0);
            rstl_mult[1] <= $signed(rdata_img1*rdata_filt1);
            rstl_mult[2] <= $signed(rdata_img2*rdata_filt2);
            rstl_mult[3] <= $signed(rdata_img3*rdata_filt3);
            rstl_mult[4] <= $signed(rdata_img4*rdata_filt4);
            rstl_mult[5] <= $signed(rdata_img5*rdata_filt5);
            rstl_mult[6] <= $signed(rdata_img6*rdata_filt6);
            rstl_mult[7] <= $signed(rdata_img7*rdata_filt7);
            rstl_mult[8] <= $signed(rdata_img8*rdata_filt8);
            save_rstl <= 0;
            end          
        s1: begin
            rstl_sum <= $signed(rstl_mult[0] + rstl_mult[1] + rstl_mult[2] + rstl_mult[3] + rstl_mult[4] + rstl_mult[5] + rstl_mult[6] + rstl_mult[7] + rstl_mult[8]);
            rst_quant <= 1;
            aux_bias <= $signed(bias_filt);
            end
        s2: begin
            num <= $signed(rstl_sum + aux_bias); //Create module memory for storage convolution operation result, NOT use this way (only test porpus)
            rst_quant <= 0;
            rst_relu <= 1;
            end  
        s3: begin
            rst_relu <= 0;
            rst_quant <= 1;
            end    
        s4: begin
            rst_relu <= 1;
            save_rstl <= 1;  
            end 
        s5: begin
            save_rstl <= 0; 
            conv_ok <= 1'd1;
//            $display("%d",num_final); 
            //$fwrite(fd,"hola");
            end                                                
      endcase 
    end 

assign conv_ready = conv_ok;
assign out_quant = num_final;

endmodule    

