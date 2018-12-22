# +------------------------+----------------+--------+--------+-----------+
# |immediate (32)          |offset (16)     |src (4) |dst (4) |opcode (8) |
# +------------------------+----------------+--------+--------+-----------+

# Valid arguments:
args_set = {

    'data': {
        '--hex':    {'description': 'Generates machine language in hexadecimal', 'value': 0},
        '--bin':    {'description': 'Generates machine language in binary', 'value': 1}
    },
    'instruction': {
        '--apart':  {'description': 'Generates two values (high and low) as the final instruction', 'value': 0},
        '--unique': {'description': 'Generates a single value as the final instruction', 'value': 1}
    }
}

# eBPF Registers:
reg_set = {

    'r0': '0000',
    'r1': '0001',
    'r2': '0010',
    'r3': '0011',
    'r4': '0100',
    'r5': '0101',
    'r6': '0110',
    'r7': '0111',
    'r8': '1000',
    'r9': '1001',
    'r10': '1010'
}

# eBPF x64 Instructions:
x64_x32_inst_set = {
    'add':  {'opcode': '00001111', 'opcodeImm': '00000111'},
    'sub':  {'opcode': '00011111', 'opcodeImm': '00010111'},
    'mul':  {'opcode': '00101111', 'opcodeImm': '00100111'},
    'div':  {'opcode': '00111111', 'opcodeImm': '00110111'},
    'or':   {'opcode': '01001111', 'opcodeImm': '01000111'},
    'and':  {'opcode': '01011111', 'opcodeImm': '01010111'},
    'lsh':  {'opcode': '01101111', 'opcodeImm': '01100111'},
    'rsh':  {'opcode': '01111111', 'opcodeImm': '01110111'},
    'neg':  {'opcode': '10000111'},
    'mod':  {'opcode': '10011111', 'opcodeImm': '10010111'},
    'xor':  {'opcode': '10101111', 'opcodeImm': '10100111'},
    'mov':  {'opcode': '10111111', 'opcodeImm': '10110111'},
    'arsh': {'opcode': '11001111', 'opcodeImm': '11000111'},
    'add32': {'opcode': '00001100', 'opcodeImm': '00000100'},
    'sub32': {'opcode': '00011100', 'opcodeImm': '00010100'},
    'mul32': {'opcode': '00101100', 'opcodeImm': '00100100'},
    'div32': {'opcode': '00111100', 'opcodeImm': '00110100'},
    'or32': {'opcode': '01001100', 'opcodeImm': '01000100'},
    'and32': {'opcode': '01011100', 'opcodeImm': '01010100'},
    'lsh32': {'opcode': '01101100', 'opcodeImm': '01100100'},
    'rsh32': {'opcode': '01111100', 'opcodeImm': '01110100'},
    'neg32': {'opcode': '10000100'},
    'mod32': {'opcode': '10011100', 'opcodeImm': '10010100'},
    'xor32': {'opcode': '10101100', 'opcodeImm': '10100100'},
    'mov32': {'opcode': '10111100', 'opcodeImm': '10110100'},
    'arsh32': {'opcode': '11001100', 'opcodeImm': '11000100'}
}

byteswap_inst_set = {
    'le16': {'imm': '0x10', 'opcode': '11010100'},
    'le32': {'imm': '0x20', 'opcode': '11010100'},
    'le64': {'imm': '0x40', 'opcode': '11010100'},
    'be16': {'imm': '0x10', 'opcode': '11011100'},
    'be32': {'imm': '0x20', 'opcode': '11011100'},
    'be64': {'imm': '0x40', 'opcode': '11011100'}
}

# eBPF Memory Access Instructions:
memory_inst_set = {
    'lddw': {'opcode': '00011000'},
    'ldabsw': {'opcode': '00100000'},
    'ldabsh': {'opcode': '00101000'},
    'ldabsb': {'opcode': '00110000'},
    'ldabsdw': {'opcode': '00111000'},
    'ldindw': {'opcode': '01000000'},
    'ldindh': {'opcode': '01001000'},
    'ldindb': {'opcode': '01010000'},
    'ldinddw': {'opcode': '01011000'},
    'ldxw': {'opcode': '01100001'},
    'ldxh': {'opcode': '01101001'},
    'ldxb': {'opcode': '01110001'},
    'ldxdw': {'opcode': '01111001'},
    'stw': {'opcode': '01100010'},
    'sth': {'opcode': '01101010'},
    'stb': {'opcode': '01110010'},
    'stdw': {'opcode': '01111010'},
    'stxw': {'opcode': '01100011'},
    'stxh': {'opcode': '01101011'},
    'stxb': {'opcode': '01110011'},
    'stxdw': {'opcode': '01111011'}
}

# eBPF Branch Instructions:
branch_inst_set = {
    'ja': {'opcode': '00000101'},
    'jeq': {'opcode': '00011101', 'opcodeImm': '00010101'},
    'jgt': {'opcode': '00101101', 'opcodeImm': '00100101'},
    'jge': {'opcode': '00111101', 'opcodeImm': '00110101'},
    'jlt': {'opcode': '10101101', 'opcodeImm': '10100101'},
    'jle': {'opcode': '10111101', 'opcodeImm': '10110101'},
    'jset': {'opcode': '01001101', 'opcodeImm': '01000101'},
    'jne': {'opcode': '01011101', 'opcodeImm': '01010101'},
    'jsgt': {'opcode': '01101101', 'opcodeImm': '01100101'},
    'jsge': {'opcode': '01111101', 'opcodeImm': '01110101'},
    'jslt': {'opcode': '11001101', 'opcodeImm': '11000101'},
    'jsle': {'opcode': '11011101', 'opcodeImm': '11010101'},
    'call': {'opcode': '10000101'},
    'exit': {'opcode': '10010101'}
}
