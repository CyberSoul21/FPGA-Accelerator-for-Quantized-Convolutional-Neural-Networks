create_project -force -name AccQuant_cnn -part xc7z020-clg400-1
set_property XPM_LIBRARIES {XPM_CDC XPM_MEMORY} [current_project]
add_files {AccQuant_cnn.v}
set_property library work [get_files {AccQuant_cnn.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/ReLu.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/ReLu.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/accQuant_cnn.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/accQuant_cnn.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider_dens.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider_dens.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider_fpga.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider_fpga.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider_max.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/clock_divider_max.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/controlMemoryAddressConv.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/controlMemoryAddressConv.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/controlMemoryAddressImg.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/controlMemoryAddressImg.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/convolution.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/convolution.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/counterPositionMemMax.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/counterPositionMemMax.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/counterPositionRstlConv.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/counterPositionRstlConv.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/counterPositionRstlMax.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/counterPositionRstlMax.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/display.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/display.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/full_connected.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/full_connected.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/maxpooling.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/maxpooling.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_0.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_0.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_1.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_1.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_2.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_2.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_3.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_3.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_4.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_4.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_5.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_5.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_6.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_6.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_7.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_7.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_8.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_8.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_9.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_dens_9.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_filter_1.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_filter_1.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_filter_2.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_filter_2.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_filter_3.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_filter_3.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_image.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_image.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_conv_1.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_conv_1.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_conv_2.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_conv_2.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_conv_3.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_conv_3.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_max_1.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/memory_rstl_max_1.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/predictMax.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/predictMax.v}]
add_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/quantization.v}
set_property library work [get_files {imports/home/javier/Documents/fpga_implementations_of_neural_networks/CNN/02_hardware/03_processor/05_soc_cnn/hardware/quantization.v}]
add_files {imports/home/javier/litex/pythondata-cpu-vexriscv/pythondata_cpu_vexriscv/verilog/VexRiscv.v}
set_property library work [get_files {imports/home/javier/litex/pythondata-cpu-vexriscv/pythondata_cpu_vexriscv/verilog/VexRiscv.v}]
read_xdc AccQuant_cnn.xdc
synth_design -top AccQuant_cnn -part xc7z020-clg400-1
report_timing_summary -file AccQuant_cnn_timing_synth.rpt
report_utilization -hierarchical -file AccQuant_cnn_utilization_hierarchical_synth.rpt
report_utilization -file AccQuant_cnn_utilization_synth.rpt
opt_design
place_design
report_utilization -hierarchical -file AccQuant_cnn_utilization_hierarchical_place.rpt
report_utilization -file AccQuant_cnn_utilization_place.rpt
report_io -file AccQuant_cnn_io.rpt
report_control_sets -verbose -file AccQuant_cnn_control_sets.rpt
report_clock_utilization -file AccQuant_cnn_clock_utilization.rpt
route_design
phys_opt_design
report_timing_summary -no_header -no_detailed_paths
write_checkpoint -force AccQuant_cnn_route.dcp
report_route_status -file AccQuant_cnn_route_status.rpt
report_drc -file AccQuant_cnn_drc.rpt
report_timing_summary -datasheet -max_paths 10 -file AccQuant_cnn_timing.rpt
report_power -file AccQuant_cnn_power.rpt