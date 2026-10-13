import os
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# Forzar la generación del archivo results.xml que GitHub Actions busca obligatoriamente
os.environ["COCOTB_RESULTS_FILE"] = "results.xml"

@cocotb.test()
async def test_morse(dut):
    dut._log.info("Iniciando test del decodificador Morse")
    
    # Configurar reloj de 50 MHz (20 ns de periodo)
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    # Aplicar reset inicial (activo en bajo)
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 10)
    
    # Liberar el reset
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 20)
    
    dut._log.info("Test finalizado con éxito")
