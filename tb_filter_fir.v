`timescale 1ns / 1ps
`define NB_INPUT 8
`define NB_ADD	 10
`define NB_OUPUT 12

module tb_filter_fir;
	
	reg 						clk;    // Clock
	reg 						rst_n;  // Asynchronous reset active low
	reg  signed [`NB_INPUT-1:0] x;
   	wire signed [`NB_OUPUT-1:0] y;   

	exercise4
		u_exercise4(
			.clk(clk),
			.rst_n(rst_n),
			.x(x),
			.y(y)
			);


	// Generate Clock
	always #5 clk = ~clk; 

	initial begin
		x 		= `NB_INPUT'd0;
		rst_n 	= 0;
		clk 	= 0;
		#10;
		rst_n	= 1;
		#10;
		x 		<= `NB_INPUT'd100;
		#10;
		x 		<= `NB_INPUT'd0;
		#320;
	 	$display("Simulation Finished");
		$display("");
		$finish;
	end // initial

endmodule