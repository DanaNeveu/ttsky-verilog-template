import os
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# Forzar la generación del archivo results.xml que exige GitHub Actions
os.environ["COCOTB_RESULTS_FILE"] = "results.xml"

@cocotb.test()
async def test_morse(dut):
    dut._log.info("Iniciando test del decodificador Morse")
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 10)
    
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 20)
    
    dut._log.info("Test finalizado con éxito")
