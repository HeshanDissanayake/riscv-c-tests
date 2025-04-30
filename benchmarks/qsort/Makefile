
RISCV_GCC := /opt/dev/cva6_riscv_regsw/bin/riscv-none-elf-gcc

SRC = /home/heshds/working_dir/riscv-c-tests/benchmarks/qsort/qsort_main.c 
EXEC = qsort_c.elf

ARCH = -march=rv64g_zba_zbb_zbs_zbc 
ARCH_C = -march=rv64gc_zba_zbb_zbs_zbc 

# CFLAGS = 
# Linker flags
LDFLAGS := -I/home/heshds/working_dir/cva6/verif/sim/../env/corev-dv/user_extension \
           -static \
           -mcmodel=medany \
           -fvisibility=hidden \
           -nostdlib \
           -nostartfiles \
           -g \
           -I/home/heshds/working_dir/regsw_tests/env \
           -I/home/heshds/working_dir/riscv-c-tests/benchmarks/common \
           -lgcc \
           -T /home/heshds/working_dir/regsw_tests/common/test.ld \
           -mabi=lp64d

# Additional source files for linking
LINK_SOURCES := /home/heshds/working_dir/regsw_tests/common/syscalls.c \
                /home/heshds/working_dir/regsw_tests/common/crt.S

all: clean $(EXEC)

$(EXEC): $(OBJ)
	$(RISCV_GCC) $(LDFLAGS) $(LINK_SOURCES)  $(ARCH_C) -o $(EXEC) $(SRC)
	/opt/dev/cva6_riscv_regsw/bin/riscv-none-elf-objdump -d -M no-aliases $(EXEC) > $(EXEC).dump

clean:
	rm -f $(OBJ) $(EXEC)

.PHONY: all clean
