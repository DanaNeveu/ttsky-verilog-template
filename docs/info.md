## How it works

Decodificador de código Morse basado en máquina de estados y antirrebote, diseñado para Tiny Tapeout (CANELOS 2026). Traduce pulsaciones cortas y largas en caracteres mostrados en un display de 7 segmentos.

## How to test

1. Conecta un botón pulsador a la entrada `ui_in[0]`.
2. Conecta un display de 7 segmentos a las salidas `uo_out[6:0]`.
3. Aplica un reset (`rst_n` en bajo y luego alto).
4. Presiona brevemente para un punto (.) o de forma sostenida para un guion (-). Tras una pausa, el carácter decodificado aparecerá en el display.
