from data import *

# This function complete a bits sequence with (n - bits) zeros
def completeBinary(string, n, signal=0):

    size = len(string)

    if size > n: print("ebpf_ic: warning: possible overflow detected")

    if signal == 0: bit = '0'
    elif signal == 1: bit = '1'

    bits = bit * (n - size)
    strset = bits + string
    return strset

def dataTypeConversor(data):

    if data.startswith('-'): negative = 1; data = data.replace('-', '')
    else: negative = 0

    if data.startswith("0x"): converted = bin(int(data[2:], 16))[2:]
    elif data.startswith("0b"): converted = data[2:]
    else: converted = bin(int(data, 10))[2:]

    if negative: converted[0] = 1

    return converted

def isRegValid(reg):
    return reg in reg_set

def isNumericDataValid(immediate):
    if immediate.startswith("-"): immediate = immediate.replace('-', '')
    if immediate.startswith("0x"): return isHexadecimal(immediate[2:])
    elif immediate.startswith("0b"): return isBinary(immediate[2:])
    else: return immediate.isdigit()

def isMemoryAccessValid(maccess):
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
    binarydigits = ('01')
    return all(char in binarydigits for char in inputString)

def isHexadecimal(inputString):
    hexdigits = ('0123456789abcdefABCDEF')
    return all(char in hexdigits for char in inputString)

def perror(code=None, line=None, arg1=None, arg2=None):
    return None
