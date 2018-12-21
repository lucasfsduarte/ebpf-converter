from data import *

# This function complete a bits sequence with (n - bits) zeros
def completeBinary(string, n, signal=0):

    size = len(string)

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

    converted = completeBinary(converted, 32)

    if negative: converted[0] = 1

    return converted

def isRegValid(reg):
    return reg in reg_set

def isImmediateValid(immediate):
    if immediate.startswith("-"): immediate = immediate.replace('-', '')
    if immediate.startswith("0x"): return isHexadecimal(immediate[2:])
    elif immediate.startswith("0b"): return isBinary(immediate[2:])
    else: return immediate.isdigit()

def isBinary(inputString):
    binarydigits = ('01')
    return all(char in binarydigits for char in inputString)

def isHexadecimal(inputString):
    hexdigits = ('0123456789abcdefABCDEF')
    return all(char in hexdigits for char in inputString)
