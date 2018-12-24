# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *  File:
# *        lib.py
# *
# *  Library:
# *        ebpf_ic/
# *
# *  Author:
# *        Lucas Duarte (lucas.f.duarte@ufv.br)
# *
# *  Description:
# *        Methods designed to support the others
# *

from data import *

def completeBinary(string, n, signal=0):
    """
    Complete a bit sequence with n - bits zeroes

    Args:
        string: a binary sequence;
        n: size of the pretended total sequence;
        signal: positive (0) or negative (1) sequence (two's complement).

    Returns:
        strset: completed sequence.

    Raises:
        None
    """

    size = len(string)
    if size > n: print("ebpf_ic: warning: possible overflow detected")
    if signal == 0: bit = '0'
    elif signal == 1: bit = '1'
    bits = bit * (n - size)
    strset = bits + string
    return strset

def dataTypeConversor(data):
    """
    Convert a numeric value with a predefined pattern from hexadecimal or decimal
    to a binary sequence.

    Args:
        data: a numeric value.

    Returns:
        converted: binary sequence equivalent to the numeric number

    Raises:
        None
    """

    if data.startswith('-'): negative = 1; data = data.replace('-', '')
    else: negative = 0

    if data.startswith("0x"): converted = bin(int(data[2:], 16))[2:]
    elif data.startswith("0b"): converted = data[2:]
    else: converted = bin(int(data, 10))[2:]

    if negative: converted[0] = 1

    return converted

def isRegValid(reg):
    """
    Verify if a register is listed as a valid register.

    Args:
        reg: register.

    Returns:
        boolean: true if the register is listed and valid; false if it isn't.

    Raises:
        None
    """

    return reg in reg_set

def isNumericDataValid(data):
    """
    Verify if a numeric value (a constant or an offset) is valid.

    Args:
        data: numeric data to be verified.

    Returns:
        boolean: true if the data is valid; false if it isn't.

    Raises:
        None
    """

    if data.startswith("-"): data = data.replace('-', '')
    if data.startswith("0x"): return isHexadecimal(data[2:])
    elif data.startswith("0b"): return isBinary(data[2:])
    else: return data.isdigit()

def isMemoryAccessValid(maccess):
    """
    Verify if a memory access is valid.

    Args:
        maccess: memory access block.

    Returns:
        data: involved parts (registers or constants) in memory access.

    Raises:
        None
    """

    data = []
    maccess = maccess.replace(' ', '')
    if maccess.find('+') != -1:
        args = maccess.split('+')
        if args[0].startswith('['): data.append(args[0].replace('[', ''))
        else: return None
        if args[1].endswith(']'): data.append(args[1].replace(']', ''))
        else: return None
        return data
    else: return None

def isBinary(inputString):
    """
    Verify if a sequence is binary.

    Args:
        inputString: input string to be verified.

    Returns:
        boolean: true if the string is binary; false if it isn't.

    Raises:
        None
    """

    binarydigits = ('01')
    return all(char in binarydigits for char in inputString)

def isHexadecimal(inputString):
    """
    Verify if a sequence is hexadecimal.

    Args:
        inputString: input string to be verified.

    Returns:
        boolean: true if the string is hexadecimal; false if it isn't.

    Raises:
        None
    """

    hexdigits = ('0123456789abcdefABCDEF')
    return all(char in hexdigits for char in inputString)

def apartInstruction(instruction, char):
    """
    Divides an instruction into two parts (high and low) between a char.

    Args:
        instruction: instruction to be divided;
        char: character to be used in the division.

    Returns:
        string: divided instruction.

    Raises:
        None
    """

    inst_hi = instruction[0:32]
    inst_lo = instruction[32:]
    return inst_hi + char + inst_lo

def transformHex(string):
    """
    Transforms a value into an hexadecimal value.

    Args:
        string: value to be transformed.

    Returns:
        string: hexadecimal transformed value.

    Raises:
        None
    """

    hexStr = '0x'
    hexHlf = ''
    for i in range(0, len(string)):
        hexHlf += string[i]
        if (i + 1) % 4 == 0:
            hexStr += hex(int(hexHlf, 2))[2:]
            hexHlf = ''
    return hexStr
