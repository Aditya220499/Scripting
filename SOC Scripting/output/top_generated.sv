// AUTO-GENERATED FILE

module top;


logic u_cpu__clk;

logic u_cpu__rst_n;

logic [7:0] u_cpu__irq;

logic [31:0] u_cpu__data_out;

logic u_dma__clk;

logic u_dma__rst_n;

logic [31:0] u_dma__data_in;

logic u_dma__done;



// Instance: u_cpu
cpu_core u_cpu (

    .clk(__clk),

    .rst_n(__rst_n),

    .irq(__irq),

    .data_out(__data_out)

);


// Instance: u_dma
dma_engine u_dma (

    .clk(__clk),

    .rst_n(__rst_n),

    .data_in(__data_in),

    .done(__done)

);



endmodule