// AUTO-GENERATED FILE

module top;

logic clk;
logic rst_n;
logic [7:0] u_cpu__irq;
logic [31:0] u_cpu__data_out;
logic [31:0] u_dma__data_in;
logic u_dma__done;


// Instance: u_cpu
cpu_core u_cpu (
.clk(clk),
.rst_n(rst_n),
.irq(u_cpu__irq),
.data_out(u_cpu__data_out)

);

// Instance: u_dma
dma_engine u_dma (
.clk(clk),
.rst_n(rst_n),
.data_in(u_dma__data_in),
.done(u_dma__done)

);

endmodule