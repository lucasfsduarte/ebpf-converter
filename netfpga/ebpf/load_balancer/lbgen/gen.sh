#!/bin/bash

PROGRAM="l4lb_xdp"
EXT_C=".c"
EXT_O=".o"
EXT_HEX=".hex"
EXT_TXT=".txt"
EXT_DIS=".dis"

#******** Gerar arquivo de entrada disassembler ********
hexdump -C $PROGRAM$EXT_O > $PROGRAM$EXT_HEX
cut $PROGRAM$EXT_HEX -s --delimiter=' ' -f 2-9,10-19 > $PROGRAM$EXT_TXT

#******** Executar disassembler ********
gcc disassembler.c -o disassembler
more $PROGRAM$EXT_TXT | ./disassembler > $PROGRAM$EXT_DIS
chmod +x instructions.txt
