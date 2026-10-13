# Decodificador Morse a 7 Segmentos (Tiny Tapeout)

Proyecto desarrollado para el taller CANELOS 2026. Este diseño implementa un decodificador de código Morse utilizando un único botón pulsador físico para ingresar puntos y rayas, mostrando el carácter alfanumérico resultante en un display de 7 segmentos.


## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## How it works

El sistema consta de cuatro módulos principales en Verilog ubicados en la carpeta `src`:
1. **`debounce`**: Filtra el ruido mecánico y los rebotes del botón físico.
2. **`morse_fsm`**: Máquina de estados que mide la duración de cada pulsación (distinguiendo puntos `< 250ms` de guiones `>= 250ms`) y detecta pausas de silencio (`> 700ms`) para cerrar y decodificar el carácter.
3. **`morse_to_7seg`**: Traductor combinacional que convierte los símbolos ingresados en patrones para un display de 7 segmentos (soportando letras A-Z, dígitos 0-9 y mostrando `=` en caso de error).
4. **`tt_um_morse_top`**: Módulo principal que unifica todo y gestiona las entradas/salidas físicas del chip estándar de Tiny Tapeout.

