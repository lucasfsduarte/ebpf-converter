#!/bin/bash

PROGRAM=$1
EXT_C=".c"
EXT_O=".o"
EXT_HEX=".hex"
EXT_TXT=".txt"
EXT_DIS=".dis"
EXT_ASM=".asm"

if [ -z $1 ]
then
    echo "Error: C program wasn't defined."
    echo "       Use ./gera_inst_ebpf.sh [program] (without extension)"
else
    #******** Gerar objeto - arquivo.o ********
    clang-3.8 -O2 -target bpfeb -I ../../includes -c $PROGRAM$EXT_C

    #******** Gerar arquivo de entrada disassembler ********
    hexdump -C $PROGRAM$EXT_O > $PROGRAM$EXT_HEX
    cut $PROGRAM$EXT_HEX -s --delimiter=' ' -f 2-9,10-19 > $PROGRAM$EXT_TXT

    #******** Executar disassembler ********
    gcc disassembler.c -o disassembler
    more $PROGRAM$EXT_TXT | ./disassembler > $PROGRAM$EXT_ASM
    chmod +x instructions.txt
fi
