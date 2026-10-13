import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_morse(dut):
    dut._log.info("Iniciando test del decodificador Morse")
    
    # Configurar reloj del sistema de 50 MHz (20 ns de periodo)
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
    
    # Simular una pulsación corta en ui_in[0] (botón presionado)
    dut.ui_in.value = 8'b0000_0001
    await ClockCycles(dut.clk, 500) # Mantener presionado (punto)
    
    # Soltar el botón y esperar el gap de silencio
    dut.ui_in.value = 8'b0000_0000
    await ClockCycles(dut.clk, 1000)
    
    dut._log.info("Test finalizado con éxito")
