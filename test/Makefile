# Makefile estándar para Tiny Tapeout / Cocotb

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# Rutas de los archivos fuente de tu proyecto
SRC_DIR = $(PWD)/../src
PROJECT_SOURCES = project.v

# Agrega aquí tus archivos Verilog si tienes más módulos separados (ej. debounce, fsm, etc.)
VERILOG_SOURCES = $(addprefix $(SRC_DIR)/, $(PROJECT_SOURCES))
# Si tienes otros archivos en src/, inclúyelos también en la lista o usa comodines:
# VERILOG_SOURCES += $(SRC_DIR)/debounce.v $(SRC_DIR)/morse_fsm.v $(SRC_DIR)/morse_to_7seg.v

TOPLEVEL = tt_um_morse_top
MODULE   = test

# Incluir las reglas de cocotb para Tiny Tapeout
include $(shell cocotb-config --makefiles)/Makefile.sim
