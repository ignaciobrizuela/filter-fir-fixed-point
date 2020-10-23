module filter_fir 
   #(
      NB_INPUT  = 8,     // signed Q2.6
      NB_OUTPUT = 12     // signed Q4.13
   )
  (
   input 		                        clk,
   input 		                        rst_n,
   input signed  [NB_INPUT -1 : 0] 	   x,
   output signed [NB_OUTPUT-1 : 0]     y
   );

   localparam NB_ADD_X = 10;
   localparam NB_ADD_Y = 12;
   
   reg  signed [NB_INPUT  -1 : 0]   x_reg [3 : 1];
   reg  signed [NB_OUTPUT -1 : 0]   y_reg [2 : 1];
   wire signed [NB_ADD_X  -1 : 0]   add_x;
   wire signed [NB_OUTPUT -1 : 0]   add_y;
   wire signed [NB_ADD_Y  -1 : 0]   y_aux;


   assign add_x = x - x_reg[1] + x_reg[2] + x_reg[3];
   assign add_y = (y_reg[1] >>> 1) + (y_reg[2] >>> 2);         //b1=0.5  b2=0.25
   assign y_aux = add_x + add_y;
   assign y     = y_aux;

   // COEFFICIENTS
   // -------------- OUTPUT --------------

   always @ (negedge clk) begin
      if (rst_n == 1'b0) begin
         //inputs
         x_reg[1] <= {NB_INPUT{1'b0}};
         x_reg[2] <= {NB_INPUT{1'b0}};
         x_reg[3] <= {NB_INPUT{1'b0}};
         //outputs
         y_reg[1] <= {NB_INPUT{1'b0}};
         y_reg[2] <= {NB_INPUT{1'b0}};
      end 
      else begin
         //inputs
         x_reg[1] <= x;
         x_reg[2] <= x_reg[1];
         x_reg[3] <= x_reg[2];
         //outputs
         y_reg[1] <= y;
         y_reg[2] <= y_reg[1];
      end
   end
endmodule  //filter_fir
