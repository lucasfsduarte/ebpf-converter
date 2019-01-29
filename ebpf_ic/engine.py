# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *  File:
# *        engine.py
# *
# *  Library:
# *        ebpf_ic/
# *
# *  Author:
# *        Lucas Duarte (lucas.f.duarte@ufv.br)
# *
# *  Description:
# *        Conversion and translation methods
# *

from Instruction import *
from data import *
from lib import *

def x64_x32_inst (op, args, line):
    """
    Converts x64 and x32 type instructions.

    Args:
        args: the operation (eg. mov), a list of arguments (eg. r0, r2) and the
        correspondent line on input file.

    Returns:
        instruction: instruction converted into machine code.

    Raises:
        None
    """

    inst = Instruction()
    if len(args) == 2 and op != 'neg' and op != 'neg32':
        if isRegValid(args[0]) and not isRegValid(args[1]):
            if isNumericDataValid(args[1]):
                inst.setDst(reg_set[args[0]])
                inst.setImm(completeBinary(dataTypeConversor(args[1]), 32))
                inst.setOpc(x64_x32_inst_set[op]['opcodeImm'])
            else:
                print("ebpf_ic: line " + str(line) + ": invalid immediate")
                return None

        elif isRegValid(args[0]) and isRegValid(args[1]):
            inst.setDst(reg_set[args[0]])
            inst.setSrc(reg_set[args[1]])
            inst.setOpc(x64_x32_inst_set[op]['opcode'])

        else:
            print("ebpf_ic: line " + str(line) + ": invalid arguments")
            return None

    elif len(args) == 1 and op == 'neg' or op == 'neg32':
        if isRegValid(args[0]):
            inst.setDst(reg_set[args[0]])
        else:
            print("ebpf_ic: line " + str(line) + ": " + args[0] + ": unknown register")
            return None
        inst.setOpc(x64_x32_inst_set[op]['opcode'])

    elif len(args) > 2:
        print("ebpf_ic: line " + str(line) + ": too many arguments")
        return None

    else:
        print("ebpf_ic: line " + str(line) + ": not enough arguments")
        return None

    return inst.toString()

def byteswap_inst (op, args, line):
    """
    Converts byteswap type instructions.

    Args:
        args: the operation, a list of arguments and the correspondent line on
        input file.

    Returns:
        instruction: instruction converted into machine code.

    Raises:
        None
    """

    inst = Instruction()
    if len(args) > 1:
        print("ebpf_ic: line " + str(line) + ": too many arguments")
        return None

    elif len(args) < 1:
        print("ebpf_ic: line " + str(line) + ": not enough arguments")
        return None

    else:
        if isRegValid(args[0]):
            inst.setDst(reg_set[args[0]])
            inst.setImm(completeBinary(bin(int(byteswap_inst_set[op]['imm'], 16))[2:], 32))
            inst.setOpc(byteswap_inst_set[op]['opcode'])
        else:
            print("ebpf_ic: line " + str(line) + ": " + args[0] + ": unknown register")
            return None
    return inst.toString()

def memory_inst (op, args, line):
    """
    Converts memory access type instructions.

    Args:
        args: the operation, a list of arguments and the correspondent line on
        input file.

    Returns:
        instruction: instruction converted into machine code.

    Raises:
        None
    """

    inst = Instruction()
    if len(args) == 2:
        if op == 'lddw':
            if isRegValid(args[0]) and not isRegValid(args[1]):
                if isNumericDataValid(args[1]):
                    inst.setDst(reg_set[args[0]])
                    inst.setImm(completeBinary(dataTypeConversor(args[1]), 32))
                    inst.setOpc(memory_inst_set[op]['opcode'])
                else:
                    print("ebpf_ic: line " + str(line) + ": invalid immediate")
                    return None
            else:
                print("ebpf_ic: line " + str(line) + ": invalid arguments")
                return None
        else:
            if isRegValid(args[0]) and not isRegValid(args[1]):
                memoryArgs = isMemoryAccessValid(args[1])
                if memoryArgs == None:
                    print("ebpf_ic: line " + str(line) + ": invalid memory access operation")
                    return None
                if isRegValid(memoryArgs[0]):
                    if isNumericDataValid(memoryArgs[1]):
                        inst.setSrc(reg_set[memoryArgs[0]])
                        inst.setDst(reg_set[args[0]])
                        inst.setOff(completeBinary(dataTypeConversor(memoryArgs[1]), 16))
                        inst.setOpc(memory_inst_set[op]['opcode'])
                    else:
                        print("ebpf_ic: line " + str(line) + ": invalid offset")
                        return None
                else:
                    print("ebpf_ic: line " + str(line) + ": unknown register")
                    return None

            elif not isRegValid(args[0]) and isRegValid(args[1]):
                memoryArgs = isMemoryAccessValid(args[0])
                if memoryArgs == None:
                    print("ebpf_ic: line " + str(line) + ": invalid memory access operation")
                    return None
                if isRegValid(memoryArgs[0]):
                    if isNumericDataValid(memoryArgs[1]):
                        inst.setSrc(reg_set[args[1]])
                        inst.setDst(reg_set[memoryArgs[0]])
                        inst.setOff(completeBinary(dataTypeConversor(memoryArgs[1]), 16))
                        inst.setOpc(memory_inst_set[op]['opcode'])
                    else:
                        print("ebpf_ic: line " + str(line) + ": invalid offset")
                        return None
                else:
                    print("ebpf_ic: line " + str(line) + ": unknown register")
                    return None

            elif not isRegValid(args[0]) and not isRegValid(args[1]):
                memoryArgs = isMemoryAccessValid(args[0])
                if memoryArgs == None:
                    print("ebpf_ic: line " + str(line) + ": invalid memory access operation")
                    return None
                if isRegValid(memoryArgs[0]):
                    if isNumericDataValid(memoryArgs[1]):
                        if isNumericDataValid(args[1]):
                            inst.setDst(reg_set[memoryArgs[0]])
                            inst.setImm(completeBinary(dataTypeConversor(args[1]), 32))
                            inst.setOff(completeBinary(dataTypeConversor(memoryArgs[1]), 16))
                            inst.setOpc(memory_inst_set[op]['opcode'])
                        else:
                            print("ebpf_ic: line " + str(line) + ": invalid immediate")
                            return None
                    else:
                        print("ebpf_ic: line " + str(line) + ": invalid offset")
                        return None
                else:
                    print("ebpf_ic: line " + str(line) + ": unknown register")
                    return None

    elif len(args) == 3:
        if isRegValid(args[0]) and isRegValid(args[1]):
            if isNumericDataValid(args[2]):
                inst.setSrc(reg_set[args[0]])
                inst.setDst(reg_set[args[1]])
                inst.setImm(completeBinary(dataTypeConversor(args[2]), 32))
                inst.setOpc(memory_inst_set[op]['opcode'])
            else:
                print("ebpf_ic: line " + str(line) + ": invalid immediate")
                return None
        else:
            print("ebpf_ic: line " + str(line) + ": unknown register")
            return None

    elif len(args) > 3:
        print("ebpf_ic: line " + str(line) + ": too many arguments")
        return None

    else:
        print("ebpf_ic: line " + str(line) + ": not enough arguments")
        return None
    return inst.toString()

def branch_inst (op, args, line):
    """
    Converts branch type instructions.

    Args:
        args: the operation, a list of arguments and the correspondent line on
        input file.

    Returns:
        instruction: instruction converted into machine code.

    Raises:
        None
    """

    inst = Instruction()
    if len(args) == 3:
        if isNumericDataValid(args[2]):
            if isRegValid(args[0]):
                if isRegValid(args[1]):
                    inst.setSrc(reg_set[args[1]])
                    inst.setOpc(branch_inst_set[op]['opcode'])
                elif isNumericDataValid(args[1]):
                    inst.setImm(completeBinary(dataTypeConversor(args[1]), 32))
                    inst.setOpc(branch_inst_set[op]['opcodeImm'])
                else:
                    print("ebpf_ic: line " + str(line) + ": invalid arguments")
                    return None
                inst.setDst(reg_set[args[0]])
                inst.setOff(completeBinary(dataTypeConversor(args[2]), 16))
            else:
                print("ebpf_ic: line " + str(line) + ": unknown register")
                return None
        else:
            print("ebpf_ic: line " + str(line) + ": invalid offset")
            return None

    elif len(args) == 1:
        if isNumericDataValid(args[0]):
            if op == 'ja':
                inst.setOff(completeBinary(dataTypeConversor(args[0]), 16))
            elif op == 'call':
                inst.setImm(completeBinary(dataTypeConversor(args[0]), 32))
            inst.setOpc(branch_inst_set[op]['opcode'])
        else:
            print("ebpf_ic: line " + str(line) + ": invalid arguments")
            return None

    elif len(args) == 0:
        if op == 'exit':
            inst.setOpc(branch_inst_set[op]['opcode'])
        else:
            print("ebpf_ic: line " + str(line) + ": not enough arguments")
            return None

    elif len(args) > 3:
        print("ebpf_ic: line " + str(line) + ": too many arguments")
        return None

    else:
        if op == 'ja' or op == 'call':
            print("ebpf_ic: line " + str(line) + ": too many arguments")
            return None
        else:
            print("ebpf_ic: line " + str(line) + ": not enough arguments")
            return None
    return inst.toString()

# List of available instructions and its correspondent translation methods
instr_set = {
    'neg'     : x64_x32_inst,
    'add'     : x64_x32_inst,
    'sub'     : x64_x32_inst,
    'mul'     : x64_x32_inst,
    'div'     : x64_x32_inst,
    'or'      : x64_x32_inst,
    'and'     : x64_x32_inst,
    'lsh'     : x64_x32_inst,
    'rsh'     : x64_x32_inst,
    'neg'     : x64_x32_inst,
    'mod'     : x64_x32_inst,
    'xor'     : x64_x32_inst,
    'mov'     : x64_x32_inst,
    'arsh'    : x64_x32_inst,

    'neg32'   : x64_x32_inst,
    'add32'   : x64_x32_inst,
    'sub32'   : x64_x32_inst,
    'mul32'   : x64_x32_inst,
    'div32'   : x64_x32_inst,
    'or32'    : x64_x32_inst,
    'and32'   : x64_x32_inst,
    'lsh32'   : x64_x32_inst,
    'rsh32'   : x64_x32_inst,
    'neg32'   : x64_x32_inst,
    'mod32'   : x64_x32_inst,
    'xor32'   : x64_x32_inst,
    'mov32'   : x64_x32_inst,
    'arsh32'  : x64_x32_inst,

    'le16'    : byteswap_inst,
    'le32'    : byteswap_inst,
    'le64'    : byteswap_inst,
    'be16'    : byteswap_inst,
    'be32'    : byteswap_inst,
    'be64'    : byteswap_inst,

    'lddw'    : memory_inst,
    'ldabsw'  : memory_inst,
    'ldabsh'  : memory_inst,
    'ldabsb'  : memory_inst,
    'ldabsdw' : memory_inst,
    'ldindw'  : memory_inst,
    'ldindh'  : memory_inst,
    'ldindb'  : memory_inst,
    'ldinddw' : memory_inst,
    'ldxw'    : memory_inst,
    'ldxh'    : memory_inst,
    'ldxb'    : memory_inst,
    'ldxdw'   : memory_inst,
    'stw'     : memory_inst,
    'sth'     : memory_inst,
    'stb'     : memory_inst,
    'stdw'    : memory_inst,
    'stxw'    : memory_inst,
    'stxh'    : memory_inst,
    'stxb'    : memory_inst,
    'stxdw'   : memory_inst,

    'ja'      : branch_inst,
    'jeq'     : branch_inst,
    'jgt'     : branch_inst,
    'jge'     : branch_inst,
    'jlt'     : branch_inst,
    'jle'     : branch_inst,
    'jset'    : branch_inst,
    'jne'     : branch_inst,
    'jsgt'    : branch_inst,
    'jsge'    : branch_inst,
    'jslt'    : branch_inst,
    'jsle'    : branch_inst,
    'call'    : branch_inst,
    'exit'    : branch_inst
}
