![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Decodificador Morse a 7 Segmentos (Tiny Tapeout)

Proyecto desarrollado para el taller CANELOS 2026. Este diseño implementa un decodificador de código Morse utilizando un único botón pulsador físico para ingresar puntos y rayas, mostrando el carácter alfanumérico resultante en un display de 7 segmentos.

- [Read the documentation for project](docs/info.md)

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## How it works

El sistema consta de cuatro módulos principales en Verilog ubicados en la carpeta `src`:
1. **`debounce`**: Filtra el ruido mecánico y los rebotes del botón físico.
2. **`morse_fsm`**: Máquina de estados que mide la duración de cada pulsación (distinguiendo puntos `< 250ms` de guiones `>= 250ms`) y detecta pausas de silencio (`> 700ms`) para cerrar y decodificar el carácter.
3. **`morse_to_7seg`**: Traductor combinacional que convierte los símbolos ingresados en patrones para un display de 7 segmentos (soportando letras A-Z, dígitos 0-9 y mostrando `=` en caso de error).
4. **`tt_um_morse_top`**: Módulo principal que unifica todo y gestiona las entradas/salidas físicas del chip estándar de Tiny Tapeout.

## Set up your Verilog project

1. Add your Verilog files to the `src` folder.
2. Edit the [info.yaml](info.yaml) and update information about your project, paying special attention to the `source_files` and `top_module` properties.
3. Edit [docs/info.md](docs/info.md) and add a description of your project.
4. Adapt the testbench to your design. See [test/README.md](test/README.md) for more information.

The GitHub action will automatically build the ASIC files using [LibreLane](https://www.zerotoasiccourse.com/terminology/librelane/).

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)

## What next?

- [Submit your design to the next shuttle](https://app.tinytapeout.com/).
- Edit [this README](README.md) and explain your design, how it works, and how to test it.
- Share your project on your social network of choice:
  - LinkedIn [#tinytapeout](https://www.linkedin.com/search/results/content/?keywords=%23tinytapeout) [@TinyTapeout](https://www.linkedin.com/company/100708654/)
  - Mastodon [#tinytapeout](https://chaos.social/tags/tinytapeout) [@matthewvenn](https://chaos.social/@matthewvenn)
  - X (formerly Twitter) [#tinytapeout](https://twitter.com/hashtag/tinytapeout) [@tinytapeout](https://twitter.com/tinytapeout)
  - Bluesky [@tinytapeout.com](https://bsky.app/profile/tinytapeout.com)
