from data import *
from lib import *

def x64_inst (op, args, line):

    # Initial values:
    instruction = 64 * '0'
    immediate = 32 * '0'
    offset = 16 * '0'
    src = 4 * '0'
    dst = 4 * '0'
    opcode = 8 * '0'

    if len(args) > 2:
        print("ebpf_ic: line " + str(line) + ": too many arguments")
        return None

    elif len(args) == 2 and op != 'neg':
        if isRegValid(args[0]) and not isRegValid(args[1]):
            if not isImmediateValid(args[1]):
                print("ebpf_ic: line " + str(line) + ": invalid immediate")
            else:
                dst = reg_set[args[0]]
                binaryImm = dataTypeConversor(args[1])
                immediate = completeBinary(binaryImm, 32)
                instruction = immediate + offset + src + dst + x64_inst_set[op]['opcodeImm']

        elif isRegValid(args[0]) and isRegValid(args[1]):
            dst = reg_set[args[0]]
            src = reg_set[args[1]]
            instruction = immediate + offset + src + dst + x64_inst_set[op]['opcode']
        else:
            print("ebpf_ic: line " + str(line) + ": invalid arguments")
            return None

    elif len(args) == 1 and op == 'neg':
        if isRegValid(args[0]):
            dst = reg_set[args[0]]
        else:
            print("ebpf_ic: line " + str(line) + ": " + args[0] + ": unknown register")
            return None
        instruction = immediate + offset + src + dst + x64_inst_set[op]['opcode']

    else:
        print("ebpf_ic: line " + line + ": not enough arguments")
        return None

    return instruction

instr_set = {
    'neg'  : x64_inst,
    'add'  : x64_inst,
    'sub'  : x64_inst,
    'mul'  : x64_inst,
    'div'  : x64_inst,
    'or'   : x64_inst,
    'and'  : x64_inst,
    'lsh'  : x64_inst,
    'rsh'  : x64_inst,
    'neg'  : x64_inst,
    'mod'  : x64_inst,
    'xor'  : x64_inst,
    'mov'  : x64_inst,
    'arsh' : x64_inst
}
