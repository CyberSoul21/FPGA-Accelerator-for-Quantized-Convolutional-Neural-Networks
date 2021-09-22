/* Machine-generated using Migen */
module AccQuant_cnn(
	output reg serial_tx,
	input serial_rx,
	input clk125,
	input cpu_reset,
	output user_led,
	output user_led_1,
	output user_led_2,
	output user_led_3,
	output user_led_4,
	output user_led_5,
	output user_led_6
);

reg soccontroller_reset_storage = 1'd0;
reg soccontroller_reset_re = 1'd0;
reg [31:0] soccontroller_scratch_storage = 32'd305419896;
reg soccontroller_scratch_re = 1'd0;
wire [31:0] soccontroller_bus_errors_status;
wire soccontroller_bus_errors_we;
reg soccontroller_bus_errors_re = 1'd0;
wire soccontroller_reset;
wire soccontroller_bus_error;
reg [31:0] soccontroller_bus_errors = 32'd0;
wire cpu_reset_1;
reg [31:0] cpu_interrupt;
wire [29:0] cpu_ibus_adr;
wire [31:0] cpu_ibus_dat_w;
wire [31:0] cpu_ibus_dat_r;
wire [3:0] cpu_ibus_sel;
wire cpu_ibus_cyc;
wire cpu_ibus_stb;
wire cpu_ibus_ack;
wire cpu_ibus_we;
wire [2:0] cpu_ibus_cti;
wire [1:0] cpu_ibus_bte;
wire cpu_ibus_err;
wire [29:0] cpu_dbus_adr;
wire [31:0] cpu_dbus_dat_w;
wire [31:0] cpu_dbus_dat_r;
wire [3:0] cpu_dbus_sel;
wire cpu_dbus_cyc;
wire cpu_dbus_stb;
wire cpu_dbus_ack;
wire cpu_dbus_we;
wire [2:0] cpu_dbus_cti;
wire [1:0] cpu_dbus_bte;
wire cpu_dbus_err;
reg [31:0] vexriscv = 32'd0;
wire [29:0] ram_bus_adr;
wire [31:0] ram_bus_dat_w;
wire [31:0] ram_bus_dat_r;
wire [3:0] ram_bus_sel;
wire ram_bus_cyc;
wire ram_bus_stb;
reg ram_bus_ack = 1'd0;
wire ram_bus_we;
wire [2:0] ram_bus_cti;
wire [1:0] ram_bus_bte;
reg ram_bus_err = 1'd0;
wire [12:0] adr;
wire [31:0] dat_r;
wire [29:0] interface0_ram_bus_adr;
wire [31:0] interface0_ram_bus_dat_w;
wire [31:0] interface0_ram_bus_dat_r;
wire [3:0] interface0_ram_bus_sel;
wire interface0_ram_bus_cyc;
wire interface0_ram_bus_stb;
reg interface0_ram_bus_ack = 1'd0;
wire interface0_ram_bus_we;
wire [2:0] interface0_ram_bus_cti;
wire [1:0] interface0_ram_bus_bte;
reg interface0_ram_bus_err = 1'd0;
wire [10:0] sram0_adr;
wire [31:0] sram0_dat_r;
reg [3:0] sram0_we;
wire [31:0] sram0_dat_w;
wire [29:0] interface1_ram_bus_adr;
wire [31:0] interface1_ram_bus_dat_w;
wire [31:0] interface1_ram_bus_dat_r;
wire [3:0] interface1_ram_bus_sel;
wire interface1_ram_bus_cyc;
wire interface1_ram_bus_stb;
reg interface1_ram_bus_ack = 1'd0;
wire interface1_ram_bus_we;
wire [2:0] interface1_ram_bus_cti;
wire [1:0] interface1_ram_bus_bte;
reg interface1_ram_bus_err = 1'd0;
wire [11:0] sram1_adr;
wire [31:0] sram1_dat_r;
reg [3:0] sram1_we;
wire [31:0] sram1_dat_w;
wire tx_sink_valid;
reg tx_sink_ready;
wire tx_sink_first;
wire tx_sink_last;
wire [7:0] tx_sink_payload_data;
reg [7:0] tx_data = 8'd0;
reg [3:0] tx_count = 4'd0;
reg tx_enable;
reg [31:0] tx_tick = 32'd0;
reg [31:0] tx_phase = 32'd0;
reg rx_source_valid;
wire rx_source_ready;
reg rx_source_first = 1'd0;
reg rx_source_last = 1'd0;
reg [7:0] rx_source_payload_data;
reg [7:0] rx_data = 8'd0;
reg [3:0] rx_count = 4'd0;
reg rx_enable;
reg [31:0] rx_tick = 32'd0;
reg [31:0] rx_phase = 32'd0;
wire rx_rx;
reg rx_rx_d = 1'd0;
reg uart_rxtx_re;
wire [7:0] uart_rxtx_r;
reg uart_rxtx_we;
wire [7:0] uart_rxtx_w;
wire uart_txfull_status;
wire uart_txfull_we;
reg uart_txfull_re = 1'd0;
wire uart_rxempty_status;
wire uart_rxempty_we;
reg uart_rxempty_re = 1'd0;
wire uart_irq;
wire uart_tx_status;
reg uart_tx_pending = 1'd0;
wire uart_tx_trigger;
reg uart_tx_clear;
reg uart_tx_trigger_d = 1'd0;
wire uart_rx_status;
reg uart_rx_pending = 1'd0;
wire uart_rx_trigger;
reg uart_rx_clear;
reg uart_rx_trigger_d = 1'd0;
wire uart_tx0;
wire uart_rx0;
reg [1:0] uart_status_status;
wire uart_status_we;
reg uart_status_re = 1'd0;
wire uart_tx1;
wire uart_rx1;
reg [1:0] uart_pending_status;
wire uart_pending_we;
reg uart_pending_re = 1'd0;
reg [1:0] uart_pending_r = 2'd0;
wire uart_tx2;
wire uart_rx2;
reg [1:0] uart_enable_storage = 2'd0;
reg uart_enable_re = 1'd0;
wire uart_txempty_status;
wire uart_txempty_we;
reg uart_txempty_re = 1'd0;
wire uart_rxfull_status;
wire uart_rxfull_we;
reg uart_rxfull_re = 1'd0;
wire uart_uart_sink_valid;
wire uart_uart_sink_ready;
wire uart_uart_sink_first;
wire uart_uart_sink_last;
wire [7:0] uart_uart_sink_payload_data;
wire uart_uart_source_valid;
wire uart_uart_source_ready;
wire uart_uart_source_first;
wire uart_uart_source_last;
wire [7:0] uart_uart_source_payload_data;
wire uart_tx_fifo_sink_valid;
wire uart_tx_fifo_sink_ready;
reg uart_tx_fifo_sink_first = 1'd0;
reg uart_tx_fifo_sink_last = 1'd0;
wire [7:0] uart_tx_fifo_sink_payload_data;
wire uart_tx_fifo_source_valid;
wire uart_tx_fifo_source_ready;
wire uart_tx_fifo_source_first;
wire uart_tx_fifo_source_last;
wire [7:0] uart_tx_fifo_source_payload_data;
wire uart_tx_fifo_re;
reg uart_tx_fifo_readable = 1'd0;
wire uart_tx_fifo_syncfifo_we;
wire uart_tx_fifo_syncfifo_writable;
wire uart_tx_fifo_syncfifo_re;
wire uart_tx_fifo_syncfifo_readable;
wire [9:0] uart_tx_fifo_syncfifo_din;
wire [9:0] uart_tx_fifo_syncfifo_dout;
reg [4:0] uart_tx_fifo_level0 = 5'd0;
reg uart_tx_fifo_replace = 1'd0;
reg [3:0] uart_tx_fifo_produce = 4'd0;
reg [3:0] uart_tx_fifo_consume = 4'd0;
reg [3:0] uart_tx_fifo_wrport_adr;
wire [9:0] uart_tx_fifo_wrport_dat_r;
wire uart_tx_fifo_wrport_we;
wire [9:0] uart_tx_fifo_wrport_dat_w;
wire uart_tx_fifo_do_read;
wire [3:0] uart_tx_fifo_rdport_adr;
wire [9:0] uart_tx_fifo_rdport_dat_r;
wire uart_tx_fifo_rdport_re;
wire [4:0] uart_tx_fifo_level1;
wire [7:0] uart_tx_fifo_fifo_in_payload_data;
wire uart_tx_fifo_fifo_in_first;
wire uart_tx_fifo_fifo_in_last;
wire [7:0] uart_tx_fifo_fifo_out_payload_data;
wire uart_tx_fifo_fifo_out_first;
wire uart_tx_fifo_fifo_out_last;
wire uart_rx_fifo_sink_valid;
wire uart_rx_fifo_sink_ready;
wire uart_rx_fifo_sink_first;
wire uart_rx_fifo_sink_last;
wire [7:0] uart_rx_fifo_sink_payload_data;
wire uart_rx_fifo_source_valid;
wire uart_rx_fifo_source_ready;
wire uart_rx_fifo_source_first;
wire uart_rx_fifo_source_last;
wire [7:0] uart_rx_fifo_source_payload_data;
wire uart_rx_fifo_re;
reg uart_rx_fifo_readable = 1'd0;
wire uart_rx_fifo_syncfifo_we;
wire uart_rx_fifo_syncfifo_writable;
wire uart_rx_fifo_syncfifo_re;
wire uart_rx_fifo_syncfifo_readable;
wire [9:0] uart_rx_fifo_syncfifo_din;
wire [9:0] uart_rx_fifo_syncfifo_dout;
reg [4:0] uart_rx_fifo_level0 = 5'd0;
reg uart_rx_fifo_replace = 1'd0;
reg [3:0] uart_rx_fifo_produce = 4'd0;
reg [3:0] uart_rx_fifo_consume = 4'd0;
reg [3:0] uart_rx_fifo_wrport_adr;
wire [9:0] uart_rx_fifo_wrport_dat_r;
wire uart_rx_fifo_wrport_we;
wire [9:0] uart_rx_fifo_wrport_dat_w;
wire uart_rx_fifo_do_read;
wire [3:0] uart_rx_fifo_rdport_adr;
wire [9:0] uart_rx_fifo_rdport_dat_r;
wire uart_rx_fifo_rdport_re;
wire [4:0] uart_rx_fifo_level1;
wire [7:0] uart_rx_fifo_fifo_in_payload_data;
wire uart_rx_fifo_fifo_in_first;
wire uart_rx_fifo_fifo_in_last;
wire [7:0] uart_rx_fifo_fifo_out_payload_data;
wire uart_rx_fifo_fifo_out_first;
wire uart_rx_fifo_fifo_out_last;
reg [31:0] timer_load_storage = 32'd0;
reg timer_load_re = 1'd0;
reg [31:0] timer_reload_storage = 32'd0;
reg timer_reload_re = 1'd0;
reg timer_en_storage = 1'd0;
reg timer_en_re = 1'd0;
reg timer_update_value_storage = 1'd0;
reg timer_update_value_re = 1'd0;
reg [31:0] timer_value_status = 32'd0;
wire timer_value_we;
reg timer_value_re = 1'd0;
wire timer_irq;
wire timer_zero_status;
reg timer_zero_pending = 1'd0;
wire timer_zero_trigger;
reg timer_zero_clear;
reg timer_zero_trigger_d = 1'd0;
wire timer_zero0;
wire timer_status_status;
wire timer_status_we;
reg timer_status_re = 1'd0;
wire timer_zero1;
wire timer_pending_status;
wire timer_pending_we;
reg timer_pending_re = 1'd0;
reg timer_pending_r = 1'd0;
wire timer_zero2;
reg timer_enable_storage = 1'd0;
reg timer_enable_re = 1'd0;
reg [31:0] timer_value = 32'd0;
wire sys_clk;
wire sys_rst;
wire por_clk;
reg int_rst = 1'd1;
wire CLK;
reg EN_storage = 1'd0;
reg EN_re = 1'd0;
reg RST_storage = 1'd0;
reg RST_re = 1'd0;
reg [3:0] SEL_storage = 4'd0;
reg SEL_re = 1'd0;
reg WEN_IMAGE_storage = 1'd0;
reg WEN_IMAGE_re = 1'd0;
reg [9:0] WADD_IMAGE_storage = 10'd0;
reg WADD_IMAGE_re = 1'd0;
reg [15:0] WDATA_IMAGE_storage = 16'd0;
reg WDATA_IMAGE_re = 1'd0;
reg REN_MEMORY_storage = 1'd0;
reg REN_MEMORY_re = 1'd0;
reg REN_IMAGE_storage = 1'd0;
reg REN_IMAGE_re = 1'd0;
reg [9:0] RADD_IMAGE_storage = 10'd0;
reg RADD_IMAGE_re = 1'd0;
wire [15:0] RDATA_IMAGE_status;
wire RDATA_IMAGE_we;
reg RDATA_IMAGE_re = 1'd0;
reg [9:0] RADD_MEMORY_storage = 10'd0;
reg RADD_MEMORY_re = 1'd0;
wire [7:0] DATA_MEMORY_status;
wire DATA_MEMORY_we;
reg DATA_MEMORY_re = 1'd0;
wire CONV_OK_status;
wire CONV_OK_we;
reg CONV_OK_re = 1'd0;
wire MAX_OK_status;
wire MAX_OK_we;
reg MAX_OK_re = 1'd0;
wire DENS_OK_status;
wire DENS_OK_we;
reg DENS_OK_re = 1'd0;
wire MEM_OK_status;
wire MEM_OK_we;
reg MEM_OK_re = 1'd0;
wire [6:0] NUMBER_OUT;
reg rs232phytx_state = 1'd0;
reg rs232phytx_next_state;
reg [3:0] tx_count_rs232phytx_next_value0;
reg tx_count_rs232phytx_next_value_ce0;
reg serial_tx_rs232phytx_next_value1;
reg serial_tx_rs232phytx_next_value_ce1;
reg [7:0] tx_data_rs232phytx_next_value2;
reg tx_data_rs232phytx_next_value_ce2;
reg rs232phyrx_state = 1'd0;
reg rs232phyrx_next_state;
reg [3:0] rx_count_rs232phyrx_next_value0;
reg rx_count_rs232phyrx_next_value_ce0;
reg [7:0] rx_data_rs232phyrx_next_value1;
reg rx_data_rs232phyrx_next_value_ce1;
reg [13:0] basesoc_adr;
reg basesoc_we;
reg [31:0] basesoc_dat_w;
wire [31:0] basesoc_dat_r;
wire [29:0] basesoc_wishbone_adr;
wire [31:0] basesoc_wishbone_dat_w;
reg [31:0] basesoc_wishbone_dat_r;
wire [3:0] basesoc_wishbone_sel;
wire basesoc_wishbone_cyc;
wire basesoc_wishbone_stb;
reg basesoc_wishbone_ack;
wire basesoc_wishbone_we;
wire [2:0] basesoc_wishbone_cti;
wire [1:0] basesoc_wishbone_bte;
reg basesoc_wishbone_err = 1'd0;
wire [29:0] shared_adr;
wire [31:0] shared_dat_w;
reg [31:0] shared_dat_r;
wire [3:0] shared_sel;
wire shared_cyc;
wire shared_stb;
reg shared_ack;
wire shared_we;
wire [2:0] shared_cti;
wire [1:0] shared_bte;
wire shared_err;
wire [1:0] request;
reg grant = 1'd0;
reg [3:0] slave_sel;
reg [3:0] slave_sel_r = 4'd0;
reg error;
wire wait_1;
wire done;
reg [19:0] count = 20'd1000000;
wire [13:0] csr_bankarray_interface0_bank_bus_adr;
wire csr_bankarray_interface0_bank_bus_we;
wire [31:0] csr_bankarray_interface0_bank_bus_dat_w;
reg [31:0] csr_bankarray_interface0_bank_bus_dat_r = 32'd0;
reg csr_bankarray_csrbank0_EN0_re;
wire csr_bankarray_csrbank0_EN0_r;
reg csr_bankarray_csrbank0_EN0_we;
wire csr_bankarray_csrbank0_EN0_w;
reg csr_bankarray_csrbank0_RST0_re;
wire csr_bankarray_csrbank0_RST0_r;
reg csr_bankarray_csrbank0_RST0_we;
wire csr_bankarray_csrbank0_RST0_w;
reg csr_bankarray_csrbank0_SEL0_re;
wire [3:0] csr_bankarray_csrbank0_SEL0_r;
reg csr_bankarray_csrbank0_SEL0_we;
wire [3:0] csr_bankarray_csrbank0_SEL0_w;
reg csr_bankarray_csrbank0_WEN_IMAGE0_re;
wire csr_bankarray_csrbank0_WEN_IMAGE0_r;
reg csr_bankarray_csrbank0_WEN_IMAGE0_we;
wire csr_bankarray_csrbank0_WEN_IMAGE0_w;
reg csr_bankarray_csrbank0_WADD_IMAGE0_re;
wire [9:0] csr_bankarray_csrbank0_WADD_IMAGE0_r;
reg csr_bankarray_csrbank0_WADD_IMAGE0_we;
wire [9:0] csr_bankarray_csrbank0_WADD_IMAGE0_w;
reg csr_bankarray_csrbank0_WDATA_IMAGE0_re;
wire [15:0] csr_bankarray_csrbank0_WDATA_IMAGE0_r;
reg csr_bankarray_csrbank0_WDATA_IMAGE0_we;
wire [15:0] csr_bankarray_csrbank0_WDATA_IMAGE0_w;
reg csr_bankarray_csrbank0_REN_MEMORY0_re;
wire csr_bankarray_csrbank0_REN_MEMORY0_r;
reg csr_bankarray_csrbank0_REN_MEMORY0_we;
wire csr_bankarray_csrbank0_REN_MEMORY0_w;
reg csr_bankarray_csrbank0_REN_IMAGE0_re;
wire csr_bankarray_csrbank0_REN_IMAGE0_r;
reg csr_bankarray_csrbank0_REN_IMAGE0_we;
wire csr_bankarray_csrbank0_REN_IMAGE0_w;
reg csr_bankarray_csrbank0_RADD_IMAGE0_re;
wire [9:0] csr_bankarray_csrbank0_RADD_IMAGE0_r;
reg csr_bankarray_csrbank0_RADD_IMAGE0_we;
wire [9:0] csr_bankarray_csrbank0_RADD_IMAGE0_w;
reg csr_bankarray_csrbank0_RDATA_IMAGE_re;
wire [15:0] csr_bankarray_csrbank0_RDATA_IMAGE_r;
reg csr_bankarray_csrbank0_RDATA_IMAGE_we;
wire [15:0] csr_bankarray_csrbank0_RDATA_IMAGE_w;
reg csr_bankarray_csrbank0_RADD_MEMORY0_re;
wire [9:0] csr_bankarray_csrbank0_RADD_MEMORY0_r;
reg csr_bankarray_csrbank0_RADD_MEMORY0_we;
wire [9:0] csr_bankarray_csrbank0_RADD_MEMORY0_w;
reg csr_bankarray_csrbank0_DATA_MEMORY_re;
wire [7:0] csr_bankarray_csrbank0_DATA_MEMORY_r;
reg csr_bankarray_csrbank0_DATA_MEMORY_we;
wire [7:0] csr_bankarray_csrbank0_DATA_MEMORY_w;
reg csr_bankarray_csrbank0_CONV_OK_re;
wire csr_bankarray_csrbank0_CONV_OK_r;
reg csr_bankarray_csrbank0_CONV_OK_we;
wire csr_bankarray_csrbank0_CONV_OK_w;
reg csr_bankarray_csrbank0_MAX_OK_re;
wire csr_bankarray_csrbank0_MAX_OK_r;
reg csr_bankarray_csrbank0_MAX_OK_we;
wire csr_bankarray_csrbank0_MAX_OK_w;
reg csr_bankarray_csrbank0_DENS_OK_re;
wire csr_bankarray_csrbank0_DENS_OK_r;
reg csr_bankarray_csrbank0_DENS_OK_we;
wire csr_bankarray_csrbank0_DENS_OK_w;
reg csr_bankarray_csrbank0_MEM_OK_re;
wire csr_bankarray_csrbank0_MEM_OK_r;
reg csr_bankarray_csrbank0_MEM_OK_we;
wire csr_bankarray_csrbank0_MEM_OK_w;
wire csr_bankarray_csrbank0_sel;
wire [13:0] csr_bankarray_interface1_bank_bus_adr;
wire csr_bankarray_interface1_bank_bus_we;
wire [31:0] csr_bankarray_interface1_bank_bus_dat_w;
reg [31:0] csr_bankarray_interface1_bank_bus_dat_r = 32'd0;
reg csr_bankarray_csrbank1_reset0_re;
wire csr_bankarray_csrbank1_reset0_r;
reg csr_bankarray_csrbank1_reset0_we;
wire csr_bankarray_csrbank1_reset0_w;
reg csr_bankarray_csrbank1_scratch0_re;
wire [31:0] csr_bankarray_csrbank1_scratch0_r;
reg csr_bankarray_csrbank1_scratch0_we;
wire [31:0] csr_bankarray_csrbank1_scratch0_w;
reg csr_bankarray_csrbank1_bus_errors_re;
wire [31:0] csr_bankarray_csrbank1_bus_errors_r;
reg csr_bankarray_csrbank1_bus_errors_we;
wire [31:0] csr_bankarray_csrbank1_bus_errors_w;
wire csr_bankarray_csrbank1_sel;
wire [13:0] csr_bankarray_sram_bus_adr;
wire csr_bankarray_sram_bus_we;
wire [31:0] csr_bankarray_sram_bus_dat_w;
reg [31:0] csr_bankarray_sram_bus_dat_r;
wire [5:0] csr_bankarray_adr;
wire [7:0] csr_bankarray_dat_r;
wire csr_bankarray_sel;
reg csr_bankarray_sel_r = 1'd0;
wire [13:0] csr_bankarray_interface2_bank_bus_adr;
wire csr_bankarray_interface2_bank_bus_we;
wire [31:0] csr_bankarray_interface2_bank_bus_dat_w;
reg [31:0] csr_bankarray_interface2_bank_bus_dat_r = 32'd0;
reg csr_bankarray_csrbank2_load0_re;
wire [31:0] csr_bankarray_csrbank2_load0_r;
reg csr_bankarray_csrbank2_load0_we;
wire [31:0] csr_bankarray_csrbank2_load0_w;
reg csr_bankarray_csrbank2_reload0_re;
wire [31:0] csr_bankarray_csrbank2_reload0_r;
reg csr_bankarray_csrbank2_reload0_we;
wire [31:0] csr_bankarray_csrbank2_reload0_w;
reg csr_bankarray_csrbank2_en0_re;
wire csr_bankarray_csrbank2_en0_r;
reg csr_bankarray_csrbank2_en0_we;
wire csr_bankarray_csrbank2_en0_w;
reg csr_bankarray_csrbank2_update_value0_re;
wire csr_bankarray_csrbank2_update_value0_r;
reg csr_bankarray_csrbank2_update_value0_we;
wire csr_bankarray_csrbank2_update_value0_w;
reg csr_bankarray_csrbank2_value_re;
wire [31:0] csr_bankarray_csrbank2_value_r;
reg csr_bankarray_csrbank2_value_we;
wire [31:0] csr_bankarray_csrbank2_value_w;
reg csr_bankarray_csrbank2_ev_status_re;
wire csr_bankarray_csrbank2_ev_status_r;
reg csr_bankarray_csrbank2_ev_status_we;
wire csr_bankarray_csrbank2_ev_status_w;
reg csr_bankarray_csrbank2_ev_pending_re;
wire csr_bankarray_csrbank2_ev_pending_r;
reg csr_bankarray_csrbank2_ev_pending_we;
wire csr_bankarray_csrbank2_ev_pending_w;
reg csr_bankarray_csrbank2_ev_enable0_re;
wire csr_bankarray_csrbank2_ev_enable0_r;
reg csr_bankarray_csrbank2_ev_enable0_we;
wire csr_bankarray_csrbank2_ev_enable0_w;
wire csr_bankarray_csrbank2_sel;
wire [13:0] csr_bankarray_interface3_bank_bus_adr;
wire csr_bankarray_interface3_bank_bus_we;
wire [31:0] csr_bankarray_interface3_bank_bus_dat_w;
reg [31:0] csr_bankarray_interface3_bank_bus_dat_r = 32'd0;
reg csr_bankarray_csrbank3_txfull_re;
wire csr_bankarray_csrbank3_txfull_r;
reg csr_bankarray_csrbank3_txfull_we;
wire csr_bankarray_csrbank3_txfull_w;
reg csr_bankarray_csrbank3_rxempty_re;
wire csr_bankarray_csrbank3_rxempty_r;
reg csr_bankarray_csrbank3_rxempty_we;
wire csr_bankarray_csrbank3_rxempty_w;
reg csr_bankarray_csrbank3_ev_status_re;
wire [1:0] csr_bankarray_csrbank3_ev_status_r;
reg csr_bankarray_csrbank3_ev_status_we;
wire [1:0] csr_bankarray_csrbank3_ev_status_w;
reg csr_bankarray_csrbank3_ev_pending_re;
wire [1:0] csr_bankarray_csrbank3_ev_pending_r;
reg csr_bankarray_csrbank3_ev_pending_we;
wire [1:0] csr_bankarray_csrbank3_ev_pending_w;
reg csr_bankarray_csrbank3_ev_enable0_re;
wire [1:0] csr_bankarray_csrbank3_ev_enable0_r;
reg csr_bankarray_csrbank3_ev_enable0_we;
wire [1:0] csr_bankarray_csrbank3_ev_enable0_w;
reg csr_bankarray_csrbank3_txempty_re;
wire csr_bankarray_csrbank3_txempty_r;
reg csr_bankarray_csrbank3_txempty_we;
wire csr_bankarray_csrbank3_txempty_w;
reg csr_bankarray_csrbank3_rxfull_re;
wire csr_bankarray_csrbank3_rxfull_r;
reg csr_bankarray_csrbank3_rxfull_we;
wire csr_bankarray_csrbank3_rxfull_w;
wire csr_bankarray_csrbank3_sel;
wire [13:0] csr_interconnect_adr;
wire csr_interconnect_we;
wire [31:0] csr_interconnect_dat_w;
wire [31:0] csr_interconnect_dat_r;
reg state = 1'd0;
reg next_state;
reg [29:0] array_muxed0;
reg [31:0] array_muxed1;
reg [3:0] array_muxed2;
reg array_muxed3;
reg array_muxed4;
reg array_muxed5;
reg [2:0] array_muxed6;
reg [1:0] array_muxed7;
(* async_reg = "true", mr_ff = "true", dont_touch = "true" *) reg regs0 = 1'd0;
(* async_reg = "true", dont_touch = "true" *) reg regs1 = 1'd0;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign cpu_reset_1 = soccontroller_reset;
assign CLK = sys_clk;
assign {user_led_6, user_led_5, user_led_4, user_led_3, user_led_2, user_led_1, user_led} = NUMBER_OUT;
assign soccontroller_bus_error = error;

// synthesis translate_off
reg dummy_d;
// synthesis translate_on
always @(*) begin
	cpu_interrupt <= 32'd0;
	cpu_interrupt[1] <= timer_irq;
	cpu_interrupt[0] <= uart_irq;
// synthesis translate_off
	dummy_d <= dummy_s;
// synthesis translate_on
end
assign soccontroller_reset = soccontroller_reset_re;
assign soccontroller_bus_errors_status = soccontroller_bus_errors;
assign adr = ram_bus_adr[12:0];
assign ram_bus_dat_r = dat_r;

// synthesis translate_off
reg dummy_d_1;
// synthesis translate_on
always @(*) begin
	sram0_we <= 4'd0;
	sram0_we[0] <= (((interface0_ram_bus_cyc & interface0_ram_bus_stb) & interface0_ram_bus_we) & interface0_ram_bus_sel[0]);
	sram0_we[1] <= (((interface0_ram_bus_cyc & interface0_ram_bus_stb) & interface0_ram_bus_we) & interface0_ram_bus_sel[1]);
	sram0_we[2] <= (((interface0_ram_bus_cyc & interface0_ram_bus_stb) & interface0_ram_bus_we) & interface0_ram_bus_sel[2]);
	sram0_we[3] <= (((interface0_ram_bus_cyc & interface0_ram_bus_stb) & interface0_ram_bus_we) & interface0_ram_bus_sel[3]);
// synthesis translate_off
	dummy_d_1 <= dummy_s;
// synthesis translate_on
end
assign sram0_adr = interface0_ram_bus_adr[10:0];
assign interface0_ram_bus_dat_r = sram0_dat_r;
assign sram0_dat_w = interface0_ram_bus_dat_w;

// synthesis translate_off
reg dummy_d_2;
// synthesis translate_on
always @(*) begin
	sram1_we <= 4'd0;
	sram1_we[0] <= (((interface1_ram_bus_cyc & interface1_ram_bus_stb) & interface1_ram_bus_we) & interface1_ram_bus_sel[0]);
	sram1_we[1] <= (((interface1_ram_bus_cyc & interface1_ram_bus_stb) & interface1_ram_bus_we) & interface1_ram_bus_sel[1]);
	sram1_we[2] <= (((interface1_ram_bus_cyc & interface1_ram_bus_stb) & interface1_ram_bus_we) & interface1_ram_bus_sel[2]);
	sram1_we[3] <= (((interface1_ram_bus_cyc & interface1_ram_bus_stb) & interface1_ram_bus_we) & interface1_ram_bus_sel[3]);
// synthesis translate_off
	dummy_d_2 <= dummy_s;
// synthesis translate_on
end
assign sram1_adr = interface1_ram_bus_adr[11:0];
assign interface1_ram_bus_dat_r = sram1_dat_r;
assign sram1_dat_w = interface1_ram_bus_dat_w;

// synthesis translate_off
reg dummy_d_3;
// synthesis translate_on
always @(*) begin
	tx_sink_ready <= 1'd0;
	tx_enable <= 1'd0;
	rs232phytx_next_state <= 1'd0;
	tx_count_rs232phytx_next_value0 <= 4'd0;
	tx_count_rs232phytx_next_value_ce0 <= 1'd0;
	serial_tx_rs232phytx_next_value1 <= 1'd0;
	serial_tx_rs232phytx_next_value_ce1 <= 1'd0;
	tx_data_rs232phytx_next_value2 <= 8'd0;
	tx_data_rs232phytx_next_value_ce2 <= 1'd0;
	rs232phytx_next_state <= rs232phytx_state;
	case (rs232phytx_state)
		1'd1: begin
			tx_enable <= 1'd1;
			if (tx_tick) begin
				serial_tx_rs232phytx_next_value1 <= tx_data;
				serial_tx_rs232phytx_next_value_ce1 <= 1'd1;
				tx_count_rs232phytx_next_value0 <= (tx_count + 1'd1);
				tx_count_rs232phytx_next_value_ce0 <= 1'd1;
				tx_data_rs232phytx_next_value2 <= {1'd1, tx_data[7:1]};
				tx_data_rs232phytx_next_value_ce2 <= 1'd1;
				if ((tx_count == 4'd9)) begin
					tx_sink_ready <= 1'd1;
					rs232phytx_next_state <= 1'd0;
				end
			end
		end
		default: begin
			tx_count_rs232phytx_next_value0 <= 1'd0;
			tx_count_rs232phytx_next_value_ce0 <= 1'd1;
			serial_tx_rs232phytx_next_value1 <= 1'd1;
			serial_tx_rs232phytx_next_value_ce1 <= 1'd1;
			if (tx_sink_valid) begin
				serial_tx_rs232phytx_next_value1 <= 1'd0;
				serial_tx_rs232phytx_next_value_ce1 <= 1'd1;
				tx_data_rs232phytx_next_value2 <= tx_sink_payload_data;
				tx_data_rs232phytx_next_value_ce2 <= 1'd1;
				rs232phytx_next_state <= 1'd1;
			end
		end
	endcase
// synthesis translate_off
	dummy_d_3 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_4;
// synthesis translate_on
always @(*) begin
	rx_source_valid <= 1'd0;
	rx_source_payload_data <= 8'd0;
	rx_enable <= 1'd0;
	rs232phyrx_next_state <= 1'd0;
	rx_count_rs232phyrx_next_value0 <= 4'd0;
	rx_count_rs232phyrx_next_value_ce0 <= 1'd0;
	rx_data_rs232phyrx_next_value1 <= 8'd0;
	rx_data_rs232phyrx_next_value_ce1 <= 1'd0;
	rs232phyrx_next_state <= rs232phyrx_state;
	case (rs232phyrx_state)
		1'd1: begin
			rx_enable <= 1'd1;
			if (rx_tick) begin
				rx_count_rs232phyrx_next_value0 <= (rx_count + 1'd1);
				rx_count_rs232phyrx_next_value_ce0 <= 1'd1;
				rx_data_rs232phyrx_next_value1 <= {rx_rx, rx_data[7:1]};
				rx_data_rs232phyrx_next_value_ce1 <= 1'd1;
				if ((rx_count == 4'd9)) begin
					rx_source_valid <= (rx_rx == 1'd1);
					rx_source_payload_data <= rx_data;
					rs232phyrx_next_state <= 1'd0;
				end
			end
		end
		default: begin
			rx_count_rs232phyrx_next_value0 <= 1'd0;
			rx_count_rs232phyrx_next_value_ce0 <= 1'd1;
			if (((rx_rx == 1'd0) & (rx_rx_d == 1'd1))) begin
				rs232phyrx_next_state <= 1'd1;
			end
		end
	endcase
// synthesis translate_off
	dummy_d_4 <= dummy_s;
// synthesis translate_on
end
assign uart_uart_sink_valid = rx_source_valid;
assign rx_source_ready = uart_uart_sink_ready;
assign uart_uart_sink_first = rx_source_first;
assign uart_uart_sink_last = rx_source_last;
assign uart_uart_sink_payload_data = rx_source_payload_data;
assign tx_sink_valid = uart_uart_source_valid;
assign uart_uart_source_ready = tx_sink_ready;
assign tx_sink_first = uart_uart_source_first;
assign tx_sink_last = uart_uart_source_last;
assign tx_sink_payload_data = uart_uart_source_payload_data;
assign uart_tx_fifo_sink_valid = uart_rxtx_re;
assign uart_tx_fifo_sink_payload_data = uart_rxtx_r;
assign uart_txfull_status = (~uart_tx_fifo_sink_ready);
assign uart_txempty_status = (~uart_tx_fifo_source_valid);
assign uart_uart_source_valid = uart_tx_fifo_source_valid;
assign uart_tx_fifo_source_ready = uart_uart_source_ready;
assign uart_uart_source_first = uart_tx_fifo_source_first;
assign uart_uart_source_last = uart_tx_fifo_source_last;
assign uart_uart_source_payload_data = uart_tx_fifo_source_payload_data;
assign uart_tx_trigger = (~uart_tx_fifo_sink_ready);
assign uart_rx_fifo_sink_valid = uart_uart_sink_valid;
assign uart_uart_sink_ready = uart_rx_fifo_sink_ready;
assign uart_rx_fifo_sink_first = uart_uart_sink_first;
assign uart_rx_fifo_sink_last = uart_uart_sink_last;
assign uart_rx_fifo_sink_payload_data = uart_uart_sink_payload_data;
assign uart_rxempty_status = (~uart_rx_fifo_source_valid);
assign uart_rxfull_status = (~uart_rx_fifo_sink_ready);
assign uart_rxtx_w = uart_rx_fifo_source_payload_data;
assign uart_rx_fifo_source_ready = (uart_rx_clear | (1'd0 & uart_rxtx_we));
assign uart_rx_trigger = (~uart_rx_fifo_source_valid);
assign uart_tx0 = uart_tx_status;
assign uart_tx1 = uart_tx_pending;

// synthesis translate_off
reg dummy_d_5;
// synthesis translate_on
always @(*) begin
	uart_tx_clear <= 1'd0;
	if ((uart_pending_re & uart_pending_r[0])) begin
		uart_tx_clear <= 1'd1;
	end
// synthesis translate_off
	dummy_d_5 <= dummy_s;
// synthesis translate_on
end
assign uart_rx0 = uart_rx_status;
assign uart_rx1 = uart_rx_pending;

// synthesis translate_off
reg dummy_d_6;
// synthesis translate_on
always @(*) begin
	uart_rx_clear <= 1'd0;
	if ((uart_pending_re & uart_pending_r[1])) begin
		uart_rx_clear <= 1'd1;
	end
// synthesis translate_off
	dummy_d_6 <= dummy_s;
// synthesis translate_on
end
assign uart_irq = ((uart_pending_status[0] & uart_enable_storage[0]) | (uart_pending_status[1] & uart_enable_storage[1]));
assign uart_tx_status = uart_tx_trigger;
assign uart_rx_status = uart_rx_trigger;
assign uart_tx_fifo_syncfifo_din = {uart_tx_fifo_fifo_in_last, uart_tx_fifo_fifo_in_first, uart_tx_fifo_fifo_in_payload_data};
assign {uart_tx_fifo_fifo_out_last, uart_tx_fifo_fifo_out_first, uart_tx_fifo_fifo_out_payload_data} = uart_tx_fifo_syncfifo_dout;
assign uart_tx_fifo_sink_ready = uart_tx_fifo_syncfifo_writable;
assign uart_tx_fifo_syncfifo_we = uart_tx_fifo_sink_valid;
assign uart_tx_fifo_fifo_in_first = uart_tx_fifo_sink_first;
assign uart_tx_fifo_fifo_in_last = uart_tx_fifo_sink_last;
assign uart_tx_fifo_fifo_in_payload_data = uart_tx_fifo_sink_payload_data;
assign uart_tx_fifo_source_valid = uart_tx_fifo_readable;
assign uart_tx_fifo_source_first = uart_tx_fifo_fifo_out_first;
assign uart_tx_fifo_source_last = uart_tx_fifo_fifo_out_last;
assign uart_tx_fifo_source_payload_data = uart_tx_fifo_fifo_out_payload_data;
assign uart_tx_fifo_re = uart_tx_fifo_source_ready;
assign uart_tx_fifo_syncfifo_re = (uart_tx_fifo_syncfifo_readable & ((~uart_tx_fifo_readable) | uart_tx_fifo_re));
assign uart_tx_fifo_level1 = (uart_tx_fifo_level0 + uart_tx_fifo_readable);

// synthesis translate_off
reg dummy_d_7;
// synthesis translate_on
always @(*) begin
	uart_tx_fifo_wrport_adr <= 4'd0;
	if (uart_tx_fifo_replace) begin
		uart_tx_fifo_wrport_adr <= (uart_tx_fifo_produce - 1'd1);
	end else begin
		uart_tx_fifo_wrport_adr <= uart_tx_fifo_produce;
	end
// synthesis translate_off
	dummy_d_7 <= dummy_s;
// synthesis translate_on
end
assign uart_tx_fifo_wrport_dat_w = uart_tx_fifo_syncfifo_din;
assign uart_tx_fifo_wrport_we = (uart_tx_fifo_syncfifo_we & (uart_tx_fifo_syncfifo_writable | uart_tx_fifo_replace));
assign uart_tx_fifo_do_read = (uart_tx_fifo_syncfifo_readable & uart_tx_fifo_syncfifo_re);
assign uart_tx_fifo_rdport_adr = uart_tx_fifo_consume;
assign uart_tx_fifo_syncfifo_dout = uart_tx_fifo_rdport_dat_r;
assign uart_tx_fifo_rdport_re = uart_tx_fifo_do_read;
assign uart_tx_fifo_syncfifo_writable = (uart_tx_fifo_level0 != 5'd16);
assign uart_tx_fifo_syncfifo_readable = (uart_tx_fifo_level0 != 1'd0);
assign uart_rx_fifo_syncfifo_din = {uart_rx_fifo_fifo_in_last, uart_rx_fifo_fifo_in_first, uart_rx_fifo_fifo_in_payload_data};
assign {uart_rx_fifo_fifo_out_last, uart_rx_fifo_fifo_out_first, uart_rx_fifo_fifo_out_payload_data} = uart_rx_fifo_syncfifo_dout;
assign uart_rx_fifo_sink_ready = uart_rx_fifo_syncfifo_writable;
assign uart_rx_fifo_syncfifo_we = uart_rx_fifo_sink_valid;
assign uart_rx_fifo_fifo_in_first = uart_rx_fifo_sink_first;
assign uart_rx_fifo_fifo_in_last = uart_rx_fifo_sink_last;
assign uart_rx_fifo_fifo_in_payload_data = uart_rx_fifo_sink_payload_data;
assign uart_rx_fifo_source_valid = uart_rx_fifo_readable;
assign uart_rx_fifo_source_first = uart_rx_fifo_fifo_out_first;
assign uart_rx_fifo_source_last = uart_rx_fifo_fifo_out_last;
assign uart_rx_fifo_source_payload_data = uart_rx_fifo_fifo_out_payload_data;
assign uart_rx_fifo_re = uart_rx_fifo_source_ready;
assign uart_rx_fifo_syncfifo_re = (uart_rx_fifo_syncfifo_readable & ((~uart_rx_fifo_readable) | uart_rx_fifo_re));
assign uart_rx_fifo_level1 = (uart_rx_fifo_level0 + uart_rx_fifo_readable);

// synthesis translate_off
reg dummy_d_8;
// synthesis translate_on
always @(*) begin
	uart_rx_fifo_wrport_adr <= 4'd0;
	if (uart_rx_fifo_replace) begin
		uart_rx_fifo_wrport_adr <= (uart_rx_fifo_produce - 1'd1);
	end else begin
		uart_rx_fifo_wrport_adr <= uart_rx_fifo_produce;
	end
// synthesis translate_off
	dummy_d_8 <= dummy_s;
// synthesis translate_on
end
assign uart_rx_fifo_wrport_dat_w = uart_rx_fifo_syncfifo_din;
assign uart_rx_fifo_wrport_we = (uart_rx_fifo_syncfifo_we & (uart_rx_fifo_syncfifo_writable | uart_rx_fifo_replace));
assign uart_rx_fifo_do_read = (uart_rx_fifo_syncfifo_readable & uart_rx_fifo_syncfifo_re);
assign uart_rx_fifo_rdport_adr = uart_rx_fifo_consume;
assign uart_rx_fifo_syncfifo_dout = uart_rx_fifo_rdport_dat_r;
assign uart_rx_fifo_rdport_re = uart_rx_fifo_do_read;
assign uart_rx_fifo_syncfifo_writable = (uart_rx_fifo_level0 != 5'd16);
assign uart_rx_fifo_syncfifo_readable = (uart_rx_fifo_level0 != 1'd0);
assign timer_zero_trigger = (timer_value != 1'd0);
assign timer_zero0 = timer_zero_status;
assign timer_zero1 = timer_zero_pending;

// synthesis translate_off
reg dummy_d_9;
// synthesis translate_on
always @(*) begin
	timer_zero_clear <= 1'd0;
	if ((timer_pending_re & timer_pending_r)) begin
		timer_zero_clear <= 1'd1;
	end
// synthesis translate_off
	dummy_d_9 <= dummy_s;
// synthesis translate_on
end
assign timer_irq = (timer_pending_status & timer_enable_storage);
assign timer_zero_status = timer_zero_trigger;
assign sys_clk = clk125;
assign por_clk = clk125;
assign sys_rst = int_rst;

// synthesis translate_off
reg dummy_d_10;
// synthesis translate_on
always @(*) begin
	basesoc_adr <= 14'd0;
	basesoc_we <= 1'd0;
	basesoc_dat_w <= 32'd0;
	basesoc_wishbone_dat_r <= 32'd0;
	basesoc_wishbone_ack <= 1'd0;
	next_state <= 1'd0;
	next_state <= state;
	case (state)
		1'd1: begin
			basesoc_wishbone_ack <= 1'd1;
			basesoc_wishbone_dat_r <= basesoc_dat_r;
			next_state <= 1'd0;
		end
		default: begin
			basesoc_dat_w <= basesoc_wishbone_dat_w;
			if ((basesoc_wishbone_cyc & basesoc_wishbone_stb)) begin
				basesoc_adr <= basesoc_wishbone_adr;
				basesoc_we <= (basesoc_wishbone_we & (basesoc_wishbone_sel != 1'd0));
				next_state <= 1'd1;
			end
		end
	endcase
// synthesis translate_off
	dummy_d_10 <= dummy_s;
// synthesis translate_on
end
assign shared_adr = array_muxed0;
assign shared_dat_w = array_muxed1;
assign shared_sel = array_muxed2;
assign shared_cyc = array_muxed3;
assign shared_stb = array_muxed4;
assign shared_we = array_muxed5;
assign shared_cti = array_muxed6;
assign shared_bte = array_muxed7;
assign cpu_ibus_dat_r = shared_dat_r;
assign cpu_dbus_dat_r = shared_dat_r;
assign cpu_ibus_ack = (shared_ack & (grant == 1'd0));
assign cpu_dbus_ack = (shared_ack & (grant == 1'd1));
assign cpu_ibus_err = (shared_err & (grant == 1'd0));
assign cpu_dbus_err = (shared_err & (grant == 1'd1));
assign request = {cpu_dbus_cyc, cpu_ibus_cyc};

// synthesis translate_off
reg dummy_d_11;
// synthesis translate_on
always @(*) begin
	slave_sel <= 4'd0;
	slave_sel[0] <= (shared_adr[29:13] == 1'd0);
	slave_sel[1] <= (shared_adr[29:11] == 16'd32768);
	slave_sel[2] <= (shared_adr[29:12] == 17'd65536);
	slave_sel[3] <= (shared_adr[29:14] == 16'd61440);
// synthesis translate_off
	dummy_d_11 <= dummy_s;
// synthesis translate_on
end
assign ram_bus_adr = shared_adr;
assign ram_bus_dat_w = shared_dat_w;
assign ram_bus_sel = shared_sel;
assign ram_bus_stb = shared_stb;
assign ram_bus_we = shared_we;
assign ram_bus_cti = shared_cti;
assign ram_bus_bte = shared_bte;
assign interface0_ram_bus_adr = shared_adr;
assign interface0_ram_bus_dat_w = shared_dat_w;
assign interface0_ram_bus_sel = shared_sel;
assign interface0_ram_bus_stb = shared_stb;
assign interface0_ram_bus_we = shared_we;
assign interface0_ram_bus_cti = shared_cti;
assign interface0_ram_bus_bte = shared_bte;
assign interface1_ram_bus_adr = shared_adr;
assign interface1_ram_bus_dat_w = shared_dat_w;
assign interface1_ram_bus_sel = shared_sel;
assign interface1_ram_bus_stb = shared_stb;
assign interface1_ram_bus_we = shared_we;
assign interface1_ram_bus_cti = shared_cti;
assign interface1_ram_bus_bte = shared_bte;
assign basesoc_wishbone_adr = shared_adr;
assign basesoc_wishbone_dat_w = shared_dat_w;
assign basesoc_wishbone_sel = shared_sel;
assign basesoc_wishbone_stb = shared_stb;
assign basesoc_wishbone_we = shared_we;
assign basesoc_wishbone_cti = shared_cti;
assign basesoc_wishbone_bte = shared_bte;
assign ram_bus_cyc = (shared_cyc & slave_sel[0]);
assign interface0_ram_bus_cyc = (shared_cyc & slave_sel[1]);
assign interface1_ram_bus_cyc = (shared_cyc & slave_sel[2]);
assign basesoc_wishbone_cyc = (shared_cyc & slave_sel[3]);
assign shared_err = (((ram_bus_err | interface0_ram_bus_err) | interface1_ram_bus_err) | basesoc_wishbone_err);
assign wait_1 = ((shared_stb & shared_cyc) & (~shared_ack));

// synthesis translate_off
reg dummy_d_12;
// synthesis translate_on
always @(*) begin
	shared_dat_r <= 32'd0;
	shared_ack <= 1'd0;
	error <= 1'd0;
	shared_ack <= (((ram_bus_ack | interface0_ram_bus_ack) | interface1_ram_bus_ack) | basesoc_wishbone_ack);
	shared_dat_r <= (((({32{slave_sel_r[0]}} & ram_bus_dat_r) | ({32{slave_sel_r[1]}} & interface0_ram_bus_dat_r)) | ({32{slave_sel_r[2]}} & interface1_ram_bus_dat_r)) | ({32{slave_sel_r[3]}} & basesoc_wishbone_dat_r));
	if (done) begin
		shared_dat_r <= 32'd4294967295;
		shared_ack <= 1'd1;
		error <= 1'd1;
	end
// synthesis translate_off
	dummy_d_12 <= dummy_s;
// synthesis translate_on
end
assign done = (count == 1'd0);
assign csr_bankarray_csrbank0_sel = (csr_bankarray_interface0_bank_bus_adr[13:9] == 1'd0);
assign csr_bankarray_csrbank0_EN0_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_13;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_EN0_re <= 1'd0;
	csr_bankarray_csrbank0_EN0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 1'd0))) begin
		csr_bankarray_csrbank0_EN0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_EN0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_13 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_RST0_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_14;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_RST0_re <= 1'd0;
	csr_bankarray_csrbank0_RST0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 1'd1))) begin
		csr_bankarray_csrbank0_RST0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_RST0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_14 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_SEL0_r = csr_bankarray_interface0_bank_bus_dat_w[3:0];

// synthesis translate_off
reg dummy_d_15;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_SEL0_re <= 1'd0;
	csr_bankarray_csrbank0_SEL0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 2'd2))) begin
		csr_bankarray_csrbank0_SEL0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_SEL0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_15 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_WEN_IMAGE0_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_16;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_WEN_IMAGE0_re <= 1'd0;
	csr_bankarray_csrbank0_WEN_IMAGE0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 2'd3))) begin
		csr_bankarray_csrbank0_WEN_IMAGE0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_WEN_IMAGE0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_16 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_WADD_IMAGE0_r = csr_bankarray_interface0_bank_bus_dat_w[9:0];

// synthesis translate_off
reg dummy_d_17;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_WADD_IMAGE0_re <= 1'd0;
	csr_bankarray_csrbank0_WADD_IMAGE0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 3'd4))) begin
		csr_bankarray_csrbank0_WADD_IMAGE0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_WADD_IMAGE0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_17 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_WDATA_IMAGE0_r = csr_bankarray_interface0_bank_bus_dat_w[15:0];

// synthesis translate_off
reg dummy_d_18;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_WDATA_IMAGE0_re <= 1'd0;
	csr_bankarray_csrbank0_WDATA_IMAGE0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 3'd5))) begin
		csr_bankarray_csrbank0_WDATA_IMAGE0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_WDATA_IMAGE0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_18 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_REN_MEMORY0_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_19;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_REN_MEMORY0_re <= 1'd0;
	csr_bankarray_csrbank0_REN_MEMORY0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 3'd6))) begin
		csr_bankarray_csrbank0_REN_MEMORY0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_REN_MEMORY0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_19 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_REN_IMAGE0_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_20;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_REN_IMAGE0_re <= 1'd0;
	csr_bankarray_csrbank0_REN_IMAGE0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 3'd7))) begin
		csr_bankarray_csrbank0_REN_IMAGE0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_REN_IMAGE0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_20 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_RADD_IMAGE0_r = csr_bankarray_interface0_bank_bus_dat_w[9:0];

// synthesis translate_off
reg dummy_d_21;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_RADD_IMAGE0_re <= 1'd0;
	csr_bankarray_csrbank0_RADD_IMAGE0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd8))) begin
		csr_bankarray_csrbank0_RADD_IMAGE0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_RADD_IMAGE0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_21 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_RDATA_IMAGE_r = csr_bankarray_interface0_bank_bus_dat_w[15:0];

// synthesis translate_off
reg dummy_d_22;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_RDATA_IMAGE_re <= 1'd0;
	csr_bankarray_csrbank0_RDATA_IMAGE_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd9))) begin
		csr_bankarray_csrbank0_RDATA_IMAGE_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_RDATA_IMAGE_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_22 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_RADD_MEMORY0_r = csr_bankarray_interface0_bank_bus_dat_w[9:0];

// synthesis translate_off
reg dummy_d_23;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_RADD_MEMORY0_re <= 1'd0;
	csr_bankarray_csrbank0_RADD_MEMORY0_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd10))) begin
		csr_bankarray_csrbank0_RADD_MEMORY0_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_RADD_MEMORY0_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_23 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_DATA_MEMORY_r = csr_bankarray_interface0_bank_bus_dat_w[7:0];

// synthesis translate_off
reg dummy_d_24;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_DATA_MEMORY_re <= 1'd0;
	csr_bankarray_csrbank0_DATA_MEMORY_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd11))) begin
		csr_bankarray_csrbank0_DATA_MEMORY_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_DATA_MEMORY_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_24 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_CONV_OK_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_25;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_CONV_OK_re <= 1'd0;
	csr_bankarray_csrbank0_CONV_OK_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd12))) begin
		csr_bankarray_csrbank0_CONV_OK_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_CONV_OK_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_25 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_MAX_OK_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_26;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_MAX_OK_re <= 1'd0;
	csr_bankarray_csrbank0_MAX_OK_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd13))) begin
		csr_bankarray_csrbank0_MAX_OK_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_MAX_OK_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_26 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_DENS_OK_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_27;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_DENS_OK_re <= 1'd0;
	csr_bankarray_csrbank0_DENS_OK_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd14))) begin
		csr_bankarray_csrbank0_DENS_OK_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_DENS_OK_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_27 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_MEM_OK_r = csr_bankarray_interface0_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_28;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank0_MEM_OK_re <= 1'd0;
	csr_bankarray_csrbank0_MEM_OK_we <= 1'd0;
	if ((csr_bankarray_csrbank0_sel & (csr_bankarray_interface0_bank_bus_adr[8:0] == 4'd15))) begin
		csr_bankarray_csrbank0_MEM_OK_re <= csr_bankarray_interface0_bank_bus_we;
		csr_bankarray_csrbank0_MEM_OK_we <= (~csr_bankarray_interface0_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_28 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank0_EN0_w = EN_storage;
assign csr_bankarray_csrbank0_RST0_w = RST_storage;
assign csr_bankarray_csrbank0_SEL0_w = SEL_storage[3:0];
assign csr_bankarray_csrbank0_WEN_IMAGE0_w = WEN_IMAGE_storage;
assign csr_bankarray_csrbank0_WADD_IMAGE0_w = WADD_IMAGE_storage[9:0];
assign csr_bankarray_csrbank0_WDATA_IMAGE0_w = WDATA_IMAGE_storage[15:0];
assign csr_bankarray_csrbank0_REN_MEMORY0_w = REN_MEMORY_storage;
assign csr_bankarray_csrbank0_REN_IMAGE0_w = REN_IMAGE_storage;
assign csr_bankarray_csrbank0_RADD_IMAGE0_w = RADD_IMAGE_storage[9:0];
assign csr_bankarray_csrbank0_RDATA_IMAGE_w = RDATA_IMAGE_status[15:0];
assign RDATA_IMAGE_we = csr_bankarray_csrbank0_RDATA_IMAGE_we;
assign csr_bankarray_csrbank0_RADD_MEMORY0_w = RADD_MEMORY_storage[9:0];
assign csr_bankarray_csrbank0_DATA_MEMORY_w = DATA_MEMORY_status[7:0];
assign DATA_MEMORY_we = csr_bankarray_csrbank0_DATA_MEMORY_we;
assign csr_bankarray_csrbank0_CONV_OK_w = CONV_OK_status;
assign CONV_OK_we = csr_bankarray_csrbank0_CONV_OK_we;
assign csr_bankarray_csrbank0_MAX_OK_w = MAX_OK_status;
assign MAX_OK_we = csr_bankarray_csrbank0_MAX_OK_we;
assign csr_bankarray_csrbank0_DENS_OK_w = DENS_OK_status;
assign DENS_OK_we = csr_bankarray_csrbank0_DENS_OK_we;
assign csr_bankarray_csrbank0_MEM_OK_w = MEM_OK_status;
assign MEM_OK_we = csr_bankarray_csrbank0_MEM_OK_we;
assign csr_bankarray_csrbank1_sel = (csr_bankarray_interface1_bank_bus_adr[13:9] == 1'd1);
assign csr_bankarray_csrbank1_reset0_r = csr_bankarray_interface1_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_29;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank1_reset0_re <= 1'd0;
	csr_bankarray_csrbank1_reset0_we <= 1'd0;
	if ((csr_bankarray_csrbank1_sel & (csr_bankarray_interface1_bank_bus_adr[8:0] == 1'd0))) begin
		csr_bankarray_csrbank1_reset0_re <= csr_bankarray_interface1_bank_bus_we;
		csr_bankarray_csrbank1_reset0_we <= (~csr_bankarray_interface1_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_29 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank1_scratch0_r = csr_bankarray_interface1_bank_bus_dat_w[31:0];

// synthesis translate_off
reg dummy_d_30;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank1_scratch0_re <= 1'd0;
	csr_bankarray_csrbank1_scratch0_we <= 1'd0;
	if ((csr_bankarray_csrbank1_sel & (csr_bankarray_interface1_bank_bus_adr[8:0] == 1'd1))) begin
		csr_bankarray_csrbank1_scratch0_re <= csr_bankarray_interface1_bank_bus_we;
		csr_bankarray_csrbank1_scratch0_we <= (~csr_bankarray_interface1_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_30 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank1_bus_errors_r = csr_bankarray_interface1_bank_bus_dat_w[31:0];

// synthesis translate_off
reg dummy_d_31;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank1_bus_errors_re <= 1'd0;
	csr_bankarray_csrbank1_bus_errors_we <= 1'd0;
	if ((csr_bankarray_csrbank1_sel & (csr_bankarray_interface1_bank_bus_adr[8:0] == 2'd2))) begin
		csr_bankarray_csrbank1_bus_errors_re <= csr_bankarray_interface1_bank_bus_we;
		csr_bankarray_csrbank1_bus_errors_we <= (~csr_bankarray_interface1_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_31 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank1_reset0_w = soccontroller_reset_storage;
assign csr_bankarray_csrbank1_scratch0_w = soccontroller_scratch_storage[31:0];
assign csr_bankarray_csrbank1_bus_errors_w = soccontroller_bus_errors_status[31:0];
assign soccontroller_bus_errors_we = csr_bankarray_csrbank1_bus_errors_we;
assign csr_bankarray_sel = (csr_bankarray_sram_bus_adr[13:9] == 2'd2);

// synthesis translate_off
reg dummy_d_32;
// synthesis translate_on
always @(*) begin
	csr_bankarray_sram_bus_dat_r <= 32'd0;
	if (csr_bankarray_sel_r) begin
		csr_bankarray_sram_bus_dat_r <= csr_bankarray_dat_r;
	end
// synthesis translate_off
	dummy_d_32 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_adr = csr_bankarray_sram_bus_adr[5:0];
assign csr_bankarray_csrbank2_sel = (csr_bankarray_interface2_bank_bus_adr[13:9] == 2'd3);
assign csr_bankarray_csrbank2_load0_r = csr_bankarray_interface2_bank_bus_dat_w[31:0];

// synthesis translate_off
reg dummy_d_33;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_load0_re <= 1'd0;
	csr_bankarray_csrbank2_load0_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 1'd0))) begin
		csr_bankarray_csrbank2_load0_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_load0_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_33 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_reload0_r = csr_bankarray_interface2_bank_bus_dat_w[31:0];

// synthesis translate_off
reg dummy_d_34;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_reload0_re <= 1'd0;
	csr_bankarray_csrbank2_reload0_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 1'd1))) begin
		csr_bankarray_csrbank2_reload0_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_reload0_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_34 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_en0_r = csr_bankarray_interface2_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_35;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_en0_re <= 1'd0;
	csr_bankarray_csrbank2_en0_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 2'd2))) begin
		csr_bankarray_csrbank2_en0_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_en0_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_35 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_update_value0_r = csr_bankarray_interface2_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_36;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_update_value0_re <= 1'd0;
	csr_bankarray_csrbank2_update_value0_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 2'd3))) begin
		csr_bankarray_csrbank2_update_value0_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_update_value0_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_36 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_value_r = csr_bankarray_interface2_bank_bus_dat_w[31:0];

// synthesis translate_off
reg dummy_d_37;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_value_re <= 1'd0;
	csr_bankarray_csrbank2_value_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 3'd4))) begin
		csr_bankarray_csrbank2_value_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_value_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_37 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_ev_status_r = csr_bankarray_interface2_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_38;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_ev_status_re <= 1'd0;
	csr_bankarray_csrbank2_ev_status_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 3'd5))) begin
		csr_bankarray_csrbank2_ev_status_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_ev_status_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_38 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_ev_pending_r = csr_bankarray_interface2_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_39;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_ev_pending_re <= 1'd0;
	csr_bankarray_csrbank2_ev_pending_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 3'd6))) begin
		csr_bankarray_csrbank2_ev_pending_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_ev_pending_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_39 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_ev_enable0_r = csr_bankarray_interface2_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_40;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank2_ev_enable0_re <= 1'd0;
	csr_bankarray_csrbank2_ev_enable0_we <= 1'd0;
	if ((csr_bankarray_csrbank2_sel & (csr_bankarray_interface2_bank_bus_adr[8:0] == 3'd7))) begin
		csr_bankarray_csrbank2_ev_enable0_re <= csr_bankarray_interface2_bank_bus_we;
		csr_bankarray_csrbank2_ev_enable0_we <= (~csr_bankarray_interface2_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_40 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank2_load0_w = timer_load_storage[31:0];
assign csr_bankarray_csrbank2_reload0_w = timer_reload_storage[31:0];
assign csr_bankarray_csrbank2_en0_w = timer_en_storage;
assign csr_bankarray_csrbank2_update_value0_w = timer_update_value_storage;
assign csr_bankarray_csrbank2_value_w = timer_value_status[31:0];
assign timer_value_we = csr_bankarray_csrbank2_value_we;
assign timer_status_status = timer_zero0;
assign csr_bankarray_csrbank2_ev_status_w = timer_status_status;
assign timer_status_we = csr_bankarray_csrbank2_ev_status_we;
assign timer_pending_status = timer_zero1;
assign csr_bankarray_csrbank2_ev_pending_w = timer_pending_status;
assign timer_pending_we = csr_bankarray_csrbank2_ev_pending_we;
assign timer_zero2 = timer_enable_storage;
assign csr_bankarray_csrbank2_ev_enable0_w = timer_enable_storage;
assign csr_bankarray_csrbank3_sel = (csr_bankarray_interface3_bank_bus_adr[13:9] == 3'd4);
assign uart_rxtx_r = csr_bankarray_interface3_bank_bus_dat_w[7:0];

// synthesis translate_off
reg dummy_d_41;
// synthesis translate_on
always @(*) begin
	uart_rxtx_re <= 1'd0;
	uart_rxtx_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 1'd0))) begin
		uart_rxtx_re <= csr_bankarray_interface3_bank_bus_we;
		uart_rxtx_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_41 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_txfull_r = csr_bankarray_interface3_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_42;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_txfull_re <= 1'd0;
	csr_bankarray_csrbank3_txfull_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 1'd1))) begin
		csr_bankarray_csrbank3_txfull_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_txfull_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_42 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_rxempty_r = csr_bankarray_interface3_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_43;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_rxempty_re <= 1'd0;
	csr_bankarray_csrbank3_rxempty_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 2'd2))) begin
		csr_bankarray_csrbank3_rxempty_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_rxempty_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_43 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_ev_status_r = csr_bankarray_interface3_bank_bus_dat_w[1:0];

// synthesis translate_off
reg dummy_d_44;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_ev_status_re <= 1'd0;
	csr_bankarray_csrbank3_ev_status_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 2'd3))) begin
		csr_bankarray_csrbank3_ev_status_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_ev_status_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_44 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_ev_pending_r = csr_bankarray_interface3_bank_bus_dat_w[1:0];

// synthesis translate_off
reg dummy_d_45;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_ev_pending_re <= 1'd0;
	csr_bankarray_csrbank3_ev_pending_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 3'd4))) begin
		csr_bankarray_csrbank3_ev_pending_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_ev_pending_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_45 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_ev_enable0_r = csr_bankarray_interface3_bank_bus_dat_w[1:0];

// synthesis translate_off
reg dummy_d_46;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_ev_enable0_re <= 1'd0;
	csr_bankarray_csrbank3_ev_enable0_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 3'd5))) begin
		csr_bankarray_csrbank3_ev_enable0_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_ev_enable0_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_46 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_txempty_r = csr_bankarray_interface3_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_47;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_txempty_re <= 1'd0;
	csr_bankarray_csrbank3_txempty_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 3'd6))) begin
		csr_bankarray_csrbank3_txempty_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_txempty_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_47 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_rxfull_r = csr_bankarray_interface3_bank_bus_dat_w[0];

// synthesis translate_off
reg dummy_d_48;
// synthesis translate_on
always @(*) begin
	csr_bankarray_csrbank3_rxfull_re <= 1'd0;
	csr_bankarray_csrbank3_rxfull_we <= 1'd0;
	if ((csr_bankarray_csrbank3_sel & (csr_bankarray_interface3_bank_bus_adr[8:0] == 3'd7))) begin
		csr_bankarray_csrbank3_rxfull_re <= csr_bankarray_interface3_bank_bus_we;
		csr_bankarray_csrbank3_rxfull_we <= (~csr_bankarray_interface3_bank_bus_we);
	end
// synthesis translate_off
	dummy_d_48 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_txfull_w = uart_txfull_status;
assign uart_txfull_we = csr_bankarray_csrbank3_txfull_we;
assign csr_bankarray_csrbank3_rxempty_w = uart_rxempty_status;
assign uart_rxempty_we = csr_bankarray_csrbank3_rxempty_we;

// synthesis translate_off
reg dummy_d_49;
// synthesis translate_on
always @(*) begin
	uart_status_status <= 2'd0;
	uart_status_status[0] <= uart_tx0;
	uart_status_status[1] <= uart_rx0;
// synthesis translate_off
	dummy_d_49 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_ev_status_w = uart_status_status[1:0];
assign uart_status_we = csr_bankarray_csrbank3_ev_status_we;

// synthesis translate_off
reg dummy_d_50;
// synthesis translate_on
always @(*) begin
	uart_pending_status <= 2'd0;
	uart_pending_status[0] <= uart_tx1;
	uart_pending_status[1] <= uart_rx1;
// synthesis translate_off
	dummy_d_50 <= dummy_s;
// synthesis translate_on
end
assign csr_bankarray_csrbank3_ev_pending_w = uart_pending_status[1:0];
assign uart_pending_we = csr_bankarray_csrbank3_ev_pending_we;
assign uart_tx2 = uart_enable_storage[0];
assign uart_rx2 = uart_enable_storage[1];
assign csr_bankarray_csrbank3_ev_enable0_w = uart_enable_storage[1:0];
assign csr_bankarray_csrbank3_txempty_w = uart_txempty_status;
assign uart_txempty_we = csr_bankarray_csrbank3_txempty_we;
assign csr_bankarray_csrbank3_rxfull_w = uart_rxfull_status;
assign uart_rxfull_we = csr_bankarray_csrbank3_rxfull_we;
assign csr_interconnect_adr = basesoc_adr;
assign csr_interconnect_we = basesoc_we;
assign csr_interconnect_dat_w = basesoc_dat_w;
assign basesoc_dat_r = csr_interconnect_dat_r;
assign csr_bankarray_interface0_bank_bus_adr = csr_interconnect_adr;
assign csr_bankarray_interface1_bank_bus_adr = csr_interconnect_adr;
assign csr_bankarray_interface2_bank_bus_adr = csr_interconnect_adr;
assign csr_bankarray_interface3_bank_bus_adr = csr_interconnect_adr;
assign csr_bankarray_sram_bus_adr = csr_interconnect_adr;
assign csr_bankarray_interface0_bank_bus_we = csr_interconnect_we;
assign csr_bankarray_interface1_bank_bus_we = csr_interconnect_we;
assign csr_bankarray_interface2_bank_bus_we = csr_interconnect_we;
assign csr_bankarray_interface3_bank_bus_we = csr_interconnect_we;
assign csr_bankarray_sram_bus_we = csr_interconnect_we;
assign csr_bankarray_interface0_bank_bus_dat_w = csr_interconnect_dat_w;
assign csr_bankarray_interface1_bank_bus_dat_w = csr_interconnect_dat_w;
assign csr_bankarray_interface2_bank_bus_dat_w = csr_interconnect_dat_w;
assign csr_bankarray_interface3_bank_bus_dat_w = csr_interconnect_dat_w;
assign csr_bankarray_sram_bus_dat_w = csr_interconnect_dat_w;
assign csr_interconnect_dat_r = ((((csr_bankarray_interface0_bank_bus_dat_r | csr_bankarray_interface1_bank_bus_dat_r) | csr_bankarray_interface2_bank_bus_dat_r) | csr_bankarray_interface3_bank_bus_dat_r) | csr_bankarray_sram_bus_dat_r);

// synthesis translate_off
reg dummy_d_51;
// synthesis translate_on
always @(*) begin
	array_muxed0 <= 30'd0;
	case (grant)
		1'd0: begin
			array_muxed0 <= cpu_ibus_adr;
		end
		default: begin
			array_muxed0 <= cpu_dbus_adr;
		end
	endcase
// synthesis translate_off
	dummy_d_51 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_52;
// synthesis translate_on
always @(*) begin
	array_muxed1 <= 32'd0;
	case (grant)
		1'd0: begin
			array_muxed1 <= cpu_ibus_dat_w;
		end
		default: begin
			array_muxed1 <= cpu_dbus_dat_w;
		end
	endcase
// synthesis translate_off
	dummy_d_52 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_53;
// synthesis translate_on
always @(*) begin
	array_muxed2 <= 4'd0;
	case (grant)
		1'd0: begin
			array_muxed2 <= cpu_ibus_sel;
		end
		default: begin
			array_muxed2 <= cpu_dbus_sel;
		end
	endcase
// synthesis translate_off
	dummy_d_53 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_54;
// synthesis translate_on
always @(*) begin
	array_muxed3 <= 1'd0;
	case (grant)
		1'd0: begin
			array_muxed3 <= cpu_ibus_cyc;
		end
		default: begin
			array_muxed3 <= cpu_dbus_cyc;
		end
	endcase
// synthesis translate_off
	dummy_d_54 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_55;
// synthesis translate_on
always @(*) begin
	array_muxed4 <= 1'd0;
	case (grant)
		1'd0: begin
			array_muxed4 <= cpu_ibus_stb;
		end
		default: begin
			array_muxed4 <= cpu_dbus_stb;
		end
	endcase
// synthesis translate_off
	dummy_d_55 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_56;
// synthesis translate_on
always @(*) begin
	array_muxed5 <= 1'd0;
	case (grant)
		1'd0: begin
			array_muxed5 <= cpu_ibus_we;
		end
		default: begin
			array_muxed5 <= cpu_dbus_we;
		end
	endcase
// synthesis translate_off
	dummy_d_56 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_57;
// synthesis translate_on
always @(*) begin
	array_muxed6 <= 3'd0;
	case (grant)
		1'd0: begin
			array_muxed6 <= cpu_ibus_cti;
		end
		default: begin
			array_muxed6 <= cpu_dbus_cti;
		end
	endcase
// synthesis translate_off
	dummy_d_57 <= dummy_s;
// synthesis translate_on
end

// synthesis translate_off
reg dummy_d_58;
// synthesis translate_on
always @(*) begin
	array_muxed7 <= 2'd0;
	case (grant)
		1'd0: begin
			array_muxed7 <= cpu_ibus_bte;
		end
		default: begin
			array_muxed7 <= cpu_dbus_bte;
		end
	endcase
// synthesis translate_off
	dummy_d_58 <= dummy_s;
// synthesis translate_on
end
assign rx_rx = regs1;

always @(posedge por_clk) begin
	int_rst <= cpu_reset;
end

always @(posedge sys_clk) begin
	if ((soccontroller_bus_errors != 32'd4294967295)) begin
		if (soccontroller_bus_error) begin
			soccontroller_bus_errors <= (soccontroller_bus_errors + 1'd1);
		end
	end
	ram_bus_ack <= 1'd0;
	if (((ram_bus_cyc & ram_bus_stb) & (~ram_bus_ack))) begin
		ram_bus_ack <= 1'd1;
	end
	interface0_ram_bus_ack <= 1'd0;
	if (((interface0_ram_bus_cyc & interface0_ram_bus_stb) & (~interface0_ram_bus_ack))) begin
		interface0_ram_bus_ack <= 1'd1;
	end
	interface1_ram_bus_ack <= 1'd0;
	if (((interface1_ram_bus_cyc & interface1_ram_bus_stb) & (~interface1_ram_bus_ack))) begin
		interface1_ram_bus_ack <= 1'd1;
	end
	{tx_tick, tx_phase} <= 22'd3958241;
	if (tx_enable) begin
		{tx_tick, tx_phase} <= (tx_phase + 22'd3958241);
	end
	rs232phytx_state <= rs232phytx_next_state;
	if (tx_count_rs232phytx_next_value_ce0) begin
		tx_count <= tx_count_rs232phytx_next_value0;
	end
	if (serial_tx_rs232phytx_next_value_ce1) begin
		serial_tx <= serial_tx_rs232phytx_next_value1;
	end
	if (tx_data_rs232phytx_next_value_ce2) begin
		tx_data <= tx_data_rs232phytx_next_value2;
	end
	rx_rx_d <= rx_rx;
	{rx_tick, rx_phase} <= 32'd2147483648;
	if (rx_enable) begin
		{rx_tick, rx_phase} <= (rx_phase + 22'd3958241);
	end
	rs232phyrx_state <= rs232phyrx_next_state;
	if (rx_count_rs232phyrx_next_value_ce0) begin
		rx_count <= rx_count_rs232phyrx_next_value0;
	end
	if (rx_data_rs232phyrx_next_value_ce1) begin
		rx_data <= rx_data_rs232phyrx_next_value1;
	end
	if (uart_tx_clear) begin
		uart_tx_pending <= 1'd0;
	end
	uart_tx_trigger_d <= uart_tx_trigger;
	if (((~uart_tx_trigger) & uart_tx_trigger_d)) begin
		uart_tx_pending <= 1'd1;
	end
	if (uart_rx_clear) begin
		uart_rx_pending <= 1'd0;
	end
	uart_rx_trigger_d <= uart_rx_trigger;
	if (((~uart_rx_trigger) & uart_rx_trigger_d)) begin
		uart_rx_pending <= 1'd1;
	end
	if (uart_tx_fifo_syncfifo_re) begin
		uart_tx_fifo_readable <= 1'd1;
	end else begin
		if (uart_tx_fifo_re) begin
			uart_tx_fifo_readable <= 1'd0;
		end
	end
	if (((uart_tx_fifo_syncfifo_we & uart_tx_fifo_syncfifo_writable) & (~uart_tx_fifo_replace))) begin
		uart_tx_fifo_produce <= (uart_tx_fifo_produce + 1'd1);
	end
	if (uart_tx_fifo_do_read) begin
		uart_tx_fifo_consume <= (uart_tx_fifo_consume + 1'd1);
	end
	if (((uart_tx_fifo_syncfifo_we & uart_tx_fifo_syncfifo_writable) & (~uart_tx_fifo_replace))) begin
		if ((~uart_tx_fifo_do_read)) begin
			uart_tx_fifo_level0 <= (uart_tx_fifo_level0 + 1'd1);
		end
	end else begin
		if (uart_tx_fifo_do_read) begin
			uart_tx_fifo_level0 <= (uart_tx_fifo_level0 - 1'd1);
		end
	end
	if (uart_rx_fifo_syncfifo_re) begin
		uart_rx_fifo_readable <= 1'd1;
	end else begin
		if (uart_rx_fifo_re) begin
			uart_rx_fifo_readable <= 1'd0;
		end
	end
	if (((uart_rx_fifo_syncfifo_we & uart_rx_fifo_syncfifo_writable) & (~uart_rx_fifo_replace))) begin
		uart_rx_fifo_produce <= (uart_rx_fifo_produce + 1'd1);
	end
	if (uart_rx_fifo_do_read) begin
		uart_rx_fifo_consume <= (uart_rx_fifo_consume + 1'd1);
	end
	if (((uart_rx_fifo_syncfifo_we & uart_rx_fifo_syncfifo_writable) & (~uart_rx_fifo_replace))) begin
		if ((~uart_rx_fifo_do_read)) begin
			uart_rx_fifo_level0 <= (uart_rx_fifo_level0 + 1'd1);
		end
	end else begin
		if (uart_rx_fifo_do_read) begin
			uart_rx_fifo_level0 <= (uart_rx_fifo_level0 - 1'd1);
		end
	end
	if (timer_en_storage) begin
		if ((timer_value == 1'd0)) begin
			timer_value <= timer_reload_storage;
		end else begin
			timer_value <= (timer_value - 1'd1);
		end
	end else begin
		timer_value <= timer_load_storage;
	end
	if (timer_update_value_re) begin
		timer_value_status <= timer_value;
	end
	if (timer_zero_clear) begin
		timer_zero_pending <= 1'd0;
	end
	timer_zero_trigger_d <= timer_zero_trigger;
	if (((~timer_zero_trigger) & timer_zero_trigger_d)) begin
		timer_zero_pending <= 1'd1;
	end
	state <= next_state;
	case (grant)
		1'd0: begin
			if ((~request[0])) begin
				if (request[1]) begin
					grant <= 1'd1;
				end
			end
		end
		1'd1: begin
			if ((~request[1])) begin
				if (request[0]) begin
					grant <= 1'd0;
				end
			end
		end
	endcase
	slave_sel_r <= slave_sel;
	if (wait_1) begin
		if ((~done)) begin
			count <= (count - 1'd1);
		end
	end else begin
		count <= 20'd1000000;
	end
	csr_bankarray_interface0_bank_bus_dat_r <= 1'd0;
	if (csr_bankarray_csrbank0_sel) begin
		case (csr_bankarray_interface0_bank_bus_adr[8:0])
			1'd0: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_EN0_w;
			end
			1'd1: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_RST0_w;
			end
			2'd2: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_SEL0_w;
			end
			2'd3: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_WEN_IMAGE0_w;
			end
			3'd4: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_WADD_IMAGE0_w;
			end
			3'd5: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_WDATA_IMAGE0_w;
			end
			3'd6: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_REN_MEMORY0_w;
			end
			3'd7: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_REN_IMAGE0_w;
			end
			4'd8: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_RADD_IMAGE0_w;
			end
			4'd9: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_RDATA_IMAGE_w;
			end
			4'd10: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_RADD_MEMORY0_w;
			end
			4'd11: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_DATA_MEMORY_w;
			end
			4'd12: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_CONV_OK_w;
			end
			4'd13: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_MAX_OK_w;
			end
			4'd14: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_DENS_OK_w;
			end
			4'd15: begin
				csr_bankarray_interface0_bank_bus_dat_r <= csr_bankarray_csrbank0_MEM_OK_w;
			end
		endcase
	end
	if (csr_bankarray_csrbank0_EN0_re) begin
		EN_storage <= csr_bankarray_csrbank0_EN0_r;
	end
	EN_re <= csr_bankarray_csrbank0_EN0_re;
	if (csr_bankarray_csrbank0_RST0_re) begin
		RST_storage <= csr_bankarray_csrbank0_RST0_r;
	end
	RST_re <= csr_bankarray_csrbank0_RST0_re;
	if (csr_bankarray_csrbank0_SEL0_re) begin
		SEL_storage[3:0] <= csr_bankarray_csrbank0_SEL0_r;
	end
	SEL_re <= csr_bankarray_csrbank0_SEL0_re;
	if (csr_bankarray_csrbank0_WEN_IMAGE0_re) begin
		WEN_IMAGE_storage <= csr_bankarray_csrbank0_WEN_IMAGE0_r;
	end
	WEN_IMAGE_re <= csr_bankarray_csrbank0_WEN_IMAGE0_re;
	if (csr_bankarray_csrbank0_WADD_IMAGE0_re) begin
		WADD_IMAGE_storage[9:0] <= csr_bankarray_csrbank0_WADD_IMAGE0_r;
	end
	WADD_IMAGE_re <= csr_bankarray_csrbank0_WADD_IMAGE0_re;
	if (csr_bankarray_csrbank0_WDATA_IMAGE0_re) begin
		WDATA_IMAGE_storage[15:0] <= csr_bankarray_csrbank0_WDATA_IMAGE0_r;
	end
	WDATA_IMAGE_re <= csr_bankarray_csrbank0_WDATA_IMAGE0_re;
	if (csr_bankarray_csrbank0_REN_MEMORY0_re) begin
		REN_MEMORY_storage <= csr_bankarray_csrbank0_REN_MEMORY0_r;
	end
	REN_MEMORY_re <= csr_bankarray_csrbank0_REN_MEMORY0_re;
	if (csr_bankarray_csrbank0_REN_IMAGE0_re) begin
		REN_IMAGE_storage <= csr_bankarray_csrbank0_REN_IMAGE0_r;
	end
	REN_IMAGE_re <= csr_bankarray_csrbank0_REN_IMAGE0_re;
	if (csr_bankarray_csrbank0_RADD_IMAGE0_re) begin
		RADD_IMAGE_storage[9:0] <= csr_bankarray_csrbank0_RADD_IMAGE0_r;
	end
	RADD_IMAGE_re <= csr_bankarray_csrbank0_RADD_IMAGE0_re;
	RDATA_IMAGE_re <= csr_bankarray_csrbank0_RDATA_IMAGE_re;
	if (csr_bankarray_csrbank0_RADD_MEMORY0_re) begin
		RADD_MEMORY_storage[9:0] <= csr_bankarray_csrbank0_RADD_MEMORY0_r;
	end
	RADD_MEMORY_re <= csr_bankarray_csrbank0_RADD_MEMORY0_re;
	DATA_MEMORY_re <= csr_bankarray_csrbank0_DATA_MEMORY_re;
	CONV_OK_re <= csr_bankarray_csrbank0_CONV_OK_re;
	MAX_OK_re <= csr_bankarray_csrbank0_MAX_OK_re;
	DENS_OK_re <= csr_bankarray_csrbank0_DENS_OK_re;
	MEM_OK_re <= csr_bankarray_csrbank0_MEM_OK_re;
	csr_bankarray_interface1_bank_bus_dat_r <= 1'd0;
	if (csr_bankarray_csrbank1_sel) begin
		case (csr_bankarray_interface1_bank_bus_adr[8:0])
			1'd0: begin
				csr_bankarray_interface1_bank_bus_dat_r <= csr_bankarray_csrbank1_reset0_w;
			end
			1'd1: begin
				csr_bankarray_interface1_bank_bus_dat_r <= csr_bankarray_csrbank1_scratch0_w;
			end
			2'd2: begin
				csr_bankarray_interface1_bank_bus_dat_r <= csr_bankarray_csrbank1_bus_errors_w;
			end
		endcase
	end
	if (csr_bankarray_csrbank1_reset0_re) begin
		soccontroller_reset_storage <= csr_bankarray_csrbank1_reset0_r;
	end
	soccontroller_reset_re <= csr_bankarray_csrbank1_reset0_re;
	if (csr_bankarray_csrbank1_scratch0_re) begin
		soccontroller_scratch_storage[31:0] <= csr_bankarray_csrbank1_scratch0_r;
	end
	soccontroller_scratch_re <= csr_bankarray_csrbank1_scratch0_re;
	soccontroller_bus_errors_re <= csr_bankarray_csrbank1_bus_errors_re;
	csr_bankarray_sel_r <= csr_bankarray_sel;
	csr_bankarray_interface2_bank_bus_dat_r <= 1'd0;
	if (csr_bankarray_csrbank2_sel) begin
		case (csr_bankarray_interface2_bank_bus_adr[8:0])
			1'd0: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_load0_w;
			end
			1'd1: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_reload0_w;
			end
			2'd2: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_en0_w;
			end
			2'd3: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_update_value0_w;
			end
			3'd4: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_value_w;
			end
			3'd5: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_ev_status_w;
			end
			3'd6: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_ev_pending_w;
			end
			3'd7: begin
				csr_bankarray_interface2_bank_bus_dat_r <= csr_bankarray_csrbank2_ev_enable0_w;
			end
		endcase
	end
	if (csr_bankarray_csrbank2_load0_re) begin
		timer_load_storage[31:0] <= csr_bankarray_csrbank2_load0_r;
	end
	timer_load_re <= csr_bankarray_csrbank2_load0_re;
	if (csr_bankarray_csrbank2_reload0_re) begin
		timer_reload_storage[31:0] <= csr_bankarray_csrbank2_reload0_r;
	end
	timer_reload_re <= csr_bankarray_csrbank2_reload0_re;
	if (csr_bankarray_csrbank2_en0_re) begin
		timer_en_storage <= csr_bankarray_csrbank2_en0_r;
	end
	timer_en_re <= csr_bankarray_csrbank2_en0_re;
	if (csr_bankarray_csrbank2_update_value0_re) begin
		timer_update_value_storage <= csr_bankarray_csrbank2_update_value0_r;
	end
	timer_update_value_re <= csr_bankarray_csrbank2_update_value0_re;
	timer_value_re <= csr_bankarray_csrbank2_value_re;
	timer_status_re <= csr_bankarray_csrbank2_ev_status_re;
	if (csr_bankarray_csrbank2_ev_pending_re) begin
		timer_pending_r <= csr_bankarray_csrbank2_ev_pending_r;
	end
	timer_pending_re <= csr_bankarray_csrbank2_ev_pending_re;
	if (csr_bankarray_csrbank2_ev_enable0_re) begin
		timer_enable_storage <= csr_bankarray_csrbank2_ev_enable0_r;
	end
	timer_enable_re <= csr_bankarray_csrbank2_ev_enable0_re;
	csr_bankarray_interface3_bank_bus_dat_r <= 1'd0;
	if (csr_bankarray_csrbank3_sel) begin
		case (csr_bankarray_interface3_bank_bus_adr[8:0])
			1'd0: begin
				csr_bankarray_interface3_bank_bus_dat_r <= uart_rxtx_w;
			end
			1'd1: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_txfull_w;
			end
			2'd2: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_rxempty_w;
			end
			2'd3: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_ev_status_w;
			end
			3'd4: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_ev_pending_w;
			end
			3'd5: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_ev_enable0_w;
			end
			3'd6: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_txempty_w;
			end
			3'd7: begin
				csr_bankarray_interface3_bank_bus_dat_r <= csr_bankarray_csrbank3_rxfull_w;
			end
		endcase
	end
	uart_txfull_re <= csr_bankarray_csrbank3_txfull_re;
	uart_rxempty_re <= csr_bankarray_csrbank3_rxempty_re;
	uart_status_re <= csr_bankarray_csrbank3_ev_status_re;
	if (csr_bankarray_csrbank3_ev_pending_re) begin
		uart_pending_r[1:0] <= csr_bankarray_csrbank3_ev_pending_r;
	end
	uart_pending_re <= csr_bankarray_csrbank3_ev_pending_re;
	if (csr_bankarray_csrbank3_ev_enable0_re) begin
		uart_enable_storage[1:0] <= csr_bankarray_csrbank3_ev_enable0_r;
	end
	uart_enable_re <= csr_bankarray_csrbank3_ev_enable0_re;
	uart_txempty_re <= csr_bankarray_csrbank3_txempty_re;
	uart_rxfull_re <= csr_bankarray_csrbank3_rxfull_re;
	if (sys_rst) begin
		soccontroller_reset_storage <= 1'd0;
		soccontroller_reset_re <= 1'd0;
		soccontroller_scratch_storage <= 32'd305419896;
		soccontroller_scratch_re <= 1'd0;
		soccontroller_bus_errors_re <= 1'd0;
		soccontroller_bus_errors <= 32'd0;
		ram_bus_ack <= 1'd0;
		interface0_ram_bus_ack <= 1'd0;
		interface1_ram_bus_ack <= 1'd0;
		serial_tx <= 1'd0;
		tx_tick <= 32'd0;
		tx_phase <= 32'd0;
		rx_tick <= 32'd0;
		rx_phase <= 32'd0;
		rx_rx_d <= 1'd0;
		uart_txfull_re <= 1'd0;
		uart_rxempty_re <= 1'd0;
		uart_tx_pending <= 1'd0;
		uart_tx_trigger_d <= 1'd0;
		uart_rx_pending <= 1'd0;
		uart_rx_trigger_d <= 1'd0;
		uart_status_re <= 1'd0;
		uart_pending_re <= 1'd0;
		uart_pending_r <= 2'd0;
		uart_enable_storage <= 2'd0;
		uart_enable_re <= 1'd0;
		uart_txempty_re <= 1'd0;
		uart_rxfull_re <= 1'd0;
		uart_tx_fifo_readable <= 1'd0;
		uart_tx_fifo_level0 <= 5'd0;
		uart_tx_fifo_produce <= 4'd0;
		uart_tx_fifo_consume <= 4'd0;
		uart_rx_fifo_readable <= 1'd0;
		uart_rx_fifo_level0 <= 5'd0;
		uart_rx_fifo_produce <= 4'd0;
		uart_rx_fifo_consume <= 4'd0;
		timer_load_storage <= 32'd0;
		timer_load_re <= 1'd0;
		timer_reload_storage <= 32'd0;
		timer_reload_re <= 1'd0;
		timer_en_storage <= 1'd0;
		timer_en_re <= 1'd0;
		timer_update_value_storage <= 1'd0;
		timer_update_value_re <= 1'd0;
		timer_value_status <= 32'd0;
		timer_value_re <= 1'd0;
		timer_zero_pending <= 1'd0;
		timer_zero_trigger_d <= 1'd0;
		timer_status_re <= 1'd0;
		timer_pending_re <= 1'd0;
		timer_pending_r <= 1'd0;
		timer_enable_storage <= 1'd0;
		timer_enable_re <= 1'd0;
		timer_value <= 32'd0;
		EN_storage <= 1'd0;
		EN_re <= 1'd0;
		RST_storage <= 1'd0;
		RST_re <= 1'd0;
		SEL_storage <= 4'd0;
		SEL_re <= 1'd0;
		WEN_IMAGE_storage <= 1'd0;
		WEN_IMAGE_re <= 1'd0;
		WADD_IMAGE_storage <= 10'd0;
		WADD_IMAGE_re <= 1'd0;
		WDATA_IMAGE_storage <= 16'd0;
		WDATA_IMAGE_re <= 1'd0;
		REN_MEMORY_storage <= 1'd0;
		REN_MEMORY_re <= 1'd0;
		REN_IMAGE_storage <= 1'd0;
		REN_IMAGE_re <= 1'd0;
		RADD_IMAGE_storage <= 10'd0;
		RADD_IMAGE_re <= 1'd0;
		RDATA_IMAGE_re <= 1'd0;
		RADD_MEMORY_storage <= 10'd0;
		RADD_MEMORY_re <= 1'd0;
		DATA_MEMORY_re <= 1'd0;
		CONV_OK_re <= 1'd0;
		MAX_OK_re <= 1'd0;
		DENS_OK_re <= 1'd0;
		MEM_OK_re <= 1'd0;
		rs232phytx_state <= 1'd0;
		rs232phyrx_state <= 1'd0;
		grant <= 1'd0;
		slave_sel_r <= 4'd0;
		count <= 20'd1000000;
		csr_bankarray_sel_r <= 1'd0;
		state <= 1'd0;
	end
	regs0 <= serial_rx;
	regs1 <= regs0;
end

reg [31:0] mem[0:5579];
reg [31:0] memdat;
always @(posedge sys_clk) begin
	memdat <= mem[adr];
end

assign dat_r = memdat;

initial begin
	$readmemh("mem.init", mem);
end

reg [31:0] mem_1[0:2047];
reg [10:0] memadr;
always @(posedge sys_clk) begin
	if (sram0_we[0])
		mem_1[sram0_adr][7:0] <= sram0_dat_w[7:0];
	if (sram0_we[1])
		mem_1[sram0_adr][15:8] <= sram0_dat_w[15:8];
	if (sram0_we[2])
		mem_1[sram0_adr][23:16] <= sram0_dat_w[23:16];
	if (sram0_we[3])
		mem_1[sram0_adr][31:24] <= sram0_dat_w[31:24];
	memadr <= sram0_adr;
end

assign sram0_dat_r = mem_1[memadr];

initial begin
	$readmemh("mem_1.init", mem_1);
end

reg [31:0] mem_2[0:4095];
reg [11:0] memadr_1;
always @(posedge sys_clk) begin
	if (sram1_we[0])
		mem_2[sram1_adr][7:0] <= sram1_dat_w[7:0];
	if (sram1_we[1])
		mem_2[sram1_adr][15:8] <= sram1_dat_w[15:8];
	if (sram1_we[2])
		mem_2[sram1_adr][23:16] <= sram1_dat_w[23:16];
	if (sram1_we[3])
		mem_2[sram1_adr][31:24] <= sram1_dat_w[31:24];
	memadr_1 <= sram1_adr;
end

assign sram1_dat_r = mem_2[memadr_1];

initial begin
	$readmemh("mem_2.init", mem_2);
end

reg [7:0] mem_3[0:51];
reg [5:0] memadr_2;
always @(posedge sys_clk) begin
	memadr_2 <= csr_bankarray_adr;
end

assign csr_bankarray_dat_r = mem_3[memadr_2];

initial begin
	$readmemh("mem_3.init", mem_3);
end

reg [9:0] storage[0:15];
reg [9:0] memdat_1;
reg [9:0] memdat_2;
always @(posedge sys_clk) begin
	if (uart_tx_fifo_wrport_we)
		storage[uart_tx_fifo_wrport_adr] <= uart_tx_fifo_wrport_dat_w;
	memdat_1 <= storage[uart_tx_fifo_wrport_adr];
end

always @(posedge sys_clk) begin
	if (uart_tx_fifo_rdport_re)
		memdat_2 <= storage[uart_tx_fifo_rdport_adr];
end

assign uart_tx_fifo_wrport_dat_r = memdat_1;
assign uart_tx_fifo_rdport_dat_r = memdat_2;

reg [9:0] storage_1[0:15];
reg [9:0] memdat_3;
reg [9:0] memdat_4;
always @(posedge sys_clk) begin
	if (uart_rx_fifo_wrport_we)
		storage_1[uart_rx_fifo_wrport_adr] <= uart_rx_fifo_wrport_dat_w;
	memdat_3 <= storage_1[uart_rx_fifo_wrport_adr];
end

always @(posedge sys_clk) begin
	if (uart_rx_fifo_rdport_re)
		memdat_4 <= storage_1[uart_rx_fifo_rdport_adr];
end

assign uart_rx_fifo_wrport_dat_r = memdat_3;
assign uart_rx_fifo_rdport_dat_r = memdat_4;

accQuant_cnn accQuant_cnn(
	.clk_fpga(CLK),
	.en(EN_storage),
	.radd_image(RADD_IMAGE_storage),
	.radd_memory(RADD_MEMORY_storage),
	.ren_image(REN_IMAGE_storage),
	.ren_memory(REN_MEMORY_storage),
	.rst(RST_storage),
	.sel(SEL_storage),
	.wadd_image(WADD_IMAGE_storage),
	.wdata_image(WDATA_IMAGE_storage),
	.wen_image(WEN_IMAGE_storage),
	.conv_ok(CONV_OK_status),
	.data_memory(DATA_MEMORY_status),
	.dens_ok(DENS_OK_status),
	.max_ok(MAX_OK_status),
	.mem_full_image(MEM_OK_status),
	.number_out(NUMBER_OUT),
	.rdata_image(RDATA_IMAGE_status)
);

VexRiscv VexRiscv(
	.clk(sys_clk),
	.dBusWishbone_ACK(cpu_dbus_ack),
	.dBusWishbone_DAT_MISO(cpu_dbus_dat_r),
	.dBusWishbone_ERR(cpu_dbus_err),
	.externalInterruptArray(cpu_interrupt),
	.externalResetVector(vexriscv),
	.iBusWishbone_ACK(cpu_ibus_ack),
	.iBusWishbone_DAT_MISO(cpu_ibus_dat_r),
	.iBusWishbone_ERR(cpu_ibus_err),
	.reset((sys_rst | cpu_reset_1)),
	.softwareInterrupt(1'd0),
	.timerInterrupt(1'd0),
	.dBusWishbone_ADR(cpu_dbus_adr),
	.dBusWishbone_BTE(cpu_dbus_bte),
	.dBusWishbone_CTI(cpu_dbus_cti),
	.dBusWishbone_CYC(cpu_dbus_cyc),
	.dBusWishbone_DAT_MOSI(cpu_dbus_dat_w),
	.dBusWishbone_SEL(cpu_dbus_sel),
	.dBusWishbone_STB(cpu_dbus_stb),
	.dBusWishbone_WE(cpu_dbus_we),
	.iBusWishbone_ADR(cpu_ibus_adr),
	.iBusWishbone_BTE(cpu_ibus_bte),
	.iBusWishbone_CTI(cpu_ibus_cti),
	.iBusWishbone_CYC(cpu_ibus_cyc),
	.iBusWishbone_DAT_MOSI(cpu_ibus_dat_w),
	.iBusWishbone_SEL(cpu_ibus_sel),
	.iBusWishbone_STB(cpu_ibus_stb),
	.iBusWishbone_WE(cpu_ibus_we)
);

endmodule
